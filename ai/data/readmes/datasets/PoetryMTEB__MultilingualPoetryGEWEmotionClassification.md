---
license: cc-by-nc-sa-4.0
task_categories:
- text-classification
task_ids:
- multi-label-classification
language:
- ar
- bg
- bn
- cs
- de
- en
- es
- fa
- fr
- hi
- hu
- it
- ja
- ko
- no
- pa
- pt
- ru
- sl
- te
- tr
- ur
- vi
- zh
multilinguality:
- multilingual
size_categories:
- 10K<n<100K
pretty_name: Multilingual Poetry GEW Emotion Classification
tags:
- poetry
- emotion-classification
- geneva-emotion-wheel
- gew
- multi-label-classification
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
  - name: labels
    sequence: int64
  - name: label_names
    sequence: string
  - name: label_names_zh
    sequence: string
  - name: centralities
    sequence: float64
  - name: intensities
    sequence: float64
  - name: valences
    sequence: float64
  - name: controls
    sequence: float64
  - name: label
    dtype: int64
  - name: label_name
    dtype: string
  - name: label_source
    dtype: string
  splits:
  - name: train
    num_examples: 22801
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
  - name: labels
    sequence: int64
  - name: label_names
    sequence: string
  - name: label_names_zh
    sequence: string
  - name: centralities
    sequence: float64
  - name: intensities
    sequence: float64
  - name: valences
    sequence: float64
  - name: controls
    sequence: float64
  - name: label
    dtype: int64
  - name: label_name
    dtype: string
  - name: label_source
    dtype: string
  splits:
  - name: test
    num_examples: 1440
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
  - name: labels
    sequence: int64
  - name: label_names
    sequence: string
  - name: label_names_zh
    sequence: string
  - name: centralities
    sequence: float64
  - name: intensities
    sequence: float64
  - name: valences
    sequence: float64
  - name: controls
    sequence: float64
  - name: label
    dtype: int64
  - name: label_name
    dtype: string
  - name: label_source
    dtype: string
  splits:
  - name: test
    num_examples: 61
---

# Multilingual Poetry GEW Emotion Classification

**Multilingual, multi-label poetic emotion classification** for PoetryMTEB / MTEB-style embedding evaluation, using the **Geneva Emotion Wheel (GEW)** taxonomy (20 emotion families + `Other`).

**Train**, **silver**, and **gold** are packaged as **three parallel peer collections** (separate Hub configs). Poem IDs are pairwise disjoint across the three collections.

## Dataset Card

| Item | Description |
|------|-------------|
| **Dataset version (PoetryMTEB)** | `1.1.6` |
| **Hub repo** | [`PoetryMTEB/MultilingualPoetryGEWEmotionClassification`](https://huggingface.co/datasets/PoetryMTEB/MultilingualPoetryGEWEmotionClassification) |
| **Taxonomy** | Geneva Emotion Wheel (GEW): **21** classes (ids 0–20) |
| **Task** | **Multi-label** emotion classification (+ primary `label` / `label_name`) |
| **Unit** | Full poem text (`poem`) |
| **Languages** | **24** (see language table) |
| **Collections (configs)** | `train` · `silver` · `gold` (peer sets; not nested train/test of one config) |
| **Size** | train=22801; silver=1440; gold=61; **total=24302** |
| **Anti-leakage** | train ∩ silver ∩ gold **poem_id** = ∅ (pairwise) |
| **License** | [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) |
| **Evaluation metrics** | Multi-label micro/macro F1; primary accuracy / F1 (`scripts/evaluate_gew_emotion.py`) |

## Collections (configs)

| Config | Hub split | n | Label quality |
|--------|-----------|--:|---------------|
| **`train`** (default) | `train` | 22801 | Single-model `gemini-3-flash-preview` |
| **`silver`** | `test` | 1440 | 3 LLMs, ≥2/3 consensus |
| **`gold`** | `test` | 61 | 5 humans ≥3/5; 2 expert-adjudicated |

```python
from datasets import load_dataset

train = load_dataset("PoetryMTEB/MultilingualPoetryGEWEmotionClassification", "train")["train"]
silver = load_dataset("PoetryMTEB/MultilingualPoetryGEWEmotionClassification", "silver")["test"]
gold = load_dataset("PoetryMTEB/MultilingualPoetryGEWEmotionClassification", "gold")["test"]
```

## Label taxonomy (GEW, 21)

Primary-label counts (argmax `centrality` after packaging normalization):

| id | label_name | name_en | name_zh | train | silver | gold |
|---:|------------|---------|---------|------:|-------:|-----:|
| 0 | `Anger` | Anger | 愤怒 | 1384 | 74 | 1 |
| 1 | `Interest` | Interest | 兴趣 | 617 | 62 | 2 |
| 2 | `Amusement` | Amusement | 嬉乐 | 924 | 113 | 6 |
| 3 | `Pride` | Pride | 自豪 | 1335 | 65 | 2 |
| 4 | `Joy` | Joy | 喜悦 | 1905 | 69 | 2 |
| 5 | `Pleasure` | Pleasure | 愉悦 | 51 | 22 | 1 |
| 6 | `Contentment` | Contentment | 满足 | 665 | 92 | 2 |
| 7 | `Love` | Love | 爱恋 | 4848 | 147 | 6 |
| 8 | `Admiration` | Admiration | 钦佩 | 2552 | 93 | 10 |
| 9 | `Relief` | Relief | 宽慰 | 38 | 30 | 2 |
| 10 | `Compassion` | Compassion | 同情 | 160 | 44 | 3 |
| 11 | `Sadness` | Sadness | 悲伤 | 6956 | 246 | 11 |
| 12 | `Guilt` | Guilt | 内疚 | 47 | 29 | 0 |
| 13 | `Regret` | Regret | 遗憾 | 46 | 33 | 1 |
| 14 | `Shame` | Shame | 羞愧 | 7 | 27 | 0 |
| 15 | `Disappointment` | Disappointment | 失望 | 229 | 55 | 1 |
| 16 | `Fear` | Fear | 恐惧 | 613 | 73 | 2 |
| 17 | `Disgust` | Disgust | 厌恶 | 24 | 23 | 1 |
| 18 | `Contempt` | Contempt | 轻蔑 | 367 | 132 | 7 |
| 19 | `Hate` | Hate | 仇恨 | 6 | 10 | 1 |
| 20 | `Other` | Other | 其他 | 27 | 1 | 0 |

Codebook: `label_taxonomy.json`.

> **Packaging normalization:** Non-GEW family strings in the raw train pool (e.g. `Hope`, `Awe`) and case variants are mapped to the 21-class GEW set (`Other` or canonical aliases), duplicates merged by max centrality, then centrality re-normalized to sum to 1.

## Features

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Stable id (`mpgew-{collection}-{poem_id}`) |
| `poem_id` | string | Corpus poem id (language = 2nd `-` field) |
| `poem` | string | **Classification input**: full poem text |
| `title` | string | Title (may be empty) |
| `author` | string | Author (may be empty) |
| `language` | string | Language code (e.g. `ARA`, `PAN`, `SLV`) |
| `language_name` | string | English language name |
| `labels` | sequence[int64] | Multi-label GEW ids (centrality desc) |
| `label_names` | sequence[string] | Multi-label GEW names |
| `label_names_zh` | sequence[string] | Chinese glosses |
| `centralities` | sequence[float64] | Consensus / normalized centrality (sums to 1) |
| `intensities` | sequence[float64] | Consensus intensity (≈1–5) |
| `valences` | sequence[float64] | Mean valence (≈−1…1) |
| `controls` | sequence[float64] | Mean control (≈−1…1) |
| `label` | int64 | Primary class id (highest centrality) |
| `label_name` | string | Primary class name |
| `label_source` | string | Provenance tag |

### `label_source` values

| Value | Collection | Meaning |
|-------|------------|---------|
| `gemini-3-flash-preview` | train | Single-model train labels |
| `llm3_majority_2` | silver | 3-model ≥2/3 consensus |
| `llm3_majority_2_fallback_primary` | silver | Empty consensus set R → primary-emotion fallback |
| `human_5H` | gold | 5 humans, ≥3/5 consensus |
| `expert_adjudication` | gold | Expert-adjudicated gold (2 poems) |

## Language coverage

| code | language | ISO | train | silver | gold |
|------|----------|-----|------:|-------:|-----:|
| `ARA` | Arabic | `ar` | 888 | 60 | 3 |
| `BEN` | Bengali | `bn` | 255 | 60 | 1 |
| `BUL` | Bulgarian | `bg` | 819 | 60 | 1 |
| `CES` | Czech | `cs` | 1804 | 60 | 7 |
| `DEU` | German | `de` | 1667 | 60 | 11 |
| `ENG` | English | `en` | 1509 | 60 | 3 |
| `FAS` | Persian | `fa` | 1592 | 60 | 8 |
| `FRA` | French | `fr` | 1895 | 60 | 2 |
| `HIN` | Hindi | `hi` | 630 | 60 | 1 |
| `HUN` | Hungarian | `hu` | 519 | 60 | 1 |
| `ITA` | Italian | `it` | 1262 | 60 | 2 |
| `JPN` | Japanese | `ja` | 2132 | 60 | 7 |
| `KOR` | Korean | `ko` | 189 | 60 | 1 |
| `NOR` | Norwegian | `no` | 189 | 60 | 1 |
| `PAN` | Punjabi | `pa` | 1006 | 60 | 1 |
| `POR` | Portuguese | `pt` | 705 | 60 | 1 |
| `RUS` | Russian | `ru` | 1650 | 60 | 3 |
| `SLV` | Slovenian | `sl` | 1239 | 60 | 1 |
| `SPA` | Spanish | `es` | 513 | 60 | 1 |
| `TEL` | Telugu | `te` | 189 | 60 | 1 |
| `TUR` | Turkish | `tr` | 714 | 60 | 1 |
| `URD` | Urdu | `ur` | 1057 | 60 | 1 |
| `VIE` | Vietnamese | `vi` | 189 | 60 | 1 |
| `ZHO` | Chinese | `zh` | 189 | 60 | 1 |

Silver uses **language × emotion quota sampling** (60 poems per language) so low-resource languages remain visible in evaluation.

## Consensus aggregation (gold & silver)

Gold and silver share the same aggregation; only the number of annotators **N** and majority threshold **K** differ.

| Collection | Annotators N | Threshold K |
|------------|-------------:|------------:|
| Gold (human) | 5 | 3 (≥3/5) |
| Silver (LLM) | 3 | 2 (≥2/3) |

Silver models: `gemini-3-flash-preview`, `deepseek-v4-pro`, `qwen3.7-plus`.

Let annotator/model *h* select emotion families with raw centrality *c*<sub>*h,e*</sub> and intensity *i*<sub>*h,e*</sub>. The indicator *y*<sub>*h,e*</sub> = 1 if emotion *e* was selected by *h*. Non-GEW names map to `Other`.

### 1. Per-annotator centrality normalization

$$
z_{h,e} =
\begin{cases}
\dfrac{c_{h,e}}{\sum_{j} y_{h,j}\, c_{h,j}} & \text{if } y_{h,e}=1 \\
0 & \text{otherwise}
\end{cases}
$$

### 2. Mean centrality across annotators

$$
\bar{c}_{e} = \frac{1}{N} \sum_{h=1}^{N} z_{h,e}
$$

### 3. Consensus emotion set R

$$
R = \left\{ e \mid \sum_{h=1}^{N} y_{h,e} \ge K \right\}
$$

### 4. Final consensus **centrality** (re-normalize inside R)

$$
c_{e}^{\mathrm{final}} = \frac{\bar{c}_{e}}{\sum_{j \in R} \bar{c}_{j}},\quad e \in R
$$

Only emotions in **R** are kept in the released `label_names` / `centralities`.

### 5. Consensus **intensity** (and valence / control)

For each emotion *e* in **R**, average the attribute **only over annotators who selected** *e*:

$$
i_{e}^{\mathrm{final}} = \frac{\sum_{h: y_{h,e}=1} i_{h,e}}{\sum_{h=1}^{N} y_{h,e}}
$$

Valence *v*<sub>*e*</sub><sup>final</sup> and control *p*<sub>*e*</sub><sup>final</sup> use the same **support-conditional mean** (annotators with *y*<sub>*h,e*</sub> = 1 only). Intensity is **not** re-normalized across emotions; centrality alone carries the blend weights.

### 6. Primary label

$$
e^{\star} = \arg\max_{e \in R} c_{e}^{\mathrm{final}}
$$

Mapped to fields `label` / `label_name`.

### Train collection

Train labels are **single-model** (`gemini-3-flash-preview`) and **do not** apply the multi-annotator consensus above. Packaging still maps families to the 21-class GEW set and re-normalizes centrality per poem.

## Construction overview

```text
compliance multilingual poems
        │
        ├─► 5 humans (61) ─► ≥3/5 (+ 2 expert adjudication) ─► gold
        │
        ├─► gemini bulk labels ─► exclude gold+silver IDs ─► train
        │
        └─► quota sample (1440) ─► 3 LLMs ─► ≥2/3 ─► silver
```

## Supporting materials

| Path | Content |
|------|---------|
| `VERSION` / `LICENSE` / `CITATION.*` / `metadata.json` | Packaging metadata |
| `label_taxonomy.json` | GEW codebook + counts |
| `dataset_infos.yaml` | Hub viewer configs |
| `splits/*_ids.*` | poem_id lists |
| `checksums.sha256` | File hashes |
| `prompts/annotation_prompt_template.md` | Annotation prompt |
| `scripts/evaluate_gew_emotion.py` | Baseline probe (train → silver/gold) |

## How to load

```python
from datasets import load_dataset

train = load_dataset("PoetryMTEB/MultilingualPoetryGEWEmotionClassification", "train", split="train")
silver = load_dataset("PoetryMTEB/MultilingualPoetryGEWEmotionClassification", "silver", split="test")
gold = load_dataset("PoetryMTEB/MultilingualPoetryGEWEmotionClassification", "gold", split="test")

print(len(train), len(silver), len(gold))
print(silver[0]["language"], silver[0]["label_names"], silver[0]["centralities"])
```

## Intended use

- PoetryMTEB multi-label / primary-label emotion probing under a shared GEW taxonomy.
- Cross-lingual analysis of poetic affective blends.
- **Not** for clinical affect diagnosis.

## Limitations

- Train = single LLM; silver = multi-LLM consensus; gold = primarily human.
- Silver is language-balanced (60/lang); train is not.

## Citation

```bibtex
@misc{multilingualpoetrygewemotionclassification,
  title     = {Multilingual Poetry GEW Emotion Classification},
  author    = {PoetryMTEB Contributors},
  year      = {2026},
  version   = {1.1.6},
  url       = {https://huggingface.co/datasets/PoetryMTEB/MultilingualPoetryGEWEmotionClassification},
  note      = {PoetryMTEB packaging; Geneva Emotion Wheel (GEW) taxonomy}
}
```

## License

Distributed under **[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)** (Creative Commons Attribution–NonCommercial–ShareAlike 4.0 International). See `LICENSE`. Non-commercial research and embedding-evaluation use with attribution and share-alike; commercial use is not permitted under this license. Poem texts additionally inherit constraints of the upstream compliance corpus.

Hub packaging: `PoetryMTEB/MultilingualPoetryGEWEmotionClassification` (version 1.1.6)
