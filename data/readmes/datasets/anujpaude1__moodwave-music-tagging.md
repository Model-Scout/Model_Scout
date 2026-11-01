---
pretty_name: MoodWave Music Tagging
license: other
license_name: moodwave-research-use-only
license_link: LICENSE.md
language:
  - hi
  - en
  - ne
  - es
  - pt
  - ar
  - ja
  - ko
  - pa
  - new
  - ur
  - bho
  - mai
language_creators:
  - found
annotations_creators:
  - expert-generated
  - machine-generated
multilinguality:
  - multilingual
source_datasets:
  - original
task_categories:
  - audio-classification
size_categories:
  - 10K<n<100K
tags:
  - music
  - music-information-retrieval
  - genre-classification
  - hindi
  - nepali
  - bollywood
  - nepali-folk
  - lok-geet
  - k-pop
  - latin-music
  - arabic-music
configs:
  - config_name: default
    data_files:
      - split: train
        path: data/train-*.parquet
      - split: validation
        path: data/validation-*.parquet
      - split: test
        path: data/test-*.parquet
---

# MoodWave Music Tagging

A multilingual music-genre dataset built for **Hindi and Nepali** repertoire, which existing
music models handle poorly, alongside Spanish, Portuguese, Arabic, Japanese, Korean and
English: **36,223 songs, 2,820 hours**. Every song has a genre and a finer style, and
the splits are **artist-disjoint**: 28,914 train / 3,640 validation / 3,669 test.

**This repository contains metadata only, no audio.** Each row carries a YouTube ID (or a
content hash for legacy rows) plus labels and provenance. See
[Getting the audio](#getting-the-audio).

## What is new in v2.0.0

- **Cleaned.** All 45,770 collected uploads were checked. An AudioSet audio model (AST)
  scored six 10-second windows of every file, LLM review agents read every row (title,
  channel, labels and the audio reading), and adjudicators settled every disagreement.
  **9,494 uploads (20.7%) were removed** because they were not songs, or not a
  new song. See [What was removed](#what-was-removed).
- **Every song has a genre and a style:** 20 genres, 248 sound-defined styles,
  15 families, with artists and languages corrected in review.
- **Artist-disjoint splits**, a per-row `sample_weight`, and a recommended training label set
  (`label_recommended_v1`, 17 classes).
- **Five new language sets:** Spanish, Portuguese, Arabic, Japanese and Korean. Version 1.x
  covered Hindi, Nepali and English.
- **New layout:** `data/{train,validation,test}-*.parquet` replaces
  `data/manifest/train-*.parquet`.
- **Columns removed** because they were empty or nearly empty across the expanded collection:
  `title_romanized`, `composer`, `film_title`, `film_industry`, `vocal_gender`,
  `origin_region`, `tradition` (superseded by `style`), `mood_source`, `source_playlist_id`
  and `audio_sha256` (legacy rows keep its first 11 hex digits in `track_id`).

Earlier versions remain available as the tags `v0.1.0` to `v1.2.0`.

## Genres

| Genre | Tier | Family | Tracks | Artists | Train / Val / Test | Styles |
|---|---|---|---:|---:|---|---:|
| Pop | A | Pop & Dance | 7,636 | 1,727 | 6,136 / 764 / 736 | 25 |
| Folk | A | Folk & Roots | 4,462 | 205 | 3,574 / 446 / 442 | 39 |
| Rock | A | Rock & Metal | 3,182 | 159 | 2,549 / 317 / 316 | 17 |
| Jazz | A | Jazz & Blues | 2,904 | 102 | 2,323 / 291 / 290 | 21 |
| Hip-Hop | A | Hip-Hop & Rap | 2,743 | 236 | 2,195 / 274 / 274 | 13 |
| Classical | A | Classical & Art Music | 2,589 | 90 | 2,071 / 259 / 259 | 21 |
| Electronic | A | Electronic | 2,141 | 244 | 1,720 / 213 / 208 | 32 |
| Country | A | Country | 1,438 | 43 | 1,150 / 144 / 144 | 10 |
| Bhajan/Devotional | B | Devotional & Spiritual | 1,321 | 148 | 1,030 / 132 / 159 | 7 |
| R&B | A | R&B, Soul & Blues | 1,227 | 107 | 981 / 123 / 123 | 10 |
| Reggae | A | Reggae & Caribbean | 1,216 | 45 | 972 / 122 / 122 | 7 |
| Ghazal | B | South Asian Classical & Light Classical | 1,173 | 28 | 929 / 94 / 150 | 3 |
| Nepali Lok Geet | B | Nepali Folk & Traditional | 883 | 241 | 707 / 88 / 88 | 13 |
| Adhunik | B | Nepali Modern | 829 | 374 | 663 / 83 / 83 | 4 |
| Lok Dohori | B | Nepali Folk & Traditional | 726 | 80 | 593 / 66 / 67 | 4 |
| Hindustani Classical | B | South Asian Classical & Light Classical | 696 | 16 | 474 / 119 / 103 | 8 |
| Bhangra/Punjabi Folk | B | Punjabi & North Indian Folk | 666 | 104 | 534 / 66 / 66 | 4 |
| Tamang Selo | B | Nepali Folk & Traditional | 202 | 38 | 162 / 20 / 20 | 3 |
| Sufi/Qawwali | B | Devotional & Spiritual | 133 | 34 | 107 / 13 / 13 | 5 |
| Deuda | B | Nepali Folk & Traditional | 56 | 38 | 44 / 6 / 6 | 2 |

`Artists` counts identified performers.

| Language | Tracks |
|---|---:|
| `hi` | 6,554 |
| `instrumental` | 5,440 |
| `en` | 4,117 |
| `ne` | 3,907 |
| `es` | 3,851 |
| `pt` | 3,704 |
| `ar` | 2,921 |
| `ja` | 1,942 |
| `ko` | 1,747 |
| `other` | 978 |
| `pa` | 861 |
| `new` | 126 |
| unknown | 48 |
| `ur` | 14 |
| `bho` | 12 |
| `mai` | 1 |

## Files

| Path | What it holds |
|---|---|
| `data/{train,validation,test}-*.parquet` | One row per song, every label (see [Schema](#schema)) |
| `label_maps/` | Genres, styles, families and the recommended classes, with ids, counts and descriptions |
| `taxonomy/` | The taxonomy definition: genres, styles, moods, vibes |
| `stats/` | Genre by language and by split, artists per genre, style counts |
| `GENRES.md` | One card per genre: its sound, its styles, merge and split notes |

## Why the taxonomy looks unusual

**Genre means sound.** "Bollywood" is not a genre here: it describes who commissioned the
music, not what it sounds like, and filmi spans Hindustani classical, folk, rock, qawwali and
EDM. A Hindi film song therefore carries `language=hi`, `is_filmi=true` **and** a musical genre.
Encoding Bollywood as a genre teaches a model "Hindi language means Bollywood", which then
mislabels every Hindi rock song. This follows Apple Music (Primary `Bollywood` + Secondary
`Soundtrack`), Spotify (`bollywood` is a child of `pop`) and MusicBrainz (no `bollywood` genre
at all, only `filmi`). The same rule files K-pop, J-pop and Arabic pop under Pop, and J-rock
and rock en espanol under Rock.

**Tier A, language-agnostic sound:** Pop, Rock, Hip-Hop, Electronic, Folk, Jazz, R&B,
Classical, Country, Reggae

**Tier B, regional traditions with a distinct acoustic signature:** Hindustani Classical,
Sufi/Qawwali, Bhajan/Devotional, Ghazal, Bhangra/Punjabi Folk, Lok Dohori, Tamang Selo, Deuda,
Nepali Lok Geet, Adhunik

- Blues folds into R&B and Metal into Rock.
- `Classical` is notated art music: the Western tradition plus, by house rule, Arabic tarab and
  maqam art music and Korean and Japanese court traditions. Indian classical is
  `Hindustani Classical`, which also absorbs Carnatic.
- `Folk` is the umbrella for acoustic, regional and roots traditions without a Tier B class of
  their own: Latin American, Iberian and Brazilian roots, Arab and Maghrebi folk, East Asian
  folk (trot, enka) and Anglo singer-songwriters.

Two boundary rules:

1. **Newa music is `Nepali Lok Geet`, not `Bhajan/Devotional`.** The Devotional class is
   defined by sound (harmonium with dholak or tabla and manjira), not by religious function.
   Newar traditions such as Dapha and Gunla Bajan use dhimay and khin drums and asta-dhatu
   cymbals, and no harmonium.
2. **`genre=Deuda` never implies `language=ne`.** Deuda is performed in the Kumaon Division of
   Uttarakhand, India as well as in far-western Nepal.

## Labels

| Column | Classes | What it is |
|---|---:|---|
| `genre` | 20 | The main training class, defined by sound |
| `style` | 248 | A finer, sound-defined style inside one genre (`k-pop`, `reggaeton`, `bossa-nova`, `trot`, `qawwali`, `teej-geet`, ...) |
| `family` | 15 | Coarse groups of related genres |
| `label_recommended_v1` | 17 | Suggested training classes: a genre trains on its own only with at least 10 identified artists and 300 tracks, otherwise it folds into its closest sibling (Sufi/Qawwali into Ghazal; Deuda and Tamang Selo into Nepali Lok Geet) |

- `sample_weight` is 1 / sqrt(tracks by the same artist in the same genre), so one prolific
  artist cannot dominate a class.
- `label_maps/styles.json` describes every style: its sound, tempo and instrument markers,
  regions, counts, and `split_ready` (`yes`, `maybe` or `no`: distinct and big enough to become
  a class of its own).
- The prose in `GENRES.md` and in the genre summaries was written before the cleanup, so counts
  quoted inside that text are approximate. The numbers in the tables and in the `tracks`,
  `artists` and split fields of `label_maps/` are exact.

Merging or splitting classes is a map over `genre` and `style`. Nothing needs relabelling:

```python
split = {"bossa-nova": "Brazilian Jazz", "samba": "Brazilian Roots", "mpb": "Brazilian Roots"}
df["label"] = df["style"].map(split).fillna(df["genre"])
```

## Splits

- **No artist appears in two splits.** Spelling variants of one artist (`이찬원` and
  `Lee Chan-won`) are linked through single-artist channels so they cannot straddle splits.
  Rows without an identified artist are grouped by channel or kept alone.
- **Near-duplicates were removed collection-wide** (audio-embedding match plus same-song
  re-uploads), so one recording cannot sit in both train and test.
- The target is 80 / 10 / 10 inside every genre. A few Tier B genres are a handful of prolific
  artists, so their splits are lumpier (Hindustani Classical is 474 / 119 / 103).
- 53 suspected AI-generated or falsely attributed uploads are kept out of every split
  and are not published.

## Schema

| Column | Type | Notes |
|---|---|---|
| `track_id` | string | `yt_<YouTube ID>`, or `lg_<11 hex>` for legacy rows (the start of the audio's SHA-256) |
| `youtube_id` | string | Empty for the 1,511 legacy rows |
| `title` | string | Upload title, verbatim (Devanagari, Hangul, Arabic and so on) |
| `artist` / `artist_id` | string | Performer as resolved in review; `artist_id` is an accent-insensitive slug. Empty when unknown (860 rows) |
| `genre` / `genre_id` / `genre_tier` | string / int64 / string | 20 genres, tier `A` or `B` |
| `style` / `style_id` | string / int64 | 248 styles |
| `family` / `family_id` | string / int64 | 15 families |
| `label_recommended_v1` / `label_recommended_v1_id` | string / int64 | 17 classes |
| `split` | string | `train`, `validation` or `test` |
| `sample_weight` | float64 | See [Labels](#labels) |
| `language` | string | ISO 639 code, `instrumental`, `other`, or empty when unknown |
| `duration_s` | float32 | The full song, not a clip |
| `source_set` | string | Collection campaign: `portuguese`, `spanish`, `hindi`, `arabic`, `hindi_genres`, `nepali`, `japanese`, `korean`, `english`, `nepali_genres`, `legacy_english` |
| `source_channel_id` | string | YouTube channel the upload came from (`legacy_hf` for legacy rows) |
| `is_filmi` `is_live` `is_cover` `is_remix` `is_instrumental` | bool | |
| `flags` | list\<string\> | `live`, `filmi`, `instrumental`, `cover`, `remix`, `archival`, `karaoke`, `medley`, `kids`, `acapella`, `mashup` |
| `mood` | string | `Energetic`, `Calm`, `Romantic`, `Sad`, `Happy`, `Angry`; empty for 35% of rows |
| `vibes` | list\<string\> | `Chill`, `Late Night`, `Party`, `Romantic`, `Focus`, `Road Trip`, `Gym`, `Wedding & Festival`, `Morning`, `Study`, `Patriotic`, `Monsoon` |
| `release_year` / `decade` | int16 / string | `-1` / empty when unknown (90% of rows) |
| `label_source` / `label_confidence` | string / float32 | Where the genre came from: `agent_reconciler` (retrieval evidence reconciled by an LLM), `channel_provenance`, `legacy_ground_truth` (hand-curated); `+review` when a review agent or adjudicator set the final label |
| `description` | string | One-line machine-written note on the recording, when the reviewer wrote one |
| `audio_verdict` | string | Audio check: `music`, `mixed_speech`, `talk_over_music`, `speech` or `silent`. Rows other than `music` were kept only after review judged them songs |
| `music_mean` / `speech_mean` | float64 | Mean AudioSet `Music` and `Speech` probability over six 10.24-second windows |
| `silent_windows` | int64 | How many of the six windows were silent |
| `taxonomy_version` | string | Matches `taxonomy/genres.json` (1.1.0) |

## Usage

```python
from datasets import load_dataset

ds = load_dataset("anujpaude1/moodwave-music-tagging", revision="v2.0.0")
train = ds["train"]
print(train[0]["title"], "|", train[0]["genre"], "|", train[0]["style"])

# the recommended 17-class scheme
classes = sorted(set(train["label_recommended_v1"]))
```

Query without downloading, through the SQL Console or DuckDB:

```sql
SELECT genre, style, count(*) AS n
FROM 'hf://datasets/anujpaude1/moodwave-music-tagging/data/train-*.parquet'
GROUP BY 1, 2 ORDER BY n DESC;
```

**Windows users:** if you load audio through `datasets`, pin `datasets<4.0`. Version 4.0 moved
audio decoding to `torchcodec`, which has no Windows build. This repository has no audio
column, so it is unaffected.

## Getting the audio

No audio is distributed here. To reconstruct it, resolve `youtube_id` yourself:

```bash
yt-dlp --js-runtimes node -f bestaudio \
       --extract-audio --audio-format best \
       -o "yt_%(id)s.%(ext)s" \
       --sleep-requests 3 --sleep-interval 6 --max-sleep-interval 15 \
       "https://www.youtube.com/watch?v=<youtube_id>"
```

The reference pipeline keeps the full song and transcodes it to **Opus 48 kbps, mono, 24 kHz**.
24 kHz rather than 16 kHz so that MERT and CLAP remain usable; discogs-effnet resamples to
16 kHz and reads nothing above 8 kHz, so the encoding is transparent to it. Some uploads will
have been taken down since collection.

Legacy rows (`lg_` prefix, 1,511 English tracks) have no YouTube ID: they came from an
earlier collection and are identified by content hash only.

## How the data was built

1. **Enumerate** official label and artist channels for each language with
   `yt-dlp --flat-playlist`.
2. **Filter** by duration and title (compilations, trailers, interviews and other non-songs).
3. **Download** the full song and transcode it, discarding the source.
4. **Label**, retrieval first (iTunes, Last.fm, MusicBrainz, channel provenance), with an LLM
   used only to reconcile that evidence onto the fixed taxonomy. English legacy labels come
   from a hand-curated ground-truth set of an earlier collection.
5. **Audit** (October 2026): the audio check, review agents over every row, adjudication of
   every conflict, artist resolution and near-duplicate detection, then the artist-disjoint
   split. Title and duration filters alone had let through about one upload in five that was
   a duplicate or not a song.

### What was removed

| Reason | Uploads |
|---|---:|
| Duplicate upload of a kept recording (official audio, MV, lyric video, Topic re-release) | 4,438 |
| Talk: vlogs, interviews, podcasts, readings, documentaries | 2,035 |
| Snippet: previews, shorts, fragments | 943 |
| Behind the scenes, making-of | 630 |
| Trailer, teaser, promo, ad | 522 |
| Compilation: jukebox, medley, full album, DJ set | 506 |
| Other: junk channels, an AI content farm, game and sports clips | 138 |
| Fan content: cheering guides, fancams, dance practice | 126 |
| Fan edits: 8D, slowed + reverb, lofi flips | 113 |
| Silence or a broken file | 17 |
| Comedy | 16 |
| Sound effects, ambience | 10 |

## Limitations

- **Labels are machine-made**: retrieval, an LLM reconciler and LLM review agents,
  cross-checked against an audio model. Only the legacy English labels are hand-curated. Treat
  them as silver labels, and quote headline accuracy only on a human-verified subset.
- **Some Tier B genres are artist-poor.** Hindustani Classical has 16 identified
  artists and each instrument style is essentially one maestro, so a model can learn the artist
  instead of the genre. Report per-class results.
- **Live versions are kept** and flagged (`is_live`); some artists have dozens of live takes of
  one song. Filter them, or lean on `sample_weight`, if that matters.
- **Sampling bias** toward what labels and artists upload to YouTube; the Hindi catalogue skews
  heavily post-2000.
- **Mood labels are weak.** Audio-only Hindi mood classification tops out around 58% F-measure
  in the literature; lyrics are needed to do better. `Romantic` is a lyrical category with no
  position in valence-arousal space and will collapse into Calm and Sad under an audio-only
  model. It also appears on the vibe axis.

## Licence

Annotations: **non-commercial research use** (see `LICENSE.md`). The underlying compositions
and recordings remain the property of their rights holders. This repository distributes no
audio.

For takedown requests, open a discussion on this repository.
