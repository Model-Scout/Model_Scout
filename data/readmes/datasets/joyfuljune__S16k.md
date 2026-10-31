---
license: cc-by-nc-sa-4.0
task_categories:
  - audio-classification
  - text-classification
language:
  - zh
  - en
  - ja
  - ko
tags:
  - music
  - music-emotion-recognition
  - multi-label
  - netease
pretty_name: S16k
size_categories:
  - 100K<n<1M
configs:
  - config_name: songs
    data_files: songs.parquet
  - config_name: songs_9822_balanced
    data_files: songs_9822.parquet
  - config_name: playlists
    data_files: playlists.parquet
  - config_name: song_playlist
    data_files: song_playlist.parquet
  - config_name: tag_taxonomy
    data_files: tag_taxonomy.parquet
---

# S16k — Multi-label Music Emotion Recognition from NetEase Cloud Music

169,148 songs with multi-label emotion annotations, the 46,613 user-curated playlists the
annotations are derived from, pre-extracted audio features, and a class-balanced subset.

Reference paper: https://doi.org/10.1007/s00530-025-01701-z

## How the labels are defined

Every playlist on NetEase Cloud Music (网易云音乐) carries editorial tags such as 流行,
治愈, 夜晚. A song inherits the tags of every playlist that contains it, and the value stored
is a **count**: `emo_healing = 3` means three playlists holding this song are tagged 治愈.

These are platform and community tags, not controlled psychological ratings. Treat them
accordingly when comparing against annotation-based corpora such as DEAM or PMEmo.

## Files

| File | Rows | Size | Content |
|---|---|---|---|
| `songs.parquet` | 169,148 | 52 MB | Main table: metadata, 74 tag columns, emotion labels |
| `songs_9822.parquet` | 9,822 | 5 MB | Class-balanced subset, same schema plus `unique_id` |
| `playlists.parquet` | 46,613 | 10 MB | Source playlists with tags and popularity statistics |
| `song_playlist.parquet` | 477,216 | 2.4 MB | Song ↔ playlist relation, long format |
| `tag_taxonomy.parquet` / `.csv` | 74 | <1 MB | Tag column ↔ English ↔ Chinese ↔ group mapping |
| `songs_169148_vggish.npz` | 169,097 | 2.7 GB | VGGish embeddings |
| `songs_9822_vggish.npz` | 9,822 | 0.16 GB | VGGish embeddings for the balanced subset |
| `spectrograms_169148.npz` | 169,148 | 17.3 GB | Log-mel spectrograms in dB |

Audio features are computed from the **middle 30 seconds** of each track. Raw audio is not
redistributed.

## Quick start

```python
import pandas as pd

songs = pd.read_parquet("songs.parquet")
tax   = pd.read_parquet("tag_taxonomy.parquet")

emo_cols = tax.loc[tax.group == "emo", "column"].tolist()
X = songs[emo_cols]                       # tag counts
Y = (songs[emo_cols] > 0).astype(int)     # binary multi-label targets
```

## `songs.parquet`

### Identifiers and metadata

| Key | Type | Description |
|---|---|---|
| `song_id` | int64 | Primary key, unique across all rows |
| `alt_ids` | list\<int64\> | Further NetEase IDs pointing at the same track. Non-empty on 8,418 rows, up to 4 entries |
| `n_ids` | int8 | `1 + len(alt_ids)` |
| `name` | string | Track title, Chinese verbatim. 4 nulls |
| `artist` | string | 5 nulls |
| `language` | dictionary\<string\> | 42 values. `instrumental` 66,244 · `en` 42,747 · `zh` 39,692 · `ja` 13,113 · `ko` 2,504 |
| `duration_ms` | int32, nullable | Null on 21,798 rows (12.9%) where the source carries no duration. Those rows are otherwise complete and should not be dropped |
| `lyric` | string | Present on 102,903 rows; absent almost exactly where `language == "instrumental"` |
| `n_playlists` | int16 | Playlists containing this song. Mean 2.82, max 198 |

### Tag columns

74 columns holding counts in the range 0–133, prefixed by group following the official
NetEase tag taxonomy:

| Prefix | Group | Count | Examples |
|---|---|---|---|
| `lang_` | Language 语种 | 6 | `lang_mandarin` 华语 · `lang_western` 欧美 · `lang_cantonese` 粤语 |
| `genre_` | Genre 风格 | 25 | `genre_pop` 流行 · `genre_rock` 摇滚 · `genre_new_age` New Age |
| `scene_` | Scene 场景 | 12 | `scene_night` 夜晚 · `scene_driving` 驾车 · `scene_study` 学习 |
| `emo_` | Emotion 情感 | 12 | `emo_healing` 治愈 · `emo_sadness` 伤感 · `emo_missing` 思念 |
| `theme_` | Theme 主题 | 18 | `theme_acg` ACG · `theme_soundtrack` 影视原声 · `theme_ktv` KTV |
| `misc_` | Outside the official taxonomy | 1 | `misc_sexy` 性感 |

`tag_taxonomy.parquet` holds the complete mapping with columns `column`, `en`, `zh`,
`group`, `is_emotion_label`, `emotion_index`.

Four tags carried by the data but not listed on the official taxonomy page are grouped by
meaning: 小语种 under `lang`, 另类/独立 and 音乐剧 under `genre`, 性感 under `misc`.
性感 sits outside `emo` so that the emotion label set stays at exactly 12 classes.

### Emotion label vectors

Three fixed-length list columns sharing one order:

| Key | Type | Description |
|---|---|---|
| `emo_tag_counts` | list\<int16\>[12] | Playlist tag counts |
| `emo_ratio` | list\<float32\>[12] | `emo_tag_counts` normalised to sum 1 |
| `emo_label` | list\<int8\>[12] | 1 where the count is above 0 |

The order lives in the Parquet schema metadata:

```python
import pyarrow.parquet as pq, json
t = pq.read_table("songs.parquet")
EMO_ORDER = json.loads(t.schema.metadata[b"emotion_order"])
# ['Healing','Nostalgia','Excitement','Sadness','Romantic','Quiet',
#  'Happiness','Loneliness','Touching','Missing','Fresh','Relaxation']
```

The three list columns and the 12 scalar `emo_*` columns carry the same information; use
whichever suits the task.

Every song carries at least one emotion label, 2.50 on average. Positive rates run from
`emo_healing` 35.7% and `emo_relaxation` 32.8% down to `emo_missing` 11.3%.

## `songs_9822.parquet`

A subset chosen so the 12 emotions have near-equal positive support:

| | Healing | Nostalgia | Excitement | Sadness | Romantic | Quiet | Happiness | Loneliness | Touching | Missing | Fresh | Relaxation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| positives | 4,949 | 4,873 | 4,873 | 4,874 | 4,874 | 4,873 | 4,873 | 4,874 | 4,874 | 4,875 | 4,873 | 4,879 |

Mean 5.96 labels per song, above the 2.50 of the full table, since balancing favours
multi-labelled tracks. The schema matches `songs.parquet` with one addition:

| Key | Type | Description |
|---|---|---|
| `unique_id` | int64 | Row identifier within the subset |

Paired features: `songs_9822_vggish.npz`.

## `playlists.parquet`

| Key | Type | Description |
|---|---|---|
| `playlist_id` | int64 | Join key for `song_playlist.parquet` |
| `name` | string | Playlist title, Chinese verbatim |
| `tags` | list\<string\> | **Chinese tag strings**, e.g. `["感动","治愈","思念"]`. 75 distinct values, 1–6 per playlist, most commonly 3 |
| `n_tags` | int64 | |
| `confidence` | dictionary\<string\> | `normal` 23,567 · `vip` 15,865 · `official` 7,181 |
| `play_count` | int64 | |
| `subscribed_count` | int64 | |
| `share_count` | int64 | |
| `comment_count` | int64 | |
| `create_time` | timestamp | |
| `description` | string | Curator's free text, Chinese verbatim |
| `creator_nickname` | string | |
| `creator_user_type` | int64 | |
| `creator_gender` | int64 | 0 unspecified · 1 male · 2 female |

`tags` holds Chinese strings while `songs.parquet` uses English column names; the `zh` and
`column` fields of `tag_taxonomy.parquet` connect the two.

The 75 Chinese tag strings map onto 74 columns because the source spells *New Age* two ways,
one with a regular space (U+0020) and one with a non-breaking space (U+00A0). Both denote the
same tag and share the column `genre_new_age`.

## `song_playlist.parquet`

| Key | Type |
|---|---|
| `song_id` | int64 |
| `playlist_id` | int64 |

477,216 rows. Every `playlist_id` resolves in `playlists.parquet`. 43,558 of the 46,613
playlists are referenced by at least one song.

This table makes the labels re-derivable under a different aggregation. The stored counts
weight every playlist equally; the relation lets you weight by popularity or restrict to
curated sources:

```python
rel = pd.read_parquet("song_playlist.parquet")
plf = pd.read_parquet("playlists.parquet")

official = plf[plf.confidence == "official"]
sub = rel[rel.playlist_id.isin(official.playlist_id)]

weight = plf.set_index("playlist_id")["play_count"]
```

Aggregating the Chinese `tags` over each song's playlists reproduces the stored tag counts
exactly.

## Audio features

Both NPZ archives are keyed by `song_id` as a **string**:

```python
import numpy as np
z = np.load("songs_169148_vggish.npz")
emb = z["1000155"]          # (31, 128) float32
```

| File | Array per song | Description |
|---|---|---|
| `songs_169148_vggish.npz` | `(31, 128)` float32, range 0–255 | VGGish embeddings, one 128-d frame per ~0.96 s across the middle 30 s, post-processed quantised output. Covers 169,097 songs |
| `songs_9822_vggish.npz` | `(31, 128)` float32 | The same for the balanced subset |
| `spectrograms_169148.npz` | `(64, 469)` float32, range −70.8–0 | Log-mel spectrogram in dB, 64 mel bands × 469 frames across the middle 30 s. Covers 169,148 songs |

`songs_169148_vggish.npz` covers 169,097 of the 169,148 songs; check key membership before
indexing.

## Licence and citation

CC BY-NC-SA 4.0. Only identifiers, metadata, tags and derived features are distributed; no
audio.

```bibtex
@article{s16k,
  doi = {10.1007/s00530-025-01701-z},
  journal = {Multimedia Systems},
  title = {A multi-label music emotion recognition dataset from NetEase Cloud Music}
}
```
