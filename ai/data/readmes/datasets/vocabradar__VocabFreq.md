---
language: [ar,bg,bn,ca,cs,da,de,el,en,es,fa,fi,fil,fr,he,hi,hu,id,is,it,ja,ko,lt,lv,mk,ms,nb,nl,pl,pt,ro,ru,sh,sk,sl,sv,ta,th,tr,uk,ur,vi,zh]
license: other
multilinguality: multilingual
pretty_name: "Three-tier Word Frequency Lists (43/347/1000 languages) / 三档词频表"
size_categories:
- 10M<n<100M
---

# Three-tier Word Frequency Lists / 三档词频表

## About VocabRadar

This dataset is a **VocabRadar** project — the vocabulary radar. The
[VocabRadar browser extension](https://vocabradar.com) marks up the words you do not know
yet while you watch videos or browse the web: definitions in place, translation, bilingual
subtitles and annotated subtitles. Whatever you watched can go on to
[vocabradar.com](https://vocabradar.com), which turns it into related exercises and games
so the words actually stick.

Word-frequency tables in three tiers, built independently (no merging) from three
sources: the cleaned [vocabradar/wordfreq](https://huggingface.co/datasets/vocabradar/wordfreq)
small lists (43 languages), the [omarkamali/wikipedia-monthly](https://huggingface.co/datasets/omarkamali/wikipedia-monthly)
Wikipedia top-100k token counts (347), and [Unicode UniLex](https://github.com/unicode-org/unilex)
frequency lists (1000). One gzip-compressed MessagePack file
per language in wordfreq cBpack format (`<tier>_<code>.msgpack.gz`, readable via
`wordfreq.read_cBpack`), where a word's coverage (share of corpus tokens) is
stored as centibels: coverage = 10^(-cB/100), bucket index = cB. A word is kept
only if its frequency is at least one per million tokens (coverage >= 1e-6,
i.e. cB <= 600). 27,155,844 rows in total.
`language` above lists the small tier; data_middle/data_large keep their source
codes verbatim (see `meta.json`).

这项工作是 **VocabRadar**（词汇雷达）的工作：[VocabRadar 浏览器扩展](https://vocabradar.com)
让你在看视频、刷网页时把还不认识的生词就地标注出来 —— 释义、翻译、双语字幕、注释字幕；
看过的内容还能送到 [vocabradar.com](https://vocabradar.com)，自动生成相关习题与游戏，把词真正记住。

> 三档词频表，三个来源各自成表、互不合并：小档（HF 清洗版
> [vocabradar/wordfreq](https://huggingface.co/datasets/vocabradar/wordfreq)，43 语）、
> 中档（[omarkamali/wikipedia-monthly](https://huggingface.co/datasets/omarkamali/wikipedia-monthly)
> 维基百科 top100k，347 语，剔除 simple）、大档（Unicode UniLex，1000 语）。
> 每语言一个 msgpack.gz（wordfreq cBpack 格式，`<档位>_<code>.msgpack.gz`，
> 可用 wordfreq.read_cBpack 读取）：词频覆盖率以厘贝存储（覆盖率=10^(-cB/100)，
> 桶索引=cB），按覆盖率降序构建；仅收录词频达到百万分之一（覆盖率 >= 1e-6，
> 即 cB <= 600）的词。

## Python package

These lists power the `vocabfreq` Python package. Data is not shipped
with the package: on first use it is downloaded from this dataset
(default mirror https://hf-mirror.com, override with `VOCABFREQ_ENDPOINT`),
cached in `~/.vocabfreq`, and every file is verified against `files.json`
(byte size + SHA-256).

```bash
pip install vocabfreq        # or: pip install -e . from the repo
```

```python
import vocabfreq
vocabfreq.word_frequency('的', 'zh')   # 0.0617 (auto-tier: small -> middle -> large)
vocabfreq.top_n_list('en', 3)          # ['the', 'to', 'and']
wf = vocabfreq.load('aai', wordlist='large')
wf.slice(100, 200)                     # band slicing: cb in [100, 200)
vocabfreq.download(['en', 'zh'])       # prefetch
```

## Files

```
├── README.md
├── meta.json                      # per-tier, per-language cleaning stats
├── files.json                     # per-file size (bytes) and SHA-256
├── data_small/  (43 files)        # small_<code>.msgpack.gz, wordfreq, MIT
├── data_middle/ (347 files)        # middle_<code>.msgpack.gz, Wikipedia, CC BY-SA 3.0 / GFDL
└── data_large/  (1000 files)        # large_<code>.msgpack.gz, UniLex, Unicode DFS-2016
```

## Cleaning rules

Only clearly-safe rules are applied (no false positives intended):
`unparsable` (empty/header/comment/unparseable rows), `invalid` (tokens with no
letter or mark — pure digits such as ISBNs and pure punctuation), `duplicate`
(kept max coverage), `below_threshold` (coverage < 1e-6). Identity per language:
`raw = unparsable + invalid + duplicate + below_threshold + kept`.

## Tier summaries

| tier | languages | raw rows | kept rows | coverage range of kept words |
|---|---|---|---|---|
| data_small | 43 | 1,712,418 | 1,712,418 | 71.0%–96.0% |
| data_middle | 347 | 26,674,554 | 16,283,612 | 67.1%–100.0% |
| data_large | 1000 | 13,777,232 | 9,159,814 | 1.9%–102.3% |

## Vocabulary lists

### data_small

<!-- BEGIN GENERATED LANGUAGE TABLE:data_small -->
`data_small/small_<code>.msgpack.gz`: wordfreq cBpack (coverage = 10^(-cB/100), kept if >= 1e-6 i.e. cB <= 600). Sorted by cumulative coverage; `float` is the top word's coverage.

| code | language | native name | first word | float | words | cumulative coverage |
|------|----------|-------------|------------|-------|-------|---------------------|
| [ur](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_ur.msgpack.gz) | Urdu | اردو | کے | 4.27e-02 | 22,442 | 96.0% |
| [ms](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_ms.msgpack.gz) | Malay | bahasa Malaysia | yang | 3.16e-02 | 28,571 | 95.9% |
| [vi](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_vi.msgpack.gz) | Vietnamese | Tiếng Việt | là | 1.82e-02 | 10,519 | 95.4% |
| [fil](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_fil.msgpack.gz) | Filipino | Filipino | sa | 7.41e-02 | 30,098 | 95.2% |
| [ca](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_ca.msgpack.gz) | Catalan | català | de | 6.03e-02 | 27,028 | 95.1% |
| [pt](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_pt.msgpack.gz) | Portuguese | português | de | 4.79e-02 | 33,123 | 94.3% |
| [fa](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_fa.msgpack.gz) | Persian | فارسی | و | 3.98e-02 | 30,108 | 94.2% |
| [sv](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_sv.msgpack.gz) | Swedish | svenska | är | 3.31e-02 | 30,515 | 94.0% |
| [nb](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_nb.msgpack.gz) | Norwegian Bokmål | norsk bokmål | i | 3.02e-02 | 25,994 | 94.0% |
| [fr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_fr.msgpack.gz) | French | français | de | 4.79e-02 | 31,203 | 93.9% |
| [mk](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_mk.msgpack.gz) | Macedonian | македонски | на | 5.89e-02 | 32,925 | 93.9% |
| [id](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_id.msgpack.gz) | Indonesian | bahasa Indonesia | yang | 2.95e-02 | 30,967 | 93.8% |
| [it](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_it.msgpack.gz) | Italian | italiano | di | 3.89e-02 | 35,954 | 93.6% |
| [es](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_es.msgpack.gz) | Spanish | español | de | 6.46e-02 | 34,740 | 93.6% |
| [en](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_en.msgpack.gz) | English | English | the | 5.37e-02 | 28,223 | 93.5% |
| [nl](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_nl.msgpack.gz) | Dutch | Nederlands | de | 5.37e-02 | 28,715 | 93.5% |
| [bn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_bn.msgpack.gz) | Bangla | বাংলা | না | 1.02e-02 | 33,062 | 93.3% |
| [hi](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_hi.msgpack.gz) | Hindi | हिन्दी | के | 3.80e-02 | 24,031 | 93.2% |
| [da](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_da.msgpack.gz) | Danish | dansk | i | 3.09e-02 | 29,321 | 93.2% |
| [lv](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_lv.msgpack.gz) | Latvian | latviešu | un | 3.31e-02 | 45,464 | 92.1% |
| [ro](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_ro.msgpack.gz) | Romanian | română | de | 5.25e-02 | 43,279 | 91.8% |
| [pl](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_pl.msgpack.gz) | Polish | polski | w | 3.55e-02 | 49,664 | 91.6% |
| [is](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_is.msgpack.gz) | Icelandic | íslenska | og | 4.79e-02 | 42,207 | 91.6% |
| [ja](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_ja.msgpack.gz) | Japanese | 日本語 | の | 5.25e-02 | 27,856 | 91.4% |
| [bg](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_bg.msgpack.gz) | Bulgarian | български | на | 5.37e-02 | 35,848 | 91.0% |
| [zh](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_zh.msgpack.gz) | Chinese | 中文 | 的 | 6.17e-02 | 35,723 | 90.7% |
| [sl](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_sl.msgpack.gz) | Slovenian | slovenščina | je | 4.68e-02 | 53,882 | 90.6% |
| [he](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_he.msgpack.gz) | Hebrew | עברית | את | 2.04e-02 | 57,405 | 90.5% |
| [de](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_de.msgpack.gz) | German | Deutsch | die | 3.02e-02 | 38,989 | 90.4% |
| [ar](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_ar.msgpack.gz) | Arabic | العربية | في | 3.47e-02 | 55,611 | 90.2% |
| [ko](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_ko.msgpack.gz) | Korean | 한국어 | 이 | 3.16e-02 | 26,807 | 90.2% |
| [uk](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_uk.msgpack.gz) | Ukrainian | українська | в | 2.51e-02 | 46,286 | 90.0% |
| [cs](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_cs.msgpack.gz) | Czech | čeština | a | 3.24e-02 | 51,744 | 89.9% |
| [el](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_el.msgpack.gz) | Greek | Ελληνικά | και | 3.24e-02 | 43,191 | 89.7% |
| [sk](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_sk.msgpack.gz) | Slovak | slovenčina | a | 3.39e-02 | 59,414 | 88.9% |
| [sh](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_sh.msgpack.gz) | Serbian (Latin) | srpski (latinica) | je | 4.37e-02 | 54,698 | 88.7% |
| [fi](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_fi.msgpack.gz) | Finnish | suomi | ja | 3.63e-02 | 59,143 | 88.7% |
| [hu](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_hu.msgpack.gz) | Hungarian | magyar | a | 9.33e-02 | 46,525 | 87.7% |
| [lt](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_lt.msgpack.gz) | Lithuanian | lietuvių | ir | 3.31e-02 | 63,973 | 87.4% |
| [ru](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_ru.msgpack.gz) | Russian | русский | в | 4.27e-02 | 59,604 | 86.9% |
| [tr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_tr.msgpack.gz) | Turkish | Türkçe | ve | 2.34e-02 | 63,130 | 86.9% |
| [ta](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_ta.msgpack.gz) | Tamil | தமிழ் | ஒரு | 1.02e-02 | 64,756 | 86.2% |
| [th](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_small/small_th.msgpack.gz) | Thai | ไทย | ที่ | 2.00e-02 | 39,680 | 71.0% |
<!-- END GENERATED LANGUAGE TABLE:data_small -->

### data_middle

<!-- BEGIN GENERATED LANGUAGE TABLE:data_middle -->
`data_middle/middle_<code>.msgpack.gz`: wordfreq cBpack (coverage = 10^(-cB/100), kept if >= 1e-6 i.e. cB <= 600). Sorted by cumulative coverage; `float` is the top word's coverage.

| code | language | native name | first word | float | words | cumulative coverage |
|------|----------|-------------|------------|-------|-------|---------------------|
| [ak](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ak.msgpack.gz) | Akan | Akan | to | 1.18e-01 | 15 | 100.0% |
| [cr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_cr.msgpack.gz) | Cree | Cree | see | 1.11e-01 | 15 | 100.0% |
| [kl](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_kl.msgpack.gz) | Kalaallisut | kalaallisut | see | 1.11e-01 | 15 | 100.0% |
| [lrc](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_lrc.msgpack.gz) | Northern Luri | لۊری شومالی | __noeditsection__ | 1.67e-01 | 6 | 100.0% |
| [mus](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_mus.msgpack.gz) | Muscogee | Mvskoke | ē | 3.17e-02 | 87 | 100.0% |
| [pih](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_pih.msgpack.gz) | Pitcairn-Norfolk | Pitcairn-Norfolk | the | 8.33e-02 | 63 | 100.0% |
| [mh](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_mh.msgpack.gz) | Marshallese | Marshallese | marshall | 2.41e-02 | 932 | 99.9% |
| [ng](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ng.msgpack.gz) | Ndonga | Ndonga | na | 1.36e-02 | 3,706 | 99.1% |
| [cho](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_cho.msgpack.gz) | Choctaw | Chahta | a | 1.04e-02 | 645 | 98.8% |
| [guc](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_guc.msgpack.gz) | Wayuu | Wayuu | tü | 4.53e-02 | 37,661 | 98.6% |
| [bo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_bo.msgpack.gz) | Tibetan | བོད་སྐད་ | པ | 3.65e-02 | 7,102 | 98.5% |
| [dz](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_dz.msgpack.gz) | Dzongkha | རྫོང་ཁ | དང | 2.37e-02 | 8,208 | 98.4% |
| [ve](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ve.msgpack.gz) | Venda | tshiVenḓa | u | 4.68e-02 | 16,813 | 98.3% |
| [blk](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_blk.msgpack.gz) | Pa'o Karen | Pa'o Karen | တ | 3.36e-02 | 5,999 | 98.3% |
| [tig](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_tig.msgpack.gz) | Tigre | Tigre | እግል | 2.54e-02 | 75,440 | 98.3% |
| [tdd](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_tdd.msgpack.gz) | Tai Nüa | Tai Nüa | ᥛᥫᥒᥰ | 1.47e-02 | 9,619 | 98.0% |
| [ho](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ho.msgpack.gz) | Hiri Motu | Hiri Motu | ia | 5.29e-02 | 263 | 97.9% |
| [syl](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_syl.msgpack.gz) | Sylheti | Sylheti | ꠀꠞ | 2.05e-02 | 26,199 | 97.7% |
| [ts](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ts.msgpack.gz) | Tsonga | Tsonga | ku | 3.64e-02 | 33,258 | 97.7% |
| [wo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_wo.msgpack.gz) | Wolof | Wolof | ci | 4.86e-02 | 42,584 | 97.7% |
| [fj](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_fj.msgpack.gz) | Fijian | Fijian | na | 1.21e-01 | 12,976 | 97.7% |
| [to](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_to.msgpack.gz) | Tongan | lea fakatonga | e | 6.02e-02 | 15,961 | 97.6% |
| [om](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_om.msgpack.gz) | Oromo | Oromoo | fi | 2.17e-02 | 92,462 | 97.6% |
| [nqo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_nqo.msgpack.gz) | N’Ko | ߒߞߏ | ߟߊ߫ | 4.02e-02 | 62,149 | 97.5% |
| [jbo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_jbo.msgpack.gz) | Lojban | la .lojban. | cu | 7.99e-02 | 26,764 | 97.5% |
| [ann](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ann.msgpack.gz) | Obolo | Obolo | me | 7.72e-02 | 9,579 | 97.4% |
| [kaj](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_kaj.msgpack.gz) | Jju | Kaje | a̱ | 4.02e-02 | 16,754 | 97.4% |
| [kbp](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_kbp.msgpack.gz) | Kabiyè | Kabiyè | nɛ | 5.29e-02 | 43,528 | 97.3% |
| [din](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_din.msgpack.gz) | Dinka | Dinka | ku | 3.95e-02 | 15,863 | 97.3% |
| [mnw](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_mnw.msgpack.gz) | Mon | Mon | င် | 3.29e-02 | 11,318 | 97.2% |
| [bdr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_bdr.msgpack.gz) | West Coast Bajau | West Coast Bajau | ni | 2.91e-02 | 6,720 | 97.1% |
| [arc](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_arc.msgpack.gz) | Aramaic | Aramaic | ܡܢ | 2.00e-02 | 18,731 | 97.0% |
| [sm](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_sm.msgpack.gz) | Samoan | Samoan | le | 1.15e-01 | 17,178 | 96.7% |
| [rki](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_rki.msgpack.gz) | Rakhine | Rakhine | ရေ | 4.40e-02 | 16,161 | 96.6% |
| [kj](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_kj.msgpack.gz) | Kuanyama | Kuanyama | zh | 1.41e-02 | 446 | 96.6% |
| [jam](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_jam.msgpack.gz) | Jamaican Creole English | Jamaican Creole English | di | 7.06e-02 | 23,404 | 96.5% |
| [rn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_rn.msgpack.gz) | Rundi | Ikirundi | mu | 5.25e-02 | 26,583 | 96.5% |
| [guw](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_guw.msgpack.gz) | Gun | Gun | to | 5.29e-02 | 34,094 | 96.5% |
| [btm](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_btm.msgpack.gz) | Batak Mandailing | Batak Mandailing | na | 3.72e-02 | 27,552 | 96.5% |
| [ace](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ace.msgpack.gz) | Acehnese | Acehnese | nakeuh | 3.99e-02 | 38,587 | 96.5% |
| [za](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_za.msgpack.gz) | Zhuang | Vahcuengh | dwg | 2.06e-02 | 29,293 | 96.4% |
| [gcr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_gcr.msgpack.gz) | Guianese Creole French | Guianese Creole French | di | 7.67e-02 | 30,517 | 96.3% |
| [pwn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_pwn.msgpack.gz) | Paiwan | Paiwan | a | 1.40e-01 | 22,129 | 96.3% |
| [kcg](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_kcg.msgpack.gz) | Tyap | Katab | ma̱ng | 2.19e-02 | 36,302 | 96.2% |
| [ki](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ki.msgpack.gz) | Kikuyu | Gikuyu | na | 4.26e-02 | 43,410 | 96.2% |
| [pi](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_pi.msgpack.gz) | Pali | Pali | च | 1.51e-02 | 11,349 | 96.2% |
| [bew](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_bew.msgpack.gz) | Betawi | Betawi | di | 2.61e-02 | 44,859 | 96.1% |
| [haw](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_haw.msgpack.gz) | Hawaiian | ʻŌlelo Hawaiʻi | ka | 6.43e-02 | 29,694 | 96.1% |
| [mni](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_mni.msgpack.gz) | Manipuri | মৈতৈলোন্ | ꯑꯁꯤ | 2.52e-02 | 94,448 | 96.0% |
| [ady](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ady.msgpack.gz) | Adyghe | Adyghe | и | 1.18e-02 | 36,433 | 96.0% |
| [atj](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_atj.msgpack.gz) | Atikamekw | Atikamekw | e | 5.33e-02 | 19,332 | 96.0% |
| [nv](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_nv.msgpack.gz) | Navajo | Diné Bizaad | éí | 1.32e-01 | 14,432 | 96.0% |
| [nia](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_nia.msgpack.gz) | Nias | Nias | ba | 8.29e-02 | 37,188 | 96.0% |
| [anp](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_anp.msgpack.gz) | Angika | Angika | के | 5.05e-02 | 60,928 | 95.9% |
| [cdo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_cdo.msgpack.gz) | Min Dong Chinese | Min Dong Chinese | gì | 3.07e-02 | 54,638 | 95.9% |
| [igl](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_igl.msgpack.gz) | Igala | Igala | the | 2.09e-02 | 65,878 | 95.9% |
| [lad](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_lad.msgpack.gz) | Ladino | Ladino | de | 7.05e-02 | 88,234 | 95.9% |
| [kge](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_kge.msgpack.gz) | Komering | Komering | say | 2.59e-02 | 25,161 | 95.8% |
| [srn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_srn.msgpack.gz) | Sranan Tongo | Sranan Tongo | e | 6.44e-02 | 11,631 | 95.8% |
| [ti](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ti.msgpack.gz) | Tigrinya | ትግርኛ | ኣብ | 3.70e-02 | 23,452 | 95.8% |
| [ppl](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ppl.msgpack.gz) | Pipil | Pipil | ne | 7.27e-02 | 32,097 | 95.8% |
| [nso](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_nso.msgpack.gz) | Northern Sotho | Sesotho sa Leboa | go | 4.36e-02 | 36,354 | 95.8% |
| [mi](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_mi.msgpack.gz) | Māori | Māori | te | 9.69e-02 | 30,232 | 95.7% |
| [iba](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_iba.msgpack.gz) | Iban | Iban | enggau | 2.91e-02 | 44,738 | 95.7% |
| [tpi](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_tpi.msgpack.gz) | Tok Pisin | Tok Pisin | i | 6.95e-02 | 10,374 | 95.7% |
| [st](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_st.msgpack.gz) | Southern Sotho | Sesotho | le | 4.11e-02 | 43,429 | 95.7% |
| [ksh](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ksh.msgpack.gz) | Colognian | Kölsch | un | 2.15e-02 | 71,967 | 95.6% |
| [ty](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ty.msgpack.gz) | Tahitian | Tahitian | te | 1.21e-01 | 7,149 | 95.6% |
| [tay](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_tay.msgpack.gz) | Atayal | Atayal | na | 4.18e-02 | 49,693 | 95.6% |
| [pcm](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_pcm.msgpack.gz) | Nigerian Pidgin | Naijíriá Píjin | for | 3.35e-02 | 43,503 | 95.6% |
| [nr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_nr.msgpack.gz) | South Ndebele | South Ndebele | i | 1.01e-02 | 42,811 | 95.5% |
| [kai](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_kai.msgpack.gz) | Karekare | Karekare | mà | 6.89e-02 | 14,008 | 95.5% |
| [trv](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_trv.msgpack.gz) | Taroko | patas Taroko | ka | 4.54e-02 | 71,321 | 95.4% |
| [dtp](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_dtp.msgpack.gz) | Central Dusun | Central Dusun | do | 3.87e-02 | 89,726 | 95.3% |
| [bm](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_bm.msgpack.gz) | Bambara | bamanakan | ye | 4.47e-02 | 16,650 | 95.2% |
| [fat](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_fat.msgpack.gz) | Fanti | Akan | a | 5.18e-02 | 43,072 | 95.2% |
| [kab](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_kab.msgpack.gz) | Kabyle | Taqbaylit | n | 8.81e-02 | 95,696 | 95.2% |
| [isv](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_isv.msgpack.gz) | Unknown language [isv] | Unknown language [isv] | v | 3.29e-02 | 96,965 | 95.2% |
| [ch](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ch.msgpack.gz) | Chamorro | Chamorro | i | 8.76e-02 | 5,789 | 95.1% |
| [fon](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_fon.msgpack.gz) | - | - | tɔn | 5.24e-02 | 29,774 | 95.1% |
| [ln](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ln.msgpack.gz) | Lingala | lingála | ya | 1.03e-01 | 53,855 | 95.1% |
| [ks](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ks.msgpack.gz) | Kashmiri | کٲشُر | مَنٛز | 3.86e-02 | 96,182 | 95.1% |
| [hak](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_hak.msgpack.gz) | Hakka Chinese | Hakka Chinese | ke | 3.08e-02 | 63,803 | 95.0% |
| [kg](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_kg.msgpack.gz) | Kongo | Kongo | ya | 1.38e-01 | 17,260 | 94.9% |
| [ang](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ang.msgpack.gz) | Old English | Ænglisc | and | 3.05e-02 | 92,865 | 94.8% |
| [bbc](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_bbc.msgpack.gz) | Batak Toba | Batak Toba | na | 3.42e-02 | 32,250 | 94.7% |
| [mag](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_mag.msgpack.gz) | Magahi | Magahi | हे | 2.60e-02 | 72,603 | 94.7% |
| [pag](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_pag.msgpack.gz) | Pangasinan | Pangasinan | ed | 3.34e-02 | 25,235 | 94.7% |
| [knc](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_knc.msgpack.gz) | Central Kanuri | Kanuri | a | 3.36e-02 | 77,535 | 94.7% |
| [got](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_got.msgpack.gz) | Gothic | Gothic | 𐌹𐌽 | 1.75e-02 | 27,180 | 94.7% |
| [bol](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_bol.msgpack.gz) | Bole | Bole | ga | 8.24e-02 | 20,556 | 94.7% |
| [ss](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ss.msgpack.gz) | Swati | siSwati | kanye | 1.32e-02 | 55,954 | 94.6% |
| [awa](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_awa.msgpack.gz) | Awadhi | Awadhi | के | 3.64e-02 | 63,307 | 94.5% |
| [kbd](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_kbd.msgpack.gz) | Kabardian | Kabardian | и | 3.56e-02 | 62,074 | 94.4% |
| [gur](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_gur.msgpack.gz) | Frafra | Frafra | la | 8.08e-02 | 43,823 | 94.4% |
| [tok](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_tok.msgpack.gz) | Toki Pona | toki pona | li | 7.94e-02 | 75,512 | 94.2% |
| [ik](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ik.msgpack.gz) | Inupiaq | Inupiaq | suli | 1.17e-02 | 8,928 | 94.2% |
| [iu](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_iu.msgpack.gz) | Inuktitut | Inuktitut | ᐊᒻᒪ | 1.63e-02 | 14,398 | 94.2% |
| [nup](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_nup.msgpack.gz) | Nupe-Nupe-Tako | Nupe-Nupe-Tako | nan | 4.18e-02 | 17,989 | 94.1% |
| [ny](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ny.msgpack.gz) | Nyanja | Nyanja | ndi | 4.43e-02 | 37,198 | 93.9% |
| [tet](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_tet.msgpack.gz) | Tetum | Tetum | iha | 3.80e-02 | 32,463 | 93.9% |
| [inh](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_inh.msgpack.gz) | Ingush | Ingush | а | 2.43e-02 | 58,806 | 93.9% |
| [lfn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_lfn.msgpack.gz) | Lingua Franca Nova | Lingua Franca Nova | la | 8.65e-02 | 38,526 | 93.9% |
| [ee](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ee.msgpack.gz) | Ewe | eʋegbe | ƒe | 5.73e-02 | 30,395 | 93.9% |
| [my](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_my.msgpack.gz) | Burmese | မြန်မာ | သည် | 2.67e-02 | 19,523 | 93.9% |
| [gor](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_gor.msgpack.gz) | Gorontalo | Gorontalo | to | 3.68e-02 | 69,498 | 93.8% |
| [pdc](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_pdc.msgpack.gz) | Pennsylvania German | Pennsylvania German | in | 2.67e-02 | 28,318 | 93.7% |
| [dty](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_dty.msgpack.gz) | Dotyali | Dotyali | रे | 1.30e-02 | 95,554 | 93.7% |
| [gan](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_gan.msgpack.gz) | Gan Chinese | Gan Chinese | 嗰 | 4.39e-02 | 42,715 | 93.6% |
| [chy](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_chy.msgpack.gz) | Cheyenne | Cheyenne | na'éstse | 3.05e-02 | 3,354 | 93.4% |
| [frp](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_frp.msgpack.gz) | Arpitan | Arpitan | de | 6.30e-02 | 65,606 | 93.4% |
| [sg](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_sg.msgpack.gz) | Sango | Sängö | tî | 5.61e-02 | 4,702 | 93.4% |
| [tly](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_tly.msgpack.gz) | Talysh | Talysh | cy | 2.12e-02 | 50,908 | 93.3% |
| [km](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_km.msgpack.gz) | Khmer | ខ្មែរ | បាន | 1.84e-02 | 33,431 | 93.3% |
| [kw](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_kw.msgpack.gz) | Cornish | kernewek | a | 4.20e-02 | 79,531 | 93.1% |
| [szy](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_szy.msgpack.gz) | Sakizaya | Sakizaya | a | 4.89e-02 | 51,922 | 93.1% |
| [skr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_skr.msgpack.gz) | Saraiki | سرائیکی | دے | 3.01e-02 | 38,501 | 93.1% |
| [stq](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_stq.msgpack.gz) | Saterland Frisian | Saterland Frisian | fon | 2.97e-02 | 83,000 | 93.0% |
| [mos](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_mos.msgpack.gz) | Mossi | Mossi | a | 6.02e-02 | 25,495 | 93.0% |
| [nap](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_nap.msgpack.gz) | Neapolitan | Neapolitan | e | 9.29e-02 | 90,741 | 92.9% |
| [tw](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_tw.msgpack.gz) | Twi | Akan | a | 5.84e-02 | 26,835 | 92.9% |
| [yi](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_yi.msgpack.gz) | Yiddish | ייִדיש | די | 3.42e-02 | 40,850 | 92.9% |
| [chr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_chr.msgpack.gz) | Cherokee | ᏣᎳᎩ | ꭰꮄ | 2.16e-02 | 13,184 | 92.9% |
| [pnt](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_pnt.msgpack.gz) | Pontic | Pontic | τη | 3.59e-02 | 12,620 | 92.8% |
| [bi](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_bi.msgpack.gz) | Bislama | Bislama | blong | 7.03e-02 | 8,565 | 92.8% |
| [av](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_av.msgpack.gz) | Avaric | Avaric | ва | 1.42e-02 | 94,335 | 92.8% |
| [bh](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_bh.msgpack.gz) | Bihari languages | भोजपुरी | के | 8.07e-02 | 40,392 | 92.8% |
| [dv](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_dv.msgpack.gz) | Divehi | Divehi | ind | 1.83e-02 | 97,018 | 92.7% |
| [lo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_lo.msgpack.gz) | Lao | ລາວ | ແລະ | 1.63e-02 | 35,674 | 92.4% |
| [tum](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_tum.msgpack.gz) | Tumbuka | Tumbuka | mu | 3.88e-02 | 50,443 | 92.3% |
| [shn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_shn.msgpack.gz) | Shan | တႆး | င်း | 4.18e-02 | 19,487 | 92.3% |
| [co](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_co.msgpack.gz) | Corsican | corsu | di | 6.31e-02 | 43,143 | 92.3% |
| [nah](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_nah.msgpack.gz) | Nahuatl languages | Nāhuatl | in | 7.34e-02 | 28,227 | 92.2% |
| [krc](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_krc.msgpack.gz) | Karachay-Balkar | Karachay-Balkar | бла | 2.08e-02 | 88,125 | 92.0% |
| [rsk](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_rsk.msgpack.gz) | Unknown language [rsk] | Unknown language [rsk] | и | 3.71e-02 | 96,365 | 92.0% |
| [cu](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_cu.msgpack.gz) | Church Slavic | Church Slavic | и | 3.59e-02 | 23,243 | 92.0% |
| [ia](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ia.msgpack.gz) | Interlingua | interlingua | le | 7.53e-02 | 42,271 | 92.0% |
| [pap](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_pap.msgpack.gz) | Papiamento | Papiamentu | di | 7.64e-02 | 38,004 | 91.9% |
| [se](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_se.msgpack.gz) | Northern Sami | davvisámegiella | lea | 3.58e-02 | 81,073 | 91.9% |
| [pfl](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_pfl.msgpack.gz) | Palatine German | Palatine German | de | 2.66e-02 | 91,182 | 91.6% |
| [ltg](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ltg.msgpack.gz) | Latgalian | Latgalian | i | 2.93e-02 | 32,841 | 91.6% |
| [wa](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_wa.msgpack.gz) | Walloon | walon | l | 2.75e-02 | 35,540 | 91.6% |
| [lld](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_lld.msgpack.gz) | Ladin | ladin | de | 7.38e-02 | 21,531 | 91.6% |
| [mwl](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_mwl.msgpack.gz) | Mirandese | Mirandese | de | 8.57e-02 | 42,730 | 91.6% |
| [dsb](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_dsb.msgpack.gz) | Lower Sorbian | dolnoserbšćina | a | 2.73e-02 | 81,621 | 91.5% |
| [bxr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_bxr.msgpack.gz) | Russia Buriat | Buriat | ба | 6.64e-03 | 94,093 | 91.5% |
| [alt](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_alt.msgpack.gz) | Southern Altai | Southern Altai | ла | 1.08e-02 | 66,151 | 91.4% |
| [csb](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_csb.msgpack.gz) | Kashubian | Kashubian | w | 3.81e-02 | 95,757 | 91.4% |
| [min](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_min.msgpack.gz) | Minangkabau | Minangkabau | dari | 3.18e-02 | 23,209 | 91.3% |
| [olo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_olo.msgpack.gz) | Livvi | Livvi | on | 4.11e-02 | 78,349 | 91.3% |
| [fur](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_fur.msgpack.gz) | Friulian | furlan | di | 4.46e-02 | 47,380 | 91.3% |
| [sd](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_sd.msgpack.gz) | Sindhi | سنڌي | جي | 4.36e-02 | 38,853 | 91.2% |
| [rmy](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_rmy.msgpack.gz) | Vlax Romani | Romany | o | 3.54e-02 | 22,317 | 91.2% |
| [pcd](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_pcd.msgpack.gz) | Picard | Picard | pi | 1.66e-02 | 93,693 | 91.0% |
| [rm](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_rm.msgpack.gz) | Romansh | rumantsch | da | 5.49e-02 | 38,481 | 90.8% |
| [dga](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_dga.msgpack.gz) | Southern Dagaare | Southern Dagaare | a | 7.18e-02 | 40,311 | 90.8% |
| [bjn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_bjn.msgpack.gz) | Banjar | Banjar | nang | 2.68e-02 | 45,327 | 90.8% |
| [kus](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_kus.msgpack.gz) | Kusaal | Kusaal | ka | 4.06e-02 | 29,425 | 90.8% |
| [tn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_tn.msgpack.gz) | Tswana | Setswana | le | 4.44e-02 | 30,405 | 90.7% |
| [sn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_sn.msgpack.gz) | Shona | chiShona | vanoti | 2.11e-02 | 65,139 | 90.7% |
| [wuu](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_wuu.msgpack.gz) | Wu Chinese | Wu Chinese | 个 | 3.60e-02 | 36,699 | 90.6% |
| [os](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_os.msgpack.gz) | Ossetic | ирон | у | 2.43e-02 | 94,186 | 90.6% |
| [th](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_th.msgpack.gz) | Thai | ไทย | ที่ | 2.08e-02 | 26,131 | 90.6% |
| [ii](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ii.msgpack.gz) | Sichuan Yi | ꆈꌠꉙ | zh | 1.03e-02 | 1,870 | 90.3% |
| [ps](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ps.msgpack.gz) | Pashto | پښتو | د | 8.65e-02 | 41,047 | 90.3% |
| [xh](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_xh.msgpack.gz) | Xhosa | IsiXhosa | kunye | 1.29e-02 | 98,092 | 89.9% |
| [udm](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_udm.msgpack.gz) | Udmurt | Udmurt | но | 1.97e-02 | 91,194 | 89.9% |
| [ig](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ig.msgpack.gz) | Igbo | Igbo | na | 9.15e-02 | 29,721 | 89.7% |
| [glk](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_glk.msgpack.gz) | Gilaki | Gilaki | أ | 5.81e-02 | 27,779 | 89.7% |
| [ami](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ami.msgpack.gz) | Amis | Amis | a | 5.80e-02 | 35,693 | 89.6% |
| [ha](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ha.msgpack.gz) | Hausa | Hausa | da | 6.38e-02 | 27,758 | 89.5% |
| [yo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_yo.msgpack.gz) | Yoruba | Èdè Yorùbá | ní | 2.37e-02 | 37,982 | 89.5% |
| [koi](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_koi.msgpack.gz) | Komi-Permyak | Komi-Permyak | коми | 1.55e-02 | 73,392 | 89.5% |
| [sc](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_sc.msgpack.gz) | Sardinian | sardu | de | 8.14e-02 | 48,818 | 89.5% |
| [ur](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ur.msgpack.gz) | Urdu | اردو | کے | 3.57e-02 | 31,639 | 89.5% |
| [zh](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_zh.msgpack.gz) | Chinese | 中文 | 的 | 3.31e-02 | 48,528 | 89.4% |
| [xal](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_xal.msgpack.gz) | Kalmyk | Kalmyk | болҗана | 1.15e-02 | 16,358 | 89.4% |
| [pms](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_pms.msgpack.gz) | Piedmontese | Piedmontese | a | 7.64e-02 | 34,294 | 89.4% |
| [lez](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_lez.msgpack.gz) | Lezghian | Lezghian | ва | 1.43e-02 | 91,798 | 89.3% |
| [fr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_fr.msgpack.gz) | French | français | de | 6.14e-02 | 44,497 | 89.3% |
| [ce](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ce.msgpack.gz) | Chechen | нохчийн | а | 3.23e-02 | 9,521 | 89.3% |
| [zea](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_zea.msgpack.gz) | Zeelandic | Zeelandic | de | 5.00e-02 | 78,994 | 89.3% |
| [en](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_en.msgpack.gz) | English | English | the | 6.75e-02 | 36,592 | 89.2% |
| [pnb](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_pnb.msgpack.gz) | Western Panjabi | لہندا پنجابی | دے | 3.58e-02 | 37,345 | 89.2% |
| [ja](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ja.msgpack.gz) | Japanese | 日本語 | の | 4.62e-02 | 39,507 | 89.2% |
| [su](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_su.msgpack.gz) | Sundanese | Basa Sunda | di | 1.86e-02 | 45,802 | 89.2% |
| [mzn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_mzn.msgpack.gz) | Mazanderani | مازرونی | و | 4.56e-02 | 29,778 | 89.2% |
| [ceb](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ceb.msgpack.gz) | Cebuano | Cebuano | sa | 5.70e-02 | 18,043 | 89.1% |
| [es](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_es.msgpack.gz) | Spanish | español | de | 7.57e-02 | 43,143 | 89.1% |
| [vi](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_vi.msgpack.gz) | Vietnamese | Tiếng Việt | là | 1.61e-02 | 22,039 | 89.1% |
| [ay](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ay.msgpack.gz) | Aymara | Aymara | de | 2.18e-02 | 64,915 | 89.0% |
| [ilo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ilo.msgpack.gz) | Iloko | Ilokano | ti | 8.66e-02 | 42,406 | 88.9% |
| [lij](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_lij.msgpack.gz) | Ligurian | ligure | a | 6.40e-02 | 57,641 | 88.9% |
| [ext](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ext.msgpack.gz) | Extremaduran | Extremaduran | de | 4.91e-02 | 69,744 | 88.9% |
| [pa](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_pa.msgpack.gz) | Punjabi | ਪੰਜਾਬੀ | ਵਿੱਚ | 2.93e-02 | 38,890 | 88.9% |
| [eml](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_eml.msgpack.gz) | Unknown language [eml] | Unknown language [eml] | al | 3.48e-02 | 41,678 | 88.8% |
| [gv](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_gv.msgpack.gz) | Manx | Gaelg | as | 2.96e-02 | 35,197 | 88.6% |
| [nrm](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_nrm.msgpack.gz) | Narom | Narom | la | 2.33e-02 | 53,327 | 88.6% |
| [so](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_so.msgpack.gz) | Somali | Soomaali | oo | 2.70e-02 | 48,692 | 88.6% |
| [gpe](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_gpe.msgpack.gz) | Ghanaian Pidgin English | Ghanaian Pidgin English | de | 4.55e-02 | 31,498 | 88.5% |
| [mt](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_mt.msgpack.gz) | Maltese | Malti | ta | 3.32e-02 | 41,497 | 88.5% |
| [avk](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_avk.msgpack.gz) | Kotava | Kotava | en | 3.61e-02 | 34,864 | 88.4% |
| [lmo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_lmo.msgpack.gz) | Lombard | Lombard | de | 6.82e-02 | 50,118 | 88.4% |
| [ab](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ab.msgpack.gz) | Abkhazian | Аԥсшәа | уи | 9.43e-03 | 95,232 | 88.3% |
| [gd](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_gd.msgpack.gz) | Scottish Gaelic | Gàidhlig | an | 5.33e-02 | 35,839 | 88.3% |
| [hi](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_hi.msgpack.gz) | Hindi | हिन्दी | के | 4.28e-02 | 38,440 | 88.2% |
| [crh](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_crh.msgpack.gz) | Crimean Tatar | Crimean Tatar | bir | 3.42e-02 | 96,928 | 88.2% |
| [rw](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_rw.msgpack.gz) | Kinyarwanda | Ikinyarwanda | mu | 3.75e-02 | 58,910 | 88.1% |
| [fa](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_fa.msgpack.gz) | Persian | فارسی | در | 3.82e-02 | 38,832 | 88.0% |
| [ht](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ht.msgpack.gz) | Haitian Creole | Kreyòl Ayisyen | nan | 3.38e-02 | 40,748 | 88.0% |
| [pt](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_pt.msgpack.gz) | Portuguese | português | de | 5.63e-02 | 44,452 | 88.0% |
| [new](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_new.msgpack.gz) | Newari | Newari | थ्व | 4.69e-02 | 26,915 | 87.9% |
| [hif](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_hif.msgpack.gz) | Fiji Hindi | Fiji Hindi | ke | 5.92e-02 | 40,068 | 87.8% |
| [sat](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_sat.msgpack.gz) | Santali | ᱥᱟᱱᱛᱟᱲᱤ | ᱨᱮ | 4.03e-02 | 40,651 | 87.7% |
| [scn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_scn.msgpack.gz) | Sicilian | sicilianu | di | 5.26e-02 | 60,385 | 87.4% |
| [mdf](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_mdf.msgpack.gz) | Moksha | мокшень кяль | isbn | 9.37e-03 | 84,011 | 87.4% |
| [am](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_am.msgpack.gz) | Amharic | አማርኛ | ነው | 1.39e-02 | 97,448 | 87.4% |
| [bcl](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_bcl.msgpack.gz) | Central Bikol | Bikol | sa | 5.31e-02 | 48,721 | 87.4% |
| [gag](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_gag.msgpack.gz) | Gagauz | Gagauz | hem | 1.16e-02 | 73,595 | 87.4% |
| [bpy](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_bpy.msgpack.gz) | Bishnupriya | Bishnupriya | বারো | 3.59e-02 | 40,912 | 87.2% |
| [lg](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_lg.msgpack.gz) | Ganda | Luganda | mu | 6.20e-02 | 51,014 | 87.2% |
| [gu](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_gu.msgpack.gz) | Gujarati | ગુજરાતી | છે | 4.13e-02 | 56,152 | 87.2% |
| [tk](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_tk.msgpack.gz) | Turkmen | türkmen dili | we | 2.20e-02 | 74,024 | 87.1% |
| [ie](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ie.msgpack.gz) | Interlingue | Interlingue | li | 6.85e-02 | 33,904 | 87.1% |
| [mai](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_mai.msgpack.gz) | Maithili | मैथिली | अछि | 2.42e-02 | 52,765 | 87.0% |
| [ga](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ga.msgpack.gz) | Irish | Gaeilge | an | 3.96e-02 | 43,228 | 87.0% |
| [kaa](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_kaa.msgpack.gz) | Kara-Kalpak | қарақалпақша | hám | 2.55e-02 | 56,432 | 86.9% |
| [vec](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_vec.msgpack.gz) | Venetian | veneto | de | 6.03e-02 | 51,474 | 86.9% |
| [sw](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_sw.msgpack.gz) | Swahili | Kiswahili | ya | 6.02e-02 | 38,764 | 86.9% |
| [it](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_it.msgpack.gz) | Italian | italiano | di | 3.93e-02 | 49,776 | 86.9% |
| [arz](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_arz.msgpack.gz) | Egyptian Arabic | Egyptian Arabic | فى | 3.65e-02 | 28,697 | 86.8% |
| [mad](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_mad.msgpack.gz) | Madurese | Madurese | è | 3.28e-02 | 49,345 | 86.8% |
| [sq](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_sq.msgpack.gz) | Albanian | shqip | të | 5.48e-02 | 51,916 | 86.7% |
| [sco](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_sco.msgpack.gz) | Scots | Scots | the | 6.73e-02 | 43,197 | 86.6% |
| [gl](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_gl.msgpack.gz) | Galician | galego | de | 5.70e-02 | 46,940 | 86.5% |
| [zgh](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_zgh.msgpack.gz) | Standard Moroccan Tamazight | ⵜⴰⵎⴰⵣⵉⵖⵜ | ⵏ | 1.15e-01 | 25,878 | 86.5% |
| [kv](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_kv.msgpack.gz) | Komi | Komi | коми | 1.61e-02 | 96,438 | 86.5% |
| [ff](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ff.msgpack.gz) | Fula | Pulaar | e | 7.46e-02 | 38,132 | 86.5% |
| [vls](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_vls.msgpack.gz) | West Flemish | West Flemish | de | 4.76e-02 | 51,455 | 86.2% |
| [ms](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ms.msgpack.gz) | Malay | bahasa Malaysia | dan | 2.33e-02 | 40,190 | 86.2% |
| [shi](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_shi.msgpack.gz) | Tachelhit | ⵜⴰⵛⵍⵃⵉⵜ | n | 1.17e-01 | 20,991 | 86.2% |
| [oc](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_oc.msgpack.gz) | Occitan | occitan | de | 7.13e-02 | 49,509 | 86.1% |
| [tcy](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_tcy.msgpack.gz) | Tulu | Tulu | ಬೊಕ್ಕ | 1.15e-02 | 90,698 | 86.1% |
| [ast](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ast.msgpack.gz) | Asturian | asturianu | de | 6.48e-02 | 49,384 | 86.0% |
| [nov](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_nov.msgpack.gz) | Novial | Novial | li | 4.59e-02 | 27,267 | 86.0% |
| [ca](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ca.msgpack.gz) | Catalan | català | de | 6.16e-02 | 43,751 | 86.0% |
| [myv](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_myv.msgpack.gz) | Erzya | эрзянь кель | ды | 1.35e-02 | 94,391 | 85.9% |
| [lbe](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_lbe.msgpack.gz) | Lak | Lak | ва | 1.64e-02 | 12,855 | 85.8% |
| [or](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_or.msgpack.gz) | Odia | ଓଡ଼ିଆ | ଓ | 1.57e-02 | 51,863 | 85.7% |
| [ku](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ku.msgpack.gz) | Kurdish | kurdî (kurmancî) | li | 2.89e-02 | 45,601 | 85.7% |
| [af](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_af.msgpack.gz) | Afrikaans | Afrikaans | die | 6.99e-02 | 42,441 | 85.6% |
| [gom](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_gom.msgpack.gz) | Goan Konkani | Goan Konkani | आनी | 1.64e-02 | 96,565 | 85.6% |
| [li](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_li.msgpack.gz) | Limburgish | Limburgish | de | 5.59e-02 | 57,713 | 85.6% |
| [he](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_he.msgpack.gz) | Hebrew | עברית | של | 2.44e-02 | 71,783 | 85.6% |
| [mrj](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_mrj.msgpack.gz) | Western Mari | Western Mari | дӓ | 1.14e-02 | 83,640 | 85.5% |
| [mhr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_mhr.msgpack.gz) | Eastern Mari | Mari | марий | 1.97e-02 | 48,661 | 85.5% |
| [war](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_war.msgpack.gz) | Waray | Waray | nga | 5.84e-02 | 33,389 | 85.5% |
| [fil](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_fil.msgpack.gz) | Filipino | Filipino | ng | 5.57e-02 | 41,689 | 85.4% |
| [sah](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_sah.msgpack.gz) | Yakut | саха тыла | уонна | 1.32e-02 | 55,601 | 85.4% |
| [fy](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_fy.msgpack.gz) | Western Frisian | Frysk | de | 4.99e-02 | 44,944 | 85.4% |
| [br](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_br.msgpack.gz) | Breton | brezhoneg | e | 4.47e-02 | 44,503 | 85.2% |
| [id](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_id.msgpack.gz) | Indonesian | bahasa Indonesia | dan | 2.25e-02 | 43,544 | 85.1% |
| [si](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_si.msgpack.gz) | Sinhala | සිංහල | සහ | 1.24e-02 | 59,667 | 85.1% |
| [as](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_as.msgpack.gz) | Assamese | অসমীয়া | আৰু | 2.71e-02 | 53,498 | 85.0% |
| [mk](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_mk.msgpack.gz) | Macedonian | македонски | на | 5.66e-02 | 52,697 | 84.8% |
| [tt](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_tt.msgpack.gz) | Tatar | татар | һәм | 1.17e-02 | 18,772 | 84.8% |
| [io](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_io.msgpack.gz) | Ido | Ido | la | 4.87e-02 | 32,407 | 84.8% |
| [ug](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ug.msgpack.gz) | Uyghur | ئۇيغۇرچە | ۋە | 1.33e-02 | 70,141 | 84.7% |
| [ckb](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ckb.msgpack.gz) | Central Kurdish | کوردیی ناوەندی | لە | 5.62e-02 | 53,512 | 84.7% |
| [ban](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ban.msgpack.gz) | Balinese | Balinese | ring | 2.71e-02 | 41,850 | 84.7% |
| [jv](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_jv.msgpack.gz) | Javanese | Jawa | ing | 2.91e-02 | 53,706 | 84.7% |
| [diq](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_diq.msgpack.gz) | Dimli (individual language) | Zaza | de | 4.55e-02 | 59,774 | 84.5% |
| [tg](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_tg.msgpack.gz) | Tajik | тоҷикӣ | дар | 3.57e-02 | 49,196 | 84.3% |
| [ary](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ary.msgpack.gz) | Moroccan Arabic | Moroccan Arabic | ف | 3.15e-02 | 45,507 | 84.2% |
| [an](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_an.msgpack.gz) | Aragonese | aragonés | de | 5.99e-02 | 44,617 | 84.1% |
| [hyw](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_hyw.msgpack.gz) | Western Armenian | Western Armenian | եւ | 2.67e-02 | 67,897 | 84.0% |
| [gn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_gn.msgpack.gz) | Guarani | avañe’ẽ | ha | 3.46e-02 | 45,557 | 84.0% |
| [mn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_mn.msgpack.gz) | Mongolian | монгол | нь | 1.87e-02 | 51,761 | 83.9% |
| [bn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_bn.msgpack.gz) | Bangla | বাংলা | এবং | 1.61e-02 | 51,567 | 83.8% |
| [ar](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ar.msgpack.gz) | Arabic | العربية | في | 3.46e-02 | 66,003 | 83.8% |
| [cy](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_cy.msgpack.gz) | Welsh | Cymraeg | y | 4.13e-02 | 37,105 | 83.6% |
| [zu](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_zu.msgpack.gz) | Zulu | isiZulu | i | 1.08e-02 | 80,323 | 83.5% |
| [el](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_el.msgpack.gz) | Greek | Ελληνικά | του | 2.89e-02 | 54,889 | 83.4% |
| [dag](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_dag.msgpack.gz) | Dagbani | Dagbani | ni | 1.76e-02 | 48,588 | 83.4% |
| [ne](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ne.msgpack.gz) | Nepali | नेपाली | र | 2.27e-02 | 56,205 | 83.3% |
| [frr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_frr.msgpack.gz) | Northern Frisian | Nordfriisk | a | 2.10e-02 | 68,041 | 83.1% |
| [ro](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ro.msgpack.gz) | Romanian | română | de | 4.15e-02 | 52,813 | 83.1% |
| [nl](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_nl.msgpack.gz) | Dutch | Nederlands | de | 6.02e-02 | 46,213 | 83.0% |
| [hsb](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_hsb.msgpack.gz) | Upper Sorbian | hornjoserbšćina | a | 2.59e-02 | 49,030 | 82.9% |
| [ky](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ky.msgpack.gz) | Kyrgyz | кыргызча | жана | 1.75e-02 | 55,728 | 82.8% |
| [rue](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_rue.msgpack.gz) | Rusyn | Rusyn | в | 2.44e-02 | 92,858 | 82.7% |
| [is](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_is.msgpack.gz) | Icelandic | íslenska | og | 3.51e-02 | 58,394 | 82.6% |
| [nn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_nn.msgpack.gz) | Norwegian Nynorsk | norsk nynorsk | i | 4.17e-02 | 47,903 | 82.6% |
| [eu](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_eu.msgpack.gz) | Basque | euskara | eta | 3.52e-02 | 58,955 | 82.4% |
| [bg](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_bg.msgpack.gz) | Bulgarian | български | на | 5.30e-02 | 56,101 | 82.3% |
| [pam](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_pam.msgpack.gz) | Pampanga | Pampanga | a | 2.52e-02 | 56,705 | 82.3% |
| [vep](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_vep.msgpack.gz) | Veps | Veps | om | 2.88e-02 | 62,252 | 82.2% |
| [fo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_fo.msgpack.gz) | Faroese | føroyskt | í | 3.92e-02 | 51,898 | 82.1% |
| [az](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_az.msgpack.gz) | Azerbaijani | azərbaycan | və | 2.67e-02 | 60,881 | 81.8% |
| [nds](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_nds.msgpack.gz) | Low German | Neddersass’sch | de | 5.31e-02 | 49,223 | 81.8% |
| [sh](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_sh.msgpack.gz) | Serbian (Latin) | srpski (latinica) | u | 3.47e-02 | 59,535 | 81.7% |
| [szl](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_szl.msgpack.gz) | Silesian | ślōnski | we | 3.19e-02 | 55,867 | 81.7% |
| [eo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_eo.msgpack.gz) | Esperanto | Esperanto | la | 7.23e-02 | 52,153 | 81.7% |
| [da](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_da.msgpack.gz) | Danish | dansk | i | 3.56e-02 | 50,971 | 81.4% |
| [ru](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ru.msgpack.gz) | Russian | русский | в | 4.19e-02 | 74,977 | 81.4% |
| [lb](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_lb.msgpack.gz) | Luxembourgish | Lëtzebuergesch | de | 2.14e-02 | 52,245 | 81.2% |
| [ba](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ba.msgpack.gz) | Bashkir | башҡорт теле | һәм | 1.94e-02 | 54,024 | 81.1% |
| [mr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_mr.msgpack.gz) | Marathi | मराठी | आणि | 1.57e-02 | 55,872 | 80.9% |
| [bug](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_bug.msgpack.gz) | Buginese | Buginese | ri | 9.06e-02 | 37,107 | 80.8% |
| [qu](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_qu.msgpack.gz) | Quechua | Runasimi | de | 1.73e-02 | 56,724 | 80.6% |
| [de](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_de.msgpack.gz) | German | Deutsch | der | 3.33e-02 | 54,636 | 80.6% |
| [uk](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_uk.msgpack.gz) | Ukrainian | українська | в | 1.84e-02 | 69,862 | 80.4% |
| [sv](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_sv.msgpack.gz) | Swedish | svenska | i | 3.16e-02 | 53,451 | 80.1% |
| [te](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_te.msgpack.gz) | Telugu | తెలుగు | నుండి | 1.44e-02 | 53,307 | 80.0% |
| [sl](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_sl.msgpack.gz) | Slovenian | slovenščina | je | 3.52e-02 | 64,633 | 79.8% |
| [kk](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_kk.msgpack.gz) | Kazakh | қазақ тілі | және | 1.24e-02 | 55,235 | 79.5% |
| [lv](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_lv.msgpack.gz) | Latvian | latviešu | un | 2.58e-02 | 65,941 | 79.5% |
| [cv](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_cv.msgpack.gz) | Chuvash | чӑваш | шыв | 1.31e-02 | 59,669 | 79.5% |
| [hr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_hr.msgpack.gz) | Croatian | hrvatski | je | 3.12e-02 | 66,728 | 79.5% |
| [pl](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_pl.msgpack.gz) | Polish | polski | w | 4.36e-02 | 68,521 | 79.2% |
| [xmf](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_xmf.msgpack.gz) | Mingrelian | Mingrelian | დო | 2.55e-02 | 70,789 | 79.1% |
| [uz](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_uz.msgpack.gz) | Uzbek | o‘zbek | va | 2.28e-02 | 57,501 | 79.1% |
| [smn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_smn.msgpack.gz) | Inari Sami | anarâškielâ | já | 2.49e-02 | 58,534 | 79.0% |
| [no](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_no.msgpack.gz) | Norwegian | norsk | i | 3.68e-02 | 50,740 | 79.0% |
| [bs](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_bs.msgpack.gz) | Bosnian | bosanski | i | 2.80e-02 | 62,061 | 78.8% |
| [sr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_sr.msgpack.gz) | Serbian | српски | је | 3.16e-02 | 65,542 | 78.7% |
| [hy](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_hy.msgpack.gz) | Armenian | հայերեն | է | 3.87e-02 | 58,989 | 78.7% |
| [vo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_vo.msgpack.gz) | Volapük | Volapük | in | 5.34e-02 | 35,249 | 78.2% |
| [azb](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_azb.msgpack.gz) | South Azerbaijani | South Azerbaijani | و | 2.08e-02 | 44,754 | 78.2% |
| [cs](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_cs.msgpack.gz) | Czech | čeština | a | 2.60e-02 | 66,575 | 78.2% |
| [mg](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_mg.msgpack.gz) | Malagasy | Malagasy | ny | 7.47e-02 | 26,840 | 78.2% |
| [tyv](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_tyv.msgpack.gz) | Tuvinian | Tuvinian | биле | 9.41e-03 | 63,964 | 78.1% |
| [ka](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ka.msgpack.gz) | Georgian | ქართული | და | 2.79e-02 | 67,121 | 78.0% |
| [sk](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_sk.msgpack.gz) | Slovak | slovenčina | v | 2.84e-02 | 65,419 | 77.7% |
| [bar](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_bar.msgpack.gz) | Bavarian | Bavarian | da | 2.31e-02 | 68,869 | 76.9% |
| [kn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_kn.msgpack.gz) | Kannada | ಕನ್ನಡ | ಮತ್ತು | 2.23e-02 | 76,773 | 76.9% |
| [ta](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ta.msgpack.gz) | Tamil | தமிழ் | மற்றும் | 1.01e-02 | 72,890 | 76.8% |
| [lt](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_lt.msgpack.gz) | Lithuanian | lietuvių | m | 2.79e-02 | 67,588 | 76.6% |
| [tr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_tr.msgpack.gz) | Turkish | Türkçe | ve | 2.34e-02 | 65,761 | 76.3% |
| [hu](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_hu.msgpack.gz) | Hungarian | magyar | a | 6.95e-02 | 67,096 | 76.1% |
| [be](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_be.msgpack.gz) | Belarusian | беларуская | і | 2.33e-02 | 63,047 | 75.3% |
| [sa](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_sa.msgpack.gz) | Sanskrit | संस्कृत भाषा | च | 1.65e-02 | 76,931 | 74.2% |
| [et](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_et.msgpack.gz) | Estonian | eesti | ja | 2.63e-02 | 72,230 | 74.2% |
| [la](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_la.msgpack.gz) | Latin | Lingua latina | et | 2.03e-02 | 61,307 | 73.7% |
| [ml](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ml.msgpack.gz) | Malayalam | മലയാളം | ഒരു | 1.09e-02 | 81,171 | 71.3% |
| [fi](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_fi.msgpack.gz) | Finnish | suomi | ja | 2.99e-02 | 72,546 | 70.8% |
| [ko](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_middle/middle_ko.msgpack.gz) | Korean | 한국어 | 년 | 2.27e-02 | 82,554 | 67.1% |
<!-- END GENERATED LANGUAGE TABLE:data_middle -->

### data_large

<!-- BEGIN GENERATED LANGUAGE TABLE:data_large -->
`data_large/large_<code>.msgpack.gz`: wordfreq cBpack (coverage = 10^(-cB/100), kept if >= 1e-6 i.e. cB <= 600). Sorted by cumulative coverage; `float` is the top word's coverage.

| code | language | native name | first word | float | words | cumulative coverage |
|------|----------|-------------|------------|-------|-------|---------------------|
| [el-Latn-u-sd-it75](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_el-Latn-u-sd-it75.msgpack.gz) | Greek (Latin) | Greek (Latin) | ce | 4.92e-02 | 16,776 | 102.3% |
| [ndz](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ndz.msgpack.gz) | Ndogo | Ndogo | tí | 5.50e-02 | 1,543 | 100.0% |
| [yam](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_yam.msgpack.gz) | Yamba | Yamba | nə | 4.14e-02 | 2,524 | 100.0% |
| [osa](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_osa.msgpack.gz) | Osage | 𐓏𐓘𐓻𐓘𐓻𐓟 | 𐓈𐒳͘ | 1.98e-02 | 1,388 | 100.0% |
| [fip](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_fip.msgpack.gz) | Fipa | Fipa | na | 2.64e-02 | 6,486 | 100.0% |
| [ig](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ig.msgpack.gz) | Igbo | Igbo | na | 7.80e-02 | 699 | 100.0% |
| [vec-u-sd-itts](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_vec-u-sd-itts.msgpack.gz) | Venetian | veneto | la | 5.30e-02 | 592 | 100.0% |
| [chj](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_chj.msgpack.gz) | Ojitlán Chinantec | Ojitlán Chinantec | e | 7.33e-02 | 581 | 100.0% |
| [ziw](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ziw.msgpack.gz) | Zigula | Zigula | na | 4.02e-02 | 6,869 | 100.0% |
| [lme](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_lme.msgpack.gz) | Pévé | Pévé | kə | 3.89e-02 | 1,269 | 100.0% |
| [cuc](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cuc.msgpack.gz) | Usila Chinantec | Usila Chinantec | i | 1.35e-01 | 840 | 100.0% |
| [bm](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bm.msgpack.gz) | Bambara | bamanakan | ka | 4.87e-02 | 1,117 | 100.0% |
| [bnp](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bnp.msgpack.gz) | Bola | Bola | a | 1.01e-01 | 2,857 | 100.0% |
| [dz](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_dz.msgpack.gz) | Dzongkha | རྫོང་ཁ | མི | 2.49e-02 | 1,259 | 100.0% |
| [ahk](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ahk.msgpack.gz) | Akha | Akha | eu | 5.31e-02 | 984 | 100.0% |
| [fuv](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_fuv.msgpack.gz) | Nigerian Fulfulde | Nigerian Fulfulde | lesdi | 5.43e-02 | 760 | 100.0% |
| [kyu](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kyu.msgpack.gz) | Western Kayah | Western Kayah | အၤ | 6.78e-02 | 1,003 | 100.0% |
| [lhu](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_lhu.msgpack.gz) | Lahu | Lahu | ve | 9.66e-02 | 1,031 | 100.0% |
| [uvl](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_uvl.msgpack.gz) | Lote | Lote | pe | 6.49e-02 | 3,663 | 100.0% |
| [kxm](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kxm.msgpack.gz) | Northern Khmer | Northern Khmer | ปเรียฮ | 3.32e-02 | 1,826 | 100.0% |
| [vec-u-sd-itvr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_vec-u-sd-itvr.msgpack.gz) | Venetian | veneto | de | 6.49e-02 | 1,390 | 100.0% |
| [cya](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cya.msgpack.gz) | Nopala Chatino | Nopala Chatino | in | 5.90e-02 | 1,432 | 100.0% |
| [ade](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ade.msgpack.gz) | Adele | Adele | fô | 5.96e-02 | 2,294 | 100.0% |
| [mio](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mio.msgpack.gz) | Pinotepa Nacional Mixtec | Pinotepa Nacional Mixtec | ra | 1.04e-01 | 1,346 | 100.0% |
| [pss](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_pss.msgpack.gz) | Kaulong | Kaulong | men | 7.52e-02 | 1,759 | 100.0% |
| [ssx](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ssx.msgpack.gz) | Samberigi | Samberigi | mo | 3.32e-02 | 9,610 | 100.0% |
| [mbt](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mbt.msgpack.gz) | Matigsalug Manobo | Matigsalug Manobo | te | 1.07e-01 | 4,593 | 100.0% |
| [hif](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_hif.msgpack.gz) | Fiji Hindi | Fiji Hindi | ke | 8.43e-02 | 3,114 | 100.0% |
| [sg](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_sg.msgpack.gz) | Sango | Sängö | ti | 1.17e-01 | 1,363 | 100.0% |
| [mzm](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mzm.msgpack.gz) | Mumuye | Mumuye | ɓɔɔ | 6.37e-02 | 1,622 | 100.0% |
| [bi](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bi.msgpack.gz) | Bislama | Bislama | i | 9.54e-02 | 1,438 | 100.0% |
| [urk](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_urk.msgpack.gz) | Urak Lawoi' | Urak Lawoi' | นะ | 3.74e-02 | 1,320 | 100.0% |
| [cso](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cso.msgpack.gz) | Sochiapam Chinantec | Sochiapam Chinantec | hi | 6.77e-02 | 1,309 | 100.0% |
| [tob](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tob.msgpack.gz) | Toba | Toba | da | 1.12e-01 | 5,925 | 100.0% |
| [cnl](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cnl.msgpack.gz) | Lalana Chinantec | Lalana Chinantec | e | 8.71e-02 | 1,278 | 100.0% |
| [pww](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_pww.msgpack.gz) | Pwo Northern Karen | Pwo Northern Karen | อ | 7.51e-02 | 1,280 | 100.0% |
| [sil](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_sil.msgpack.gz) | Tumulung Sisaala | Tumulung Sisaala | nɛ | 4.36e-02 | 2,562 | 100.0% |
| [nho](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_nho.msgpack.gz) | Takuu | Takuu | naa | 6.67e-02 | 2,532 | 100.0% |
| [lln](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_lln.msgpack.gz) | Lele (Chad) | Lele (Chad) | go | 5.41e-02 | 4,253 | 100.0% |
| [lis](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_lis.msgpack.gz) | Lisu | Lisu | ꓟ | 5.01e-02 | 1,388 | 100.0% |
| [mmo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mmo.msgpack.gz) | Mangga Buang | Mangga Buang | vu | 2.64e-02 | 3,730 | 100.0% |
| [nin](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_nin.msgpack.gz) | Ninzo | Ninzo | na | 4.81e-02 | 1,561 | 100.0% |
| [srn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_srn.msgpack.gz) | Sranan Tongo | Sranan Tongo | a | 6.80e-02 | 1,531 | 100.0% |
| [iri](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_iri.msgpack.gz) | Rigwe | Rigwe | ne | 5.91e-02 | 1,615 | 100.0% |
| [pmf](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_pmf.msgpack.gz) | Pamona | Pamona | to | 6.48e-02 | 4,029 | 100.0% |
| [bib](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bib.msgpack.gz) | Bissa | Bissa | a | 6.75e-02 | 2,009 | 100.0% |
| [kgr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kgr.msgpack.gz) | Abun | Abun | ne | 4.28e-02 | 1,410 | 100.0% |
| [djk](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_djk.msgpack.gz) | Eastern Maroon Creole | Eastern Maroon Creole | a | 7.49e-02 | 1,490 | 100.0% |
| [cnt](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cnt.msgpack.gz) | Tepetotutla Chinantec | Tepetotutla Chinantec | ca | 5.69e-02 | 1,169 | 100.0% |
| [xrb](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_xrb.msgpack.gz) | Eastern Karaboro | Eastern Karaboro | ye | 5.36e-02 | 2,037 | 100.0% |
| [mzk](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mzk.msgpack.gz) | Nigeria Mambila | Nigeria Mambila | éh | 5.17e-02 | 1,589 | 100.0% |
| [kno](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kno.msgpack.gz) | Kono (Sierra Leone) | Kono (Sierra Leone) | a | 1.54e-01 | 1,393 | 100.0% |
| [atg](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_atg.msgpack.gz) | Ivbie North-Okpela-Arhe | Ivbie North-Okpela-Arhe | ọ | 4.64e-02 | 2,269 | 100.0% |
| [pis](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_pis.msgpack.gz) | Pijin | Pijin | hemi | 6.22e-02 | 1,537 | 100.0% |
| [hns](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_hns.msgpack.gz) | Caribbean Hindustani | Caribbean Hindustani | ne̱ | 6.63e-02 | 2,014 | 100.0% |
| [cle](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cle.msgpack.gz) | Lealao Chinantec | Lealao Chinantec | hi | 7.19e-02 | 1,593 | 100.0% |
| [qxh](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_qxh.msgpack.gz) | Panao Huánuco Quechua | Panao Huánuco Quechua | Tayta | 4.17e-02 | 9,066 | 100.0% |
| [prf](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_prf.msgpack.gz) | Paranan | Paranan | a | 9.85e-02 | 4,613 | 100.0% |
| [mpm](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mpm.msgpack.gz) | Yosondúa Mixtec | Yosondúa Mixtec | ni | 6.41e-02 | 1,691 | 100.0% |
| [jam](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_jam.msgpack.gz) | Jamaican Creole English | Jamaican Creole English | dem | 4.95e-02 | 1,832 | 100.0% |
| [pez](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_pez.msgpack.gz) | Eastern Penan | Eastern Penan | éh | 6.93e-02 | 1,904 | 100.0% |
| [yre](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_yre.msgpack.gz) | Yaouré | Yaouré | a | 5.74e-02 | 1,605 | 100.0% |
| [nfr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_nfr.msgpack.gz) | Nafaanra | Nafaanra | na | 9.00e-02 | 1,865 | 100.0% |
| [dnw](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_dnw.msgpack.gz) | Western Dani | Western Dani | o | 4.23e-02 | 4,654 | 100.0% |
| [mda](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mda.msgpack.gz) | Mada (Nigeria) | Mada (Nigeria) | sē | 3.71e-02 | 1,661 | 100.0% |
| [bbo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bbo.msgpack.gz) | Northern Bobo Madaré | Northern Bobo Madaré | na | 6.18e-02 | 2,074 | 100.0% |
| [muh](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_muh.msgpack.gz) | Mündü | Mündü | wü | 4.54e-02 | 1,596 | 100.0% |
| [bzi](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bzi.msgpack.gz) | Bisu | Bisu | แน | 4.05e-02 | 1,921 | 100.0% |
| [ho](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ho.msgpack.gz) | Hiri Motu | Hiri Motu | ia | 6.76e-02 | 1,854 | 100.0% |
| [acn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_acn.msgpack.gz) | Achang | Achang | lyis | 4.87e-02 | 2,297 | 100.0% |
| [mhx](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mhx.msgpack.gz) | Maru | Maru | ra | 5.43e-02 | 1,906 | 100.0% |
| [aau](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_aau.msgpack.gz) | Abau | Abau | me | 3.16e-02 | 1,904 | 100.0% |
| [blt-Latn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_blt-Latn.msgpack.gz) | Tai Dam (Latin) | Tai Dam (Latin) | Chảu | 2.59e-02 | 1,587 | 100.0% |
| [btt](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_btt.msgpack.gz) | Bete-Bendi | Bete-Bendi | a | 4.73e-02 | 2,086 | 100.0% |
| [ncu](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ncu.msgpack.gz) | Chumburung | Chumburung | ne̱ | 6.62e-02 | 2,014 | 100.0% |
| [xtm](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_xtm.msgpack.gz) | Magdalena Peñasco Mixtec | Magdalena Peñasco Mixtec | ma | 7.77e-02 | 1,627 | 100.0% |
| [bjv](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bjv.msgpack.gz) | Bedjond | Bedjond | kɨ | 8.35e-02 | 1,954 | 100.0% |
| [gqr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_gqr.msgpack.gz) | Gor | Gor | kɨ | 9.79e-02 | 3,729 | 100.0% |
| [tgp](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tgp.msgpack.gz) | Tangoa | Tangoa | na | 7.06e-02 | 2,328 | 100.0% |
| [pbi](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_pbi.msgpack.gz) | Parkwa | Parkwa | a | 3.98e-02 | 3,391 | 100.0% |
| [bru](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bru.msgpack.gz) | Eastern Bru | Eastern Bru | án | 3.13e-02 | 1,980 | 100.0% |
| [zne](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_zne.msgpack.gz) | Zande (individual language) | Zande (individual language) | ni | 3.13e-02 | 2,146 | 100.0% |
| [taw](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_taw.msgpack.gz) | Kalam-Tai | Kalam-Tai | ak | 6.20e-02 | 4,062 | 100.0% |
| [hag](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_hag.msgpack.gz) | Hanga | Hanga | n | 8.34e-02 | 2,160 | 100.0% |
| [nii](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_nii.msgpack.gz) | - | - | ei | 5.22e-02 | 2,103 | 100.0% |
| [lee](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_lee.msgpack.gz) | Lyélé | Lyélé | ń | 3.65e-02 | 2,201 | 100.0% |
| [urb](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_urb.msgpack.gz) | Urubú-Kaapor | Urubú-Kaapor | ta | 5.86e-02 | 2,139 | 100.0% |
| [gng](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_gng.msgpack.gz) | Ngangam | Ngangam | ki | 5.43e-02 | 3,557 | 100.0% |
| [fon](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_fon.msgpack.gz) | - | - | ɔ́ | 4.91e-02 | 2,169 | 100.0% |
| [ndy](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ndy.msgpack.gz) | Lutos | Lutos | ma | 4.58e-02 | 2,375 | 100.0% |
| [gur](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_gur.msgpack.gz) | Frafra | Frafra | la | 9.14e-02 | 2,623 | 100.0% |
| [sur](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_sur.msgpack.gz) | Mwaghavul | Mwaghavul | mo | 6.21e-02 | 2,280 | 100.0% |
| [ach](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ach.msgpack.gz) | Acoli | Acoli | ma | 5.10e-02 | 4,989 | 100.0% |
| [gsw-u-sd-chfr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_gsw-u-sd-chfr.msgpack.gz) | Swiss German | Schwiizertüütsch | ù | 3.33e-02 | 1,808 | 100.0% |
| [xtd](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_xtd.msgpack.gz) | Diuxi-Tilantongo Mixtec | Diuxi-Tilantongo Mixtec | n | 9.18e-02 | 1,924 | 100.0% |
| [bus](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bus.msgpack.gz) | Bokobaru | Bokobaru | à | 6.71e-02 | 4,903 | 100.0% |
| [gam](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_gam.msgpack.gz) | Kandawo | Kandawo | ge | 5.09e-02 | 3,101 | 100.0% |
| [ntr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ntr.msgpack.gz) | Delo | Delo | na | 3.85e-02 | 2,076 | 100.0% |
| [raj](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_raj.msgpack.gz) | Rajasthani | राजस्थानी | के | 4.09e-02 | 4,631 | 100.0% |
| [meq](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_meq.msgpack.gz) | Merey | Merey | a | 6.22e-02 | 2,738 | 100.0% |
| [bzj](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bzj.msgpack.gz) | Belize Kriol English | Belize Kriol English | di | 6.14e-02 | 2,253 | 100.0% |
| [bav](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bav.msgpack.gz) | Vengo | Vengo | nə | 4.66e-02 | 2,083 | 100.0% |
| [gso](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_gso.msgpack.gz) | Southwest Gbaya | Southwest Gbaya | ha | 6.04e-02 | 2,218 | 100.0% |
| [la](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_la.msgpack.gz) | Latin | Lingua latina | in | 4.86e-02 | 3,081 | 100.0% |
| [cko](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cko.msgpack.gz) | Anufo | Anufo | i | 6.25e-02 | 2,173 | 100.0% |
| [sig](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_sig.msgpack.gz) | Paasaal | Paasaal | ʋ | 4.48e-02 | 2,264 | 100.0% |
| [las](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_las.msgpack.gz) | Lama (Togo) | Lama (Togo) | na | 6.62e-02 | 2,481 | 100.0% |
| [wob](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_wob.msgpack.gz) | Wè Northern | Wè Northern | ɛ | 4.66e-02 | 2,073 | 100.0% |
| [mgo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mgo.msgpack.gz) | Metaʼ | metaʼ | nɨ | 4.72e-02 | 2,206 | 100.0% |
| [cmr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cmr.msgpack.gz) | Mro-Khimi Chin | Mro-Khimi Chin | de | 7.85e-02 | 2,142 | 100.0% |
| [mhi](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mhi.msgpack.gz) | Ma'di | Ma'di | ni | 4.73e-02 | 3,369 | 100.0% |
| [sm](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_sm.msgpack.gz) | Samoan | Samoan | o | 7.48e-02 | 2,382 | 100.0% |
| [gv](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_gv.msgpack.gz) | Manx | Gaelg | dy | 4.63e-02 | 4,062 | 100.0% |
| [kqw](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kqw.msgpack.gz) | Kandas | Kandas | a | 8.13e-02 | 2,433 | 100.0% |
| [kcg](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kcg.msgpack.gz) | Tyap | Katab | si̱ | 3.42e-02 | 2,133 | 100.0% |
| [zpt](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_zpt.msgpack.gz) | San Vicente Coatlán Zapotec | San Vicente Coatlán Zapotec | le'a | 6.87e-02 | 2,691 | 100.0% |
| [ife](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ife.msgpack.gz) | Ifè | Ifè | tsí | 5.36e-02 | 2,490 | 100.0% |
| [kub](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kub.msgpack.gz) | Kutep | Kutep | tī | 8.48e-02 | 1,778 | 100.0% |
| [bwu](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bwu.msgpack.gz) | Buli (Ghana) | Buli (Ghana) | a | 9.27e-02 | 2,357 | 100.0% |
| [ptp](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ptp.msgpack.gz) | Patep | Patep | ge | 3.94e-02 | 1,920 | 100.0% |
| [mqb](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mqb.msgpack.gz) | Mbuko | Mbuko | a | 6.86e-02 | 2,177 | 100.0% |
| [myw](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_myw.msgpack.gz) | Muyuw | Muyuw | mo | 3.26e-02 | 10,212 | 100.0% |
| [gog](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_gog.msgpack.gz) | Gogo | Gogo | u | 2.04e-02 | 6,813 | 100.0% |
| [icr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_icr.msgpack.gz) | Islander Creole English | Islander Creole English | di | 5.05e-02 | 2,241 | 100.0% |
| [kjb](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kjb.msgpack.gz) | Q'anjob'al | Q'anjob'al | eb | 4.86e-02 | 3,883 | 100.0% |
| [acr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_acr.msgpack.gz) | Achi | Achi | ri | 1.22e-01 | 4,908 | 100.0% |
| [biv](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_biv.msgpack.gz) | Southern Birifor | Southern Birifor | a | 1.30e-01 | 2,206 | 100.0% |
| [nnw](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_nnw.msgpack.gz) | Southern Nuni | Southern Nuni | nə | 8.77e-02 | 2,214 | 100.0% |
| [yrb](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_yrb.msgpack.gz) | Yareba | Yareba | i | 3.94e-02 | 4,574 | 100.0% |
| [myk](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_myk.msgpack.gz) | Mamara Senoufo | Mamara Senoufo | na | 7.15e-02 | 2,582 | 100.0% |
| [pny](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_pny.msgpack.gz) | Pinyin | Pinyin | a | 7.47e-02 | 2,565 | 100.0% |
| [acf](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_acf.msgpack.gz) | Saint Lucian Creole French | Saint Lucian Creole French | an | 4.56e-02 | 2,239 | 100.0% |
| [mfq](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mfq.msgpack.gz) | Moba | Moba | k | 1.07e-01 | 3,097 | 100.0% |
| [mcu](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mcu.msgpack.gz) | Cameroon Mambila | Cameroon Mambila | né | 5.21e-02 | 2,405 | 100.0% |
| [far](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_far.msgpack.gz) | Fataleka | Fataleka | na | 4.97e-02 | 2,271 | 100.0% |
| [bfo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bfo.msgpack.gz) | Malba Birifor | Malba Birifor | a | 1.78e-01 | 2,291 | 100.0% |
| [trs](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_trs.msgpack.gz) | Chicahuaxtla Triqui | Chicahuaxtla Triqui | nej | 8.22e-02 | 2,697 | 100.0% |
| [kri](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kri.msgpack.gz) | Krio | Krio | dɛn | 5.51e-02 | 1,531 | 100.0% |
| [tpz](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tpz.msgpack.gz) | Tinputz | Tinputz | to | 5.86e-02 | 2,610 | 100.0% |
| [kms](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kms.msgpack.gz) | Kamasau | Kamasau | ni | 5.30e-02 | 2,679 | 100.0% |
| [tyz](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tyz.msgpack.gz) | Tày | Tày | ak | 6.29e-02 | 2,785 | 100.0% |
| [ktj](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ktj.msgpack.gz) | Plapo Krumen | Plapo Krumen | a | 8.56e-02 | 2,161 | 100.0% |
| [alj](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_alj.msgpack.gz) | Alangan | Alangan | in | 9.10e-02 | 2,908 | 100.0% |
| [mtj](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mtj.msgpack.gz) | Moskona | Moskona | noga | 5.63e-02 | 2,760 | 100.0% |
| [gui](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_gui.msgpack.gz) | Eastern Bolivian Guaraní | Eastern Bolivian Guaraní | reta | 5.95e-02 | 3,526 | 100.0% |
| [kne](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kne.msgpack.gz) | Kankanaey | Kankanaey | ay | 9.16e-02 | 5,497 | 100.0% |
| [rmo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_rmo.msgpack.gz) | Sinte Romani | Sinte Romani | o | 6.47e-02 | 2,581 | 100.0% |
| [asg](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_asg.msgpack.gz) | Cishingini | Cishingini | a | 6.75e-02 | 2,449 | 100.0% |
| [buk](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_buk.msgpack.gz) | Bugawac | Bugawac | ma | 4.28e-02 | 2,621 | 100.0% |
| [rug](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_rug.msgpack.gz) | Roviana | Roviana | si | 5.33e-02 | 6,238 | 100.0% |
| [mhy](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mhy.msgpack.gz) | Ma'anyan | Ma'anyan | sa | 4.23e-02 | 3,854 | 100.0% |
| [gux](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_gux.msgpack.gz) | Gourmanchéma | Gourmanchéma | ki | 5.18e-02 | 2,764 | 100.0% |
| [bex](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bex.msgpack.gz) | Jur Modo | Jur Modo | ma | 3.01e-02 | 2,275 | 100.0% |
| [sab](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_sab.msgpack.gz) | Buglere | Buglere | kwian | 4.23e-02 | 2,835 | 100.0% |
| [atb](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_atb.msgpack.gz) | Zaiwa | Zaiwa | é | 7.51e-02 | 2,558 | 100.0% |
| [dyi](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_dyi.msgpack.gz) | Djimini Senoufo | Djimini Senoufo | na | 4.99e-02 | 2,227 | 100.0% |
| [fj](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_fj.msgpack.gz) | Fijian | Fijian | na | 1.13e-01 | 2,846 | 100.0% |
| [pbc](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_pbc.msgpack.gz) | Patamona | Patamona | màlà | 3.77e-02 | 4,634 | 100.0% |
| [leu](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_leu.msgpack.gz) | Kara (Papua New Guinea) | Kara (Papua New Guinea) | a | 8.44e-02 | 3,491 | 100.0% |
| [hig](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_hig.msgpack.gz) | Kamwe | Kamwe | kə | 4.59e-02 | 2,279 | 100.0% |
| [box](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_box.msgpack.gz) | Buamu | Buamu | á | 4.13e-02 | 2,446 | 100.0% |
| [xuo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_xuo.msgpack.gz) | Kuo | Kuo | ká | 4.86e-02 | 2,355 | 100.0% |
| [iba](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_iba.msgpack.gz) | Iban | Iban | iya | 3.96e-02 | 2,632 | 100.0% |
| [luc](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_luc.msgpack.gz) | Aringa | Aringa | rĩ | 4.98e-02 | 2,817 | 100.0% |
| [blh](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_blh.msgpack.gz) | Kuwaa | Kuwaa | dè | 4.65e-02 | 2,910 | 100.0% |
| [kje](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kje.msgpack.gz) | Kisar | Kisar | man | 2.56e-02 | 3,511 | 100.0% |
| [kab](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kab.msgpack.gz) | Kabyle | Taqbaylit | d | 8.05e-02 | 2,482 | 100.0% |
| [bep](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bep.msgpack.gz) | Besoa | Besoa | to | 6.48e-02 | 5,597 | 100.0% |
| [ted](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ted.msgpack.gz) | Tepo Krumen | Tepo Krumen | a | 8.30e-02 | 2,302 | 100.0% |
| [lok](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_lok.msgpack.gz) | Loko | Loko | na | 6.79e-02 | 2,937 | 100.0% |
| [izr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_izr.msgpack.gz) | Izere | Izere | a | 5.31e-02 | 2,615 | 100.0% |
| [kia](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kia.msgpack.gz) | Kim | Kim | ge | 1.05e-01 | 2,876 | 100.0% |
| [mxb](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mxb.msgpack.gz) | Tezoatlán Mixtec | Tezoatlán Mixtec | ni̱ | 5.16e-02 | 2,755 | 100.0% |
| [bwq](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bwq.msgpack.gz) | Southern Bobo Madaré | Southern Bobo Madaré | ye | 4.89e-02 | 2,313 | 100.0% |
| [kma](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kma.msgpack.gz) | Konni | Konni | dɩ | 6.92e-02 | 2,784 | 100.0% |
| [yss](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_yss.msgpack.gz) | Yessan-Mayo | Yessan-Mayo | re | 4.99e-02 | 3,095 | 100.0% |
| [maw](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_maw.msgpack.gz) | Mampruli | Mampruli | ka | 6.15e-02 | 3,011 | 100.0% |
| [gej](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_gej.msgpack.gz) | Gen | Gen | a | 7.84e-02 | 3,197 | 100.0% |
| [cme](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cme.msgpack.gz) | Cerma | Cerma | i | 7.59e-02 | 3,026 | 100.0% |
| [hot](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_hot.msgpack.gz) | Hote | Hote | ma | 7.11e-02 | 3,003 | 100.0% |
| [cac](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cac.msgpack.gz) | Chuj | Chuj | eb | 5.80e-02 | 4,408 | 100.0% |
| [ksd](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ksd.msgpack.gz) | Kuanua | Kuanua | ra | 8.58e-02 | 3,033 | 100.0% |
| [sus](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_sus.msgpack.gz) | Susu | Susu | a | 8.18e-02 | 2,899 | 100.0% |
| [mfh](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mfh.msgpack.gz) | Matal | Matal | à | 8.68e-02 | 4,234 | 100.0% |
| [tna](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tna.msgpack.gz) | Tacana | Tacana | su | 6.14e-02 | 3,676 | 100.0% |
| [pam](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_pam.msgpack.gz) | Pampanga | Pampanga | ing | 4.73e-02 | 4,819 | 100.0% |
| [bvc](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bvc.msgpack.gz) | Baelelea | Baelelea | ka | 4.49e-02 | 2,456 | 100.0% |
| [kkj](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kkj.msgpack.gz) | Kako | kakɔ | ká | 5.09e-02 | 2,803 | 100.0% |
| [cbl](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cbl.msgpack.gz) | Bualkhaw Chin | Bualkhaw Chin | si | 6.55e-02 | 3,400 | 100.0% |
| [tmc](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tmc.msgpack.gz) | Tumak | Tumak | ɗᵻ | 1.18e-01 | 2,669 | 100.0% |
| [zas](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_zas.msgpack.gz) | Santo Domingo Albarradas Zapotec | Santo Domingo Albarradas Zapotec | ree | 5.14e-02 | 4,986 | 100.0% |
| [ddn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ddn.msgpack.gz) | Dendi (Benin) | Dendi (Benin) | kɑ | 5.77e-02 | 2,031 | 100.0% |
| [sgz](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_sgz.msgpack.gz) | Sursurunga | Sursurunga | má | 5.31e-02 | 3,036 | 100.0% |
| [jic](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_jic.msgpack.gz) | Tol | Tol | la | 3.93e-02 | 2,772 | 100.0% |
| [kyf](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kyf.msgpack.gz) | Kouya | Kouya | ɔ | 5.43e-02 | 3,202 | 100.0% |
| [eka](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_eka.msgpack.gz) | Ekajuk | Ekajuk | go | 3.28e-02 | 3,054 | 100.0% |
| [rej](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_rej.msgpack.gz) | Rejang | Rejang | ngen | 5.94e-02 | 3,976 | 100.0% |
| [din](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_din.msgpack.gz) | Dinka | Dinka | ku | 5.94e-02 | 3,176 | 100.0% |
| [okv](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_okv.msgpack.gz) | Orokaiva | Orokaiva | ta | 5.83e-02 | 5,270 | 100.0% |
| [czt](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_czt.msgpack.gz) | Zotung Chin | Zotung Chin | ae | 6.08e-02 | 3,646 | 100.0% |
| [moa](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_moa.msgpack.gz) | Mwan | Mwan | ɛ | 5.65e-02 | 2,486 | 100.0% |
| [zpz](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_zpz.msgpack.gz) | Texmelucan Zapotec | Texmelucan Zapotec | nu | 9.98e-02 | 2,671 | 100.0% |
| [daa](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_daa.msgpack.gz) | Dangaléat | Dangaléat | ɗo | 4.20e-02 | 5,363 | 100.0% |
| [tqo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tqo.msgpack.gz) | Toaripi | Toaripi | la | 3.98e-02 | 2,711 | 100.0% |
| [kqp](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kqp.msgpack.gz) | Kimré | Kimré | a | 5.08e-02 | 2,673 | 100.0% |
| [kpz](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kpz.msgpack.gz) | Kupsabiny | Kupsabiny | nye | 3.06e-02 | 6,277 | 100.0% |
| [tik](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tik.msgpack.gz) | Tikar | Tikar | nun | 3.88e-02 | 3,181 | 100.0% |
| [acd](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_acd.msgpack.gz) | Gikyode | Gikyode | mɔ | 8.95e-02 | 1,979 | 100.0% |
| [bgr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bgr.msgpack.gz) | Bawm Chin | Bawm Chin | a | 6.48e-02 | 2,855 | 100.0% |
| [aoz](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_aoz.msgpack.gz) | Uab Meto | Uab Meto | ma | 4.11e-02 | 3,343 | 100.0% |
| [guq](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_guq.msgpack.gz) | Aché | Aché | go | 4.54e-02 | 4,072 | 100.0% |
| [rai](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_rai.msgpack.gz) | Ramoaaina | Ramoaaina | a | 6.44e-02 | 2,710 | 100.0% |
| [bch](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bch.msgpack.gz) | Bariai | Bariai | ngan | 6.38e-02 | 3,694 | 100.0% |
| [oku](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_oku.msgpack.gz) | - | - | se | 5.93e-02 | 3,100 | 100.0% |
| [mit](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mit.msgpack.gz) | Southern Puebla Mixtec | Southern Puebla Mixtec | nì | 4.37e-02 | 3,584 | 100.0% |
| [jbu](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_jbu.msgpack.gz) | Jukun Takum | Jukun Takum | ki | 4.82e-02 | 3,419 | 100.0% |
| [hvn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_hvn.msgpack.gz) | Sabu | Sabu | do | 9.05e-02 | 2,758 | 100.0% |
| [mh](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mh.msgpack.gz) | Marshallese | Marshallese | im | 7.54e-02 | 5,451 | 100.0% |
| [amn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_amn.msgpack.gz) | Amanab | Amanab | Afa | 4.40e-02 | 6,369 | 100.0% |
| [kwf](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kwf.msgpack.gz) | Kwara'ae | Kwara'ae | na | 5.36e-02 | 2,544 | 100.0% |
| [gnd](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_gnd.msgpack.gz) | Zulgo-Gemzek | Zulgo-Gemzek | a | 1.26e-01 | 3,107 | 100.0% |
| [cnk](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cnk.msgpack.gz) | Khumi Chin | Khumi Chin | a | 6.17e-02 | 3,397 | 100.0% |
| [due](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_due.msgpack.gz) | Umiray Dumaget Agta | Umiray Dumaget Agta | a | 1.12e-01 | 3,698 | 100.0% |
| [yut](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_yut.msgpack.gz) | Yopno | Yopno | da | 5.26e-02 | 6,218 | 100.0% |
| [krj](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_krj.msgpack.gz) | Kinaray-a | Kinaray-a | nga | 8.03e-02 | 5,061 | 100.0% |
| [sba](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_sba.msgpack.gz) | Ngambay | Ngambay | gə́ | 6.77e-02 | 3,581 | 100.0% |
| [adj](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_adj.msgpack.gz) | Adioukrou | Adioukrou | a | 7.14e-02 | 3,491 | 100.0% |
| [neb](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_neb.msgpack.gz) | Toura (Côte d'Ivoire) | Toura (Côte d'Ivoire) | à | 6.73e-02 | 3,403 | 100.0% |
| [mif](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mif.msgpack.gz) | Mofu-Gudur | Mofu-Gudur | a | 7.58e-02 | 2,876 | 100.0% |
| [bmv](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bmv.msgpack.gz) | Bum | Bum | a | 5.58e-02 | 2,847 | 100.0% |
| [avu](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_avu.msgpack.gz) | Avokaya | Avokaya | rî | 6.70e-02 | 2,812 | 100.0% |
| [mxt](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mxt.msgpack.gz) | Jamiltepec Mixtec | Jamiltepec Mixtec | ra | 9.92e-02 | 2,787 | 100.0% |
| [mfe](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mfe.msgpack.gz) | Morisyen | kreol morisien | zot | 4.76e-02 | 3,077 | 100.0% |
| [ljp](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ljp.msgpack.gz) | Lampung Api | Lampung Api | sai | 5.16e-02 | 4,154 | 100.0% |
| [kln](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kln.msgpack.gz) | Kalenjin | Kalenjin | kule | 3.19e-02 | 7,135 | 100.0% |
| [bkv](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bkv.msgpack.gz) | Bekwarra | Bekwarra | e | 3.50e-02 | 2,763 | 100.0% |
| [miq](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_miq.msgpack.gz) | Mískito | Mískito | ba | 6.11e-02 | 2,894 | 100.0% |
| [mej](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mej.msgpack.gz) | Meyah | Meyah | ongga | 5.76e-02 | 3,249 | 100.0% |
| [kus](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kus.msgpack.gz) | Kusaal | Kusaal | ka | 9.35e-02 | 3,349 | 100.0% |
| [zca](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_zca.msgpack.gz) | Coatecas Altas Zapotec | Coatecas Altas Zapotec | rë | 4.08e-02 | 3,246 | 100.0% |
| [yle](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_yle.msgpack.gz) | Yele | Yele | u | 5.22e-02 | 3,434 | 100.0% |
| [mbh](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mbh.msgpack.gz) | Mangseng | Mangseng | i | 8.19e-02 | 4,043 | 100.0% |
| [dop](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_dop.msgpack.gz) | Lukpa | Lukpa | na | 6.43e-02 | 3,536 | 100.0% |
| [lcm](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_lcm.msgpack.gz) | Tungag | Tungag | na | 4.99e-02 | 3,055 | 100.0% |
| [kdi](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kdi.msgpack.gz) | Kumam | Kumam | kame | 3.81e-02 | 3,802 | 100.0% |
| [bov](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bov.msgpack.gz) | Tuwuli | Tuwuli | a | 8.22e-02 | 4,472 | 100.0% |
| [stn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_stn.msgpack.gz) | Owa | Owa | ka | 6.09e-02 | 3,311 | 100.0% |
| [nak](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_nak.msgpack.gz) | Nakanai | Nakanai | la | 1.29e-01 | 4,995 | 100.0% |
| [con](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_con.msgpack.gz) | Cofán | Cofán | tsu | 3.97e-02 | 6,705 | 100.0% |
| [dug](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_dug.msgpack.gz) | Duruma | Duruma | na | 5.81e-02 | 7,873 | 100.0% |
| [sps](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_sps.msgpack.gz) | Saposa | Saposa | te | 4.76e-02 | 3,096 | 100.0% |
| [wwa](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_wwa.msgpack.gz) | Waama | Waama | ò | 4.63e-02 | 3,280 | 100.0% |
| [nyf](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_nyf.msgpack.gz) | Giryama | Giryama | na | 5.41e-02 | 7,491 | 100.0% |
| [sld](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_sld.msgpack.gz) | Sissala | Sissala | ná | 4.04e-02 | 3,829 | 100.0% |
| [pkb](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_pkb.msgpack.gz) | Pokomo | Pokomo | na | 6.35e-02 | 7,625 | 100.0% |
| [ceg](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ceg.msgpack.gz) | Chamacoco | Chamacoco | uje | 9.15e-02 | 3,662 | 100.0% |
| [plw](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_plw.msgpack.gz) | Brooke's Point Palawano | Brooke's Point Palawano | et | 6.32e-02 | 5,725 | 100.0% |
| [bmr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bmr.msgpack.gz) | Muinane | Muinane | bu | 2.84e-02 | 8,377 | 100.0% |
| [mib](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mib.msgpack.gz) | Atatláhuca Mixtec | Atatláhuca Mixtec | ni | 6.15e-02 | 2,804 | 100.0% |
| [dgi](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_dgi.msgpack.gz) | Northern Dagara | Northern Dagara | a | 1.58e-01 | 2,199 | 100.0% |
| [abt](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_abt.msgpack.gz) | Ambulas | Ambulas | dé | 4.15e-02 | 3,600 | 100.0% |
| [bbr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bbr.msgpack.gz) | Girawa | Girawa | kiro | 3.54e-02 | 6,347 | 100.0% |
| [ppk](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ppk.msgpack.gz) | Uma | Uma | to | 5.67e-02 | 4,320 | 100.0% |
| [vag](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_vag.msgpack.gz) | Vagla | Vagla | di | 5.05e-02 | 3,091 | 100.0% |
| [yal](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_yal.msgpack.gz) | Yalunka | Yalunka | a | 8.10e-02 | 3,555 | 100.0% |
| [mkl](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mkl.msgpack.gz) | Mokole | Mokole | í | 5.93e-02 | 2,842 | 100.0% |
| [pag](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_pag.msgpack.gz) | Pangasinan | Pangasinan | a | 4.33e-02 | 5,652 | 100.0% |
| [ttc](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ttc.msgpack.gz) | Tektiteko | Tektiteko | te | 6.45e-02 | 4,431 | 100.0% |
| [ipi](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ipi.msgpack.gz) | Ipili | Ipili | wandakali | 2.14e-02 | 4,898 | 100.0% |
| [twu](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_twu.msgpack.gz) | Termanu | Termanu | fo | 2.76e-02 | 3,856 | 100.0% |
| [knk](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_knk.msgpack.gz) | Kuranko | Kuranko | a | 5.76e-02 | 2,930 | 100.0% |
| [rnl](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_rnl.msgpack.gz) | Ranglong | Ranglong | na | 6.33e-02 | 4,601 | 100.0% |
| [tfr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tfr.msgpack.gz) | Teribe | Teribe | ga | 8.16e-02 | 3,037 | 100.0% |
| [apz](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_apz.msgpack.gz) | Safeyoka | Safeyoka | aꞌamu | 3.06e-02 | 19,429 | 100.0% |
| [gkn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_gkn.msgpack.gz) | Gokana | Gokana | e | 6.44e-02 | 3,937 | 100.0% |
| [seh](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_seh.msgpack.gz) | Sena | sena | na | 6.16e-02 | 6,165 | 100.0% |
| [bim](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bim.msgpack.gz) | Bimoba | Bimoba | ki | 1.08e-01 | 3,715 | 100.0% |
| [byx](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_byx.msgpack.gz) | Qaqet | Qaqet | ama | 7.76e-02 | 3,461 | 100.0% |
| [tem](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tem.msgpack.gz) | Timne | Timne | ka | 5.19e-02 | 3,990 | 100.0% |
| [mop](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mop.msgpack.gz) | Mopán Maya | Mopán Maya | a | 1.23e-01 | 4,507 | 100.0% |
| [gvf](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_gvf.msgpack.gz) | Golin | Golin | i | 3.24e-02 | 4,253 | 100.0% |
| [mcp](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mcp.msgpack.gz) | Makaa | Makaa | nə́ | 4.13e-02 | 4,242 | 100.0% |
| [zap](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_zap.msgpack.gz) | Zapotec | Zapotec | ne | 4.43e-02 | 3,143 | 100.0% |
| [pau](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_pau.msgpack.gz) | Palauan | Palauan | a | 1.57e-01 | 4,360 | 100.0% |
| [mil](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mil.msgpack.gz) | Peñoles Mixtec | Peñoles Mixtec | te | 6.41e-02 | 2,949 | 100.0% |
| [gil](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_gil.msgpack.gz) | Gilbertese | Gilbertese | te | 6.34e-02 | 3,622 | 100.0% |
| [hne](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_hne.msgpack.gz) | Chhattisgarhi | Chhattisgarhi | के | 5.67e-02 | 4,297 | 100.0% |
| [aia](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_aia.msgpack.gz) | Arosi | Arosi | a | 3.10e-02 | 3,913 | 100.0% |
| [cdf](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cdf.msgpack.gz) | Chiru | Chiru | kha | 6.22e-02 | 4,703 | 100.0% |
| [xav](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_xav.msgpack.gz) | Xavánte | Xavánte | te | 7.46e-02 | 4,354 | 100.0% |
| [nwi](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_nwi.msgpack.gz) | Southwest Tanna | Southwest Tanna | ye | 2.94e-02 | 4,833 | 100.0% |
| [prk](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_prk.msgpack.gz) | Parauk | Parauk | ka | 4.79e-02 | 4,056 | 100.0% |
| [lia](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_lia.msgpack.gz) | West-Central Limba | West-Central Limba | ka | 7.17e-02 | 3,894 | 100.0% |
| [bmq](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bmq.msgpack.gz) | Bomu | Bomu | a | 8.92e-02 | 3,462 | 100.0% |
| [xsi](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_xsi.msgpack.gz) | Sio | Sio | tamâta | 2.97e-02 | 3,309 | 100.0% |
| [mpg](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mpg.msgpack.gz) | Marba | Marba | mi | 5.95e-02 | 3,960 | 100.0% |
| [akp](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_akp.msgpack.gz) | Siwu | Siwu | i | 4.70e-02 | 3,945 | 100.0% |
| [kao](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kao.msgpack.gz) | Xaasongaxango | Xaasongaxango | xa | 4.42e-02 | 3,438 | 100.0% |
| [rmc](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_rmc.msgpack.gz) | Carpathian Romani | Carpathian Romani | o | 5.50e-02 | 4,644 | 100.0% |
| [itv](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_itv.msgpack.gz) | Itawit | Itawit | ya | 1.02e-01 | 4,770 | 100.0% |
| [cwe](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cwe.msgpack.gz) | Kwere | Kwere | na | 6.52e-02 | 6,546 | 100.0% |
| [dga](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_dga.msgpack.gz) | Southern Dagaare | Southern Dagaare | a | 9.87e-02 | 3,683 | 100.0% |
| [hus](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_hus.msgpack.gz) | Huastec | Huastec | an | 4.26e-02 | 3,979 | 100.0% |
| [nij](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_nij.msgpack.gz) | Ngaju | Ngaju | je | 4.35e-02 | 3,481 | 100.0% |
| [bfd](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bfd.msgpack.gz) | Bafut | Bafut | a | 6.69e-02 | 5,128 | 100.0% |
| [cni](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cni.msgpack.gz) | Asháninka | Asháninka | aisati | 3.56e-02 | 8,255 | 100.0% |
| [sua](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_sua.msgpack.gz) | Sulka | Sulka | e | 3.82e-02 | 4,126 | 100.0% |
| [mza](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mza.msgpack.gz) | Santa María Zacatepec Mixtec | Santa María Zacatepec Mixtec | ma | 6.97e-02 | 2,920 | 100.0% |
| [gym](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_gym.msgpack.gz) | Ngäbere | Ngäbere | abko | 3.73e-02 | 3,484 | 100.0% |
| [mmx](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mmx.msgpack.gz) | Madak | Madak | la | 4.60e-02 | 4,128 | 100.0% |
| [mnf](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mnf.msgpack.gz) | Mundani | Mundani | la | 4.21e-02 | 3,362 | 100.0% |
| [iry](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_iry.msgpack.gz) | Iraya | Iraya | da | 8.39e-02 | 3,753 | 100.0% |
| [ury](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ury.msgpack.gz) | Orya | Orya | de | 3.86e-02 | 4,974 | 100.0% |
| [guo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_guo.msgpack.gz) | Guayabero | Guayabero | wʉt | 4.87e-02 | 7,734 | 100.0% |
| [ker](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ker.msgpack.gz) | Kera | Kera | bə | 6.45e-02 | 3,877 | 100.0% |
| [xsm](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_xsm.msgpack.gz) | Kasem | Kasem | o | 5.63e-02 | 3,495 | 100.0% |
| [mnw](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mnw.msgpack.gz) | Mon | Mon | န် | 4.63e-02 | 3,762 | 100.0% |
| [mfz](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mfz.msgpack.gz) | Mabaan | Mabaan | ɔci | 5.71e-02 | 4,852 | 100.0% |
| [kpw](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kpw.msgpack.gz) | Kobon | Kobon | u | 4.34e-02 | 3,758 | 100.0% |
| [xsr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_xsr.msgpack.gz) | Sherpa | Sherpa | ति | 3.28e-02 | 4,431 | 100.0% |
| [soy](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_soy.msgpack.gz) | Miyobe | Miyobe | nɛ | 4.23e-02 | 4,615 | 100.0% |
| [med](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_med.msgpack.gz) | Melpa | Melpa | ei | 5.37e-02 | 4,051 | 100.0% |
| [laj](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_laj.msgpack.gz) | Lango (Uganda) | Lango (Uganda) | i | 5.05e-02 | 4,475 | 100.0% |
| [huu](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_huu.msgpack.gz) | Murui Huitoto | Murui Huitoto | omoɨ | 2.27e-02 | 5,830 | 100.0% |
| [nhu](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_nhu.msgpack.gz) | Noone | Noone | ɛ | 6.03e-02 | 3,375 | 100.0% |
| [grb](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_grb.msgpack.gz) | Grebo | Grebo | mǒ | 1.99e-02 | 4,030 | 100.0% |
| [ntm](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ntm.msgpack.gz) | Nateni | Nateni | é | 3.44e-02 | 3,845 | 100.0% |
| [bps](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bps.msgpack.gz) | Sarangani Blaan | Sarangani Blaan | i | 8.33e-02 | 4,355 | 100.0% |
| [vid](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_vid.msgpack.gz) | Vidunda | Vidunda | na | 6.60e-02 | 6,599 | 100.0% |
| [dip](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_dip.msgpack.gz) | Northeastern Dinka | Northeastern Dinka | e | 6.48e-02 | 3,619 | 100.0% |
| [alz](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_alz.msgpack.gz) | Alur | Alur | ma | 5.29e-02 | 5,037 | 100.0% |
| [kqc](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kqc.msgpack.gz) | Doromu-Koki | Doromu-Koki | bi | 5.22e-02 | 3,693 | 100.0% |
| [bqp](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bqp.msgpack.gz) | Busa | Busa | kũ | 6.20e-02 | 4,700 | 100.0% |
| [bpr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bpr.msgpack.gz) | Koronadal Blaan | Koronadal Blaan | i | 8.44e-02 | 4,234 | 100.0% |
| [sas](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_sas.msgpack.gz) | Sasak | Sasak | saq | 4.41e-02 | 3,686 | 100.0% |
| [nus](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_nus.msgpack.gz) | Nuer | Thok Nath | kä | 6.30e-02 | 3,675 | 100.0% |
| [spp](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_spp.msgpack.gz) | Supyire Senoufo | Supyire Senoufo | na | 5.33e-02 | 3,549 | 100.0% |
| [mgd](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mgd.msgpack.gz) | Moru | Moru | ago | 3.28e-02 | 4,064 | 100.0% |
| [naf](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_naf.msgpack.gz) | Nabak | Nabak | ke | 2.22e-02 | 16,014 | 100.0% |
| [kew](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kew.msgpack.gz) | West Kewa | West Kewa | go | 2.84e-02 | 8,252 | 100.0% |
| [nwb](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_nwb.msgpack.gz) | Nyabwa | Nyabwa | ɔ | 6.80e-02 | 3,440 | 100.0% |
| [gyr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_gyr.msgpack.gz) | Guarayu | Guarayu | va'e | 3.88e-02 | 4,596 | 100.0% |
| [zyp](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_zyp.msgpack.gz) | Zyphe Chin | Zyphe Chin | a | 1.10e-01 | 3,371 | 100.0% |
| [gde](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_gde.msgpack.gz) | Gude | Gude | ka | 5.92e-02 | 4,342 | 100.0% |
| [sja](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_sja.msgpack.gz) | Epena | Epena | Tachi | 2.39e-02 | 5,334 | 100.0% |
| [kqe](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kqe.msgpack.gz) | Kalagan | Kalagan | na | 7.33e-02 | 4,160 | 100.0% |
| [nkf](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_nkf.msgpack.gz) | Inpui Naga | Inpui Naga | bi | 2.69e-02 | 3,591 | 100.0% |
| [fue](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_fue.msgpack.gz) | Borgu Fulfulde | Borgu Fulfulde | e | 5.54e-02 | 5,864 | 100.0% |
| [msm](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_msm.msgpack.gz) | Agusan Manobo | Agusan Manobo | to | 1.33e-01 | 5,178 | 100.0% |
| [kue](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kue.msgpack.gz) | Kuman (Papua New Guinea) | Kuman (Papua New Guinea) | ana | 3.80e-02 | 5,812 | 100.0% |
| [gnw](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_gnw.msgpack.gz) | Western Bolivian Guaraní | Western Bolivian Guaraní | reta | 6.52e-02 | 3,997 | 100.0% |
| [lip](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_lip.msgpack.gz) | Sekpele | Sekpele | lǝ | 5.98e-02 | 5,366 | 100.0% |
| [zpi](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_zpi.msgpack.gz) | Santa María Quiegolani Zapotec | Santa María Quiegolani Zapotec | ne | 1.05e-01 | 3,712 | 100.0% |
| [dts](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_dts.msgpack.gz) | Toro So Dogon | Toro So Dogon | gɔ | 3.79e-02 | 4,884 | 100.0% |
| [lsi](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_lsi.msgpack.gz) | Lashi | Lashi | da | 4.38e-02 | 4,115 | 100.0% |
| [caa](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_caa.msgpack.gz) | Chortí | Chortí | e | 1.02e-01 | 4,138 | 100.0% |
| [bts](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bts.msgpack.gz) | Batak Simalungun | Batak Simalungun | na | 5.68e-02 | 4,769 | 100.0% |
| [fal](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_fal.msgpack.gz) | South Fali | South Fali | a | 5.65e-02 | 3,551 | 100.0% |
| [gud](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_gud.msgpack.gz) | Yocoboué Dida | Yocoboué Dida | lɛ | 5.98e-02 | 3,918 | 100.0% |
| [mog](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mog.msgpack.gz) | Mongondow | Mongondow | in | 4.41e-02 | 5,389 | 100.0% |
| [yli](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_yli.msgpack.gz) | Angguruk Yali | Angguruk Yali | lit | 2.30e-02 | 4,327 | 100.0% |
| [lus](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_lus.msgpack.gz) | Mizo | Mizo | a | 1.25e-01 | 4,852 | 100.0% |
| [gun](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_gun.msgpack.gz) | Mbyá Guaraní | Mbyá Guaraní | Ha'e | 4.00e-02 | 4,361 | 100.0% |
| [maj](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_maj.msgpack.gz) | Jalapa De Díaz Mazatec | Jalapa De Díaz Mazatec | xi | 8.96e-02 | 5,585 | 100.0% |
| [bnj](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bnj.msgpack.gz) | Eastern Tawbuid | Eastern Tawbuid | at | 7.68e-02 | 3,457 | 100.0% |
| [nou](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_nou.msgpack.gz) | Ewage-Notu | Ewage-Notu | awa | 6.04e-02 | 4,913 | 100.0% |
| [bgz](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bgz.msgpack.gz) | Banggai | Banggai | doi | 5.69e-02 | 6,018 | 100.0% |
| [zia](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_zia.msgpack.gz) | - | - | mene | 2.80e-02 | 6,497 | 100.0% |
| [gfk](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_gfk.msgpack.gz) | Patpatar | Patpatar | na | 4.98e-02 | 3,494 | 100.0% |
| [gvl](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_gvl.msgpack.gz) | Gulay | Gulay | ke | 6.94e-02 | 3,453 | 100.0% |
| [obo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_obo.msgpack.gz) | Obo Manobo | Obo Manobo | to | 6.64e-02 | 3,313 | 100.0% |
| [mna](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mna.msgpack.gz) | Mbula | Mbula | mi | 5.21e-02 | 4,874 | 100.0% |
| [mta](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mta.msgpack.gz) | Cotabato Manobo | Cotabato Manobo | sa | 1.04e-01 | 3,599 | 100.0% |
| [sey](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_sey.msgpack.gz) | Secoya | Secoya | Ja̱je | 2.60e-02 | 6,100 | 100.0% |
| [ae-Latn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ae-Latn.msgpack.gz) | Avestan (Latin) | Avestan (Latin) | yazamaide | 1.64e-02 | 5,576 | 100.0% |
| [lef](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_lef.msgpack.gz) | Lelemi | Lelemi | na | 1.03e-01 | 4,765 | 100.0% |
| [cjp](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cjp.msgpack.gz) | Cabécar | Cabécar | je | 4.08e-02 | 4,659 | 100.0% |
| [jvn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_jvn.msgpack.gz) | Caribbean Javanese | Caribbean Javanese | sing | 4.03e-02 | 3,864 | 100.0% |
| [pcm](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_pcm.msgpack.gz) | Nigerian Pidgin | Naijíriá Píjin | di | 4.91e-02 | 3,925 | 100.0% |
| [hla](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_hla.msgpack.gz) | Halia | Halia | e | 6.99e-02 | 5,920 | 100.0% |
| [xsb](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_xsb.msgpack.gz) | Sambal | Sambal | a | 5.98e-02 | 5,072 | 100.0% |
| [yon](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_yon.msgpack.gz) | Yongkom | Yongkom | kuu | 8.61e-02 | 6,358 | 100.0% |
| [rom](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_rom.msgpack.gz) | Romany | Romany | e | 5.43e-02 | 3,717 | 100.0% |
| [agn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_agn.msgpack.gz) | Agutaynen | Agutaynen | ang | 7.46e-02 | 5,181 | 100.0% |
| [gor](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_gor.msgpack.gz) | Gorontalo | Gorontalo | lo | 4.55e-02 | 5,170 | 100.0% |
| [aaz](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_aaz.msgpack.gz) | Amarasi | Amarasi | re | 3.27e-02 | 4,988 | 100.0% |
| [maz](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_maz.msgpack.gz) | Central Mazahua | Central Mazahua | c'o | 4.23e-02 | 4,657 | 100.0% |
| [mur](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mur.msgpack.gz) | Murle | Murle | o | 5.73e-02 | 5,174 | 100.0% |
| [sck](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_sck.msgpack.gz) | Sadri | Sadri | कर | 5.25e-02 | 4,428 | 100.0% |
| [wsk](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_wsk.msgpack.gz) | Waskia | Waskia | mu | 5.41e-02 | 4,982 | 100.0% |
| [kpg](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kpg.msgpack.gz) | Kapingamarangi | Kapingamarangi | di | 5.41e-02 | 3,842 | 100.0% |
| [muy](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_muy.msgpack.gz) | Muyang | Muyang | ti | 6.30e-02 | 4,842 | 100.0% |
| [cok](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cok.msgpack.gz) | Santa Teresa Cora | Santa Teresa Cora | ɨ | 1.08e-01 | 6,620 | 100.0% |
| [nmz](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_nmz.msgpack.gz) | Nawdm | Nawdm | n | 7.39e-02 | 4,043 | 100.0% |
| [kac](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kac.msgpack.gz) | Kachin | Kachin | ai | 7.74e-02 | 4,893 | 100.0% |
| [toh](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_toh.msgpack.gz) | Gitonga | Gitonga | gu | 5.16e-02 | 4,868 | 100.0% |
| [lwo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_lwo.msgpack.gz) | Luwo | Luwo | ke | 3.54e-02 | 4,452 | 100.0% |
| [swp](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_swp.msgpack.gz) | Suau | Suau | i | 6.16e-02 | 8,591 | 100.0% |
| [shk](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_shk.msgpack.gz) | Shilluk | Shilluk | ɑ | 6.75e-02 | 4,769 | 100.0% |
| [kbm](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kbm.msgpack.gz) | Iwal | Iwal | be | 6.04e-02 | 3,525 | 100.0% |
| [bmh](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bmh.msgpack.gz) | Kein | Kein | go | 6.32e-02 | 5,377 | 100.0% |
| [ncj](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ncj.msgpack.gz) | Northern Puebla Nahuatl | Northern Puebla Nahuatl | in | 1.08e-01 | 6,344 | 100.0% |
| [snp](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_snp.msgpack.gz) | Siane | Siane | ya | 7.61e-02 | 5,367 | 100.0% |
| [kzf](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kzf.msgpack.gz) | Da'a Kaili | Da'a Kaili | to | 4.18e-02 | 4,656 | 100.0% |
| [xed](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_xed.msgpack.gz) | Hdi | Hdi | ta | 9.67e-02 | 4,497 | 100.0% |
| [sny](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_sny.msgpack.gz) | Saniyo-Hiyewe | Saniyo-Hiyewe | a'i | 4.14e-02 | 3,916 | 100.0% |
| [mzi](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mzi.msgpack.gz) | Ixcatlán Mazatec | Ixcatlán Mazatec | xi | 7.66e-02 | 5,239 | 100.0% |
| [imo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_imo.msgpack.gz) | Imbongu | Imbongu | kinye | 2.29e-02 | 7,788 | 100.0% |
| [lgg](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_lgg.msgpack.gz) | Lugbara | Lugbara | ma | 5.71e-02 | 3,992 | 100.0% |
| [bhw](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bhw.msgpack.gz) | Biak | Biak | ma | 4.40e-02 | 5,270 | 100.0% |
| [amk](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_amk.msgpack.gz) | Ambai | Ambai | we | 4.33e-02 | 5,774 | 100.0% |
| [ong](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ong.msgpack.gz) | Olo | Olo | le | 6.73e-02 | 5,196 | 100.0% |
| [kki](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kki.msgpack.gz) | Kagulu | Kagulu | na | 6.02e-02 | 7,242 | 100.0% |
| [loe](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_loe.msgpack.gz) | Saluan | Saluan | i | 4.87e-02 | 5,023 | 100.0% |
| [ake](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ake.msgpack.gz) | Akawaio | Akawaio | pe | 5.53e-02 | 4,631 | 100.0% |
| [cce](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cce.msgpack.gz) | Chopi | Chopi | a | 4.33e-02 | 4,846 | 100.0% |
| [cgc](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cgc.msgpack.gz) | Kagayanen | Kagayanen | na | 1.18e-01 | 3,866 | 100.0% |
| [nyn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_nyn.msgpack.gz) | Nyankole | Runyankore | omu | 2.57e-02 | 8,273 | 100.0% |
| [ann](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ann.msgpack.gz) | Obolo | Obolo | me | 5.56e-02 | 4,997 | 100.0% |
| [udu](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_udu.msgpack.gz) | Uduk | Uduk | mo | 1.46e-01 | 4,231 | 100.0% |
| [war](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_war.msgpack.gz) | Waray | Waray | nga | 7.03e-02 | 5,076 | 100.0% |
| [yaz](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_yaz.msgpack.gz) | Lokaa | Lokaa | kạ | 4.43e-02 | 4,818 | 100.0% |
| [keo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_keo.msgpack.gz) | Kakwa | Kakwa | ku | 5.07e-02 | 4,268 | 100.0% |
| [ifu](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ifu.msgpack.gz) | Mayoyao Ifugao | Mayoyao Ifugao | an | 8.23e-02 | 4,901 | 100.0% |
| [lid](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_lid.msgpack.gz) | Nyindrou | Nyindrou | ta | 5.00e-02 | 3,169 | 100.0% |
| [bud](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bud.msgpack.gz) | Ntcham | Ntcham | ní | 4.86e-02 | 4,397 | 100.0% |
| [emp](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_emp.msgpack.gz) | Northern Emberá | Northern Emberá | b̶ʌa | 1.42e-02 | 5,831 | 100.0% |
| [sgb](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_sgb.msgpack.gz) | Mag-antsi Ayta | Mag-antsi Ayta | ya | 9.11e-02 | 4,475 | 100.0% |
| [ptu](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ptu.msgpack.gz) | Bambam | Bambam | anna | 4.19e-02 | 6,571 | 100.0% |
| [bcw](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bcw.msgpack.gz) | Bana | Bana | na | 4.86e-02 | 4,690 | 100.0% |
| [ifk](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ifk.msgpack.gz) | Tuwali Ifugao | Tuwali Ifugao | ya | 5.73e-02 | 5,571 | 100.0% |
| [men](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_men.msgpack.gz) | Mende | Mende | a | 5.23e-02 | 4,900 | 100.0% |
| [waj](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_waj.msgpack.gz) | Waffa | Waffa | kua | 1.74e-02 | 12,277 | 100.0% |
| [azg](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_azg.msgpack.gz) | San Pedro Amuzgos Amuzgo | San Pedro Amuzgos Amuzgo | na | 1.46e-01 | 5,941 | 100.0% |
| [tuf](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tuf.msgpack.gz) | Central Tunebo | Central Tunebo | cat | 2.09e-02 | 5,213 | 100.0% |
| [dad](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_dad.msgpack.gz) | Marik | Marik | anĩ | 3.30e-02 | 5,898 | 100.0% |
| [ban](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ban.msgpack.gz) | Balinese | Balinese | Ida | 3.49e-02 | 5,934 | 100.0% |
| [myb](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_myb.msgpack.gz) | Mbay | Mbay | kï | 7.35e-02 | 4,635 | 100.0% |
| [cab](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cab.msgpack.gz) | Garifuna | Garifuna | le | 4.83e-02 | 6,777 | 100.0% |
| [mgh](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mgh.msgpack.gz) | Makhuwa-Meetto | Makua | ni | 5.25e-02 | 6,762 | 100.0% |
| [ote](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ote.msgpack.gz) | Mezquital Otomi | Mezquital Otomi | ra | 5.38e-02 | 4,795 | 100.0% |
| [knf](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_knf.msgpack.gz) | Mankanya | Mankanya | kë | 3.89e-02 | 6,201 | 100.0% |
| [mwv](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mwv.msgpack.gz) | Mentawai | Mentawai | ka | 8.13e-02 | 5,916 | 100.0% |
| [kru](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kru.msgpack.gz) | Kurukh | Kurukh | अरा | 3.83e-02 | 5,628 | 100.0% |
| [pir](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_pir.msgpack.gz) | Piratapuyo | Piratapuyo | tiquiro | 3.84e-02 | 5,667 | 100.0% |
| [agd](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_agd.msgpack.gz) | Agarabi | Agarabi | ma | 5.54e-02 | 11,421 | 100.0% |
| [npy](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_npy.msgpack.gz) | Napu | Napu | au | 6.25e-02 | 5,790 | 100.0% |
| [nzi](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_nzi.msgpack.gz) | Nzima | Nzima | ne | 5.20e-02 | 4,680 | 100.0% |
| [ssg](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ssg.msgpack.gz) | Seimat | Seimat | ti | 6.17e-02 | 5,004 | 100.0% |
| [pad](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_pad.msgpack.gz) | Paumarí | Paumarí | ida | 6.36e-02 | 8,232 | 100.0% |
| [myy](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_myy.msgpack.gz) | Macuna | Macuna | ĩ | 3.88e-02 | 6,260 | 100.0% |
| [dgz](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_dgz.msgpack.gz) | Daga | Daga | gapan | 2.25e-02 | 7,928 | 100.0% |
| [duo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_duo.msgpack.gz) | Dupaninan Agta | Dupaninan Agta | a | 9.94e-02 | 4,659 | 100.0% |
| [mfk](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mfk.msgpack.gz) | North Mofu | North Mofu | ma | 1.01e-01 | 3,326 | 100.0% |
| [pjt](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_pjt.msgpack.gz) | Pitjantjatjara | Pitjantjatjara | panya | 3.75e-02 | 4,972 | 100.0% |
| [ctu](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ctu.msgpack.gz) | Chol | Chol | i | 7.18e-02 | 3,862 | 100.0% |
| [taj](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_taj.msgpack.gz) | Eastern Tamang | Eastern Tamang | भिसी | 2.13e-02 | 5,095 | 100.0% |
| [tlj](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tlj.msgpack.gz) | Talinga-Bwisi | Talinga-Bwisi | mu | 2.89e-02 | 7,782 | 100.0% |
| [tbc](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tbc.msgpack.gz) | Takia | Takia | lo | 2.98e-02 | 5,220 | 100.0% |
| [kdj](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kdj.msgpack.gz) | Karamojong | Karamojong | a | 4.73e-02 | 6,229 | 100.0% |
| [mfi](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mfi.msgpack.gz) | Wandala | Wandala | á | 7.75e-02 | 4,733 | 100.0% |
| [usp](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_usp.msgpack.gz) | Uspanteco | Uspanteco | ri | 4.76e-02 | 4,996 | 100.0% |
| [sri](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_sri.msgpack.gz) | Siriano | Siriano | merã | 2.65e-02 | 6,729 | 100.0% |
| [avn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_avn.msgpack.gz) | Avatime | Avatime | lɛ | 4.19e-02 | 5,434 | 100.0% |
| [bku](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bku.msgpack.gz) | Buhid | Buhid | manga | 3.67e-02 | 4,338 | 100.0% |
| [mag](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mag.msgpack.gz) | Magahi | Magahi | के | 6.78e-02 | 5,158 | 100.0% |
| [zpq](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_zpq.msgpack.gz) | Zoogocho Zapotec | Zoogocho Zapotec | na | 5.98e-02 | 6,257 | 100.0% |
| [zpc](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_zpc.msgpack.gz) | Choapan Zapotec | Choapan Zapotec | ben | 4.65e-02 | 6,260 | 100.0% |
| [vut](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_vut.msgpack.gz) | Vute | Vute | á | 3.99e-02 | 5,272 | 100.0% |
| [ccp](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ccp.msgpack.gz) | Chakma | 𑄌𑄋𑄴𑄟𑄳𑄦 | 𑄚𑄧 | 1.57e-02 | 4,770 | 100.0% |
| [new](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_new.msgpack.gz) | Newari | Newari | हे | 2.52e-02 | 6,156 | 100.0% |
| [quc](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_quc.msgpack.gz) | Kʼicheʼ | Kʼicheʼ | ri | 1.86e-01 | 5,033 | 100.0% |
| [xog](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_xog.msgpack.gz) | Soga | Olusoga | mu | 3.93e-02 | 8,021 | 100.0% |
| [bzh](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bzh.msgpack.gz) | Mapos Buang | Mapos Buang | vu | 3.68e-02 | 5,602 | 100.0% |
| [nca](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_nca.msgpack.gz) | Iyo | Iyo | uni | 2.95e-02 | 6,554 | 100.0% |
| [ae](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ae.msgpack.gz) | Avestan | Avestan | 𐬫𐬀𐬰𐬀𐬨𐬀𐬌𐬛𐬈 | 1.58e-02 | 5,561 | 100.0% |
| [lob](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_lob.msgpack.gz) | Lobi | Lobi | na | 5.23e-02 | 5,299 | 100.0% |
| [cak](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cak.msgpack.gz) | Kaqchikel | Kaqchikel | ri | 1.54e-01 | 4,825 | 100.0% |
| [gof](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_gof.msgpack.gz) | Gofa | Gofa | ሂንቴ | 1.41e-02 | 6,773 | 100.0% |
| [kyq](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kyq.msgpack.gz) | Kenga | Kenga | se | 7.77e-02 | 4,354 | 100.0% |
| [xsu](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_xsu.msgpack.gz) | Sanumá | Sanumá | ĩ | 9.27e-02 | 4,652 | 100.0% |
| [blz](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_blz.msgpack.gz) | Balantak | Balantak | men | 5.66e-02 | 5,109 | 100.0% |
| [fuq](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_fuq.msgpack.gz) | Central-Eastern Niger Fulfulde | Central-Eastern Niger Fulfulde | e | 4.71e-02 | 5,857 | 100.0% |
| [cjv](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cjv.msgpack.gz) | Chuave | Chuave | yokamai | 3.97e-02 | 5,284 | 100.0% |
| [bvz](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bvz.msgpack.gz) | Bauzi | Bauzi | bak | 5.04e-02 | 5,881 | 100.0% |
| [bik](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bik.msgpack.gz) | Bikol | Bikol | an | 6.33e-02 | 4,767 | 100.0% |
| [viv](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_viv.msgpack.gz) | Iduna | Iduna | againe | 2.49e-02 | 13,884 | 100.0% |
| [nia](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_nia.msgpack.gz) | Nias | Nias | ba | 9.93e-02 | 4,799 | 100.0% |
| [nnb](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_nnb.msgpack.gz) | Nande | Nande | omo | 2.70e-02 | 7,904 | 100.0% |
| [cui](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cui.msgpack.gz) | Cuiba | Cuiba | xua | 5.67e-02 | 7,569 | 100.0% |
| [xla](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_xla.msgpack.gz) | Kamula | Kamula | dla | 4.84e-02 | 9,480 | 100.0% |
| [min](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_min.msgpack.gz) | Minangkabau | Minangkabau | nan | 5.41e-02 | 4,925 | 100.0% |
| [alp](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_alp.msgpack.gz) | Alune | Alune | esi | 4.35e-02 | 3,601 | 100.0% |
| [sat](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_sat.msgpack.gz) | Santali | ᱥᱟᱱᱛᱟᱲᱤ | ᱨᱮ | 3.25e-02 | 5,714 | 100.0% |
| [ycn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ycn.msgpack.gz) | Yucuna | Yucuna | ke | 2.97e-02 | 5,895 | 100.0% |
| [tpm](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tpm.msgpack.gz) | Tampulma | Tampulma | a | 4.41e-02 | 5,938 | 100.0% |
| [cbv](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cbv.msgpack.gz) | Cacua | Cacua | ã | 5.04e-02 | 4,834 | 100.0% |
| [nlc](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_nlc.msgpack.gz) | Nalca | Nalca | dara | 3.21e-02 | 6,635 | 100.0% |
| [sda](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_sda.msgpack.gz) | Toraja-Sa'dan | Toraja-Sa'dan | tu | 6.47e-02 | 6,636 | 100.0% |
| [bao](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bao.msgpack.gz) | Waimaha | Waimaha | ca | 9.84e-02 | 5,825 | 100.0% |
| [toc](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_toc.msgpack.gz) | Coyutla Totonac | Coyutla Totonac | y | 3.79e-02 | 8,645 | 100.0% |
| [lem](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_lem.msgpack.gz) | Nomaande | Nomaande | a | 2.75e-02 | 5,003 | 100.0% |
| [mqn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mqn.msgpack.gz) | Moronene | Moronene | da | 5.46e-02 | 6,040 | 100.0% |
| [gn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_gn.msgpack.gz) | Guarani | avañe’ẽ | ha | 6.00e-02 | 6,024 | 100.0% |
| [grt](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_grt.msgpack.gz) | Garo | Garo | আরো | 3.20e-02 | 6,812 | 100.0% |
| [kwi](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kwi.msgpack.gz) | Awa-Cuaiquer | Awa-Cuaiquer | aizpa | 2.43e-02 | 7,091 | 100.0% |
| [ter](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ter.msgpack.gz) | Tereno | Tereno | ne | 4.75e-02 | 7,988 | 100.0% |
| [hui](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_hui.msgpack.gz) | Huli | Huli | howa | 1.94e-02 | 9,937 | 100.0% |
| [kzj](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kzj.msgpack.gz) | Central Dusun | Central Dusun | do | 1.10e-01 | 4,985 | 100.0% |
| [wuv](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_wuv.msgpack.gz) | Wuvulu-Aua | Wuvulu-Aua | fei | 5.13e-02 | 7,483 | 100.0% |
| [eri](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_eri.msgpack.gz) | Ogea | Ogea | no | 5.09e-02 | 6,194 | 100.0% |
| [mvp](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mvp.msgpack.gz) | Duri | Duri | to | 6.91e-02 | 6,563 | 100.0% |
| [bkl](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bkl.msgpack.gz) | Berik | Berik | jei | 5.58e-02 | 6,148 | 100.0% |
| [hil](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_hil.msgpack.gz) | Hiligaynon | Ilonggo | sa | 7.94e-02 | 4,808 | 100.0% |
| [ndj](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ndj.msgpack.gz) | Ndamba | Ndamba | na | 5.93e-02 | 6,444 | 100.0% |
| [tpp](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tpp.msgpack.gz) | Pisaflores Tepehua | Pisaflores Tepehua | an | 1.23e-01 | 7,640 | 100.0% |
| [tcc](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tcc.msgpack.gz) | Datooga | Datooga | ak | 4.56e-02 | 6,735 | 100.0% |
| [nko](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_nko.msgpack.gz) | Nkonya | Nkonya | mʋ | 3.43e-02 | 5,389 | 100.0% |
| [apr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_apr.msgpack.gz) | Arop-Lokep | Arop-Lokep | ngan | 4.66e-02 | 4,478 | 100.0% |
| [mai](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mai.msgpack.gz) | Maithili | मैथिली | सभ | 4.72e-02 | 5,038 | 100.0% |
| [mpx](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mpx.msgpack.gz) | Misima-Panaeati | Misima-Panaeati | i | 6.73e-02 | 4,989 | 100.0% |
| [chr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_chr.msgpack.gz) | Cherokee | ᏣᎳᎩ | ᎠᎴ | 7.12e-02 | 8,252 | 100.0% |
| [soq](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_soq.msgpack.gz) | Kanasi | Kanasi | me | 2.77e-02 | 15,618 | 100.0% |
| [poh](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_poh.msgpack.gz) | Poqomchi' | Poqomchi' | i | 1.21e-01 | 4,923 | 100.0% |
| [mee](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mee.msgpack.gz) | Mengen | Mengen | ka | 5.44e-02 | 5,464 | 100.0% |
| [fuf](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_fuf.msgpack.gz) | Pular | Pular | e | 5.53e-02 | 6,348 | 100.0% |
| [kaq](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kaq.msgpack.gz) | Capanahua | Capanahua | ta | 4.19e-02 | 6,833 | 100.0% |
| [cax](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cax.msgpack.gz) | Chiquitano | Chiquitano | axɨna | 2.70e-02 | 4,801 | 100.0% |
| [chz](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_chz.msgpack.gz) | Ozumacín Chinantec | Ozumacín Chinantec | heˉ | 3.81e-02 | 4,047 | 100.0% |
| [ayo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ayo.msgpack.gz) | Ayoreo | Ayoreo | ore | 6.21e-02 | 6,547 | 100.0% |
| [btx](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_btx.msgpack.gz) | Batak Karo | Batak Karo | si | 5.97e-02 | 4,509 | 100.0% |
| [irk](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_irk.msgpack.gz) | Iraqw | Iraqw | nee | 3.48e-02 | 6,554 | 100.0% |
| [jac](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_jac.msgpack.gz) | Popti' | Popti' | Comam | 5.10e-02 | 5,853 | 100.0% |
| [anv](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_anv.msgpack.gz) | Denya | Denya | ne | 5.82e-02 | 6,252 | 100.0% |
| [tzj](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tzj.msgpack.gz) | Tz'utujil | Tz'utujil | y | 2.90e-02 | 5,913 | 100.0% |
| [bbb](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bbb.msgpack.gz) | Barai | Barai | ije | 6.53e-02 | 9,306 | 100.0% |
| [mak](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mak.msgpack.gz) | Makasar | Makasar | ri | 7.10e-02 | 7,096 | 100.0% |
| [ura](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ura.msgpack.gz) | Urarina | Urarina | nii | 4.13e-02 | 7,730 | 100.0% |
| [lsm](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_lsm.msgpack.gz) | Saamia | Saamia | mu | 2.96e-02 | 8,081 | 100.0% |
| [top](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_top.msgpack.gz) | Papantla Totonac | Papantla Totonac | y | 4.75e-02 | 7,839 | 100.0% |
| [mco](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mco.msgpack.gz) | Coatlán Mixe | Coatlán Mixe | ajcxy | 5.86e-02 | 7,450 | 100.0% |
| [wos](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_wos.msgpack.gz) | Hanga Hundi | Hanga Hundi | dé | 5.08e-02 | 6,290 | 100.0% |
| [mca](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mca.msgpack.gz) | Maca | Maca | qa | 1.09e-01 | 7,146 | 100.0% |
| [mbb](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mbb.msgpack.gz) | Western Bukidnon Manobo | Western Bukidnon Manobo | te | 9.16e-02 | 4,907 | 100.0% |
| [kpx](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kpx.msgpack.gz) | Mountain Koiali | Mountain Koiali | ke | 3.26e-02 | 8,700 | 100.0% |
| [akb](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_akb.msgpack.gz) | Batak Angkola | Batak Angkola | na | 6.53e-02 | 4,821 | 100.0% |
| [quw](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_quw.msgpack.gz) | Tena Lowland Quichua | Tena Lowland Quichua | mana | 2.53e-02 | 6,903 | 100.0% |
| [ubu](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ubu.msgpack.gz) | Umbu-Ungu | Umbu-Ungu | kinia | 2.91e-02 | 4,651 | 100.0% |
| [btd](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_btd.msgpack.gz) | Batak Dairi | Batak Dairi | i | 5.47e-02 | 5,314 | 100.0% |
| [nuj](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_nuj.msgpack.gz) | Nyole | Nyole | ni | 4.06e-02 | 9,309 | 100.0% |
| [cbr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cbr.msgpack.gz) | Cashibo-Cacataibo | Cashibo-Cacataibo | ca | 6.04e-02 | 6,305 | 100.0% |
| [yo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_yo.msgpack.gz) | Yoruba | Èdè Yorùbá | ti | 4.25e-02 | 5,837 | 100.0% |
| [twb](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_twb.msgpack.gz) | Western Tawbuid | Western Tawbuid | ay | 7.22e-02 | 3,562 | 100.0% |
| [kez](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kez.msgpack.gz) | Kukele | Kukele | ka | 6.25e-02 | 5,202 | 100.0% |
| [ee](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ee.msgpack.gz) | Ewe | eʋegbe | la | 4.92e-02 | 8,070 | 100.0% |
| [xal](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_xal.msgpack.gz) | Kalmyk | Kalmyk | гиҗ | 1.64e-02 | 7,745 | 100.0% |
| [poi](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_poi.msgpack.gz) | Highland Popoluca | Highland Popoluca | jém | 1.46e-01 | 6,168 | 100.0% |
| [lnd](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_lnd.msgpack.gz) | Lundayeh | Lundayeh | idi | 6.98e-02 | 6,113 | 100.0% |
| [dsh](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_dsh.msgpack.gz) | Daasanach | Daasanach | hí | 4.24e-02 | 5,925 | 100.0% |
| [sxn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_sxn.msgpack.gz) | Sangir | Sangir | i | 6.47e-02 | 7,305 | 100.0% |
| [iu](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_iu.msgpack.gz) | Inuktitut | Inuktitut | ᓄᓇᕗᑦ | 1.22e-02 | 38,568 | 100.0% |
| [teo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_teo.msgpack.gz) | Teso | Kiteso | ka | 2.73e-02 | 6,904 | 100.0% |
| [nsu](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_nsu.msgpack.gz) | Sierra Negra Nahuatl | Sierra Negra Nahuatl | tlen | 5.05e-02 | 6,484 | 100.0% |
| [ruf](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ruf.msgpack.gz) | Luguru | Luguru | na | 4.45e-02 | 6,728 | 100.0% |
| [ata](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ata.msgpack.gz) | Pele-Ata | Pele-Ata | la | 4.60e-02 | 9,286 | 100.0% |
| [heh](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_heh.msgpack.gz) | Hehe | Hehe | na | 5.38e-02 | 7,903 | 100.0% |
| [kv](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kv.msgpack.gz) | Komi | Komi | да | 3.52e-02 | 7,489 | 100.0% |
| [cbi](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cbi.msgpack.gz) | Chachi | Chachi | bain | 3.92e-02 | 8,109 | 100.0% |
| [ilo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ilo.msgpack.gz) | Iloko | Ilokano | ti | 9.10e-02 | 6,761 | 100.0% |
| [zad](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_zad.msgpack.gz) | Cajonos Zapotec | Cajonos Zapotec | na | 7.38e-02 | 6,372 | 100.0% |
| [or](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_or.msgpack.gz) | Odia | ଓଡ଼ିଆ | ଓ | 1.94e-02 | 6,682 | 100.0% |
| [ngp](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ngp.msgpack.gz) | Ngulu | Ngulu | na | 3.38e-02 | 6,916 | 100.0% |
| [ssd](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ssd.msgpack.gz) | Siroi | Siroi | nu | 5.02e-02 | 6,304 | 100.0% |
| [old](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_old.msgpack.gz) | Mochi | Mochi | na | 6.31e-02 | 7,466 | 100.0% |
| [pah](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_pah.msgpack.gz) | Tenharim | Tenharim | pe | 6.69e-02 | 7,767 | 100.0% |
| [car](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_car.msgpack.gz) | Carib | Carib | moro | 4.17e-02 | 5,767 | 100.0% |
| [ify](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ify.msgpack.gz) | Keley-I Kallahan | Keley-I Kallahan | ni | 8.13e-02 | 12,642 | 100.0% |
| [ewo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ewo.msgpack.gz) | Ewondo | ewondo | a | 5.18e-02 | 4,581 | 100.0% |
| [otd](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_otd.msgpack.gz) | Ot Danum | Ot Danum | ijo | 4.67e-02 | 4,814 | 100.0% |
| [taq](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_taq.msgpack.gz) | Tamasheq | Tamasheq | a | 5.00e-02 | 6,298 | 100.0% |
| [tbo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tbo.msgpack.gz) | Tawala | Tawala | i | 4.79e-02 | 7,375 | 100.0% |
| [snw](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_snw.msgpack.gz) | Selee | Selee | ni | 5.14e-02 | 6,010 | 100.0% |
| [nim](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_nim.msgpack.gz) | Nilamba | Nilamba | wa | 2.05e-02 | 7,826 | 100.0% |
| [txu](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_txu.msgpack.gz) | Kayapó | Kayapó | ne | 6.28e-02 | 5,659 | 100.0% |
| [adh](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_adh.msgpack.gz) | Adhola | Adhola | ma | 3.69e-02 | 4,663 | 100.0% |
| [kmg](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kmg.msgpack.gz) | Kâte | Kâte | e | 1.98e-02 | 11,842 | 100.0% |
| [ian](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ian.msgpack.gz) | Iatmul | Iatmul | kat | 7.00e-02 | 9,326 | 100.0% |
| [yva](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_yva.msgpack.gz) | Yawa | Yawa | po | 3.05e-02 | 4,580 | 100.0% |
| [tgo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tgo.msgpack.gz) | Sudest | Sudest | i | 6.82e-02 | 8,489 | 100.0% |
| [vun](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_vun.msgpack.gz) | Vunjo | Kyivunjo | na | 6.47e-02 | 6,195 | 100.0% |
| [lmk](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_lmk.msgpack.gz) | Lamkang | Lamkang | ngi | 5.47e-02 | 6,047 | 100.0% |
| [nhy](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_nhy.msgpack.gz) | Northern Oaxaca Nahuatl | Northern Oaxaca Nahuatl | iwan | 5.34e-02 | 6,507 | 100.0% |
| [alt](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_alt.msgpack.gz) | Southern Altai | Southern Altai | деп | 1.70e-02 | 7,647 | 100.0% |
| [zaa](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_zaa.msgpack.gz) | Sierra de Juárez Zapotec | Sierra de Juárez Zapotec | nna | 6.12e-02 | 5,461 | 100.0% |
| [kwj](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kwj.msgpack.gz) | Kwanga | Kwanga | ri | 3.80e-02 | 5,443 | 100.0% |
| [nch](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_nch.msgpack.gz) | Central Huasteca Nahuatl | Central Huasteca Nahuatl | huan | 7.10e-02 | 6,710 | 100.0% |
| [yuj](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_yuj.msgpack.gz) | Karkar-Yuri | Karkar-Yuri | te | 4.34e-02 | 8,094 | 100.0% |
| [bss](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bss.msgpack.gz) | Akoose | Akoose | á | 3.20e-02 | 6,942 | 100.0% |
| [zae](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_zae.msgpack.gz) | Yareni Zapotec | Yareni Zapotec | ka | 4.62e-02 | 6,685 | 100.0% |
| [gvc](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_gvc.msgpack.gz) | Guanano | Guanano | to | 3.42e-02 | 5,842 | 100.0% |
| [des](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_des.msgpack.gz) | Desano | Desano | ĩgʉ | 4.58e-02 | 7,054 | 100.0% |
| [ken](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ken.msgpack.gz) | Kenyang | Kɛnyaŋ | nɛ | 4.19e-02 | 5,839 | 100.0% |
| [iou](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_iou.msgpack.gz) | Tuma-Irumu | Tuma-Irumu | u | 2.50e-02 | 8,136 | 100.0% |
| [wmw](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_wmw.msgpack.gz) | Mwani | Mwani | na | 4.32e-02 | 6,909 | 100.0% |
| [myx](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_myx.msgpack.gz) | Masaaba | Masaaba | ni | 5.01e-02 | 7,302 | 100.0% |
| [bon](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bon.msgpack.gz) | Bine | Bine | me | 3.31e-02 | 8,299 | 100.0% |
| [cbs](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cbs.msgpack.gz) | Cashinahua | Cashinahua | jatu | 2.69e-02 | 8,775 | 100.0% |
| [su](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_su.msgpack.gz) | Sundanese | Basa Sunda | anu | 3.05e-02 | 6,937 | 100.0% |
| [emi](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_emi.msgpack.gz) | Mussau-Emira | Mussau-Emira | me | 6.26e-02 | 6,823 | 100.0% |
| [boa](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_boa.msgpack.gz) | Bora | Bora | o | 1.97e-02 | 8,695 | 100.0% |
| [dww](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_dww.msgpack.gz) | Dawawa | Dawawa | be | 7.24e-02 | 7,816 | 100.0% |
| [kdn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kdn.msgpack.gz) | Kunda | Kunda | na | 4.70e-02 | 7,104 | 100.0% |
| [tav](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tav.msgpack.gz) | Tatuyo | Tatuyo | cʉ | 5.04e-02 | 7,773 | 100.0% |
| [lon](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_lon.msgpack.gz) | Malawi Lomwe | Malawi Lomwe | wi | 4.63e-02 | 7,272 | 100.0% |
| [cuk](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cuk.msgpack.gz) | San Blas Kuna | San Blas Kuna | be | 3.12e-02 | 7,742 | 100.0% |
| [tsz](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tsz.msgpack.gz) | Purepecha | Purepecha | ka | 9.43e-02 | 7,327 | 100.0% |
| [dyu](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_dyu.msgpack.gz) | Dyula | Dyula | ka | 5.44e-02 | 8,406 | 100.0% |
| [jv](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_jv.msgpack.gz) | Javanese | Jawa | kang | 4.00e-02 | 6,225 | 100.0% |
| [akh](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_akh.msgpack.gz) | Angal Heneng | Angal Heneng | ora | 4.01e-02 | 5,977 | 100.0% |
| [cul](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cul.msgpack.gz) | Culina | Culina | huati | 1.74e-02 | 8,929 | 100.0% |
| [dyo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_dyo.msgpack.gz) | Jola-Fonyi | joola | di | 1.02e-01 | 7,942 | 100.0% |
| [gbi](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_gbi.msgpack.gz) | Galela | Galela | o | 1.04e-01 | 6,325 | 100.0% |
| [txa](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_txa.msgpack.gz) | Tombonuo | Tombonuo | nu | 9.06e-02 | 4,379 | 100.0% |
| [smt](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_smt.msgpack.gz) | Simte | Simte | a | 6.22e-02 | 5,717 | 100.0% |
| [mqj](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mqj.msgpack.gz) | Mamasa | Mamasa | anna | 3.70e-02 | 6,422 | 100.0% |
| [rwo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_rwo.msgpack.gz) | Rawa | Rawa | ngu | 7.41e-02 | 5,079 | 100.0% |
| [kqy](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kqy.msgpack.gz) | Koorete | Koorete | ኤ | 6.26e-02 | 7,847 | 100.0% |
| [mor](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mor.msgpack.gz) | Moro | Moro | ŋen | 5.58e-02 | 6,411 | 100.0% |
| [kpf](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kpf.msgpack.gz) | Komba | Komba | a | 3.68e-02 | 8,974 | 100.0% |
| [rav](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_rav.msgpack.gz) | Sampang | Sampang | खकामा | 4.46e-02 | 8,222 | 100.0% |
| [poy](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_poy.msgpack.gz) | Pogolo | Pogolo | na | 6.35e-02 | 6,671 | 100.0% |
| [yml](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_yml.msgpack.gz) | Iamalele | Iamalele | i | 1.14e-01 | 7,332 | 100.0% |
| [nog](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_nog.msgpack.gz) | Nogai | Nogai | эм | 2.12e-02 | 7,513 | 100.0% |
| [qul](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_qul.msgpack.gz) | North Bolivian Quechua | North Bolivian Quechua | jinataq | 2.06e-02 | 9,886 | 100.0% |
| [krc](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_krc.msgpack.gz) | Karachay-Balkar | Karachay-Balkar | да | 3.27e-02 | 7,926 | 100.0% |
| [guc](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_guc.msgpack.gz) | Wayuu | Wayuu | tü | 5.32e-02 | 8,313 | 100.0% |
| [sbl](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_sbl.msgpack.gz) | Botolan Sambal | Botolan Sambal | ya | 6.88e-02 | 4,941 | 100.0% |
| [kmo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kmo.msgpack.gz) | Kwoma | Kwoma | ma | 3.44e-02 | 8,265 | 100.0% |
| [csk](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_csk.msgpack.gz) | Jola-Kasa | Jola-Kasa | li | 1.26e-01 | 7,532 | 100.0% |
| [kto](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kto.msgpack.gz) | Kuot | Kuot | ga | 7.21e-02 | 7,710 | 100.0% |
| [law](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_law.msgpack.gz) | Lauje | Lauje | ma | 4.35e-02 | 8,018 | 100.0% |
| [udm](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_udm.msgpack.gz) | Udmurt | Udmurt | но | 4.02e-02 | 8,052 | 100.0% |
| [avt](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_avt.msgpack.gz) | Au | Au | mɨt | 3.95e-02 | 7,271 | 100.0% |
| [fil](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_fil.msgpack.gz) | Filipino | Filipino | sa | 7.20e-02 | 5,457 | 100.0% |
| [gub](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_gub.msgpack.gz) | Guajajára | Guajajára | a'e | 5.24e-02 | 8,470 | 100.0% |
| [maa](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_maa.msgpack.gz) | San Jerónimo Tecóatl Mazatec | San Jerónimo Tecóatl Mazatec | la̱ | 6.59e-02 | 7,582 | 100.0% |
| [cnh](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cnh.msgpack.gz) | Hakha Chin | Hakha Chin | a | 8.14e-02 | 7,642 | 100.0% |
| [ese](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ese.msgpack.gz) | Ese Ejja | Ese Ejja | pea | 2.40e-02 | 7,406 | 100.0% |
| [wnu](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_wnu.msgpack.gz) | Usan | Usan | eng | 6.82e-02 | 7,196 | 100.0% |
| [kbr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kbr.msgpack.gz) | Kafa | Kafa | bi | 4.35e-02 | 8,380 | 100.0% |
| [os](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_os.msgpack.gz) | Ossetic | ирон | æмæ | 3.38e-02 | 8,720 | 100.0% |
| [ht](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ht.msgpack.gz) | Haitian Creole | Kreyòl Ayisyen | yo | 5.55e-02 | 6,031 | 100.0% |
| [huv](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_huv.msgpack.gz) | San Mateo Del Mar Huave | San Mateo Del Mar Huave | wüx | 3.54e-02 | 4,429 | 100.0% |
| [mad](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mad.msgpack.gz) | Madurese | Madurese | se | 4.65e-02 | 10,306 | 100.0% |
| [cot](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cot.msgpack.gz) | Caquinte | Caquinte | Aapani | 2.93e-02 | 9,834 | 100.0% |
| [ktb](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ktb.msgpack.gz) | Kambaata | Kambaata | እኮዳ | 1.38e-02 | 9,096 | 100.0% |
| [snn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_snn.msgpack.gz) | Siona | Siona | yë'ë | 1.78e-02 | 5,892 | 100.0% |
| [bqj](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bqj.msgpack.gz) | Bandial | Bandial | me | 5.47e-02 | 7,717 | 100.0% |
| [tlf](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tlf.msgpack.gz) | Telefol | Telefol | uyo | 3.24e-02 | 6,304 | 100.0% |
| [shp](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_shp.msgpack.gz) | Shipibo-Conibo | Shipibo-Conibo | iki | 6.58e-02 | 7,229 | 100.0% |
| [meu](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_meu.msgpack.gz) | Motu | Motu | e | 6.73e-02 | 6,329 | 100.0% |
| [ksr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ksr.msgpack.gz) | Borong | Borong | ii | 3.13e-02 | 13,502 | 100.0% |
| [kdc](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kdc.msgpack.gz) | Kutu | Kutu | na | 5.93e-02 | 6,613 | 100.0% |
| [yaa](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_yaa.msgpack.gz) | Yaminahua | Yaminahua | ato | 3.66e-02 | 8,089 | 100.0% |
| [bua](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bua.msgpack.gz) | Buriat | Buriat | гэжэ | 2.00e-02 | 9,234 | 100.0% |
| [ozm](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ozm.msgpack.gz) | Koonzime | Koonzime | ó | 5.39e-02 | 5,150 | 100.0% |
| [mlp](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mlp.msgpack.gz) | Bargam | Bargam | in | 5.69e-02 | 7,358 | 100.0% |
| [tih](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tih.msgpack.gz) | Timugon Murut | Timugon Murut | ra | 1.08e-01 | 10,154 | 100.0% |
| [zaw](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_zaw.msgpack.gz) | Mitla Zapotec | Mitla Zapotec | ni | 3.83e-02 | 6,913 | 100.0% |
| [tpt](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tpt.msgpack.gz) | Tlachichilco Tepehua | Tlachichilco Tepehua | ni | 7.71e-02 | 6,597 | 100.0% |
| [msy](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_msy.msgpack.gz) | Aruamu | Aruamu | a | 3.43e-02 | 8,531 | 100.0% |
| [to](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_to.msgpack.gz) | Tongan | lea fakatonga | he | 3.93e-02 | 6,721 | 100.0% |
| [knv](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_knv.msgpack.gz) | Tabo | Tabo | ba | 2.58e-02 | 7,884 | 100.0% |
| [nyy](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_nyy.msgpack.gz) | Nyakyusa-Ngonde | Nyakyusa-Ngonde | bo | 2.44e-02 | 8,071 | 100.0% |
| [gmv-Latn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_gmv-Latn.msgpack.gz) | Gamo (Latin) | Gamo (Latin) | ta | 1.91e-02 | 7,642 | 100.0% |
| [nyo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_nyo.msgpack.gz) | Nyoro | Nyoro | omu | 2.91e-02 | 8,246 | 100.0% |
| [knj](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_knj.msgpack.gz) | Western Kanjobal | Western Kanjobal | eb | 4.63e-02 | 8,197 | 100.0% |
| [qvm](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_qvm.msgpack.gz) | Margos-Yarowilca-Lauricocha Quechua | Margos-Yarowilca-Lauricocha Quechua | Tayta | 2.93e-02 | 9,377 | 100.0% |
| [arl](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_arl.msgpack.gz) | Arabela | Arabela | na | 5.45e-02 | 8,256 | 100.0% |
| [lif](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_lif.msgpack.gz) | Limbu | Limbu | हे़क्‍क्‍याङ् | 2.72e-02 | 9,129 | 100.0% |
| [bsn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bsn.msgpack.gz) | Barasana-Eduria | Barasana-Eduria | ĩ | 4.58e-02 | 8,042 | 100.0% |
| [jae](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_jae.msgpack.gz) | Yabem | Yabem | ma | 3.62e-02 | 6,116 | 100.0% |
| [tlb](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tlb.msgpack.gz) | Tobelo | Tobelo | o | 1.24e-01 | 7,561 | 100.0% |
| [kij](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kij.msgpack.gz) | Kilivila | Kilivila | e | 5.56e-02 | 5,953 | 100.0% |
| [bdd](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bdd.msgpack.gz) | Bunama | Bunama | ma | 8.59e-02 | 12,081 | 100.0% |
| [atq](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_atq.msgpack.gz) | Aralle-Tabulahan | Aralle-Tabulahan | di | 4.68e-02 | 6,547 | 100.0% |
| [mnb](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mnb.msgpack.gz) | Muna | Muna | ne | 3.52e-02 | 7,571 | 100.0% |
| [sue](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_sue.msgpack.gz) | Suena | Suena | awa | 6.00e-02 | 7,226 | 100.0% |
| [wiu](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_wiu.msgpack.gz) | Wiru | Wiru | wa | 3.23e-02 | 12,588 | 100.0% |
| [yad](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_yad.msgpack.gz) | Yagua | Yagua | ji̱ta | 4.14e-02 | 8,614 | 100.0% |
| [kvn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kvn.msgpack.gz) | Border Kuna | Border Kuna | tule | 3.68e-02 | 7,499 | 100.0% |
| [hae](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_hae.msgpack.gz) | Eastern Oromo | Eastern Oromo | ti | 2.18e-02 | 7,758 | 100.0% |
| [cfm](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cfm.msgpack.gz) | Falam Chin | Falam Chin | a | 9.18e-02 | 6,664 | 100.0% |
| [haw](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_haw.msgpack.gz) | Hawaiian | ʻŌlelo Hawaiʻi | ka | 6.49e-02 | 8,910 | 100.0% |
| [pwg](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_pwg.msgpack.gz) | Gapapaiwa | Gapapaiwa | ma | 7.17e-02 | 8,501 | 100.0% |
| [awa](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_awa.msgpack.gz) | Awadhi | Awadhi | क | 7.16e-02 | 6,273 | 100.0% |
| [kpr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kpr.msgpack.gz) | Korafe-Yegha | Korafe-Yegha | da | 2.97e-02 | 7,396 | 100.0% |
| [tim](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tim.msgpack.gz) | Timbe | Timbe | are | 2.44e-02 | 9,631 | 100.0% |
| [noa](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_noa.msgpack.gz) | Woun Meu | Woun Meu | mag | 3.22e-02 | 8,564 | 100.0% |
| [coe](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_coe.msgpack.gz) | Koreguaje | Koreguaje | repaʉ | 2.80e-02 | 7,800 | 100.0% |
| [nnq](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_nnq.msgpack.gz) | Ngindo | Ngindo | na | 4.55e-02 | 7,260 | 100.0% |
| [way](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_way.msgpack.gz) | Wayana | Wayana | Masike | 4.11e-02 | 6,857 | 100.0% |
| [tap](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tap.msgpack.gz) | Taabwa | Taabwa | ni | 5.81e-02 | 6,594 | 100.0% |
| [ghs](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ghs.msgpack.gz) | Guhu-Samane | Guhu-Samane | ma | 2.92e-02 | 11,088 | 100.0% |
| [hub](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_hub.msgpack.gz) | Huambisa | Huambisa | tusa | 2.52e-02 | 10,017 | 100.0% |
| [myv](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_myv.msgpack.gz) | Erzya | эрзянь кель | ды | 4.43e-02 | 8,640 | 100.0% |
| [hnn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_hnn.msgpack.gz) | Hanunoo | Hanunoo | sa | 8.63e-02 | 4,435 | 100.0% |
| [kjh](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kjh.msgpack.gz) | Khakas | Khakas | паза | 1.64e-02 | 7,932 | 100.0% |
| [lex](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_lex.msgpack.gz) | Luang | Luang | la | 4.70e-02 | 7,355 | 100.0% |
| [ik](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ik.msgpack.gz) | Inupiaq | Inupiaq | suli | 2.69e-02 | 7,980 | 100.0% |
| [dtb](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_dtb.msgpack.gz) | Labuk-Kinabatangan Kadazan | Labuk-Kinabatangan Kadazan | do | 9.66e-02 | 6,136 | 100.0% |
| [nvm](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_nvm.msgpack.gz) | Namiae | Namiae | iji | 7.09e-02 | 9,655 | 100.0% |
| [mhl](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mhl.msgpack.gz) | Mauwake | Mauwake | oi | 3.11e-02 | 12,530 | 100.0% |
| [mlh](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mlh.msgpack.gz) | Mape | Mape | oi | 3.11e-02 | 12,530 | 100.0% |
| [qvn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_qvn.msgpack.gz) | North Junín Quechua | North Junín Quechua | chay | 2.83e-02 | 10,216 | 100.0% |
| [spl](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_spl.msgpack.gz) | Selepet | Selepet | yakât | 2.47e-02 | 9,984 | 100.0% |
| [qvo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_qvo.msgpack.gz) | Napo Lowland Quechua | Napo Lowland Quechua | mana | 3.12e-02 | 7,049 | 100.0% |
| [fai](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_fai.msgpack.gz) | Faiwol | Faiwol | kinim | 2.83e-02 | 11,964 | 100.0% |
| [kn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kn.msgpack.gz) | Kannada | ಕನ್ನಡ | ಎಂದು | 1.60e-02 | 10,023 | 100.0% |
| [guh](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_guh.msgpack.gz) | Guahibo | Guahibo | Dioso | 3.78e-02 | 10,412 | 100.0% |
| [gdn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_gdn.msgpack.gz) | Umanakaina | Umanakaina | ki | 7.01e-02 | 8,318 | 100.0% |
| [ntp](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ntp.msgpack.gz) | Northern Tepehuan | Northern Tepehuan | dai | 6.59e-02 | 6,770 | 100.0% |
| [qub](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_qub.msgpack.gz) | Huallaga Huánuco Quechua | Huallaga Huánuco Quechua | Tayta | 3.19e-02 | 9,647 | 100.0% |
| [big](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_big.msgpack.gz) | Biangai | Biangai | logo | 3.25e-02 | 9,159 | 100.0% |
| [kek](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kek.msgpack.gz) | Kekchí | Kekchí | li | 1.21e-01 | 10,215 | 100.0% |
| [mam](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mam.msgpack.gz) | - | - | ex | 4.09e-02 | 9,197 | 100.0% |
| [suz](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_suz.msgpack.gz) | Sunwar | Sunwar | कली | 4.31e-02 | 12,360 | 100.0% |
| [nhw](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_nhw.msgpack.gz) | Western Huasteca Nahuatl | Western Huasteca Nahuatl | huan | 7.10e-02 | 6,753 | 100.0% |
| [mtp](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mtp.msgpack.gz) | Wichí Lhamtés Nocten | Wichí Lhamtés Nocten | tà | 1.47e-01 | 7,220 | 100.0% |
| [dah](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_dah.msgpack.gz) | Gwahatike | Gwahatike | Al | 2.39e-02 | 5,979 | 100.0% |
| [av](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_av.msgpack.gz) | Avaric | Avaric | ва | 1.49e-02 | 7,864 | 100.0% |
| [qvi](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_qvi.msgpack.gz) | Imbabura Highland Quichua | Imbabura Highland Quichua | na | 2.80e-02 | 9,329 | 100.0% |
| [snc](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_snc.msgpack.gz) | Sinaugoro | Sinaugoro | tu | 4.37e-02 | 9,565 | 100.0% |
| [rn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_rn.msgpack.gz) | Rundi | Ikirundi | mu | 2.56e-02 | 8,163 | 100.0% |
| [mux](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mux.msgpack.gz) | Bo-Ung | Bo-Ung | kene | 4.05e-02 | 6,983 | 100.0% |
| [ml](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ml.msgpack.gz) | Malayalam | മലയാളം | ഞാന്‍ | 1.86e-02 | 9,721 | 100.0% |
| [amf](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_amf.msgpack.gz) | Hamer-Banna | Hamer-Banna | ki | 2.62e-02 | 8,110 | 100.0% |
| [boj](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_boj.msgpack.gz) | Anjam | Anjam | naŋgi | 3.98e-02 | 10,565 | 100.0% |
| [jmc](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_jmc.msgpack.gz) | Machame | Kimachame | na | 5.49e-02 | 6,818 | 100.0% |
| [sgw](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_sgw.msgpack.gz) | Sebat Bet Gurage | Sebat Bet Gurage | ሰብ | 2.63e-02 | 8,574 | 100.0% |
| [qvz](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_qvz.msgpack.gz) | Northern Pastaza Quichua | Northern Pastaza Quichua | mana | 3.07e-02 | 8,328 | 100.0% |
| [gwr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_gwr.msgpack.gz) | Gwere | Gwere | era | 3.45e-02 | 10,135 | 100.0% |
| [mfy](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mfy.msgpack.gz) | Mayo | Mayo | ä | 3.82e-02 | 7,525 | 100.0% |
| [eu](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_eu.msgpack.gz) | Basque | euskara | eta | 5.48e-02 | 7,712 | 100.0% |
| [cbc](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cbc.msgpack.gz) | Carapana | Carapana | cũ̶ | 5.20e-02 | 8,725 | 100.0% |
| [mti](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mti.msgpack.gz) | Maiwa (Papua New Guinea) | Maiwa (Papua New Guinea) | me | 5.95e-02 | 6,396 | 100.0% |
| [qxl](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_qxl.msgpack.gz) | Salasaca Highland Quichua | Salasaca Highland Quichua | na | 3.54e-02 | 8,862 | 100.0% |
| [hay](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_hay.msgpack.gz) | Haya | Haya | omu | 2.51e-02 | 8,205 | 100.0% |
| [agr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_agr.msgpack.gz) | Aguaruna | Aguaruna | Apajuí | 1.95e-02 | 10,349 | 100.0% |
| [chm](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_chm.msgpack.gz) | Mari | Mari | да | 3.10e-02 | 7,003 | 100.0% |
| [cub](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cub.msgpack.gz) | Cubeo | Cubeo | ʉ̃i | 2.81e-02 | 8,384 | 100.0% |
| [wlx](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_wlx.msgpack.gz) | Wali (Ghana) | Wali (Ghana) | a | 6.22e-02 | 9,208 | 100.0% |
| [mps](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mps.msgpack.gz) | Dadibi | Dadibi | te | 1.20e-01 | 8,747 | 100.0% |
| [npl](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_npl.msgpack.gz) | Southeastern Puebla Nahuatl | Southeastern Puebla Nahuatl | iwa | 5.88e-02 | 6,631 | 100.0% |
| [amr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_amr.msgpack.gz) | Amarakaeri | Amarakaeri | kenpaʼti | 1.64e-02 | 8,460 | 100.0% |
| [ms](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ms.msgpack.gz) | Malay | bahasa Malaysia | yang | 3.36e-02 | 9,518 | 100.0% |
| [tab](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tab.msgpack.gz) | Tabassaran | Tabassaran | ва | 2.78e-02 | 8,476 | 100.0% |
| [gaw](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_gaw.msgpack.gz) | Nobonob | Nobonob | amu | 5.80e-02 | 8,309 | 100.0% |
| [bba](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bba.msgpack.gz) | Baatonum | Baatonum | u | 5.39e-02 | 8,572 | 100.0% |
| [cv](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cv.msgpack.gz) | Chuvash | чӑваш | те | 2.26e-02 | 7,120 | 100.0% |
| [yuw](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_yuw.msgpack.gz) | Yau (Morobe Province) | Yau (Morobe Province) | yu | 3.55e-02 | 12,703 | 100.0% |
| [dob](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_dob.msgpack.gz) | Dobu | Dobu | ta | 4.89e-02 | 10,130 | 100.0% |
| [aby](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_aby.msgpack.gz) | Aneme Wake | Aneme Wake | i | 4.27e-02 | 10,257 | 100.0% |
| [kgf](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kgf.msgpack.gz) | Kube | Kube | imi | 3.82e-02 | 10,571 | 100.0% |
| [thk](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_thk.msgpack.gz) | Tharaka | Tharaka | na | 6.30e-02 | 7,103 | 100.0% |
| [bhl](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bhl.msgpack.gz) | Bimin | Bimin | te | 2.73e-02 | 8,362 | 100.0% |
| [mcb](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mcb.msgpack.gz) | Machiguenga | Machiguenga | Tasorintsi | 2.96e-02 | 9,512 | 100.0% |
| [mcd](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mcd.msgpack.gz) | Sharanahua | Sharanahua | un | 2.40e-02 | 8,474 | 100.0% |
| [cjo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cjo.msgpack.gz) | Ashéninka Pajonal | Ashéninka Pajonal | eejatzi | 3.47e-02 | 8,964 | 100.0% |
| [ctd-Latn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ctd-Latn.msgpack.gz) | Tedim Chin (Latin) | Tedim Chin (Latin) | a | 9.29e-02 | 10,651 | 100.0% |
| [cwt](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cwt.msgpack.gz) | Kuwaataay | Kuwaataay | i | 2.63e-02 | 7,585 | 100.0% |
| [kog](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kog.msgpack.gz) | Cogui | Cogui | ekí | 3.20e-02 | 10,756 | 100.0% |
| [tif](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tif.msgpack.gz) | Tifal | Tifal | tunum | 2.40e-02 | 9,252 | 100.0% |
| [not](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_not.msgpack.gz) | Nomatsiguenga | Nomatsiguenga | cara | 4.13e-02 | 8,287 | 100.0% |
| [cbt](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cbt.msgpack.gz) | Chayahuita | Chayahuita | co | 4.19e-02 | 8,287 | 100.0% |
| [tos](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tos.msgpack.gz) | Highland Totonac | Highland Totonac | chu̱ | 3.66e-02 | 9,170 | 100.0% |
| [pab](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_pab.msgpack.gz) | Parecís | Parecís | hoka | 8.28e-02 | 6,468 | 100.0% |
| [tnr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tnr.msgpack.gz) | Ménik | Ménik | Urün | 3.12e-02 | 8,469 | 100.0% |
| [kyc](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kyc.msgpack.gz) | Kyaka | Kyaka | lao | 3.32e-02 | 8,908 | 100.0% |
| [aoj](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_aoj.msgpack.gz) | Mufian | Mufian | ma | 2.02e-02 | 7,984 | 100.0% |
| [hto](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_hto.msgpack.gz) | Minica Huitoto | Minica Huitoto | izói | 2.37e-02 | 8,322 | 100.0% |
| [pck](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_pck.msgpack.gz) | Paite Chin | Paite Chin | a | 1.09e-01 | 13,569 | 100.0% |
| [sll](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_sll.msgpack.gz) | Salt-Yui | Salt-Yui | i | 2.72e-02 | 5,706 | 100.0% |
| [dln](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_dln.msgpack.gz) | Darlong | Darlong | a | 7.94e-02 | 10,770 | 100.0% |
| [kyz](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kyz.msgpack.gz) | Kayabí | Kayabí | ga | 1.11e-01 | 6,940 | 100.0% |
| [tte](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tte.msgpack.gz) | Bwanabwana | Bwanabwana | yo | 3.99e-02 | 9,781 | 100.0% |
| [tby](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tby.msgpack.gz) | Tabaru | Tabaru | ma | 9.71e-02 | 6,867 | 100.0% |
| [tue](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tue.msgpack.gz) | Tuyuca | Tuyuca | cũ̶ũ̶ | 2.31e-02 | 7,608 | 100.0% |
| [kaa](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kaa.msgpack.gz) | Kara-Kalpak | қарақалпақша | менен | 1.29e-02 | 8,693 | 100.0% |
| [mto](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mto.msgpack.gz) | Totontepec Mixe | Totontepec Mixe | je̱ | 1.30e-01 | 7,643 | 100.0% |
| [sim](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_sim.msgpack.gz) | Mende (Papua New Guinea) | Mende (Papua New Guinea) | or | 3.76e-02 | 7,827 | 100.0% |
| [rim](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_rim.msgpack.gz) | Nyaturu | Nyaturu | na | 5.51e-02 | 6,802 | 100.0% |
| [mi](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mi.msgpack.gz) | Māori | Māori | te | 8.03e-02 | 10,180 | 100.0% |
| [quf](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_quf.msgpack.gz) | Lambayeque Quechua | Lambayeque Quechua | chay | 3.47e-02 | 10,273 | 100.0% |
| [acu](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_acu.msgpack.gz) | Achuar-Shiwiar | Achuar-Shiwiar | Tura | 3.62e-02 | 9,000 | 100.0% |
| [nsn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_nsn.msgpack.gz) | Nehan | Nehan | tar | 5.21e-02 | 10,240 | 100.0% |
| [kbh](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kbh.msgpack.gz) | Camsá | Camsá | y | 5.26e-02 | 8,598 | 100.0% |
| [mox](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mox.msgpack.gz) | Molima | Molima | ta | 6.40e-02 | 9,253 | 100.0% |
| [ubr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ubr.msgpack.gz) | Ubir | Ubir | on | 1.21e-01 | 9,611 | 100.0% |
| [kud](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kud.msgpack.gz) | 'Auhelawa | 'Auhelawa | na | 7.07e-02 | 12,514 | 100.0% |
| [tca](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tca.msgpack.gz) | Ticuna | Ticuna | rü | 1.31e-01 | 7,345 | 100.0% |
| [pib](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_pib.msgpack.gz) | Yine | Yine | wa | 1.15e-01 | 7,152 | 100.0% |
| [vmw](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_vmw.msgpack.gz) | Makhuwa | emakhuwa | wira | 4.26e-02 | 7,372 | 100.0% |
| [kyg](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kyg.msgpack.gz) | Keyagana | Keyagana | huno | 2.78e-02 | 14,571 | 100.0% |
| [mcq](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mcq.msgpack.gz) | Ese | Ese | kaꞌene | 2.78e-02 | 15,072 | 100.0% |
| [qve](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_qve.msgpack.gz) | Eastern Apurímac Quechua | Eastern Apurímac Quechua | chay | 2.74e-02 | 11,229 | 100.0% |
| [gum](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_gum.msgpack.gz) | Guambiano | Guambiano | tru | 3.15e-02 | 8,851 | 100.0% |
| [jiv](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_jiv.msgpack.gz) | Shuar | Shuar | Tura | 2.62e-02 | 8,779 | 100.0% |
| [aai](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_aai.msgpack.gz) | Arifama-Miniafia | Arifama-Miniafia | ana | 3.89e-02 | 12,256 | 100.0% |
| [mpt](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mpt.msgpack.gz) | Mian | Mian | Gode | 2.14e-02 | 15,551 | 100.0% |
| [wer](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_wer.msgpack.gz) | Weri | Weri | Pël | 2.08e-02 | 9,239 | 100.0% |
| [qvs](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_qvs.msgpack.gz) | San Martín Quechua | San Martín Quechua | Tata | 3.32e-02 | 8,951 | 100.0% |
| [aso](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_aso.msgpack.gz) | Dano | Dano | nene | 6.33e-02 | 12,529 | 100.0% |
| [roo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_roo.msgpack.gz) | Rotokas | Rotokas | ia | 4.09e-02 | 12,920 | 100.0% |
| [amu](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_amu.msgpack.gz) | Guerrero Amuzgo | Guerrero Amuzgo | na | 1.50e-01 | 6,401 | 100.0% |
| [cap](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cap.msgpack.gz) | Chipaya | Chipaya | ni | 8.27e-02 | 7,826 | 100.0% |
| [jun](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_jun.msgpack.gz) | Juang | Juang | ଏରେ | 2.96e-02 | 6,635 | 100.0% |
| [qup](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_qup.msgpack.gz) | Southern Pastaza Quechua | Southern Pastaza Quechua | Yaya | 3.19e-02 | 9,887 | 100.0% |
| [khz](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_khz.msgpack.gz) | Keapara | Keapara | na | 5.13e-02 | 10,942 | 100.0% |
| [kbp](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kbp.msgpack.gz) | Kabiyè | Kabiyè | nɛ | 6.49e-02 | 10,781 | 100.0% |
| [zlm](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_zlm.msgpack.gz) | Malay (individual language) | Malay (individual language) | yang | 3.38e-02 | 11,976 | 100.0% |
| [wap](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_wap.msgpack.gz) | Wapishana | Wapishana | na'iki | 3.00e-02 | 6,485 | 100.0% |
| [kjs](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kjs.msgpack.gz) | East Kewa | East Kewa | Go | 3.30e-02 | 8,220 | 100.0% |
| [inb](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_inb.msgpack.gz) | Inga | Inga | mana | 3.56e-02 | 9,116 | 100.0% |
| [quy](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_quy.msgpack.gz) | Ayacucho Quechua | Ayacucho Quechua | mana | 2.22e-02 | 9,933 | 100.0% |
| [gdr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_gdr.msgpack.gz) | Wipi | Wipi | re | 3.12e-02 | 9,442 | 100.0% |
| [enb](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_enb.msgpack.gz) | Markweeta | Markweeta | nyoo | 3.31e-02 | 6,783 | 100.0% |
| [ame](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ame.msgpack.gz) | Yanesha' | Yanesha' | ñeñth | 5.44e-02 | 11,134 | 100.0% |
| [ppo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ppo.msgpack.gz) | Folopa | Folopa | fo | 1.99e-02 | 9,210 | 100.0% |
| [opm](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_opm.msgpack.gz) | Oksapmin | Oksapmin | oh | 5.86e-02 | 10,806 | 100.0% |
| [ino](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ino.msgpack.gz) | Inoke-Yate | Inoke-Yate | ani | 2.38e-02 | 17,597 | 100.0% |
| [ign](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ign.msgpack.gz) | Ignaciano | Ignaciano | eta | 1.46e-01 | 10,011 | 100.0% |
| [ded](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ded.msgpack.gz) | Dedua | Dedua | nga | 3.23e-02 | 13,563 | 100.0% |
| [aey](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_aey.msgpack.gz) | Amele | Amele | eu | 4.13e-02 | 12,553 | 100.0% |
| [mek](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mek.msgpack.gz) | Mekeo | Mekeo | auga | 4.07e-02 | 9,589 | 100.0% |
| [tbz](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tbz.msgpack.gz) | Ditammari | Ditammari | kɛ̀ | 4.38e-02 | 12,592 | 100.0% |
| [kk](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kk.msgpack.gz) | Kazakh | қазақ тілі | Sputnik | 1.39e-02 | 21,055 | 100.0% |
| [dtp](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_dtp.msgpack.gz) | Central Dusun | Central Dusun | do | 9.80e-02 | 11,016 | 100.0% |
| [faa](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_faa.msgpack.gz) | Fasu | Fasu | aporo | 3.58e-02 | 10,458 | 100.0% |
| [yua](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_yua.msgpack.gz) | Yucateco | Yucateco | u | 9.73e-02 | 15,378 | 100.0% |
| [uz](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_uz.msgpack.gz) | Uzbek | o‘zbek | ва | 1.63e-02 | 9,731 | 100.0% |
| [azz](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_azz.msgpack.gz) | Highland Puebla Nahuatl | Highland Puebla Nahuatl | Huan | 4.80e-02 | 8,705 | 100.0% |
| [kum](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kum.msgpack.gz) | Kumyk | Kumyk | да | 2.36e-02 | 8,045 | 100.0% |
| [kxc](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kxc.msgpack.gz) | Konso | Konso | ከ | 6.79e-02 | 7,886 | 100.0% |
| [qxo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_qxo.msgpack.gz) | Southern Conchucos Ancash Quechua | Southern Conchucos Ancash Quechua | Tayta | 2.96e-02 | 10,296 | 100.0% |
| [eza](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_eza.msgpack.gz) | Ezaa | Ezaa | iya | 2.85e-02 | 14,105 | 100.0% |
| [tzh](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tzh.msgpack.gz) | Tzeltal | Tzeltal | te | 1.32e-01 | 13,448 | 100.0% |
| [izz](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_izz.msgpack.gz) | Izii | Izii | ono | 3.01e-02 | 13,754 | 100.0% |
| [cof](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cof.msgpack.gz) | Colorado | Colorado | Junni | 3.15e-02 | 7,712 | 100.0% |
| [kup](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kup.msgpack.gz) | Kunimaipa | Kunimaipa | Met | 2.77e-02 | 10,451 | 100.0% |
| [ifb](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ifb.msgpack.gz) | Batad Ifugao | Batad Ifugao | ya | 9.13e-02 | 18,938 | 100.0% |
| [amm](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_amm.msgpack.gz) | Ama (Papua New Guinea) | Ama (Papua New Guinea) | mo | 8.07e-02 | 11,538 | 100.0% |
| [fit](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_fit.msgpack.gz) | Tornedalen Finnish | Tornedalen Finnish | ja | 2.70e-02 | 12,295 | 100.0% |
| [mrw](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mrw.msgpack.gz) | Maranao | Maranao | a | 1.04e-01 | 14,695 | 100.0% |
| [ace](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ace.msgpack.gz) | Acehnese | Acehnese | nyang | 4.29e-02 | 16,739 | 100.0% |
| [enq](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_enq.msgpack.gz) | Enga | Enga | doko | 4.14e-02 | 10,192 | 100.0% |
| [awb](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_awb.msgpack.gz) | Awa (Papua New Guinea) | Awa (Papua New Guinea) | íre | 2.31e-02 | 18,087 | 100.0% |
| [yby](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_yby.msgpack.gz) | Yaweyuha | Yaweyuha | maya | 3.78e-02 | 17,252 | 100.0% |
| [mva](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mva.msgpack.gz) | Manam | Manam | be | 9.03e-02 | 10,441 | 100.0% |
| [aon](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_aon.msgpack.gz) | Bumbita Arapesh | Bumbita Arapesh | aria | 6.62e-02 | 13,135 | 100.0% |
| [ape](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ape.msgpack.gz) | Bukiyip | Bukiyip | aria | 6.62e-02 | 13,135 | 100.0% |
| [ce](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ce.msgpack.gz) | Chechen | нохчийн | а | 8.08e-02 | 19,905 | 100.0% |
| [gag](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_gag.msgpack.gz) | Gagauz | Gagauz | hem | 1.20e-02 | 15,505 | 100.0% |
| [ceb](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ceb.msgpack.gz) | Cebuano | Cebuano | sa | 1.15e-01 | 15,283 | 100.0% |
| [bqc](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bqc.msgpack.gz) | Boko (Benin) | Boko (Benin) | ń | 4.84e-02 | 15,749 | 100.0% |
| [rro](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_rro.msgpack.gz) | Waima | Waima | hanona | 3.76e-02 | 10,525 | 100.0% |
| [bjr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bjr.msgpack.gz) | Binumarien | Binumarien | faqa | 2.52e-02 | 22,456 | 100.0% |
| [qxn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_qxn.msgpack.gz) | Northern Conchucos Ancash Quechua | Northern Conchucos Ancash Quechua | Dios | 2.49e-02 | 10,725 | 100.0% |
| [so](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_so.msgpack.gz) | Somali | Soomaali | oo | 3.47e-02 | 18,582 | 100.0% |
| [byr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_byr.msgpack.gz) | Baruya | Baruya | a'mwe | 1.76e-02 | 10,243 | 100.0% |
| [mdy](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mdy.msgpack.gz) | Male (Ethiopia) | Male (Ethiopia) | ታ | 1.48e-02 | 19,342 | 100.0% |
| [enx](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_enx.msgpack.gz) | Enxet | Enxet | axta | 5.84e-02 | 16,819 | 100.0% |
| [bef](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bef.msgpack.gz) | Benabena | Benabena | huto | 1.98e-02 | 14,814 | 100.0% |
| [rm-puter](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_rm-puter.msgpack.gz) | Romansh | rumantsch | da | 6.13e-02 | 19,808 | 100.0% |
| [rm-sutsilv](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_rm-sutsilv.msgpack.gz) | Romansh | rumantsch | da | 6.44e-02 | 18,247 | 100.0% |
| [ha](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ha.msgpack.gz) | Hausa | Hausa | da | 6.19e-02 | 15,717 | 100.0% |
| [ifa](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ifa.msgpack.gz) | Amganad Ifugao | Amganad Ifugao | ya | 7.11e-02 | 17,152 | 100.0% |
| [kbq](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kbq.msgpack.gz) | Kamano | Kamano | huno | 1.83e-02 | 26,100 | 100.0% |
| [bmu](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bmu.msgpack.gz) | Somba-Siawari | Somba-Siawari | mi | 2.62e-02 | 13,962 | 100.0% |
| [iws](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_iws.msgpack.gz) | Sepik Iwam | Sepik Iwam | mɨ | 8.16e-02 | 15,691 | 100.0% |
| [ba](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ba.msgpack.gz) | Bashkir | башҡорт теле | менән | 1.35e-02 | 25,171 | 100.0% |
| [rw](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_rw.msgpack.gz) | Kinyarwanda | Ikinyarwanda | mu | 4.87e-02 | 18,975 | 100.0% |
| [aom](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_aom.msgpack.gz) | Ömie | Ömie | God | 2.09e-02 | 16,634 | 100.0% |
| [gah](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_gah.msgpack.gz) | Alekano | Alekano | nene | 4.25e-02 | 14,425 | 100.0% |
| [qxr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_qxr.msgpack.gz) | Cañar Highland Quichua | Cañar Highland Quichua | mana | 2.43e-02 | 20,946 | 100.0% |
| [usa](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_usa.msgpack.gz) | Usarufa | Usarufa | íma | 1.48e-02 | 22,341 | 100.0% |
| [tk](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tk.msgpack.gz) | Turkmen | türkmen dili | we | 1.35e-02 | 25,914 | 100.0% |
| [wnc](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_wnc.msgpack.gz) | Wantoat | Wantoat | aminu | 2.34e-02 | 12,906 | 100.0% |
| [nop](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_nop.msgpack.gz) | Numanggang | Numanggang | adi | 3.50e-02 | 12,930 | 100.0% |
| [agg](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_agg.msgpack.gz) | Angor | Angor | ai | 4.78e-02 | 19,979 | 100.0% |
| [da](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_da.msgpack.gz) | Danish | dansk | og | 5.63e-02 | 14,764 | 100.0% |
| [kze](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kze.msgpack.gz) | Kosena | Kosena | íma | 2.26e-02 | 20,476 | 100.0% |
| [vec](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_vec.msgpack.gz) | Venetian | veneto | de | 3.61e-02 | 32,585 | 100.0% |
| [pxm](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_pxm.msgpack.gz) | Quetzaltepec Mixe | Quetzaltepec Mixe | ja | 9.14e-02 | 23,805 | 100.0% |
| [kmu](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kmu.msgpack.gz) | Kanite | Kanite | huno | 2.65e-02 | 19,261 | 100.0% |
| [for](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_for.msgpack.gz) | Fore | Fore | Piya | 2.72e-02 | 20,478 | 100.0% |
| [shn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_shn.msgpack.gz) | Shan | တႆး | င်း | 3.56e-02 | 13,598 | 100.0% |
| [gu](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_gu.msgpack.gz) | Gujarati | ગુજરાતી | અને | 3.48e-02 | 21,828 | 100.0% |
| [nas](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_nas.msgpack.gz) | Naasioi | Naasioi | tee | 4.76e-02 | 22,676 | 100.0% |
| [mg](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mg.msgpack.gz) | Malagasy | Malagasy | ny | 7.66e-02 | 27,333 | 100.0% |
| [pt-PT](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_pt-PT.msgpack.gz) | Portuguese (Portugal) | português (Portugal) | de | 4.97e-02 | 23,215 | 100.0% |
| [amp](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_amp.msgpack.gz) | Alamblak | Alamblak | nd | 3.27e-02 | 25,985 | 100.0% |
| [wrs](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_wrs.msgpack.gz) | Waris | Waris | os | 2.62e-02 | 21,043 | 100.0% |
| [si](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_si.msgpack.gz) | Sinhala | සිංහල | බව | 1.16e-02 | 24,331 | 100.0% |
| [ay](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ay.msgpack.gz) | Aymara | Aymara | uka | 2.47e-02 | 30,988 | 100.0% |
| [ti](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ti.msgpack.gz) | Tigrinya | ትግርኛ | ኣብ | 4.25e-02 | 24,072 | 100.0% |
| [ja](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ja.msgpack.gz) | Japanese | 日本語 | の | 5.79e-02 | 20,999 | 100.0% |
| [dwr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_dwr.msgpack.gz) | Dawro | Dawro | taani | 1.35e-02 | 17,614 | 100.0% |
| [tyv](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tyv.msgpack.gz) | Tuvinian | Tuvinian | ол | 1.75e-02 | 20,994 | 100.0% |
| [auy](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_auy.msgpack.gz) | Awiyaana | Awiyaana | ímba | 2.09e-02 | 19,615 | 100.0% |
| [kab-Tfng](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kab-Tfng.msgpack.gz) | Kabyle (Tifinagh) | Kabyle (Tifinagh) | ⵏ | 1.36e-01 | 35,580 | 100.0% |
| [hu](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_hu.msgpack.gz) | Hungarian | magyar | a | 8.66e-02 | 27,352 | 100.0% |
| [rm-surmiran](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_rm-surmiran.msgpack.gz) | Romansh | rumantsch | da | 4.60e-02 | 29,576 | 100.0% |
| [quh](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_quh.msgpack.gz) | South Bolivian Quechua | South Bolivian Quechua | chay | 2.12e-02 | 35,690 | 100.0% |
| [ku](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ku.msgpack.gz) | Kurdish | kurdî (kurmancî) | li | 3.50e-02 | 32,409 | 100.0% |
| [tt](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tt.msgpack.gz) | Tatar | татар | да | 1.53e-02 | 39,458 | 100.0% |
| [vec-u-sd-itpd](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_vec-u-sd-itpd.msgpack.gz) | Venetian | veneto | de | 5.06e-02 | 28,415 | 100.0% |
| [te](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_te.msgpack.gz) | Telugu | తెలుగు | ఆ | 1.87e-02 | 30,375 | 100.0% |
| [crh](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_crh.msgpack.gz) | Crimean Tatar | Crimean Tatar | ве | 3.06e-02 | 23,089 | 100.0% |
| [aak](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_aak.msgpack.gz) | Ankave | Ankave | nánɨ | 3.93e-02 | 20,221 | 100.0% |
| [kab-Arab](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kab-Arab.msgpack.gz) | Kabyle (Arabic) | Kabyle (Arabic) | ن | 4.92e-02 | 37,590 | 100.0% |
| [kj](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_kj.msgpack.gz) | Kuanyama | Kuanyama | ya | 2.14e-02 | 32,531 | 100.0% |
| [be](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_be.msgpack.gz) | Belarusian | беларуская | і | 2.95e-02 | 43,075 | 100.0% |
| [ta](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ta.msgpack.gz) | Tamil | தமிழ் | பிபிசி | 1.47e-02 | 43,412 | 100.0% |
| [lv](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_lv.msgpack.gz) | Latvian | latviešu | un | 2.54e-02 | 44,282 | 100.0% |
| [qu](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_qu.msgpack.gz) | Quechua | Runasimi | chay | 1.68e-02 | 36,685 | 100.0% |
| [agm](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_agm.msgpack.gz) | Angaataha | Angaataha | amɨ | 3.49e-02 | 34,495 | 100.0% |
| [sn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_sn.msgpack.gz) | Shona | chiShona | kuti | 2.46e-02 | 44,622 | 100.0% |
| [am](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_am.msgpack.gz) | Amharic | አማርኛ | ላይ | 1.07e-02 | 63,573 | 100.0% |
| [ny](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ny.msgpack.gz) | Nyanja | Nyanja | ndi | 4.15e-02 | 11,788 | 100.0% |
| [mbc](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mbc.msgpack.gz) | Macushi | Macushi | pe | 3.76e-02 | 5,434 | 100.0% |
| [qvc](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_qvc.msgpack.gz) | Cajamarca Quechua | Cajamarca Quechua | chay | 4.47e-02 | 10,257 | 100.0% |
| [gsw-u-sd-chag](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_gsw-u-sd-chag.msgpack.gz) | Swiss German | Schwiizertüütsch | de | 6.19e-02 | 3,903 | 100.0% |
| [fo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_fo.msgpack.gz) | Faroese | føroyskt | í | 4.20e-02 | 20,583 | 100.0% |
| [qvw](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_qvw.msgpack.gz) | Huaylla Wanca Quechua | Huaylla Wanca Quechua | mana | 2.25e-02 | 9,741 | 100.0% |
| [tbg](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tbg.msgpack.gz) | North Tairora | North Tairora | vi | 2.59e-02 | 7,011 | 100.0% |
| [lew](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_lew.msgpack.gz) | Ledo Kaili | Ledo Kaili | bo | 3.40e-02 | 5,372 | 100.0% |
| [srm](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_srm.msgpack.gz) | Saramaccan | Saramaccan | a | 5.23e-02 | 1,835 | 100.0% |
| [gsw-u-sd-chbe](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_gsw-u-sd-chbe.msgpack.gz) | Swiss German | Schwiizertüütsch | u | 3.65e-02 | 3,015 | 100.0% |
| [qwh](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_qwh.msgpack.gz) | Huaylas Ancash Quechua | Huaylas Ancash Quechua | y | 3.11e-02 | 10,230 | 100.0% |
| [my](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_my.msgpack.gz) | Burmese | မြန်မာ | တွေ | 3.05e-02 | 6,402 | 100.0% |
| [lo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_lo.msgpack.gz) | Lao | ລາວ | ການ | 2.03e-02 | 8,376 | 99.8% |
| [bo](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bo.msgpack.gz) | Tibetan | བོད་སྐད་ | པ | 2.32e-02 | 6,408 | 99.8% |
| [ur](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ur.msgpack.gz) | Urdu | اردو | کے | 4.62e-02 | 19,513 | 99.7% |
| [mt](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mt.msgpack.gz) | Maltese | Malti | li | 4.23e-02 | 30,637 | 99.4% |
| [km](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_km.msgpack.gz) | Khmer | ខ្មែរ | បាន | 1.99e-02 | 10,603 | 99.4% |
| [ro-MD](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ro-MD.msgpack.gz) | Romanian (Moldova) | română (Republica Moldova) | de | 5.48e-02 | 38,111 | 99.1% |
| [rm-rumgr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_rm-rumgr.msgpack.gz) | Romansh | rumantsch | da | 5.97e-02 | 33,572 | 99.0% |
| [tpi](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tpi.msgpack.gz) | Tok Pisin | Tok Pisin | long | 8.54e-02 | 18,533 | 99.0% |
| [cs](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cs.msgpack.gz) | Czech | čeština | v | 3.08e-02 | 43,748 | 99.0% |
| [id](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_id.msgpack.gz) | Indonesian | bahasa Indonesia | yang | 2.79e-02 | 25,642 | 98.9% |
| [az](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_az.msgpack.gz) | Azerbaijani | azərbaycan | və | 2.18e-02 | 48,036 | 98.9% |
| [rm-vallader](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_rm-vallader.msgpack.gz) | Romansh | rumantsch | da | 6.07e-02 | 31,534 | 98.8% |
| [cy](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_cy.msgpack.gz) | Welsh | Cymraeg | yn | 5.85e-02 | 23,607 | 98.7% |
| [hi](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_hi.msgpack.gz) | Hindi | हिन्दी | के | 4.45e-02 | 24,568 | 98.7% |
| [oc](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_oc.msgpack.gz) | Occitan | occitan | de | 6.99e-02 | 45,363 | 98.7% |
| [fa-AF](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_fa-AF.msgpack.gz) | Persian (Afghanistan) | فارسی (افغانستان) | در | 3.72e-02 | 24,430 | 98.7% |
| [ps](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ps.msgpack.gz) | Pashto | پښتو | د | 9.97e-02 | 25,006 | 98.6% |
| [el](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_el.msgpack.gz) | Greek | Ελληνικά | και | 2.84e-02 | 37,553 | 98.6% |
| [rm-sursilv](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_rm-sursilv.msgpack.gz) | Romansh | rumantsch | da | 4.14e-02 | 29,547 | 98.4% |
| [fa](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_fa.msgpack.gz) | Persian | فارسی | در | 4.23e-02 | 30,287 | 98.4% |
| [fr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_fr.msgpack.gz) | French | français | de | 5.77e-02 | 30,646 | 98.4% |
| [lb](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_lb.msgpack.gz) | Luxembourgish | Lëtzebuergesch | an | 2.89e-02 | 48,818 | 98.3% |
| [sq](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_sq.msgpack.gz) | Albanian | shqip | të | 7.48e-02 | 34,447 | 98.2% |
| [ga](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ga.msgpack.gz) | Irish | Gaeilge | an | 4.64e-02 | 31,446 | 97.9% |
| [sah](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_sah.msgpack.gz) | Yakut | саха тыла | да | 1.09e-02 | 62,012 | 97.8% |
| [gd](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_gd.msgpack.gz) | Scottish Gaelic | Gàidhlig | a | 6.89e-02 | 28,249 | 97.8% |
| [mk](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mk.msgpack.gz) | Macedonian | македонски | на | 6.15e-02 | 37,758 | 97.8% |
| [pa](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_pa.msgpack.gz) | Punjabi | ਪੰਜਾਬੀ | ਦੇ | 2.92e-02 | 23,946 | 97.8% |
| [bn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bn.msgpack.gz) | Bangla | বাংলা | এই | 1.04e-02 | 39,844 | 97.7% |
| [sw](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_sw.msgpack.gz) | Swahili | Kiswahili | ya | 5.95e-02 | 32,194 | 97.6% |
| [pt](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_pt.msgpack.gz) | Portuguese | português | de | 5.12e-02 | 31,641 | 97.6% |
| [ro](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ro.msgpack.gz) | Romanian | română | de | 5.10e-02 | 41,106 | 97.6% |
| [pl](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_pl.msgpack.gz) | Polish | polski | w | 4.17e-02 | 58,555 | 97.5% |
| [es](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_es.msgpack.gz) | Spanish | español | de | 7.13e-02 | 33,078 | 97.4% |
| [bg](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bg.msgpack.gz) | Bulgarian | български | на | 5.51e-02 | 42,920 | 97.4% |
| [sr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_sr.msgpack.gz) | Serbian | српски | је | 3.88e-02 | 50,369 | 97.4% |
| [ug](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ug.msgpack.gz) | Uyghur | ئۇيغۇرچە | ۋە | 1.59e-02 | 41,331 | 97.2% |
| [hr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_hr.msgpack.gz) | Croatian | hrvatski | u | 3.57e-02 | 54,789 | 97.2% |
| [it](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_it.msgpack.gz) | Italian | italiano | di | 4.03e-02 | 37,218 | 97.1% |
| [bs](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_bs.msgpack.gz) | Bosnian | bosanski | u | 3.76e-02 | 52,890 | 96.9% |
| [fi](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_fi.msgpack.gz) | Finnish | suomi | on | 3.12e-02 | 73,039 | 96.9% |
| [sr-Latn](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_sr-Latn.msgpack.gz) | Serbian (Latin) | srpski (latinica) | u | 3.56e-02 | 52,313 | 96.9% |
| [ka](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ka.msgpack.gz) | Georgian | ქართული | და | 2.80e-02 | 55,270 | 96.8% |
| [sv](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_sv.msgpack.gz) | Swedish | svenska | att | 3.38e-02 | 35,423 | 96.4% |
| [uk](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_uk.msgpack.gz) | Ukrainian | українська | у | 2.10e-02 | 53,807 | 96.4% |
| [et](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_et.msgpack.gz) | Estonian | eesti | ja | 3.34e-02 | 69,387 | 96.1% |
| [ky](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ky.msgpack.gz) | Kyrgyz | кыргызча | менен | 1.23e-02 | 49,306 | 96.1% |
| [nl](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_nl.msgpack.gz) | Dutch | Nederlands | de | 6.57e-02 | 37,244 | 96.1% |
| [tr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_tr.msgpack.gz) | Turkish | Türkçe | ve | 2.00e-02 | 55,043 | 96.1% |
| [sl](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_sl.msgpack.gz) | Slovenian | slovenščina | je | 3.52e-02 | 61,729 | 96.0% |
| [de](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_de.msgpack.gz) | German | Deutsch | die | 3.74e-02 | 43,815 | 95.6% |
| [hy](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_hy.msgpack.gz) | Armenian | հայերեն | է | 3.92e-02 | 53,763 | 95.6% |
| [mr](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_mr.msgpack.gz) | Marathi | मराठी | आहे | 2.32e-02 | 61,003 | 95.4% |
| [ar](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ar.msgpack.gz) | Arabic | العربية | في | 4.02e-02 | 53,858 | 95.1% |
| [be-tarask](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_be-tarask.msgpack.gz) | Belarusian | беларуская | на | 2.32e-02 | 46,910 | 94.4% |
| [ru](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ru.msgpack.gz) | Russian | русский | в | 4.70e-02 | 58,476 | 94.3% |
| [sk](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_sk.msgpack.gz) | Slovak | slovenčina | v | 2.88e-02 | 64,206 | 93.3% |
| [lt](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_lt.msgpack.gz) | Lithuanian | lietuvių | ir | 2.79e-02 | 65,239 | 92.8% |
| [ca-valencia](https://huggingface.co/datasets/vocabradar/VocabFreq/resolve/main/data_large/large_ca-valencia.msgpack.gz) | Catalan | català | de | 1.45e-03 | 2,508 | 1.9% |
<!-- END GENERATED LANGUAGE TABLE:data_large -->

## Sources

- data_small: HF dataset [vocabradar/wordfreq](https://huggingface.co/datasets/vocabradar/wordfreq) — cleaned wordfreq small lists (every word with frequency >= 1e-6), MIT.
- data_middle: HF dataset [omarkamali/wikipedia-monthly](https://huggingface.co/datasets/omarkamali/wikipedia-monthly) (20261001 snapshot) — Wikipedia token counts tokenized with pyicu; per-language top-100k + corpus total_tokens, CC BY-SA 3.0 / GFDL.
- data_large: [Unicode UniLex](https://github.com/unicode-org/unilex) frequency (Form\tFrequency, per billion tokens), Unicode DFS-2016.
