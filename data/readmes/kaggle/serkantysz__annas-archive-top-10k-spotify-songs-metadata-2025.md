# Anna’s Archive Top 10K Spotify Songs Expanded 2025

Full audio and lyric embeddings, feature engineering. Similarity files and more

# New Update: 2026-09-03

The dataset includes both CSV and Parquet files for songs, artists, and genres. These are the base source files. Everything else was extracted or generated from these files and the audio files, which are not uploaded here.

The dataset has been expanded beyond the original Spotify metadata into a larger multimodal audio, lyrics, and music similarity dataset. The dataset has been refreshed, some incorrect lyrics have been fixed, and inaccuracies in some columns (e.g., genres and duration) have been corrected in the original dataset. It now also includes full-track audio embeddings, lyric embeddings, emotion features, genre representations, and precomputed similarity data (the top 250 most similar songs for each song).

### Full audio files and quality checks

Full-length audio was downloaded for all 10,000 songs using a pipeline built with yt-dlp. Every file was decoded and checked against Spotify's catalog duration. Audio files with duration mismatches were identified and fixed. Only one song has a 30-second preview instead of the full track because it was deleted from Spotify and was not available on YouTube either.

### Lyrics and language data

Some songs had incorrect lyrics, which have now been fixed. Language identification was run across 26 languages and writing systems, including Romanized Hindi/Hinglish, Japanese, Korean, Spanish, and others.

Additional lyric features include lexical richness and readability metrics, along with instrumental-track detection.

### Audio features and embeddings

Unlike many music datasets that use 30-second previews, these features were extracted from the full duration of each track.

The audio data includes:

* **LAION-CLAP** — 512 dimensions
* **MERT-v1-330M** — 1,024 dimensions
* **Google VGGish** — 128 dimensions
* **PANNs Cnn14** — 2,048 dimensions
* **88 DSP features** extracted with Librosa, including MFCCs, spectral contrast, onset rate, and loudness
* **Silero VAD features** measuring vocal ratio and estimated vocal duration

### Lyrics, meaning, and emotion features

Full lyrics were embedded using **Microsoft Harrier-0.6B**, **Multilingual-E5-Large**, and **BGE-M3**.

The dataset also includes 28 emotion probabilities from GoEmotions and 8 sentiment dimensions based on NRC.

### Precomputed music similarity

Several similarity spaces are included for different recommendation and retrieval tasks. Each one has a precomputed Top-250 nearest-neighbor table, so similarity search does not need to be calculated from scratch.

* **Master Multimodal (3,795-D):** Weighted combination of sound, lyrics, mood, genre, and era (38% audio embeddings, 35% lyric embedings, 27% musical and temporal context)
* **Acoustic Sound (1,664-D):** CLAP, MERT-330M, and VGGish for sound-focused similarity
* **Lyric Narrative (2,048-D):** Harrier and E5 for lyrical and semantic similarity
* **Unified Mood & Context (83-D):** Weighted combination of genre representations (40%), Spotify audio features (30%), temporal era (15%), and vocal dynamics (15%)

The feature combinations and weights were selected through leave-one-group-out ablation testing to remove signals that did not improve the similarity results. For example, PANNs was removed from acoustic similarity, BGE-M3 was removed from lyric similarity, and text-based emotion features (GoEmotions/NRC) were removed from mood similarity and UMAP projections to avoid zero-padding disparity on non-English tracks in favor of genre and temporal context.

### Splits and visualizations

The dataset now includes **5-fold GroupKFold splits grouped by artist**, preventing the same artist from appearing in both training and test data. Chronological splits are also included for time-based evaluation.

For exploration and visualization, 2D UMAP projections are provided for the main feature spaces.

### More Information

Check the Markdown files in the `docs` directory for more information. Also you can check column names of parquet files directly from kaggle, just check out `data/features/qc/features_audit.json` file.

# Top 10,000 Most Popular Spotify Songs

## Dataset Description
This dataset contains metadata for the top 10,000 most popular songs on Spotify as of **July 2025**. It captures a snapshot of the most trending and widely played tracks, providing valuable insights into current musical tastes and artist popularity. The popularity of songs ranges from 70 to 100.

## Origin
The data is sourced from [Anna's Archive](https://en.wikipedia.org/wiki/Anna%27s_Archive). We expand this source data (14 columns) to have audio  features, full lyrics, genres and artist data (32 columns).

## About Dataset
This dataset provides a deep dive into the top popular 10,000 songs on Spotify as of **July 2025**. 

We took the raw top 10k export and performed significant post-processing:
1.  **Lyrics Integration:** Fetched and matched lyrics for **~96%** of the dataset from [lrclib](https://lrclib.net/docs)
2.  **Gap Filling:** Identified **1,612 artists** who were missing genre data in the official Spotify API and filled them using external sources.
3.  **"Main Genre" Standardization:** Spotify uses thousands of micro-genres. We mapped these into **17 standardized parent genres** to make high-level analysis possible.

## Content
The dataset contains **10,000 rows** and **32 columns**.

### Column Descriptions

| Column | Description |
| :--- | :--- |
| `rank` | Position in the Top 10,000 list. |
| `popularity` | Current popularity score (0-100). |
| `duration` | Song duration in human-readable format. |
| `explicit` | Whether the track contains explicit content (1=Yes, 0=No). |
| `release_date` | Date of release. |
| `album_type` | Type of release (album, single, compilation). |
| `isrc` | International Standard Recording Code. |
| `copies` | Estimated number of copies/sales. |
| `danceability` | Suitability for dancing (0.0 to 1.0). |
| `energy` | Intensity and activity level of the track. |
| `key` | The key the track is in using standard Pitch Class notation. |
| `loudness` | Overall loudness in decibels (dB). |
| `mode` | Modality (Major=1, Minor=0). |
| `speechiness` | Presence of spoken words (0.0 to 1.0). |
| `acousticness` | Confidence measure of acoustic nature (0.0 to 1.0). |
| `instrumentalness` | Probability that the track contains no vocals. |
| `liveness` | Probability that the track was recorded with an audience. |
| `valence` | Musical positiveness/happiness (0.0 to 1.0). |
| `tempo` | Estimated tempo in beats per minute (BPM). |
| `duration_ms` | Song duration in milliseconds. |
| `time_signature` | Estimated overall time signature. |
| `total_artist_followers` | Total combined followers of all artists on the track. |
| `avg_artist_popularity` | Average popularity score of the artists. |
| `artist_genres` | Original granular sub-genres from Spotify. |
| `main_genres` | Standardized high-level parent genres. |
| `lyrics` | Full textual lyrics of the song. |

### The "Main Genres"
To facilitate better classification models, the `main_genres` column standardizes artists into these 17 categories:
*   Blues, Christian, Classical, Country, Easy Listening, Electronic, Folk, Hip Hop, Jazz, Latin, Metal,New Age, Pop, R&B, Reggae, Rock, Traditional Music.
*(Note: A song may belong to multiple categories, e.g., "Pop, Rock")*

## Acknowledgements
We acquired the base metadata from Anna's Archive and enriched it with audio features, artist details, genres, and lyrics using various sources.

출처: Kaggle (serkantysz/annas-archive-top-10k-spotify-songs-metadata-2025)
태그: music, art, nlp, tabular, multimodal
라이선스: MIT
수정일: 2026-09-05T21:21:33.670Z
