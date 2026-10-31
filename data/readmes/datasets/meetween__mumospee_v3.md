---
license: cc-by-4.0
task_categories:
- automatic-speech-recognition
language:
- "ar"
- "az"
- "bg"
- "ca"
- "cs"
- "cy"
- "da"
- "de"
- "el"
- "en"
- "es"
- "et"
- "fi"
- "fr"
- "gl"
- "gu"
- "he"
- "hi"
- "hu"
- "id"
- "it"
- "ja"
- "kk"
- "ko"
- "mr"
- "ms"
- "nl"
- "no"
- "pl"
- "pt"
- "ro"
- "ru"
- "sk"
- "sl"
- "sr"
- "sv"
- "sw"
- "ta"
- "tl"
- "tr"
- "uk"
- "ur"
- "vi"
size_categories:
- 1M<n<10M
pretty_name: Mumospee V3
tags:
- speech
- youtube
- whisper
- creative-commons
configs:
- config_name: default
  data_files:
  - split: "asr"
    path: data/asr/*/*.parquet
---

# Mumospee V3

## Dataset summary

Mumospee V3 is a speech corpus of 6,448,108 sentence-level clips cut from 46,373 YouTube
videos in 43 languages, 29,751 hours in total. The videos come from the YouTube
collection of [Mumospee V2](https://huggingface.co/datasets/meetween/mumospee_V2) (`youtube_meeting` split): 33,275 of the
46,373 videos (71.8%) are in that split, and the others are videos of the same
collection that are not included in it.

The corpus is organised in splits, one per task. Every row of a clip-level split refers to a clip
of the corpus through `clip_id`, so the rows of different tasks on the same clip can be joined. The
audio is not included in this repository; `audio_input_path` gives the relative path of each
clip's audio file (see [Audio files](#audio-files)).

All source videos were published under the Creative Commons Attribution license. The license of
every video was checked with the YouTube Data API on 2026-10-15; videos that were no longer
published under this license on that date are not included.

This is release v1: it contains the videos in languages other than English and a sample of about
8,000 hours of English videos. The remaining English videos are planned for a later release.

## Splits

| Split | Task | Rows | Videos | Hours | Languages | Files |
|---|---|---:|---:|---:|---:|---|
| `asr` | Automatic speech recognition (ASR) | 6,448,108 | 46,373 | 29,751.0 | 43 | `data/asr/<lang>/` |

Each task is one split with all its languages. The files of each language are in their own folder
(`data/<task>/<lang>/`), so one language can be loaded on its own by selecting its files (see
[Usage](#usage)).

## Usage

```python
from datasets import load_dataset

# one task, all languages, streamed
ds = load_dataset("meetween/mumospee_v3", split="asr", streaming=True)

# one task, one language: select the files of the language
ds = load_dataset("meetween/mumospee_v3", data_files={"asr": "data/asr/nl/*.parquet"}, split="asr")
row = next(iter(ds))
print(row["clip_id"], row["video_id"], row["start"], row["end"], row["text_output"])
```

The source video of a clip is `https://www.youtube.com/watch?v=<video_id>`; the clip is the
interval from `start` to `end` seconds.

## Dataset structure

```text
data/<task>/<lang>/train-NNNNN-of-MMMMM.parquet    one folder per task and language
scripts/make_clips.py                              cuts the clip audio from source videos
```

### Audio files

The audio files are not part of this repository. `audio_input_path` is the relative path of the clip
audio (16 kHz mono FLAC), the same in every clip-level split:

```text
audio/<lang>/<video_id>/<clip_id>.flac      e.g. audio/nl/-H9G_NHn4Xc/-H9G_NHn4Xc_0000.flac
```

`<lang>` is the video language. If the folder that contains `audio/` is `<root>`, the audio of a row
is `<root>/<audio_input_path>`. The script [`scripts/make_clips.py`](scripts/make_clips.py) cuts the
clips from source videos that you have downloaded and writes them at these paths; see
[`scripts/README.md`](scripts/README.md).

### Split `asr`: Automatic speech recognition (ASR)

One row per clip: the clip audio is the input, the Whisper large-v3-turbo transcript of the clip (cased and punctuated) is the target (`text_output`).

Files: `data/asr/<lang>/train-NNNNN-of-MMMMM.parquet`, at most 500,000 rows per
file, 51 files. The language of a folder is the language of the video, determined from
the language labels of its clips; individual clips can be in another language (code-switching),
given per clip in `lid_text_predicted`.

| Language | Files | Rows | Videos | Hours |
|---|---|---:|---:|---:|
| Spanish (`es`) | `data/asr/es/` | 1,821,626 | 11,319 | 8,675.6 |
| English (`en`) | `data/asr/en/` | 1,902,083 | 16,778 | 8,537.1 |
| French (`fr`) | `data/asr/fr/` | 1,091,144 | 7,465 | 5,019.6 |
| Russian (`ru`) | `data/asr/ru/` | 449,162 | 2,993 | 2,027.0 |
| Portuguese (`pt`) | `data/asr/pt/` | 431,715 | 2,411 | 2,021.8 |
| German (`de`) | `data/asr/de/` | 259,535 | 1,921 | 1,193.7 |
| Italian (`it`) | `data/asr/it/` | 194,942 | 1,332 | 972.9 |
| Indonesian (`id`) | `data/asr/id/` | 121,149 | 619 | 531.6 |
| Dutch (`nl`) | `data/asr/nl/` | 76,344 | 609 | 323.4 |
| Ukrainian (`uk`) | `data/asr/uk/` | 17,296 | 96 | 82.1 |
| Swedish (`sv`) | `data/asr/sv/` | 15,552 | 113 | 67.6 |
| Korean (`ko`) | `data/asr/ko/` | 12,791 | 139 | 60.1 |
| Turkish (`tr`) | `data/asr/tr/` | 11,933 | 82 | 52.9 |
| Hindi (`hi`) | `data/asr/hi/` | 7,535 | 168 | 30.8 |
| Vietnamese (`vi`) | `data/asr/vi/` | 5,643 | 69 | 24.4 |
| Norwegian (`no`) | `data/asr/no/` | 3,918 | 23 | 18.0 |
| Arabic (`ar`) | `data/asr/ar/` | 4,192 | 26 | 16.9 |
| Catalan (`ca`) | `data/asr/ca/` | 2,936 | 24 | 13.9 |
| Polish (`pl`) | `data/asr/pl/` | 2,350 | 23 | 11.2 |
| Hebrew (`he`) | `data/asr/he/` | 2,299 | 31 | 10.7 |
| Greek (`el`) | `data/asr/el/` | 2,859 | 15 | 9.9 |
| Japanese (`ja`) | `data/asr/ja/` | 1,978 | 31 | 8.9 |
| Kazakh (`kk`) | `data/asr/kk/` | 1,753 | 9 | 7.4 |
| Czech (`cs`) | `data/asr/cs/` | 1,585 | 13 | 7.3 |
| Finnish (`fi`) | `data/asr/fi/` | 1,497 | 8 | 7.0 |
| Tagalog (`tl`) | `data/asr/tl/` | 1,618 | 12 | 6.7 |
| Galician (`gl`) | `data/asr/gl/` | 610 | 6 | 2.9 |
| Serbian (`sr`) | `data/asr/sr/` | 533 | 3 | 2.5 |
| Malay (`ms`) | `data/asr/ms/` | 290 | 2 | 1.4 |
| Bulgarian (`bg`) | `data/asr/bg/` | 254 | 7 | 1.2 |
| Azerbaijani (`az`) | `data/asr/az/` | 200 | 4 | 0.9 |
| Danish (`da`) | `data/asr/da/` | 170 | 5 | 0.8 |
| Hungarian (`hu`) | `data/asr/hu/` | 106 | 2 | 0.5 |
| Slovak (`sk`) | `data/asr/sk/` | 143 | 1 | 0.5 |
| Slovenian (`sl`) | `data/asr/sl/` | 73 | 1 | 0.3 |
| Tamil (`ta`) | `data/asr/ta/` | 70 | 2 | 0.3 |
| Swahili (`sw`) | `data/asr/sw/` | 62 | 3 | 0.3 |
| Urdu (`ur`) | `data/asr/ur/` | 53 | 2 | 0.2 |
| Welsh (`cy`) | `data/asr/cy/` | 46 | 2 | 0.2 |
| Estonian (`et`) | `data/asr/et/` | 25 | 1 | 0.1 |
| Romanian (`ro`) | `data/asr/ro/` | 15 | 1 | 0.1 |
| Gujarati (`gu`) | `data/asr/gu/` | 11 | 1 | 0.1 |
| Marathi (`mr`) | `data/asr/mr/` | 12 | 1 | 0.1 |
| all languages | `data/asr/*/` | 6,448,108 | 46,373 | 29,751.0 |

Example row (the columns that have a value; 39 columns of this row are null). The transcript is
shortened here, and `attribution`, which is stored as a JSON string, is shown parsed.

```json
{
  "sample_id": "youtube_-H9G_NHn4Xc_0000_asr",
  "task": [
    "asr"
  ],
  "split": "train",
  "source_dataset": "youtube_clips_v1",
  "license": "CC-BY-4.0",
  "audio_input_path": "audio/nl/-H9G_NHn4Xc/-H9G_NHn4Xc_0000.flac",
  "audio_input_duration": 15.75,
  "audio_input_sample_rate": 16000,
  "audio_input_num_channels": 1,
  "audio_input_codec": "flac",
  "text_output": "In deze video laat ik zien hoe je GA4 e-commerce setting instelt aan de hand van Tag Manager. Je moet helaas zelf gebeurtenissen toevoegen. In dit voorbeeld mak ...",
  "text_output_normalized": "in deze video laat ik zien hoe je ga4 e-commerce setting instelt aan de hand van tag manager. je moet helaas zelf gebeurtenissen toevoegen. in dit voorbeeld maken we gebruik van een datalayer die ga3 evenementen heeft.",
  "num_words_output": 37,
  "language_audio_input": "nl",
  "language_text_output": "nl",
  "lid_audio_predicted": "nl",
  "language_confidence_audio": 0.999,
  "lid_text_predicted": "nl",
  "language_confidence_text": 0.988,
  "repetition_score": 0.0,
  "words_per_second": 2.3492063492063493,
  "chars_per_second": 13.841269841269842,
  "text_duplicate_score": 0.0,
  "clip_id": "-H9G_NHn4Xc_0000",
  "video_id": "-H9G_NHn4Xc",
  "start": 0.0,
  "end": 15.75,
  "is_gold_transcript": false,
  "flags": [],
  "attribution": {
    "title": "E-commerce instellen in Google Analytics 4",
    "uploader": "Altijd Bekend",
    "channel_url": "https://www.youtube.com/channel/UC0ILpCCSKhitmVEp9ykZKsg",
    "video_id": "-H9G_NHn4Xc"
  }
}
```

### Columns

The rows use the dataset format of [speechLMM-v2](https://github.com/Meetween/speechlmm-v2), a shared format for speech and
multimodal training data in which each row names its task and uses generic input, output, language
and quality columns. All splits have the same columns. The table lists the 31 columns used
in the `asr` split; all other columns of the format are null.

| Column | Type | Value in this dataset | Explanation |
|---|---|---|---|
| `sample_id` | string | `youtube_<clip_id>_<task>` | Unique ID of the row, also across splits |
| `task` | list of strings | `["asr"]` | Task of the row; the same as the Hugging Face split |
| `split` | string | `train` | Data split in the speechLMM format: all rows are training data. The Hugging Face split is the task (`asr`) |
| `source_dataset` | string | `youtube_clips_v1` | Name of the source corpus, used when corpora are combined |
| `license` | string | `CC-BY-4.0` | License of the row |
| `audio_input_path` | string | `audio/<lang>/<video_id>/<clip_id>.flac` | Relative path of the clip audio (16 kHz mono FLAC); the audio files are not part of this repository (see [Audio files](#audio-files)) |
| `audio_input_duration` | float64 | seconds, e.g. `15.75` | Duration of the clip |
| `audio_input_sample_rate` | int64 | `16000` | Sample rate in Hz of the clip audio from which the transcript was made |
| `audio_input_num_channels` | int64 | `1` | Number of audio channels (mono) |
| `audio_input_codec` | string | `flac` | Codec of the clip audio |
| `text_output` | string | transcript | Target text: the Whisper large-v3-turbo transcript of the clip, cased and punctuated |
| `text_output_normalized` | string | lower-cased transcript | `text_output` in lower case, with whitespace collapsed to single spaces; punctuation is kept |
| `num_words_output` | int64 | e.g. `37` | Number of words in `text_output` |
| `language_audio_input` | string | ISO 639-1 code or null | Language of the input audio, as metadata of the row. Set to the label predicted from the transcript (`lid_text_predicted`). Null if no language was identified (28,212 rows of `asr`, 0.4%), so that tools treat the language as unknown instead of as a language code |
| `language_text_output` | string | ISO 639-1 code or null | Language of `text_output`, as metadata of the row; same value as `language_audio_input`, and null in the same rows |
| `lid_audio_predicted` | string | ISO 639-1 code or null | Spoken language detected by Whisper large-v3-turbo from the audio of the source video (first 30 seconds of speech); one value per video, not per clip. Null for the videos of the first processing batch, which were transcribed with the language set in advance, so no detection was made (2,819,246 rows, 43.7%) |
| `language_confidence_audio` | float64 | 0 to 1 or null | Probability of `lid_audio_predicted` given by Whisper |
| `lid_text_predicted` | string | ISO 639-1 code or `und` | Output of the language classifier (fastText `lid.176`) on the transcript. Unlike the two columns above, it records the classifier result and is never null: `und` (ISO 639-2 code for "undetermined") means that the classifier ran but identified no language. These rows also have the flag `lang_und` |
| `language_confidence_text` | float64 | 0 to 1 | Confidence of `lid_text_predicted` |
| `words_per_second` | float64 | e.g. `2.35` | Speaking rate: `num_words_output` divided by `audio_input_duration` |
| `chars_per_second` | float64 | e.g. `13.8` | Characters of `text_output` per second of audio |
| `repetition_score` | float64 | 0 to 1 | Share of repeated word 3-grams in `text_output_normalized`: 1 − distinct 3-grams / all 3-grams (character 3-grams for Japanese and other languages written without spaces; 0 for texts of 3 tokens or fewer). High values indicate a repetition loop of the speech recognition model; 13,370 rows have a score above 0.5 |
| `text_duplicate_score` | float64 | `0.0` or `1.0` | `1.0` if another row with a smaller `clip_id` has the same `text_output_normalized` (123,799 rows), otherwise `0.0` |
| `text_duplicate_of` | string | `clip_id` or null | For rows with `text_duplicate_score` 1.0, the `clip_id` of the first row (smallest `clip_id`) with the same text; null otherwise |
| `clip_id` | string | `<video_id>_<index>` | ID of the clip; the index is the position of the clip in its video, from 0. Rows of all splits built on the same clip use the same `clip_id` |
| `video_id` | string | YouTube video ID | Source video: `https://www.youtube.com/watch?v=<video_id>` |
| `start` | float64 | seconds | Start of the clip in the source video |
| `end` | float64 | seconds | End of the clip in the source video |
| `is_gold_transcript` | bool | `false` | Whether the transcript is a human reference; `false` because the transcripts are model output |
| `flags` | list of strings | empty, `fallback_cut`, `lang_und` | Quality warnings. `fallback_cut`: no sentence ended within 30 seconds, so the clip ends at the longest pause instead of a sentence end. `lang_und`: the language of the transcript could not be identified |
| `attribution` | string (JSON) | `title`, `uploader`, `channel_url`, `video_id` | Title, channel name, channel URL and ID of the source video, for the attribution required by the CC BY license |

## Licensing and attribution

The dataset is released under the Creative Commons Attribution 4.0 license (`CC-BY-4.0`). Each
source video was published on YouTube under the Creative Commons Attribution license on
2026-10-15. When you use or redistribute the data, credit the authors of the source videos; the
`attribution` column gives the title, channel name and channel URL of each video.

Uploaders can change the license of a video or remove it after the check. The license status
refers to the date of the check.
