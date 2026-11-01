---
pretty_name: Yap Movie Clips
language:
  - de
  - en
  - fr
  - hi
  - it
  - ja
  - ko
  - pt
  - ru
  - es
  - th
  - zh
license: other
license_name: film-clips-see-card
license_link: https://yap.town/privacy
task_categories:
  - automatic-speech-recognition
  - audio-classification
  - text-to-speech
tags:
  - speech
  - phonemes
  - language-learning
  - movies
  - subtitles
  - forced-alignment
size_categories:
  - 100K<n<1M
configs:
  - config_name: deu
    data_files:
      - split: train
        path: data/deu/clips.parquet
  - config_name: eng
    data_files:
      - split: train
        path: data/eng/clips.parquet
  - config_name: fra
    data_files:
      - split: train
        path: data/fra/clips.parquet
  - config_name: hin
    data_files:
      - split: train
        path: data/hin/clips.parquet
  - config_name: ita
    data_files:
      - split: train
        path: data/ita/clips.parquet
  - config_name: jpn
    data_files:
      - split: train
        path: data/jpn/clips.parquet
  - config_name: kor
    data_files:
      - split: train
        path: data/kor/clips.parquet
  - config_name: por
    data_files:
      - split: train
        path: data/por/clips.parquet
  - config_name: rus
    data_files:
      - split: train
        path: data/rus/clips.parquet
  - config_name: spa
    data_files:
      - split: train
        path: data/spa/clips.parquet
  - config_name: tha
    data_files:
      - split: train
        path: data/tha/clips.parquet
  - config_name: zho-hans
    data_files:
      - split: train
        path: data/zho-hans/clips.parquet
---

# Yap Movie Clips

187,721 short video clips of film dialogue from 411 films, one
sentence per clip, in 12 languages. Every clip comes with the sentence as
written in the film's official subtitles, word-level timings, the surrounding
subtitle cues, an independent speech-to-text transcript of the same audio, and
the phoneme sequence the sentence was expected to contain versus what a
phoneme recogniser actually heard.

This is the corpus behind the listening and pronunciation cards at
[yap.town](https://yap.town), a language-learning app. It is published so that
the same material can be used for research on speech recognition, phoneme
recognition, forced alignment, and pronunciation assessment on real,
noisy, acted speech rather than read speech.

| course | clips | films | hours | hi (GB) | lo (GB) |
|---|---:|---:|---:|---:|---:|
| deu | 8,018 | 22 | 20.1 | 35.4 | 3.8 |
| eng | 89,383 | 151 | 257.0 | 344.8 | 39.6 |
| fra | 16,637 | 43 | 45.9 | 66.4 | 7.8 |
| hin | 7,724 | 24 | 20.6 | 18.8 | 3.1 |
| ita | 8,156 | 17 | 20.4 | 30.6 | 3.7 |
| jpn | 11,538 | 32 | 30.2 | 34.8 | 4.6 |
| kor | 12,817 | 23 | 33.4 | 41.3 | 5.3 |
| por | 2,576 | 10 | 7.0 | 12.8 | 1.7 |
| rus | 6,926 | 18 | 15.6 | 17.3 | 2.6 |
| spa | 9,410 | 18 | 26.1 | 36.0 | 4.8 |
| tha | 6,063 | 19 | 15.4 | 13.6 | 2.3 |
| zho-hans | 8,473 | 34 | 21.2 | 25.4 | 3.8 |
| **total** | **187,721** | **411** | **512.9** | **677.1** | **82.9** |


## What makes a clip

A clip is included only when three independent witnesses agree that the
subtitle sentence is what is said on the soundtrack:

1. **Official subtitles.** The film's own subtitle track (disc text, OCR'd
   disc bitmaps, or a downloaded file), re-synced to the audio, split into
   sentences. For Japanese, Chinese, Korean and Thai, cues are merged and
   split into sentences by an LLM; for the other languages by rules.
2. **A word-timed transcript** of the whole film (ElevenLabs Scribe), which
   must contain the sentence verbatim (word error rate 0 after normalisation)
   and supplies the word timings.
3. **A phoneme recogniser** ([lexide-pronunciation](https://huggingface.co/anchpop/lexide-pronunciation),
   a wav2vec2 CTC model over IPA) scoring the audio against the sentence's
   expected phonemes (from [g2p](https://github.com/anchpop/g2p)). The clip
   passes if the expected sequence is likely enough under the model, its edges
   are clean, and the padding around the sentence has no competing speech.

Whole films are also checked for being verbatim rather than paraphrased
subtitles; films below the bar are dropped entirely.

Clips are cut generously: neighbouring subtitle lines are kept as context when
the gap is small (total clip ≤ ~15 s), and `critical_start_ms`/`critical_end_ms`
mark where the target sentence sits inside the clip. Context lines were never
verified; only the target sentence was.

## Files

- `data/<course>/clips.parquet` — one row per clip (schema below). Loadable with
  `datasets.load_dataset("anchpop/yap-movie-clips", "<course>")`.
- `clips/<course>/lo/<course>-lo-NNNNN.tar` — tar shards holding
  `<id>/lo.mp4` (H.264 480p, AAC 96 kbps stereo, loudness-normalised) and
  `<id>/meta.json` (the full sidecar the row was flattened from).
- `clips/<course>/hi/<course>-hi-NNNNN.tar` — same layout with `<id>/hi.mp4`
  (H.264 up to 1440p, AAC 160 kbps); only present if the hi rendition was
  packed. `hi_shard` is null otherwise, but `hi_url` still resolves.

Each parquet row names the shard its clip lives in (`hi_shard`, `lo_shard`) and
the same files are also served at `hi_url`/`lo_url`, so you can fetch a single
clip without a shard.

Course codes are ISO 639-3 (`zho-hans` is Mandarin with simplified-script
subtitles). Speech in a course is in that language; the films are mostly
originally in it, with a few dubs.

## Schema

All times are milliseconds. `source_*` fields are film-absolute; everything else
is clip-relative (0 = start of the mp4).

| column | meaning |
|---|---|
| `id` | `<imdb_id>-<sha256(sentence)[:8]>-<occurrence>`; stable across rebuilds |
| `language`, `imdb_id`, `title`, `year` | course and film |
| `sentence` | the target sentence, as in the official subtitles |
| `course_sentence` | whether yap's course filters accept the sentence (length, no numerals, etc.) |
| `speaker` | film-local speaker id from the transcript's diarisation |
| `words` | `[{text, at_ms, until_ms}]` — the sentence's words, timed |
| `subtitles` | `[{text, at_ms, until_ms, role}]` — every official cue overlapping the clip; `role` is `sentence`, `context-before` or `context-after` |
| `transcript_words` | `[{text, at_ms, until_ms, kind, speaker, logprob}]` — the transcript over the whole clip, `kind` is `word` or `audio_event` |
| `target_ipa` | expected phonemes for the sentence (g2p) |
| `heard_ipa` | phonemes the recogniser decoded from the audio |
| `phoneme_alignment` | `[{ph, at_ms, until_ms, logp}]` — forced alignment of `target_ipa` under the recogniser (null for clips built before alignment was exported) |
| `duration_ms` | clip length |
| `critical_start_ms`, `critical_end_ms` | the target sentence's span inside the clip, with ~300 ms lead-in |
| `context_lines_before/after` | how many neighbouring cues were kept |
| `source_sentence_*_ms`, `source_cut_*_ms` | film-absolute sentence span and cut window |
| `pad_before_ms`, `pad_after_ms` | silence kept around the sentence inside `critical` |
| `subtitle_digest`, `transcript_digest` | provenance hashes of the inputs the clip was built from |
| `transcript_wer` | word error rate between subtitle sentence and transcript (0 by construction) |
| `phoneme_ratio` | recogniser score the gate used (higher is better; gate at −2.0) |
| `logp_target_per_phoneme` | mean log-probability of the expected phonemes |
| `width`, `height`, `aspect_ratio`, `source_hdr` | source video properties (hi.mp4 is scaled to ≤1440p, HDR tone-mapped) |
| `hi_bytes`, `lo_bytes`, `hi_url`, `lo_url`, `hi_shard`, `lo_shard` | where the media is |
| `meta_format` | sidecar format version the row came from |
| `verification_json`, `media_json` | the full gate measurements/provenance and encode stamp, as JSON strings |

## Loading

```python
from datasets import load_dataset
fra = load_dataset("anchpop/yap-movie-clips", "fra", split="train")
row = fra[0]
print(row["sentence"], row["words"], row["hi_url"])
```

```python
# One shard of 480p clips
from huggingface_hub import hf_hub_download
import tarfile
p = hf_hub_download("anchpop/yap-movie-clips", "clips/fra/lo/fra-lo-00000.tar", repo_type="dataset")
tarfile.open(p).extractall("fra-lo-00000")
```

## Caveats

- Subtitle sentences are what the subtitle author wrote, not a phonetic
  transcription; contractions, dropped particles and slurring are common. The
  transcript and `heard_ipa` are independent views of the same audio.
- The phoneme gate was calibrated per language; pass rates and therefore
  the mix of clean vs. noisy audio differ between courses.
- Speaker ids are only meaningful within one film.
- Clips are excerpts of copyrighted films, published for research and
  language-learning use. If you are a rights holder and want material removed,
  contact andre@popovit.ch.

## Pipeline

Built by [`subtitle-corpus`](https://github.com/anchpop/yap/tree/main/libraries/subtitle-corpus)
(inventory → subtitle extraction/OCR → sync → transcription → sentence
segmentation → verbatim check → phoneme verification → clip cut → export) and
packaged by `scripts/hf_dataset.py` in the same directory.
