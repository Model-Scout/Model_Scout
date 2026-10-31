---
license: other
license_name: poetrymteb-mixed-copyright-research-use
license_link: https://huggingface.co/datasets/PoetryMTEB/MultilingualPoetryThemeClassification
task_categories:
- text-classification
task_ids:
- multi-class-classification
language:
- af
- am
- ar
- as
- ay
- be
- bg
- bn
- br
- bs
- ca
- cnr
- cs
- cy
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
- gd
- gl
- gu
- he
- hi
- hr
- hu
- hy
- id
- is
- it
- ja
- ka
- kk
- kl
- kn
- ko
- ku
- lt
- lv
- lzh
- mk
- ml
- mr
- ms
- mt
- my
- ne
- nl
- no
- or
- pa
- pl
- pt
- rm
- ro
- ru
- sd
- se
- sk
- sl
- sma
- sn
- sq
- sr
- sv
- sw
- ta
- te
- tn
- tr
- uk
- ur
- uz
- vi
- xh
- yi
- zh
multilinguality:
- multilingual
size_categories:
- 10K<n<100K
pretty_name: Multilingual Poetry Theme Classification
tags:
- poetry
- theme-classification
- topic-classification
- multilingual
- mteb
- poetrymteb
- embedding-evaluation
annotations_creators:
- expert-generated
- machine-generated
configs:
- config_name: train
  data_files:
  - split: train
    path: train/train-*
  default: true
- config_name: silver
  data_files:
  - split: test
    path: silver/test-*
- config_name: gold
  data_files:
  - split: test
    path: gold/test-*
dataset_info:
- config_name: train
  features:
  - name: id
    dtype: string
  - name: poem_id
    dtype: string
  - name: poem
    dtype: string
  - name: title
    dtype: string
  - name: author
    dtype: string
  - name: language
    dtype: string
  - name: language_name
    dtype: string
  - name: url
    dtype: string
  - name: label
    dtype: int64
  - name: label_name
    dtype: string
  - name: theme_category
    dtype: string
  - name: theme_category_en
    dtype: string
  - name: label_source
    dtype: string
  - name: deepseek-v3-1-250821
    dtype: string
  - name: kimi-k2-250905
    dtype: string
  - name: doubao-seed-1-6-lite-251015
    dtype: string
  splits:
  - name: train
    num_examples: 12466
- config_name: silver
  features:
  - name: id
    dtype: string
  - name: poem_id
    dtype: string
  - name: poem
    dtype: string
  - name: title
    dtype: string
  - name: author
    dtype: string
  - name: language
    dtype: string
  - name: language_name
    dtype: string
  - name: url
    dtype: string
  - name: label
    dtype: int64
  - name: label_name
    dtype: string
  - name: theme_category
    dtype: string
  - name: theme_category_en
    dtype: string
  - name: label_source
    dtype: string
  - name: deepseek-v3-1-250821
    dtype: string
  - name: kimi-k2-250905
    dtype: string
  - name: doubao-seed-1-6-lite-251015
    dtype: string
  splits:
  - name: test
    num_examples: 3133
- config_name: gold
  features:
  - name: id
    dtype: string
  - name: poem_id
    dtype: string
  - name: poem
    dtype: string
  - name: title
    dtype: string
  - name: author
    dtype: string
  - name: language
    dtype: string
  - name: language_name
    dtype: string
  - name: url
    dtype: string
  - name: label
    dtype: int64
  - name: label_name
    dtype: string
  - name: theme_category
    dtype: string
  - name: theme_category_en
    dtype: string
  - name: label_source
    dtype: string
  - name: deepseek-v3-1-250821
    dtype: string
  - name: kimi-k2-250905
    dtype: string
  - name: doubao-seed-1-6-lite-251015
    dtype: string
  splits:
  - name: test
    num_examples: 90
---

# Multilingual Poetry Theme Classification

**Multilingual, single-label poetic theme classification** for PoetryMTEB / MTEB-style embedding evaluation, using a **six-way theme taxonomy** (T1–T6).

**Train**, **silver**, and **gold** are packaged as **three parallel peer collections** (separate Hub configs). Poem texts are pairwise disjoint across train/gold and silver/gold (content soft-hash decontamination).

## Dataset Card

| Item | Description |
|------|-------------|
| **Dataset version (PoetryMTEB)** | `1.3.0` |
| **Hub repo** | [`PoetryMTEB/MultilingualPoetryThemeClassification`](https://huggingface.co/datasets/PoetryMTEB/MultilingualPoetryThemeClassification) |
| **Taxonomy** | T1–T6 (**6** theme classes) |
| **Task** | **Single-label** theme classification |
| **Unit** | Full poem text (`poem`) |
| **Languages** | **83+** (see language table) |
| **Collections (configs)** | `train` · `silver` · `gold` (peer sets) |
| **Size** | train=12466; silver=3133; gold=90; **total=15689** |
| **Anti-leakage** | gold poems removed from train & silver by content soft-hash |
| **License** | **other** (`poetrymteb-mixed-copyright-research-use`) — see License |
| **Evaluation metrics** | Accuracy; macro/micro F1 (`scripts/evaluate_theme.py`) |

## Collections (configs)

| Config | Hub split | n | Label quality |
|--------|-----------|--:|---------------|
| **`train`** (default) | `train` | 12466 | 3-LLM majority (`deepseek-v3-1-250821`, `kimi-k2-250905`, `doubao-seed-1-6-lite-251015`) |
| **`silver`** | `test` | 3133 | Same 3-LLM majority (held-out peer set) |
| **`gold`** | `test` | 90 | 5 humans ≥3/5; else expert adjudication |

```python
from datasets import load_dataset

train = load_dataset("PoetryMTEB/MultilingualPoetryThemeClassification", "train")["train"]
silver = load_dataset("PoetryMTEB/MultilingualPoetryThemeClassification", "silver")["test"]
gold = load_dataset("PoetryMTEB/MultilingualPoetryThemeClassification", "gold")["test"]
```

## Label taxonomy (T1–T6)

| id | code | name_en | name_zh | train | silver | gold |
|---:|------|---------|---------|------:|-------:|-----:|
| 0 | `T1` | Nature, Cosmos, and Sense of Place | 自然、宇宙与地方感 | 1833 | 463 | 16 |
| 1 | `T2` | Love, Emotion, and Relationships | 爱、情感与人际关系 | 3909 | 985 | 14 |
| 2 | `T3` | Life, Time, and Existence | 生命、时间与存在 | 2586 | 651 | 9 |
| 3 | `T4` | Society, Power, and History | 社会、权力与历史 | 2245 | 559 | 27 |
| 4 | `T5` | The Sacred, Transcendence, and Wisdom | 神圣、超验与智慧 | 1341 | 333 | 16 |
| 5 | `T6` | Language, Art, and Creation | 语言、艺术与创造 | 552 | 142 | 8 |

Codebook: `label_taxonomy.json`.

## Features

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Stable id (`mptheme-{collection}-{poem_id}`) |
| `poem_id` | string | Poem id (gold: `THEME-xxx`; train/silver: synthetic if absent) |
| `poem` | string | **Classification input**: full poem text |
| `title` | string | Title (decorative `*` / `[]` stripped) |
| `author` | string | Author (may be empty) |
| `language` | string | Language code (e.g. `ARA`, `ZHO`, `LZH`) |
| `language_name` | string | English language name |
| `url` | string | Source URL when matched from deduplicated corpus (`link`) |
| `label` | int64 | Theme class id (0–5) |
| `label_name` | string | Theme code (`T1`…`T6`) |
| `theme_category` | string | Chinese category name |
| `theme_category_en` | string | English category name |
| `label_source` | string | Provenance tag |
| `deepseek-v3-1-250821` | string | Per-model theme code (T1–T6 or empty) |
| `kimi-k2-250905` | string | Per-model theme code |
| `doubao-seed-1-6-lite-251015` | string | Per-model theme code |

### `label_source` values

| Value | Collection | Meaning |
|-------|------------|---------|
| `llm3_majority` | train / silver | 3-model majority theme code |
| `human_5H` | gold | 5 humans, ≥3/5 consensus |
| `expert_adjudication` | gold | Expert-adjudicated when no human majority |

Train and silver consensus `label` / `label_name` are derived from the three model columns. Gold `label` is human/expert; the three model columns are retained for comparison.

## Language coverage

| code | language | ISO | train | silver | gold |
|------|----------|-----|------:|-------:|-----:|
| `AFR` | Afrikaans | `af` | 3 | 0 | 1 |
| `AMH` | Amharic | `am` | 0 | 0 | 1 |
| `ARA` | Arabic | `ar` | 2165 | 543 | 2 |
| `ASM` | Assamese | `as` | 170 | 41 | 2 |
| `AYM` | Aymara | `ay` | 0 | 0 | 1 |
| `BEL` | Belarusian | `be` | 12 | 3 | 1 |
| `BEN` | Bengali | `bn` | 212 | 54 | 2 |
| `BOS` | Bosnian | `bs` | 6 | 3 | 1 |
| `BRE` | Breton | `br` | 4 | 1 | 1 |
| `BUL` | Bulgarian | `bg` | 189 | 48 | 2 |
| `CAT` | Catalan | `ca` | 13 | 3 | 1 |
| `CES` | Czech | `cs` | 742 | 186 | 2 |
| `CNR` | Montenegrin | `cnr` | 5 | 1 | 1 |
| `CYM` | Welsh | `cy` | 4 | 1 | 1 |
| `DAN` | Danish | `da` | 10 | 3 | 1 |
| `DEU` | German | `de` | 558 | 140 | 2 |
| `ELL` | Greek | `el` | 8 | 2 | 2 |
| `ENG` | English | `en` | 454 | 114 | 2 |
| `EST` | Estonian | `et` | 16 | 3 | 1 |
| `EUS` | Basque | `eu` | 3 | 0 | 0 |
| `FAS` | Persian | `fa` | 217 | 54 | 2 |
| `FIN` | Finnish | `fi` | 8 | 3 | 1 |
| `FRA` | French | `fr` | 198 | 52 | 2 |
| `GLA` | Scottish Gaelic | `gd` | 2 | 0 | 1 |
| `GLE` | Irish | `ga` | 3 | 2 | 1 |
| `GLG` | Galician | `gl` | 3 | 1 | 1 |
| `GUJ` | Gujarati | `gu` | 1 | 0 | 0 |
| `HEB` | Hebrew | `he` | 14 | 4 | 1 |
| `HIN` | Hindi | `hi` | 193 | 49 | 2 |
| `HRV` | Croatian | `hr` | 14 | 4 | 1 |
| `HUN` | Hungarian | `hu` | 179 | 45 | 2 |
| `HYE` | Armenian | `hy` | 1 | 0 | 0 |
| `IND` | Indonesian | `id` | 236 | 60 | 1 |
| `ISL` | Icelandic | `is` | 4 | 1 | 1 |
| `ITA` | Italian | `it` | 494 | 124 | 2 |
| `JPN` | Japanese | `ja` | 352 | 88 | 1 |
| `KAL` | Kalaallisut | `kl` | 1 | 0 | 0 |
| `KAN` | Kannada | `kn` | 2 | 0 | 1 |
| `KAT` | Georgian | `ka` | 3 | 1 | 1 |
| `KAZ` | Kazakh | `kk` | 3 | 1 | 0 |
| `KOR` | Korean | `ko` | 7 | 2 | 1 |
| `KUR` | Kurdish | `ku` | 2 | 1 | 1 |
| `LAV` | Latvian | `lv` | 7 | 3 | 1 |
| `LIT` | Lithuanian | `lt` | 15 | 4 | 1 |
| `LZH` | Classical Chinese | `lzh` | 2909 | 729 | 2 |
| `MAL` | Malayalam | `ml` | 2 | 0 | 1 |
| `MAR` | Marathi | `mr` | 2 | 0 | 1 |
| `MKD` | Macedonian | `mk` | 8 | 1 | 1 |
| `MLT` | Maltese | `mt` | 1 | 1 | 0 |
| `MSA` | Malay | `ms` | 2 | 0 | 0 |
| `MYA` | Burmese | `my` | 1 | 0 | 0 |
| `NEP` | Nepali | `ne` | 0 | 1 | 0 |
| `NLD` | Dutch | `nl` | 18 | 4 | 1 |
| `NOR` | Norwegian | `no` | 12 | 5 | 2 |
| `ORI` | Odia | `or` | 1 | 0 | 1 |
| `PAN` | Punjabi | `pa` | 199 | 51 | 2 |
| `POL` | Polish | `pl` | 11 | 2 | 1 |
| `POR` | Portuguese | `pt` | 225 | 58 | 2 |
| `ROH` | Romansh | `rm` | 4 | 1 | 1 |
| `RON` | Romanian | `ro` | 9 | 1 | 1 |
| `RUS` | Russian | `ru` | 670 | 169 | 2 |
| `SLK` | Slovak | `sk` | 6 | 1 | 1 |
| `SLV` | Slovenian | `sl` | 151 | 39 | 2 |
| `SMA` | Southern Sami | `sma` | 2 | 0 | 0 |
| `SME` | Northern Sami | `se` | 1 | 0 | 0 |
| `SNA` | Shona | `sn` | 1 | 0 | 0 |
| `SND` | Sindhi | `sd` | 2 | 0 | 0 |
| `SPA` | Spanish | `es` | 312 | 78 | 2 |
| `SQI` | Albanian | `sq` | 5 | 2 | 1 |
| `SRP` | Serbian | `sr` | 8 | 1 | 1 |
| `SWA` | Swahili | `sw` | 1 | 0 | 1 |
| `SWE` | Swedish | `sv` | 10 | 3 | 1 |
| `TAM` | Tamil | `ta` | 1 | 0 | 1 |
| `TEL` | Telugu | `te` | 2 | 0 | 0 |
| `TSN` | Tswana | `tn` | 1 | 0 | 0 |
| `TUR` | Turkish | `tr` | 228 | 58 | 2 |
| `UKR` | Ukrainian | `uk` | 12 | 3 | 1 |
| `UNK` | Unknown | `und` | 6 | 1 | 1 |
| `URD` | Urdu | `ur` | 205 | 52 | 2 |
| `UZB` | Uzbek | `uz` | 2 | 1 | 0 |
| `VIE` | Vietnamese | `vi` | 5 | 1 | 1 |
| `XHO` | Xhosa | `xh` | 0 | 1 | 0 |
| `YID` | Yiddish | `yi` | 4 | 0 | 1 |
| `ZHO` | Chinese | `zh` | 894 | 224 | 2 |

## Construction overview

```text
original MultilingualPoetryThemeClassification train ∪ test
        │
        ├─► stratified multilingual sample (90)
        │         │
        │         ├─► 5 humans ≥3/5 ─► human_5H
        │         └─► else Expert.jsonl ─► expert_adjudication ─► gold
        │
        ├─► train.jsonl  − gold (soft-hash) ─► train
        └─► test.jsonl   − gold (soft-hash) ─► silver
```

## Supporting materials

| Path | Content |
|------|---------|
| `VERSION` / `LICENSE` / `CITATION.*` / `metadata.json` | Packaging metadata |
| `label_taxonomy.json` | T1–T6 codebook + counts |
| `dataset_infos.yaml` | Hub viewer configs |
| `splits/*_ids.*` | poem_id lists |
| `checksums.sha256` | File hashes |
| `prompts/annotation_prompt_template.md` | Annotation prompt |
| `scripts/evaluate_theme.py` | Baseline probe (train → silver/gold) |

## How to load

```python
from datasets import load_dataset

train = load_dataset("PoetryMTEB/MultilingualPoetryThemeClassification", "train", split="train")
silver = load_dataset("PoetryMTEB/MultilingualPoetryThemeClassification", "silver", split="test")
gold = load_dataset("PoetryMTEB/MultilingualPoetryThemeClassification", "gold", split="test")

print(len(train), len(silver), len(gold))
print(gold[0]["language"], gold[0]["label_name"], gold[0]["theme_category_en"])
print(train[0]["deepseek-v3-1-250821"], train[0]["kimi-k2-250905"], train[0]["doubao-seed-1-6-lite-251015"])
```

## Intended use

- PoetryMTEB single-label theme probing under a shared T1–T6 taxonomy.
- Cross-lingual analysis of poetic thematic distributions.
- Comparison of individual LLM labels vs consensus / gold.

## Limitations

- Train and silver consensus labels are model-majority (silver standard), not human gold.
- Gold is small (n=90) but multilingual and human/expert curated.
- Some poems have empty `url` when the upstream deduplicated `link` is missing.
- **Some poem texts remain under copyright** in one or more jurisdictions; this packaging does **not** place those texts under an open Creative Commons license.

## Citation

```bibtex
@misc{multilingualpoetrythemeclassification,
  title     = {Multilingual Poetry Theme Classification},
  author    = {PoetryMTEB Contributors},
  year      = {2026},
  version   = {1.3.0},
  url       = {https://huggingface.co/datasets/PoetryMTEB/MultilingualPoetryThemeClassification},
  note      = {PoetryMTEB packaging; T1-T6 theme taxonomy; mixed copyright}
}
```

## License

**License tag:** `other` · **Name:** `poetrymteb-mixed-copyright-research-use`

This dataset is a **mixed-rights** packaging for PoetryMTEB research and embedding evaluation:

1. **Poem texts** — A non-trivial subset of poems is still within the **copyright term** (or otherwise rights-restricted) under applicable law. Redistribution of this packaging **does not transfer** copyright in those texts to users. Rights remain with the original authors / rights holders / upstream sources. Users must comply with local copyright law and any upstream source terms (including when following `url`).
2. **Annotation layer** — Theme labels (consensus and per-model columns), taxonomy definitions, Dataset Card, and supporting scripts are provided by PoetryMTEB for **non-commercial research and evaluation** with attribution to `PoetryMTEB/MultilingualPoetryThemeClassification`.
3. **No CC grant over protected texts** — Because of (1), the full dataset is **not** released under CC BY / CC BY-NC-SA or similar. Do not treat poem bodies as freely reusable open content.
4. **Takedown** — Rights holders may request removal of specific poems via the Hub repo discussion / contact channels used by PoetryMTEB.

See `LICENSE` for the same terms.

Hub packaging: `PoetryMTEB/MultilingualPoetryThemeClassification` (version 1.3.0)
