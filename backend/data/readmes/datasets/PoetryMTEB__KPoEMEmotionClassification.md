---
license: cc-by-4.0
task_categories:
- text-classification
task_ids:
- multi-label-classification
language:
- ko
multilinguality:
- monolingual
size_categories:
- 1K<n<10K
pretty_name: KPoEMEmotionClassification
tags:
- poetry
- korean
- emotion-classification
- multi-label-classification
- kote
- modern-poetry
- mteb
- poetrymteb
- embedding-evaluation
annotations_creators:
- expert-generated
source_datasets:
- AKS-DHLAB/KPoEM
configs:
- config_name: line
  data_files:
  - split: train
    path: line/train-*
  - split: validation
    path: line/validation-*
  - split: test
    path: line/test-*
  default: true
- config_name: poem
  data_files:
  - split: train
    path: poem/train-*
  - split: validation
    path: poem/validation-*
  - split: test
    path: poem/test-*
dataset_info:
- config_name: line
  features:
  - name: id
    dtype: string
  - name: poem_id
    dtype: string
  - name: line_id
    dtype: string
  - name: title
    dtype: string
  - name: poet
    dtype: string
  - name: poem
    dtype: string
  - name: labels
    sequence: int64
  - name: label_names
    sequence: string
  - name: label_names_en
    sequence: string
  - name: label_names_zh
    sequence: string
  splits:
  - name: train
    num_examples: 5638
  - name: validation
    num_examples: 575
  - name: test
    num_examples: 794
- config_name: poem
  features:
  - name: id
    dtype: string
  - name: poem_id
    dtype: string
  - name: seg_id
    dtype: string
  - name: title
    dtype: string
  - name: sub_title
    dtype: string
  - name: poetry_book
    dtype: string
  - name: poet
    dtype: string
  - name: poem
    dtype: string
  - name: labels
    sequence: int64
  - name: label_names
    sequence: string
  - name: label_names_en
    sequence: string
  - name: label_names_zh
    sequence: string
  splits:
  - name: train
    num_examples: 489
  - name: validation
    num_examples: 59
  - name: test
    num_examples: 67
---

# KPoEMEmotionClassification

Multi-label **Korean modern poetry emotion classification** for PoetryMTEB, derived from [KPoEM](https://zenodo.org/records/15598092) (KOTE 44 emotions; 5 expert annotators).

Two configs mirror the upstream dual annotation layers:

| Config | Unit | Description |
|--------|------|-------------|
| `line` (default) | Verse line | Local emotion cues (lines partially shuffled upstream) |
| `poem` | Work / segment | Full-context emotion labels |

## Dataset Card

| Item | Description |
|------|-------------|
| **Source** | [Zenodo 15598092](https://zenodo.org/records/15598092); [AKS-DHLAB/KPoEM](https://huggingface.co/datasets/AKS-DHLAB/KPoEM); code [AKS-DHLAB/KPoEM](https://github.com/AKS-DHLAB/KPoEM) |
| **Paper** | LIM, Kim & Ji, *The Review of Korean Studies* 29(1); also [arXiv:2509.03932](https://arxiv.org/abs/2509.03932) |
| **Languages** | Korean (`ko`) |
| **Poets** | 김소월, 윤동주, 임화, 이상, 한용운 |
| **Labels** | Multi-label subset of **44** KOTE emotions |
| **Aggregation** | Majority vote **≥3/5** annotators; if empty, keep top-vote emotion(s) |
| **Splits** | Shared **poem_id** split stratified by poet ≈ 80% / 10% / 10%, seed=42 (no poem crosses splits) |
| **line size** | train=5638; validation=575; test=794 |
| **poem size** | train=489; validation=59; test=67 |
| **License** | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) (Zenodo) |
| **Evaluation metrics** | Multi-label classification on embeddings: **macro/micro F1**, **Average Precision (AP)** |

## Features

### `line`

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Example id |
| `poem_id` | string | Poem id (split key) |
| `line_id` | string | Upstream line id |
| `title` | string | Poem title |
| `poet` | string | Poet |
| `poem` | string | **Line** text (classification input) |
| `labels` | list[int64] | Emotion indices |
| `label_names` | list[string] | Emotion names (Korean / KOTE) |
| `label_names_en` | list[string] | Emotion names (English; KOTE taxonomy) |
| `label_names_zh` | list[string] | Emotion names (Chinese gloss) |

### `poem`

Same as above, plus `seg_id`, `sub_title`, `poetry_book`; `poem` holds the work/segment text.

English glosses follow the [KOTE](https://arxiv.org/abs/2205.05300) / LREC 2024 label descriptions; Chinese glosses are provided for PoetryMTEB documentation.

## Label taxonomy (44)

### line counts

| id | label_name (ko) | label_name_en | label_name_zh | train | validation | test | total |
|---:|-----------------|---------------|---------------|------:|-----------:|-----:|------:|
| 0 | `불안/걱정` | anxiety/worry | 焦虑/担心 | 1192 | 129 | 161 | 1482 |
| 1 | `슬픔` | sadness | 悲伤 | 876 | 83 | 145 | 1104 |
| 2 | `기대감` | anticipation | 期待 | 1131 | 109 | 115 | 1355 |
| 3 | `안타까움/실망` | pitifulness/disappointment | 惋惜/失望 | 930 | 74 | 122 | 1126 |
| 4 | `서러움` | sorrow | 哀伤 | 598 | 54 | 93 | 745 |
| 5 | `신기함/관심` | curiosity/interest | 新奇/兴趣 | 954 | 106 | 121 | 1181 |
| 6 | `비장함` | resolute | 悲壮/决绝 | 790 | 68 | 100 | 958 |
| 7 | `아껴주는` | caring | 疼爱/珍惜 | 792 | 49 | 146 | 987 |
| 8 | `감동/감탄` | impressed/admiration | 感动/赞叹 | 559 | 60 | 62 | 681 |
| 9 | `당황/난처` | embarrassment/awkwardness | 慌乱/尴尬 | 481 | 48 | 72 | 601 |
| 10 | `깨달음` | realization | 顿悟/领悟 | 379 | 56 | 72 | 507 |
| 11 | `힘듦/지침` | fatigue/exhaustion | 疲惫/精疲力尽 | 356 | 27 | 51 | 434 |
| 12 | `불쌍함/연민` | pity/compassion | 可怜/怜悯 | 442 | 43 | 73 | 558 |
| 13 | `부담/안_내킴` | burden/unwillingness | 负担/不情愿 | 312 | 28 | 43 | 383 |
| 14 | `기쁨` | joy | 喜悦 | 438 | 53 | 52 | 543 |
| 15 | `놀람` | surprise | 惊讶 | 322 | 29 | 59 | 410 |
| 16 | `흐뭇함(귀여움/예쁨)` | pleased(cute/pretty) | 欣慰(可爱/漂亮) | 326 | 40 | 45 | 411 |
| 17 | `환영/호의` | welcome/favor | 欢迎/好感 | 154 | 19 | 16 | 189 |
| 18 | `불평/불만` | complaint/dissatisfaction | 抱怨/不满 | 189 | 25 | 34 | 248 |
| 19 | `절망` | despair | 绝望 | 152 | 16 | 22 | 190 |
| 20 | `의심/불신` | doubt/distrust | 怀疑/不信任 | 214 | 31 | 32 | 277 |
| 21 | `없음` | NO EMOTION | 无情感 | 343 | 30 | 49 | 422 |
| 22 | `행복` | happiness | 幸福 | 140 | 18 | 26 | 184 |
| 23 | `공포/무서움` | fear/scary | 恐惧/害怕 | 213 | 24 | 25 | 262 |
| 24 | `패배/자기혐오` | defeat/self-hatred | 挫败/自我厌弃 | 121 | 15 | 19 | 155 |
| 25 | `편안/쾌적` | comfort/cozy | 舒适/惬意 | 163 | 22 | 25 | 210 |
| 26 | `존경` | respect | 尊敬 | 124 | 19 | 24 | 167 |
| 27 | `안심/신뢰` | relief/trust | 安心/信任 | 66 | 6 | 16 | 88 |
| 28 | `즐거움/신남` | pleasure/excitement | 快乐/兴奋 | 115 | 12 | 13 | 140 |
| 29 | `지긋지긋` | fed up | 厌烦/受够了 | 62 | 7 | 17 | 86 |
| 30 | `경악` | shock | 惊骇 | 88 | 6 | 16 | 110 |
| 31 | `뿌듯함` | pride | 自豪/充实感 | 84 | 8 | 14 | 106 |
| 32 | `한심함` | pathetic | 可怜又可悲 | 87 | 10 | 14 | 111 |
| 33 | `고마움` | gratitude | 感激 | 66 | 7 | 20 | 93 |
| 34 | `화남/분노` | anger/rage | 生气/愤怒 | 77 | 6 | 9 | 92 |
| 35 | `증오/혐오` | loathing/hatred | 憎恶/仇恨 | 81 | 12 | 16 | 109 |
| 36 | `짜증` | irritation | 烦躁 | 48 | 5 | 9 | 62 |
| 37 | `부끄러움` | shame | 羞愧 | 46 | 4 | 4 | 54 |
| 38 | `죄책감` | guilt | 内疚 | 17 | 3 | 4 | 24 |
| 39 | `어이없음` | preposterous | 荒谬/无语 | 25 | 1 | 9 | 35 |
| 40 | `우쭐댐/무시함` | arrogance/disregard | 得意忘形/轻视 | 36 | 9 | 9 | 54 |
| 41 | `재미없음` | boredom | 无聊 | 19 | 2 | 7 | 28 |
| 42 | `귀찮음` | laziness | 嫌麻烦/懒得 | 9 | 1 | 4 | 14 |
| 43 | `역겨움/징그러움` | disgust/repulsiveness | 恶心/厌恶 | 27 | 1 | 6 | 34 |

### poem counts

| id | label_name (ko) | label_name_en | label_name_zh | train | validation | test | total |
|---:|-----------------|---------------|---------------|------:|-----------:|-----:|------:|
| 0 | `불안/걱정` | anxiety/worry | 焦虑/担心 | 162 | 18 | 18 | 198 |
| 1 | `슬픔` | sadness | 悲伤 | 232 | 26 | 35 | 293 |
| 2 | `기대감` | anticipation | 期待 | 96 | 12 | 10 | 118 |
| 3 | `안타까움/실망` | pitifulness/disappointment | 惋惜/失望 | 175 | 23 | 21 | 219 |
| 4 | `서러움` | sorrow | 哀伤 | 162 | 17 | 20 | 199 |
| 5 | `신기함/관심` | curiosity/interest | 新奇/兴趣 | 57 | 5 | 7 | 69 |
| 6 | `비장함` | resolute | 悲壮/决绝 | 143 | 13 | 15 | 171 |
| 7 | `아껴주는` | caring | 疼爱/珍惜 | 126 | 11 | 21 | 158 |
| 8 | `감동/감탄` | impressed/admiration | 感动/赞叹 | 72 | 9 | 5 | 86 |
| 9 | `당황/난처` | embarrassment/awkwardness | 慌乱/尴尬 | 30 | 2 | 4 | 36 |
| 10 | `깨달음` | realization | 顿悟/领悟 | 132 | 18 | 15 | 165 |
| 11 | `힘듦/지침` | fatigue/exhaustion | 疲惫/精疲力尽 | 77 | 9 | 16 | 102 |
| 12 | `불쌍함/연민` | pity/compassion | 可怜/怜悯 | 74 | 7 | 14 | 95 |
| 13 | `부담/안_내킴` | burden/unwillingness | 负担/不情愿 | 8 | 3 | 1 | 12 |
| 14 | `기쁨` | joy | 喜悦 | 26 | 2 | 2 | 30 |
| 15 | `놀람` | surprise | 惊讶 | 3 | 0 | 1 | 4 |
| 16 | `흐뭇함(귀여움/예쁨)` | pleased(cute/pretty) | 欣慰(可爱/漂亮) | 39 | 4 | 5 | 48 |
| 17 | `환영/호의` | welcome/favor | 欢迎/好感 | 14 | 1 | 1 | 16 |
| 18 | `불평/불만` | complaint/dissatisfaction | 抱怨/不满 | 20 | 6 | 2 | 28 |
| 19 | `절망` | despair | 绝望 | 61 | 5 | 8 | 74 |
| 20 | `의심/불신` | doubt/distrust | 怀疑/不信任 | 16 | 2 | 4 | 22 |
| 21 | `없음` | NO EMOTION | 无情感 | 0 | 0 | 0 | 0 |
| 22 | `행복` | happiness | 幸福 | 21 | 4 | 3 | 28 |
| 23 | `공포/무서움` | fear/scary | 恐惧/害怕 | 23 | 5 | 2 | 30 |
| 24 | `패배/자기혐오` | defeat/self-hatred | 挫败/自我厌弃 | 31 | 8 | 8 | 47 |
| 25 | `편안/쾌적` | comfort/cozy | 舒适/惬意 | 14 | 3 | 2 | 19 |
| 26 | `존경` | respect | 尊敬 | 22 | 4 | 2 | 28 |
| 27 | `안심/신뢰` | relief/trust | 安心/信任 | 9 | 0 | 1 | 10 |
| 28 | `즐거움/신남` | pleasure/excitement | 快乐/兴奋 | 11 | 2 | 2 | 15 |
| 29 | `지긋지긋` | fed up | 厌烦/受够了 | 2 | 0 | 0 | 2 |
| 30 | `경악` | shock | 惊骇 | 8 | 0 | 1 | 9 |
| 31 | `뿌듯함` | pride | 自豪/充实感 | 12 | 1 | 1 | 14 |
| 32 | `한심함` | pathetic | 可怜又可悲 | 9 | 1 | 2 | 12 |
| 33 | `고마움` | gratitude | 感激 | 10 | 0 | 3 | 13 |
| 34 | `화남/분노` | anger/rage | 生气/愤怒 | 11 | 2 | 3 | 16 |
| 35 | `증오/혐오` | loathing/hatred | 憎恶/仇恨 | 11 | 2 | 3 | 16 |
| 36 | `짜증` | irritation | 烦躁 | 2 | 2 | 1 | 5 |
| 37 | `부끄러움` | shame | 羞愧 | 9 | 1 | 1 | 11 |
| 38 | `죄책감` | guilt | 内疚 | 5 | 3 | 0 | 8 |
| 39 | `어이없음` | preposterous | 荒谬/无语 | 5 | 0 | 0 | 5 |
| 40 | `우쭐댐/무시함` | arrogance/disregard | 得意忘形/轻视 | 2 | 1 | 0 | 3 |
| 41 | `재미없음` | boredom | 无聊 | 0 | 0 | 0 | 0 |
| 42 | `귀찮음` | laziness | 嫌麻烦/懒得 | 0 | 0 | 0 | 0 |
| 43 | `역겨움/징그러움` | disgust/repulsiveness | 恶心/厌恶 | 1 | 0 | 1 | 2 |

Codebook: `label_taxonomy.json`.

## Citation

```bibtex
@article{10.25024/REVIEW.2026.29.1.006,
  author    = {LIM I RO and Kim, Byungjun and Haein Ji},
  title     = {KPoEM: A Human-Annotated Dataset for Emotion Classification and RAG-Based Poetry Generation in Korean Modern Poetry},
  journal   = {The Review of Korean Studies},
  publisher = {한국학중앙연구원},
  volume    = {29},
  number    = {1},
  year      = {2025},
  url       = {https://doi.org/10.25024/review.2026.29.1.161}
}
```

Dataset DOI: [10.5281/zenodo.15598092](https://doi.org/10.5281/zenodo.15598092)
