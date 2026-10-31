---
dataset_info:
- config_name: bengali
  features:
  - name: text
    dtype: string
  - name: english
    dtype: string
  splits:
  - name: harmful
    num_bytes: 108126
    num_examples: 416
  - name: harmless
    num_bytes: 87911
    num_examples: 416
  download_size: 74553
  dataset_size: 196037
- config_name: english
  features:
  - name: text
    dtype: string
  - name: english
    dtype: string
  splits:
  - name: harmful
    num_bytes: 64214
    num_examples: 416
  - name: harmless
    num_bytes: 47790
    num_examples: 416
  download_size: 57084
  dataset_size: 112004
- config_name: french
  features:
  - name: text
    dtype: string
  - name: english
    dtype: string
  splits:
  - name: harmful
    num_bytes: 74129
    num_examples: 416
  - name: harmless
    num_bytes: 53614
    num_examples: 416
  download_size: 62134
  dataset_size: 127743
- config_name: hindi
  features:
  - name: text
    dtype: string
  - name: english
    dtype: string
  splits:
  - name: harmful
    num_bytes: 113654
    num_examples: 416
  - name: harmless
    num_bytes: 83586
    num_examples: 416
  download_size: 76095
  dataset_size: 197240
- config_name: italian
  features:
  - name: text
    dtype: string
  - name: english
    dtype: string
  splits:
  - name: harmful
    num_bytes: 68512
    num_examples: 416
  - name: harmless
    num_bytes: 51009
    num_examples: 416
  download_size: 60546
  dataset_size: 119521
- config_name: korean
  features:
  - name: text
    dtype: string
  - name: english
    dtype: string
  splits:
  - name: harmful
    num_bytes: 68225
    num_examples: 416
  - name: harmless
    num_bytes: 52909
    num_examples: 416
  download_size: 57918
  dataset_size: 121134
- config_name: marathi
  features:
  - name: text
    dtype: string
  - name: english
    dtype: string
  splits:
  - name: harmful
    num_bytes: 116257
    num_examples: 416
  - name: harmless
    num_bytes: 83588
    num_examples: 416
  download_size: 76969
  dataset_size: 199845
- config_name: russian
  features:
  - name: text
    dtype: string
  - name: english
    dtype: string
  splits:
  - name: harmful
    num_bytes: 94132
    num_examples: 416
  - name: harmless
    num_bytes: 68334
    num_examples: 416
  download_size: 74660
  dataset_size: 162466
- config_name: tamil
  features:
  - name: text
    dtype: string
  - name: english
    dtype: string
  splits:
  - name: harmful
    num_bytes: 139475
    num_examples: 416
  - name: harmless
    num_bytes: 99916
    num_examples: 416
  download_size: 84979
  dataset_size: 239391
configs:
- config_name: bengali
  data_files:
  - split: harmful
    path: data/bengali/harmful-*
  - split: harmless
    path: data/bengali/harmless-*
- config_name: english
  data_files:
  - split: harmful
    path: data/english/harmful-*
  - split: harmless
    path: data/english/harmless-*
- config_name: french
  data_files:
  - split: harmful
    path: data/french/harmful-*
  - split: harmless
    path: data/french/harmless-*
- config_name: hindi
  data_files:
  - split: harmful
    path: data/hindi/harmful-*
  - split: harmless
    path: data/hindi/harmless-*
- config_name: italian
  data_files:
  - split: harmful
    path: data/italian/harmful-*
  - split: harmless
    path: data/italian/harmless-*
- config_name: korean
  data_files:
  - split: harmful
    path: data/korean/harmful-*
  - split: harmless
    path: data/korean/harmless-*
- config_name: marathi
  data_files:
  - split: harmful
    path: data/marathi/harmful-*
  - split: harmless
    path: data/marathi/harmless-*
- config_name: russian
  data_files:
  - split: harmful
    path: data/russian/harmful-*
  - split: harmless
    path: data/russian/harmless-*
- config_name: tamil
  data_files:
  - split: harmful
    path: data/tamil/harmful-*
  - split: harmless
    path: data/tamil/harmless-*
license: cc-by-sa-4.0
language:
- bn
- en
- hi
- mr
- fr
- it
- ru
- ta
- ko
tags:
- heretic
- multilingual
- harmless
- harmful
- prompts
- abliteration
---

# Multilingual Harmless and Harmful Prompts

## What is this?

This dataset contains the **Translations** of the [(1) `heretic-org/Semantic-Harmless`](https://huggingface.co/datasets/heretic-org/Semantic-Harmless) dataset and the [(2) `heretic-org/Semantic-Harmful`](https://huggingface.co/datasets/heretic-org/Semantic-Harmful) dataset into **9** languages *(including original English data)*.

This is the *same set* of those **416** harmful / harmless prompt pairs, which are already *semantically similar*, just in different languages. The original dataset is **English only**, so I *translated* it, in the hope that people can use this dataset for any research related to *["Abliteration in a multilingual model. GitHub #65"](https://github.com/p-e-w/heretic/issues/65)* or *"How refusal behavior differs across different languages"* or any similar topics.

> [!NOTE]
> I speak Hindi, Marathi, and somewhat Italian, so I actually checked the translations for a few of them. But I'm not going to pretend that I'm an expert linguist who can guarantee everything is "perfect". **So far, it Looks good to me**. The rest of the languages like Bengali, French, Russian, Tamil... I don't really understand any of them, so I can't say how good those translations are.
> 
> If you find any wrong translations, PRs to fix them are much welcome.

---

## Usage with Heretic

Each language in this dataset has its own `config/subset`, where each of these configs have two splits: *harmless* and *harmful*.

### 1. Example using CLI

```bash
heretic --model Qwen/Qwen3-VL-8B-Instruct \
--good-prompts.dataset "heretic-org/Multilingual-Harmless-Harmful" \
--good-prompts.config "hindi" \
--good-prompts.split "harmless[:400]" \
--good-prompts.column "text" \
--bad-prompts.dataset "heretic-org/Multilingual-Harmless-Harmful" \
--bad-prompts.config "hindi" \
--bad-prompts.split "harmful[:400]" \
--bad-prompts.column "text"
```

To support specifying a dataset's specific `config/subset`, it was implemented in [feat: Support specifying a dataset's specific config/subset #445](https://github.com/p-e-w/heretic/pull/445) for [p-e-w/heretic](https://github.com/p-e-w/heretic).

### 2. Example using `config.toml`

For heretic `>=v2.0.0` *(plugin-based)*

```toml
# Using first 5 prompts for abliteration.
[good_prompts]
dataset = "heretic-org/Multilingual-Harmless-Harmful"
config = "hindi"
split = "harmless[:5]"
column = "text"

[bad_prompts]
dataset = "heretic-org/Multilingual-Harmless-Harmful"
config = "hindi"
split = "harmful[:5]"
column = "text"

# Using first 6-10 prompts for evaluation.
[scorer.KLDivergence.prompts]
dataset = "heretic-org/Multilingual-Harmless-Harmful"
config = "hindi"
split = "harmless[5:10]"
column = "text"

[scorer.KeywordRate.prompts]
dataset = "heretic-org/Multilingual-Harmless-Harmful"
config = "hindi"
split = "harmful[5:10]"
column = "text"
```

<details>
  <summary>For heretic `v1.4.0` and before</summary>

```toml
# Using first 5 prompts for abliteration.
[good_prompts]
dataset = "heretic-org/Multilingual-Harmless-Harmful"
config = "hindi"
split = "harmless[:5]"
column = "text"

[bad_prompts]
dataset = "heretic-org/Multilingual-Harmless-Harmful"
config = "hindi"
split = "harmful[:5]"
column = "text"

# Using first 6-10 prompts for evaluation.
[good_evaluation_prompts]
dataset = "heretic-org/Multilingual-Harmless-Harmful"
config = "hindi"
split = "harmless[5:10]"
column = "text"

[bad_evaluation_prompts]
dataset = "heretic-org/Multilingual-Harmless-Harmful"
config = "hindi"
split = "harmful[5:10]"
column = "text"
```

</details>

> [!TIP]
> You can use the `keyword_markers` from the translated multilingual [`config.multilingual.toml`](https://huggingface.co/datasets/heretic-org/Multilingual-Harmless-Harmful/blob/main/config.multilingual.toml) file.

---

## Languages

| No. | Language | Code |
|---|------------|------|
| 1 | English (original)    | `en` |
| 2 | Bengali    | `bn` |
| 3 | French     | `fr` |
| 4 | Hindi      | `hi` |
| 5 | Italian    | `it` |
| 6 | Korean     | `ko` |
| 7 | Marathi    | `mr` |
| 8 | Russian    | `ru` |
| 9 | Tamil      | `ta` |

## Extra

For convenience, this dataset is also available in **PLAINTEXT (`.txt`)**, **CSV (`.csv`)**, and **JSON (`.json`)** formats inside the [`content/`](content/) folder.

**1. Structure:**

```
content/
└── hindi/
    ├── text/
    │   ├── hindi_harmful.txt
    │   └── hindi_harmless.txt
    ├── json/
    │   └── hindi.json
    └── csv/
        └── hindi.csv
```

**2. Format:**

One line = One prompt in each of the `.txt` files. Columns: `text` (the translation), `english` (the original). Each language has two splits: `harmful` and `harmless`.

---

## Sources

All translations are based on the [heretic-org/Semantic-Harmless](https://huggingface.co/datasets/heretic-org/Semantic-Harmless) and [heretic-org/Semantic-Harmful](https://huggingface.co/datasets/heretic-org/Semantic-Harmful) datasets. For more details, see the `README.md` file of one of these datasets.

## Contributing

**You know a language that's not here?**

I'd love to add it. You can open a [Pull Request](https://huggingface.co/docs/hub/main/en/repositories-pull-requests-discussions#pull-requests-and-discussions) for contributing more languages. See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the details.

## License

Copyright &copy; 2026 Vinay Umrethe <umrethevinay@gmail.com>.

This dataset is available under the **Creative Commons Attribution Share Alike 4.0 International** License.