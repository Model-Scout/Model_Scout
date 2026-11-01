---
license: cc-by-nc-4.0
task_categories:
  - text-classification
language:
  - en
  - id
  - ja
  - ko
  - es
  - fr
  - de
  - zh
  - pt
  - ru
  - it
tags:
  - music
  - lyrics
  - emotion
  - go-emotions
  - mbti
  - personality
  - multilingual
  - math-rock
  - midwest-emo
  - synthetic
size_categories:
  - 100K<n<1M
pretty_name: Multilingual Math Rock Lyrics for Emotion and MBTI Classification
configs:
  - config_name: default
    data_files:
      - split: train
        path: train-00000-of-00001.parquet
---

# Multilingual Math Rock Lyrics for Emotion and MBTI Classification

## Dataset Summary

This dataset contains **120,060** song-lyric passages annotated with two independent
classification targets: a fine-grained **emotion** label (28 categories based on the
GoEmotions taxonomy) and a **Myers-Briggs Type Indicator (MBTI)** personality type
(16 categories). All passages are written in the stylistic register of the
**math rock** and **midwest emo** genres and span eleven languages.

The corpus was built to train two multilingual text classifiers,
[`anggars/xlm-emotion`](https://huggingface.co/anggars/xlm-emotion) and
[`anggars/xlm-mbti`](https://huggingface.co/anggars/xlm-mbti), which form the textual
branch of a broader multimodal emotion-and-personality analysis system.

> **Composition notice.** The overwhelming majority of the passages are **synthetic**,
> generated with the **Gemma** large language model, while a small set of authentic
> lyrics was retrieved from public sources. See [Data Sources](#data-sources) for exact
> counts. The dataset is intended for research and educational use only.

## Supported Tasks

- **Emotion classification** (`text-classification`): predict one of 28 emotion
  categories from a lyric passage.
- **MBTI personality classification** (`text-classification`): predict one of 16 MBTI
  personality types from a lyric passage.

The two targets are provided as separate columns and are meant to be trained as two
independent single-label classifiers.

## Languages

The `Text` field is multilingual. The approximate distribution is:

| Language | Code | Rows | Share |
| --- | --- | ---: | ---: |
| English | en | 41,759 | 34.79% |
| Indonesian | id | 25,176 | 20.98% |
| Japanese | ja | 13,647 | 11.37% |
| Korean | ko | 9,974 | 8.31% |
| Spanish | es | 8,514 | 7.09% |
| French | fr | 7,019 | 5.85% |
| German | de | 4,112 | 3.43% |
| Chinese | zh | 4,080 | 3.40% |
| Portuguese | pt | 2,890 | 2.41% |
| Russian | ru | 2,843 | 2.37% |
| Italian | it | 1 | <0.01% |
| **Total** | | **120,060** | **100%** |

## Dataset Structure

### Data Fields

| Field | Type | Description |
| --- | --- | --- |
| `Text` | string | The lyric passage. |
| `Emotion` | string | One of 28 GoEmotions categories (see below). |
| `MBTI` | string | One of 16 MBTI personality types (see below). |
| `Language` | string | ISO 639-1 language code of `Text`. |
| `source` | string | Provenance of the row: `gemma` (synthetic) or `genius` (organic). |
| `Title` | string | Song title (populated for authentic rows; tagged as `[Synthetic Data]` for generated rows). |
| `Artist` | string | Performing artist (populated for authentic rows; tagged as `[Synthetic Gemma]` for generated rows). |

### Data Splits

The dataset ships as a single `train` split. Users are expected to create their own
validation and test partitions (for example, a stratified 80/20 split with a fixed seed).

| Split | Rows |
| --- | ---: |
| train | 120,060 |

## Class Labels

### Emotion (28 categories, GoEmotions taxonomy)

`admiration`, `amusement`, `anger`, `annoyance`, `approval`, `caring`, `confusion`,
`curiosity`, `desire`, `disappointment`, `disapproval`, `disgust`, `embarrassment`,
`excitement`, `fear`, `gratitude`, `grief`, `joy`, `love`, `nervousness`, `optimism`,
`pride`, `realization`, `relief`, `remorse`, `sadness`, `surprise`, `neutral`

The emotion labels are approximately balanced, with roughly **4,287 to 4,288** rows per
category.

### MBTI (16 personality types)

`INTJ`, `INTP`, `ENTJ`, `ENTP`, `INFJ`, `INFP`, `ENFJ`, `ENFP`,
`ISTJ`, `ISFJ`, `ESTJ`, `ESFJ`, `ISTP`, `ISFP`, `ESTP`, `ESFP`

The MBTI labels are approximately balanced, with roughly **7,503 to 7,504** rows per type.

## Data Sources

| Source | Rows | Share | Description |
| --- | ---: | ---: | --- |
| `gemma` | 119,967 | 99.92% | Passages generated with the Gemma large language model. |
| `genius` | 93 | 0.08% | Authentic lyrics retrieved from public sources. |
| **Total** | **120,060** | **100%** | |

## Data Collection and Processing

1. **Authentic lyric retrieval.** A limited pool of genuine math rock and midwest emo
   lyrics was collected from public lyric providers, then cleaned and language-tagged.
2. **Synthetic generation.** To reach a balanced, large-scale corpus, the remaining
   passages were generated with the Gemma large language model, conditioned on a target
   emotion category, a target MBTI type, a target language, and the math rock / midwest
   emo stylistic register.
3. **Data Cleaning & Re-ordering.** Unused features (e.g., `Style`) were dropped. Metadata was normalized, ensuring synthetic data titles and artists are explicitly labeled as `[Synthetic Data]` and `[Synthetic Gemma]`. Finally, the dataset was reordered using a custom hierarchy to prioritize authentic lyrics from key math rock / midwest emo bands at the top of the dataset, while synthetic data was pushed to the bottom.

## Intended Uses

This dataset is designed for:

- Fine-tuning multilingual transformer classifiers for lyric-level emotion recognition.
- Fine-tuning multilingual transformer classifiers for exploratory MBTI inference from text.
- Research on affective and stylistic modeling of the math rock and midwest emo genres.

## Limitations and Biases

- **Predominantly synthetic.** About 99.9% of the passages are machine-generated rather
  than authored by human songwriters. Models trained on this corpus may learn artifacts
  of the generating model instead of genuine lyric phenomena.
- **Weak MBTI supervision.** MBTI is a self-report typology with limited scientific
  validity, and the labels here are assigned as exploratory proxies rather than
  clinically validated annotations. Results should be interpreted cautiously.
- **Genre and length skew.** Passages are constrained to a narrow stylistic register and
  may not generalize to other genres or to full-length songs.
- **Uneven language coverage.** English and Indonesian dominate the corpus, and some
  languages (for example, Italian) are represented by only a handful of rows.
- **Copyright.** Authentic passages remain the property of their respective rights
  holders and are included in limited quantity for research purposes only.

## Citation

If you use this dataset, please cite the associated undergraduate thesis project on
multimodal emotion and MBTI analysis of math rock music.

## License

Released under **CC BY-NC 4.0** for non-commercial research and educational use.