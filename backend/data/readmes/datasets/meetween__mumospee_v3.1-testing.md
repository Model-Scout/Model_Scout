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
annotations_creators:
- machine-generated
language_creators:
- found
multilinguality:
- multilingual
source_datasets:
- original
size_categories:
- 1M<n<10M
pretty_name: Mumospee V3
tags:
- speech
- youtube
- whisper
- creative-commons
configs:
- config_name: "asr"
  default: true
  data_files:
  - split: train
    path: data/asr/*/*.parquet
---

# Mumospee V3: A MUltiMOdal SPEEch Corpus

The Mumospee dataset supports the aim of the [Meetween](https://meetween.eu/) project: inclusive,
language-neutral collaboration in virtual environments.

**Mumospee V3** is derived from [Mumospee V2](https://huggingface.co/datasets/meetween/mumospee_V2). It contains real speech
recordings with machine-generated annotations, which are used to train multimodal large language
models on different downstream tasks: ASR, SQA, SUM, CHAT, ST, LIGEN and LIPREAD. Each task has its
own subset. This release contains only the ASR subset. Later releases will add the subsets of the
other tasks.

Earlier versions: [Mumospee V1](https://huggingface.co/datasets/meetween/mumospee) and [Mumospee V2](https://huggingface.co/datasets/meetween/mumospee_V2).

The [Mumospee V3 overview](#mumospee-v3-overview) gives the information that applies to all
subsets. After it, each task has its own section with the information that applies only to its
subset.

## Mumospee V3 overview

| Task | Description | Subset | Status | Rows | Columns |
|---|---|---|---|---:|---|
| ASR | Automatic speech recognition | `asr` | available ([details](#asr)) | 6,448,108 | 22 (10 common + 12 task) |
| SQA | Spoken question answering | – | planned | – | – |
| SUM | Summarization | – | planned | – | – |
| CHAT | – | – | planned | – | – |
| ST | Speech translation | – | planned | – | – |
| LIGEN | – | – | planned | – | – |
| LIPREAD | Lip reading | – | planned | – | – |

All subsets have the same structure:

- **Clips.** The subsets use the same set of clips. Each row of a clip subset refers to one clip
  through `clip_id`. You can join the rows of different tasks on the same clip.
- **No media.** This repository does not contain audio or video files. It contains the text data and
  the metadata. `audio_input_path` gives the relative path of the audio file of each clip (refer to
  [Audio files](#audio-files)).
- **Columns.** The column names and types come from the dataset format of
  [speechLMM-v2](https://github.com/Meetween/speechlmm-v2), a shared format for speech and multimodal training data. The
  schema of this dataset is not the same as the speechLMM-v2 schema. Each subset contains only the
  [common columns](#common-columns) and the columns of its task. The speechLMM-v2 schema has more
  columns, and it also keeps the values that are the same in all rows.
- **Values that are not in columns.** Some values are the same in all rows. The subsets do not keep
  them in columns:
  - The clip audio is 16 kHz, mono, FLAC.
  - The targets are model output, not human references.
  - All rows are training data (split `train`).
- **Adaptation to speechLMM-v2.** speechLMM-v2 has a script that converts a subset to the
  speechLMM-v2 schema: the `mumospee_v3` corpus module
  (`src/speechlmm/data/processing/mumospee_v3/`). The script adds the missing columns and their
  values, and extracts the clip audio.

### Data source

The clips come from the YouTube collection of [Mumospee V2](https://huggingface.co/datasets/meetween/mumospee_V2). All videos in this
collection had the Creative Commons Attribution license. 33,275 of the 46,373 videos
(71.8%) are in the `youtube_meeting` split of Mumospee V2. The other videos are in the
same collection, but not in that split.

The collection has 155,029 videos with a video file and a caption track. We selected
56,503 of these videos (36.4%) for processing:

- all videos in languages other than English;
- a sample of English videos, approximately 8,000 hours.

A fixed random seed selected the English sample. The sample is divided equally across six
video-length ranges: less than 2, 2–5, 5–15, 15–30, 30–60 and more than 60 minutes. The sample size
applies to the videos with the crawl label English. The English folder has more hours, because it
also contains videos that are in English but have a different crawl label (mostly Hindi). The
language distribution of the clips is a result of this selection. It is not the distribution of
languages on YouTube.

### Clip construction

1. **Audio.** We decoded the audio track of each video to 16 kHz mono. We did not use the video
   frames.
2. **Transcription.** Whisper large-v3-turbo transcribed the audio (faster-whisper implementation,
   batched inference, voice activity detection). The output is text with upper and lower case and
   punctuation, and a start time and an end time for each word. In the first processing batch, we
   set the language to the crawl label of the video. In the second batch, Whisper detected the
   language from the audio. The transcripts are the targets of the [ASR subset](#asr).
3. **Segmentation.** We cut the clips between words. A clip ends at the first sentence end after 12
   seconds. If no sentence ends between 12 and 30 seconds, the clip ends at the last sentence end
   between 3 and 12 seconds. If there is no such sentence end, the clip ends at the longest pause
   between words. The last clip of a video ends where the speech ends; this end can be without a
   sentence end. The ASR subset marks the clips that do not end at a sentence end with the flag
   `fallback_cut`. We added 0.15 s of padding before and after each clip.
4. **Quality filter.** The filter rejected a full video if its output showed that the transcription
   failed. These are the rejection conditions:
   - degenerate clip lengths: a median of less than 2 s, or more than 30% of clips shorter than 1.5 s;
   - less than 40% of clips end with sentence punctuation;
   - the source file cannot be decoded;
   - the video gave no clips.
5. **Deduplication.** Some videos were selected for more than one crawl language. We kept one copy of
   these videos.

The rejection log of the quality filter has 9,670 entries:

- 6,373 for degenerate output;
- 3,016 for few sentence ends;
- 181 for an unreadable source file;
- 100 for videos without clips.

7,399 of the entries are for videos with the crawl label Hindi.

Of the 56,503 selected videos, 9,302 gave no clips, and 47,201
videos gave clips. The [license check](#license-check) removed 828 of these videos.
Mumospee V3 contains the clips of 46,373 videos.

### Clips by language

The folder language is the language of the video. We found it from the language labels of the
transcripts of its clips. Some clips can be in a different language (code-switching). The folder `data/<subset>/<lang>/` contains
the clips of the videos in that language. The last column gives the percentage of clips that end at
a pause, not at a sentence end.

| Language | Folder | Clips | Videos | Hours | Clips that end at a pause |
|---|---|---:|---:|---:|---:|
| Spanish (`es`) | `es` | 1,821,626 | 11,319 | 8,675.6 | 4.1% |
| English (`en`) | `en` | 1,902,083 | 16,778 | 8,537.1 | 20.5% |
| French (`fr`) | `fr` | 1,091,144 | 7,465 | 5,019.6 | 2.2% |
| Russian (`ru`) | `ru` | 449,162 | 2,993 | 2,027.0 | 3.3% |
| Portuguese (`pt`) | `pt` | 431,715 | 2,411 | 2,021.8 | 2.0% |
| German (`de`) | `de` | 259,535 | 1,921 | 1,193.7 | 1.7% |
| Italian (`it`) | `it` | 194,942 | 1,332 | 972.9 | 13.3% |
| Indonesian (`id`) | `id` | 121,149 | 619 | 531.6 | 10.8% |
| Dutch (`nl`) | `nl` | 76,344 | 609 | 323.4 | 0.7% |
| Ukrainian (`uk`) | `uk` | 17,296 | 96 | 82.1 | 4.7% |
| Swedish (`sv`) | `sv` | 15,552 | 113 | 67.6 | 0.7% |
| Korean (`ko`) | `ko` | 12,791 | 139 | 60.1 | 13.6% |
| Turkish (`tr`) | `tr` | 11,933 | 82 | 52.9 | 2.9% |
| Hindi (`hi`) | `hi` | 7,535 | 168 | 30.8 | 48.0% |
| Vietnamese (`vi`) | `vi` | 5,643 | 69 | 24.4 | 21.2% |
| Norwegian (`no`) | `no` | 3,918 | 23 | 18.0 | 0.6% |
| Arabic (`ar`) | `ar` | 4,192 | 26 | 16.9 | 38.8% |
| Catalan (`ca`) | `ca` | 2,936 | 24 | 13.9 | 2.2% |
| Polish (`pl`) | `pl` | 2,350 | 23 | 11.2 | 1.8% |
| Hebrew (`he`) | `he` | 2,299 | 31 | 10.7 | 17.3% |
| Greek (`el`) | `el` | 2,859 | 15 | 9.9 | 38.5% |
| Japanese (`ja`) | `ja` | 1,978 | 31 | 8.9 | 48.0% |
| Kazakh (`kk`) | `kk` | 1,753 | 9 | 7.4 | 18.5% |
| Czech (`cs`) | `cs` | 1,585 | 13 | 7.3 | 9.5% |
| Finnish (`fi`) | `fi` | 1,497 | 8 | 7.0 | 2.6% |
| Tagalog (`tl`) | `tl` | 1,618 | 12 | 6.7 | 3.6% |
| Galician (`gl`) | `gl` | 610 | 6 | 2.9 | 9.2% |
| Serbian (`sr`) | `sr` | 533 | 3 | 2.5 | 0.9% |
| Malay (`ms`) | `ms` | 290 | 2 | 1.4 | 2.8% |
| Bulgarian (`bg`) | `bg` | 254 | 7 | 1.2 | 5.1% |
| Azerbaijani (`az`) | `az` | 200 | 4 | 0.9 | 16.0% |
| Danish (`da`) | `da` | 170 | 5 | 0.8 | 0.6% |
| Hungarian (`hu`) | `hu` | 106 | 2 | 0.5 | 0.0% |
| Slovak (`sk`) | `sk` | 143 | 1 | 0.5 | 21.7% |
| Slovenian (`sl`) | `sl` | 73 | 1 | 0.3 | 8.2% |
| Tamil (`ta`) | `ta` | 70 | 2 | 0.3 | 14.3% |
| Swahili (`sw`) | `sw` | 62 | 3 | 0.3 | 0.0% |
| Urdu (`ur`) | `ur` | 53 | 2 | 0.2 | 47.2% |
| Welsh (`cy`) | `cy` | 46 | 2 | 0.2 | 19.6% |
| Estonian (`et`) | `et` | 25 | 1 | 0.1 | 0.0% |
| Romanian (`ro`) | `ro` | 15 | 1 | 0.1 | 0.0% |
| Gujarati (`gu`) | `gu` | 11 | 1 | 0.1 | 54.5% |
| Marathi (`mr`) | `mr` | 12 | 1 | 0.1 | 41.7% |
| all languages | all | 6,448,108 | 46,373 | 29,751.0 | 8.8% |

### Clip statistics

| Measure | Value | Percentage of clips |
|---|---:|---:|
| Clips | 6,448,108 |  |
| Total audio duration | 29,751.0 h |  |
| Average clip duration | 16.6 s |  |
| Source videos | 46,373 |  |
| Languages | 43 |  |
| Clips that end at a pause, not at a sentence end | 569,035 | 8.8% |
| Clips shorter than 3 s | 156,927 | 2.4% |
| Longest clip | 30.3 s |  |
| Clips with no audio language (`lid_audio_predicted` is null; first processing batch) | 2,819,246 | 43.7% |

Most clips shorter than 3 s are the last clip of a video or clips that end at a pause.

### Notes for use

- **Split by video.** Clips of the same video have the same speakers and recording conditions. Split
  the training, development and test data by `video_id`, not by clip.
- **Join subsets on `clip_id`.** The rows of different subsets for the same clip have the same
  `clip_id`.
- **Record the revision.** Later releases will add subsets and videos. Record the revision (commit)
  of this repository that you use in each experiment (refer to [Changelog](#changelog)).

The section of each task has more notes for its subset.

### Data structure

The path of the files is `data/<subset>/<lang>/train-NNNNN-of-MMMMM.parquet`. Each subset is one
configuration with the split `train`. Each language has its own folder. To load only one language,
select the files in its folder.

Each subset has the common columns and the columns of its task. The section of each task gives the
columns of its task (for ASR, refer to [ASR columns](#asr-columns)).

#### Common columns

The common columns describe the clip. They have the same values in all subsets that contain the clip.

| Column | Type | Value in this dataset | Explanation |
|---|---|---|---|
| `clip_id` | string | `<video_id>_<index>` | ID of the clip. The index is the position of the clip in its video; the first clip has the index 0. Rows of all subsets that use the same clip have the same `clip_id` |
| `video_id` | string | YouTube video ID | Source video: `https://www.youtube.com/watch?v=<video_id>` |
| `start` | float64 | seconds | Start time of the clip in the source video |
| `end` | float64 | seconds | End time of the clip in the source video |
| `audio_input_path` | string | `audio/<lang>/<video_id>/<clip_id>.flac` | Relative path of the clip audio (16 kHz, mono, FLAC). This repository does not contain the audio files (refer to [Audio files](#audio-files)) |
| `audio_input_duration` | float64 | seconds, for example `15.75` | Duration of the clip |
| `lid_audio_predicted` | string | ISO 639-1 code or null | Spoken language of the source video. Whisper large-v3-turbo detected it from the first 30 seconds of speech. There is one value for each video, not for each clip. The value is null for the videos of the first processing batch (2,819,246 rows, 43.7%). For these videos, Whisper used the crawl label of the video as the language and did not detect the language. Some crawl labels are wrong (refer to [Known limitations](#known-limitations)) |
| `language_confidence_audio` | float64 | 0 to 1 or null | Probability of `lid_audio_predicted` from Whisper |
| `license` | string | `CC-BY-4.0` | License of the row |
| `attribution` | string | `title`, `uploader`, `channel_url`, `video_id` | JSON string with the title, channel name, channel URL and ID of the source video. The CC BY license makes this attribution necessary |

#### Example row

Common columns of a row. In the data, `attribution` is a JSON string. The example shows it as parsed
JSON. The section of each task gives the task columns of the same row.

```json
{
  "clip_id": "-H9G_NHn4Xc_0000",
  "video_id": "-H9G_NHn4Xc",
  "start": 0.0,
  "end": 15.75,
  "audio_input_path": "audio/nl/-H9G_NHn4Xc/-H9G_NHn4Xc_0000.flac",
  "audio_input_duration": 15.75,
  "lid_audio_predicted": "nl",
  "language_confidence_audio": 0.999,
  "license": "CC-BY-4.0",
  "attribution": {
    "title": "E-commerce instellen in Google Analytics 4",
    "uploader": "Altijd Bekend",
    "channel_url": "https://www.youtube.com/channel/UC0ILpCCSKhitmVEp9ykZKsg",
    "video_id": "-H9G_NHn4Xc"
  }
}
```

### Example usage

Set `subset` to the subset of the task (refer to the table in
[Mumospee V3 overview](#mumospee-v3-overview)).

```python
from datasets import load_dataset

subset = "asr"

# one subset, all languages, streamed
ds = load_dataset("meetween/mumospee_v3.1-testing", subset, split="train", streaming=True)

# one subset, one language: select the files of the language
ds = load_dataset("meetween/mumospee_v3.1-testing", data_files=f"data/{subset}/nl/*.parquet", split="train")
row = next(iter(ds))
print(row["clip_id"], row["video_id"], row["start"], row["end"])
```

The source video of a clip is `https://www.youtube.com/watch?v=<video_id>`. The clip is the interval
from `start` to `end` seconds.

### Audio files

`audio_input_path` is the relative path of the clip audio (16 kHz, mono, FLAC). This path is the same
in all clip subsets:

```text
audio/<lang>/<video_id>/<clip_id>.flac      for example audio/nl/-H9G_NHn4Xc/-H9G_NHn4Xc_0000.flac
```

`<lang>` is the language of the video. If `<root>` is the folder that contains `audio/`, the audio of
a row is at `<root>/<audio_input_path>`.

The script [`scripts/make_clips.py`](scripts/make_clips.py) cuts the clips from source videos that you
downloaded. It writes the clips at these paths. Refer to [`scripts/README.md`](scripts/README.md).

To get the audio, you must download the source videos from YouTube. The full dataset has 46,373
source videos. This is a large download. Some source videos will not be available in the future,
because uploaders can delete a video, make it private or change its license.

## ASR

Each row is one clip. The input is the clip audio. The target is the transcript of the clip
(`text_output`). Whisper large-v3-turbo made the transcripts. They have upper and lower case and
punctuation.

### ASR overview

The ASR subset has one row for each clip, so it covers all clips, videos and languages in
[Clips by language](#clips-by-language).

| Measure | Value | Percentage of clips |
|---|---:|---:|
| Rows (one for each clip) | 6,448,108 |  |
| Parquet files | 51 (at most 500,000 rows each) |  |
| Columns | 22 (10 common + 12 ASR) |  |
| Words in all transcripts | 260,298,599 |  |
| Average transcript length | 40.4 words |  |
| Clips with no identified transcript language (flag `lang_und`) | 28,212 | 0.4% |
| Clips with the same transcript as a different clip (`text_duplicate_score` 1.0) | 123,799 | 1.9% |
| Clips with a `repetition_score` of more than 0.5 | 13,370 | 0.2% |

### ASR notes for use

- **Evaluate on human transcripts.** The targets are the output of Whisper large-v3-turbo. A model
  that you train on them learns to give the same output as this model. Use test sets with human
  transcripts for evaluation.
- **Sentence-complete targets.** Clips with the flag `fallback_cut` (8.8%) can end in
  the middle of a sentence. If your targets must be complete sentences, remove these clips.
- **Per-clip language.** If your training uses the language, use the per-clip label
  (`lid_text_predicted`, `language_confidence_text`). Do not use the folder name. If the label of a
  clip is different from the folder language, the clip is code-switched or its label is incorrect.
- **Processing batch.** Rows with a null `lid_audio_predicted` are from the first processing batch.
  If the transcript must be in the spoken language, remove these rows.
- **Repeated text.** To remove repeated transcripts, use `text_duplicate_score` and
  `repetition_score`.

### ASR columns

The files of the ASR subset are in `data/asr/<lang>/`. Each row has the
[common columns](#common-columns) and these ASR columns:

| Column | Type | Value in this dataset | Explanation |
|---|---|---|---|
| `text_output` | string | transcript | Target text: the transcript of the clip from Whisper large-v3-turbo, with upper and lower case and punctuation |
| `text_output_normalized` | string | lower-case transcript | `text_output` in lower case. Each sequence of whitespace is changed to one space. The punctuation is not changed |
| `num_words_output` | int64 | for example `37` | Number of words in `text_output` |
| `language_text_output` | string | ISO 639-1 code or null | Language of `text_output`. The value is the label in `lid_text_predicted`. If the classifier identified no language, the value is null (28,212 rows, 0.4%); a null value tells tools that the language is unknown. In rows with a value in `lid_audio_predicted`, Whisper transcribed the audio in the detected spoken language. In these rows, this column normally also gives the language of the audio. In the other rows (first processing batch), Whisper transcribed the audio in the crawl language. The transcript language can be different from the spoken language, and this column cannot show the difference |
| `lid_text_predicted` | string | ISO 639-1 code or `und` | Output of the language classifier (fastText `lid.176`) on the transcript. The value is never null. `und` (ISO 639-2 code for "undetermined") tells that the classifier identified no language. These rows also have the flag `lang_und` |
| `language_confidence_text` | float64 | 0 to 1 | Confidence of `lid_text_predicted` |
| `words_per_second` | float64 | for example `2.35` | Speech rate: `num_words_output` divided by `audio_input_duration` |
| `chars_per_second` | float64 | for example `13.8` | Number of characters in `text_output` for each second of audio |
| `repetition_score` | float64 | 0 to 1 | Ratio of repeated word 3-grams in `text_output_normalized`: 1 − (different 3-grams / all 3-grams). For Japanese and other languages without spaces between words, the score uses character 3-grams. For texts with 3 tokens or fewer, the score is 0. A high value shows a repetition loop of the speech recognition model. 13,370 rows have a score of more than 0.5 |
| `text_duplicate_score` | float64 | `0.0` or `1.0` | `1.0` if a different row with a smaller `clip_id` has the same `text_output_normalized` (123,799 rows). If not, `0.0` |
| `text_duplicate_of` | string | `clip_id` or null | In rows with `text_duplicate_score` 1.0: the `clip_id` of the first row (smallest `clip_id`) with the same text. In other rows: null |
| `flags` | list of strings | empty, `fallback_cut`, `lang_und` | Quality warnings. `fallback_cut`: the clip does not end at a sentence end. No sentence ended between 3 and 30 seconds, so the clip ends at the longest pause; or the speech of the video ended without a sentence end. `lang_und`: the classifier did not identify the language of the transcript |

ASR columns of the [example row](#example-row). In this example, the transcript is shorter than in
the data.

```json
{
  "text_output": "In deze video laat ik zien hoe je GA4 e-commerce setting instelt aan de hand van Tag Manager. Je moet helaas zelf gebeurtenissen toevoegen. In dit voorbeeld mak ...",
  "text_output_normalized": "in deze video laat ik zien hoe je ga4 e-commerce setting instelt aan de hand van tag manager. je moet helaas zelf gebeurtenissen toevoegen. in dit voorbeeld mak ...",
  "num_words_output": 37,
  "language_text_output": "nl",
  "lid_text_predicted": "nl",
  "language_confidence_text": 0.988,
  "words_per_second": 2.3492063492063493,
  "chars_per_second": 13.841269841269842,
  "repetition_score": 0.0,
  "text_duplicate_score": 0.0,
  "text_duplicate_of": null,
  "flags": []
}
```

## Intended uses

Mumospee V3 is for the training of SpeechLLMs and other multimodal large language models. These
models support language-neutral applications for virtual meetings. [Notes for use](#notes-for-use)
applies to all subsets. The section of each task has more notes for its subset.

## Known limitations

- **Machine-generated targets.** The targets are model output (for ASR, Whisper large-v3-turbo). We
  did not compare them with human references. The word error rate is not known.
- **Language of the first processing batch.** For 2,819,246 clips (43.7%),
  Whisper used the crawl language label of the video and did not detect the spoken language
  (`lid_audio_predicted` is null). Some crawl labels are wrong, so the transcript language can be
  different from the spoken language.
- **Uneven language distribution.** The nine largest languages have 98.5% of the hours.
  23 of the 43 languages have less than 10 hours.
- **Partial release.** We did not process 98,526 English videos of the
  collection (approximately 63,800 hours). Later releases will add them, and
  the English share will increase.
- **Few non-Latin scripts.** The quality filter rejects videos in which few clips end with sentence
  punctuation. This removes most videos for which Whisper gives no punctuation.
- **Not included.** The clips have no speaker labels, and there is no development or test split. We
  did not check the clips for overlap with other YouTube corpora.

## Personal and sensitive information

The clips contain the voices of people who can be identified. The text data, for example the
transcripts, can contain names and other personal data from the videos. The `attribution` column
contains the channel name and channel URL of each video, because the CC BY license makes attribution
necessary.

We did not remove or anonymize personal data. A Creative Commons license on a video gives permissions
under copyright. It does not give the consent of the speakers to use their voices to train speech
models. When you use the data, obey the data protection law that applies to you.

## License

The dataset has the Creative Commons Attribution 4.0 license (`CC-BY-4.0`). The license applies to
all subsets. When you use or distribute the data, give credit to the authors of the source videos.
The `attribution` column gives the title, channel name and channel URL of each video.

### License check

On 2026-10-15, we checked the license of each source video with the YouTube Data API. On that date,
each source video in Mumospee V3 had the Creative Commons Attribution license on YouTube. The
processed data had 47,201 videos (6,546,994 clips). Mumospee V3 does not include
828 of these videos (98,886 clips):

- 203 videos had the standard YouTube license on that date.
- 625 videos were not available on that date.

Uploaders can change the license of a video or remove the video after the check. The license status
is the status on the date of the check.

## Changelog

### 2026-10-27

- First release of Mumospee V3. It contains the ASR subset: 6,448,108 clips from 46,373 videos in
  43 languages (29,751 hours).

Later releases will add the subsets of more tasks and the other English videos. Record the
revision (commit) of this repository that you use in each experiment. To load a revision, use
`load_dataset(..., revision="<commit>")`. This keeps your results comparable.

## Contact

For questions and removal requests, open a discussion in the Community tab of this repository.
