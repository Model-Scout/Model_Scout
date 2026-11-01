---
license: cc-by-nc-4.0
language:
- ar
- de
- en
- es
- fr
- hi
- id
- ja
- ko
- mr
- pt
- ru
- tr
- ur
- vi
- zh
pretty_name: "CROWS Multilingual: CRowdsourced Open World Speech in 16 Languages"
task_categories:
- automatic-speech-recognition
- audio-classification
size_categories:
- 100K<n<1M
tags:
- audio
- speech
- multilingual
- read-speech
- crowdsourced
- deepfake-audio-detection
- synthetic-speech-detection
- anti-spoofing
- asr
configs:
- config_name: all
  default: true
  data_files:
  - split: full
    path: data/*/*.parquet
- config_name: ar
  data_files:
  - split: full
    path: data/ar/*.parquet
- config_name: de
  data_files:
  - split: full
    path: data/de/*.parquet
- config_name: en
  data_files:
  - split: full
    path: data/en/*.parquet
- config_name: es
  data_files:
  - split: full
    path: data/es/*.parquet
- config_name: fr
  data_files:
  - split: full
    path: data/fr/*.parquet
- config_name: hi
  data_files:
  - split: full
    path: data/hi/*.parquet
- config_name: id
  data_files:
  - split: full
    path: data/id/*.parquet
- config_name: ja
  data_files:
  - split: full
    path: data/ja/*.parquet
- config_name: ko
  data_files:
  - split: full
    path: data/ko/*.parquet
- config_name: mr
  data_files:
  - split: full
    path: data/mr/*.parquet
- config_name: pt
  data_files:
  - split: full
    path: data/pt/*.parquet
- config_name: ru
  data_files:
  - split: full
    path: data/ru/*.parquet
- config_name: tr
  data_files:
  - split: full
    path: data/tr/*.parquet
- config_name: ur
  data_files:
  - split: full
    path: data/ur/*.parquet
- config_name: vi
  data_files:
  - split: full
    path: data/vi/*.parquet
- config_name: zh
  data_files:
  - split: full
    path: data/zh/*.parquet
- config_name: scripts
  data_files:
  - split: full
    path: scripts/scripts.parquet
- config_name: breadth_gt_6_all
  data_files:
  - split: full
    path: synthetic_risk/data_from_users_with_breadth_gt_6/*/*.parquet
- config_name: breadth_gt_6_ar
  data_files:
  - split: full
    path: synthetic_risk/data_from_users_with_breadth_gt_6/ar/*.parquet
- config_name: breadth_gt_6_de
  data_files:
  - split: full
    path: synthetic_risk/data_from_users_with_breadth_gt_6/de/*.parquet
- config_name: breadth_gt_6_en
  data_files:
  - split: full
    path: synthetic_risk/data_from_users_with_breadth_gt_6/en/*.parquet
- config_name: breadth_gt_6_es
  data_files:
  - split: full
    path: synthetic_risk/data_from_users_with_breadth_gt_6/es/*.parquet
- config_name: breadth_gt_6_fr
  data_files:
  - split: full
    path: synthetic_risk/data_from_users_with_breadth_gt_6/fr/*.parquet
- config_name: breadth_gt_6_hi
  data_files:
  - split: full
    path: synthetic_risk/data_from_users_with_breadth_gt_6/hi/*.parquet
- config_name: breadth_gt_6_id
  data_files:
  - split: full
    path: synthetic_risk/data_from_users_with_breadth_gt_6/id/*.parquet
- config_name: breadth_gt_6_ja
  data_files:
  - split: full
    path: synthetic_risk/data_from_users_with_breadth_gt_6/ja/*.parquet
- config_name: breadth_gt_6_ko
  data_files:
  - split: full
    path: synthetic_risk/data_from_users_with_breadth_gt_6/ko/*.parquet
- config_name: breadth_gt_6_mr
  data_files:
  - split: full
    path: synthetic_risk/data_from_users_with_breadth_gt_6/mr/*.parquet
- config_name: breadth_gt_6_pt
  data_files:
  - split: full
    path: synthetic_risk/data_from_users_with_breadth_gt_6/pt/*.parquet
- config_name: breadth_gt_6_ru
  data_files:
  - split: full
    path: synthetic_risk/data_from_users_with_breadth_gt_6/ru/*.parquet
- config_name: breadth_gt_6_tr
  data_files:
  - split: full
    path: synthetic_risk/data_from_users_with_breadth_gt_6/tr/*.parquet
- config_name: breadth_gt_6_ur
  data_files:
  - split: full
    path: synthetic_risk/data_from_users_with_breadth_gt_6/ur/*.parquet
- config_name: breadth_gt_6_vi
  data_files:
  - split: full
    path: synthetic_risk/data_from_users_with_breadth_gt_6/vi/*.parquet
- config_name: breadth_gt_6_zh
  data_files:
  - split: full
    path: synthetic_risk/data_from_users_with_breadth_gt_6/zh/*.parquet
- config_name: profiles
  data_files:
  - split: full
    path: profiles/profiles.parquet
- config_name: pred_synthetic_gt_0_3_all
  data_files:
  - split: full
    path: synthetic_risk/data_from_users_with_pred_synthetic_proportion_gt_0_3/*/*.parquet
- config_name: pred_synthetic_gt_0_3_ar
  data_files:
  - split: full
    path: synthetic_risk/data_from_users_with_pred_synthetic_proportion_gt_0_3/ar/*.parquet
- config_name: pred_synthetic_gt_0_3_de
  data_files:
  - split: full
    path: synthetic_risk/data_from_users_with_pred_synthetic_proportion_gt_0_3/de/*.parquet
- config_name: pred_synthetic_gt_0_3_en
  data_files:
  - split: full
    path: synthetic_risk/data_from_users_with_pred_synthetic_proportion_gt_0_3/en/*.parquet
- config_name: pred_synthetic_gt_0_3_es
  data_files:
  - split: full
    path: synthetic_risk/data_from_users_with_pred_synthetic_proportion_gt_0_3/es/*.parquet
- config_name: pred_synthetic_gt_0_3_fr
  data_files:
  - split: full
    path: synthetic_risk/data_from_users_with_pred_synthetic_proportion_gt_0_3/fr/*.parquet
- config_name: pred_synthetic_gt_0_3_hi
  data_files:
  - split: full
    path: synthetic_risk/data_from_users_with_pred_synthetic_proportion_gt_0_3/hi/*.parquet
- config_name: pred_synthetic_gt_0_3_id
  data_files:
  - split: full
    path: synthetic_risk/data_from_users_with_pred_synthetic_proportion_gt_0_3/id/*.parquet
- config_name: pred_synthetic_gt_0_3_ja
  data_files:
  - split: full
    path: synthetic_risk/data_from_users_with_pred_synthetic_proportion_gt_0_3/ja/*.parquet
- config_name: pred_synthetic_gt_0_3_ko
  data_files:
  - split: full
    path: synthetic_risk/data_from_users_with_pred_synthetic_proportion_gt_0_3/ko/*.parquet
- config_name: pred_synthetic_gt_0_3_mr
  data_files:
  - split: full
    path: synthetic_risk/data_from_users_with_pred_synthetic_proportion_gt_0_3/mr/*.parquet
- config_name: pred_synthetic_gt_0_3_pt
  data_files:
  - split: full
    path: synthetic_risk/data_from_users_with_pred_synthetic_proportion_gt_0_3/pt/*.parquet
- config_name: pred_synthetic_gt_0_3_ru
  data_files:
  - split: full
    path: synthetic_risk/data_from_users_with_pred_synthetic_proportion_gt_0_3/ru/*.parquet
- config_name: pred_synthetic_gt_0_3_tr
  data_files:
  - split: full
    path: synthetic_risk/data_from_users_with_pred_synthetic_proportion_gt_0_3/tr/*.parquet
- config_name: pred_synthetic_gt_0_3_ur
  data_files:
  - split: full
    path: synthetic_risk/data_from_users_with_pred_synthetic_proportion_gt_0_3/ur/*.parquet
- config_name: pred_synthetic_gt_0_3_vi
  data_files:
  - split: full
    path: synthetic_risk/data_from_users_with_pred_synthetic_proportion_gt_0_3/vi/*.parquet
- config_name: pred_synthetic_gt_0_3_zh
  data_files:
  - split: full
    path: synthetic_risk/data_from_users_with_pred_synthetic_proportion_gt_0_3/zh/*.parquet
---

# CROWS Multilingual: CRowdsourced Open World Speech in 16 Languages

Crowdsourced Open World Speech (CROWS) Multilingual is a speech corpus collected by Poseidon AI, Inc.
It contains **821,361 scripted read-speech recordings** from **46,298 speaker
profiles** across **16 languages**. Every recording comes with its reading
prompt, an automatic transcript, an English translation, and per-recording
quality and speaker-consistency scores. Recordings from contributors flagged
as likely synthetic-speech submitters are separated into their own partitions,
so you can use the data for multilingual ASR and for synthetic-speech
(deepfake) detection research.

[**Need a custom speech dataset? Talk to Poseidon →**](https://www.psdn.ai/contact?utm_source=huggingface&utm_medium=dataset_card&utm_campaign=crows-multilingual&utm_content=custom_datasets_top)

<table>
  <tbody>
    <tr><td>Corpus</td><td><strong>821,361 recordings</strong> · <strong>~939 GB</strong> of original WAV audio</td></tr>
    <tr><td>Languages</td><td>16: Arabic, German, English, Spanish, French, Hindi, Indonesian, Japanese, Korean, Marathi, Portuguese, Russian, Turkish, Urdu, Vietnamese, Mandarin Chinese</td></tr>
    <tr><td>Speakers</td><td>46,298 pseudonymous speaker profiles. 12,719 profiles recorded in more than one language.</td></tr>
    <tr><td>Speech type</td><td>Scripted, single-speaker read speech</td></tr>
    <tr><td>Prompts</td><td>51,885 unique reading prompts. Each non-English prompt includes an English back-translation and a link to its English source prompt.</td></tr>
    <tr><td>Transcripts</td><td>Automatic Whisper-large transcript plus an English translation for every recording</td></tr>
    <tr><td>Quality signals</td><td>Per-recording WER, CER, semantic similarity to the prompt, and speaker-consistency score</td></tr>
    <tr><td>Synthetic-risk partitions</td><td>8,897 recordings from contributors flagged as higher risk, kept separate from the main data</td></tr>
    <tr><td>Audio</td><td>Original WAV files, byte-for-byte (no resampling, normalization, or transcoding), available embedded in Parquet or as TAR archives</td></tr>
    <tr><td>Integrity</td><td>Every recording decode-checked; SHA-256 checksum for every WAV file and every published artifact (see <code>release_manifest.json</code>)</td></tr>
  </tbody>
</table>

## Main and Synthetic Risk Partitions

Main `data`, `archives`, `checksums`, and root `metadata.csv` contain **812,464 recordings**. The two disjoint risk partitions are in [synthetic_risk](synthetic_risk/README.md):

- [data_from_users_with_breadth_gt_6](synthetic_risk/data_from_users_with_breadth_gt_6/README.md): **2,260 recordings**, relocated from `suspect_data`, selected by `breadth_gt_6.csv`.
- [data_from_users_with_pred_synthetic_proportion_gt_0_3](synthetic_risk/data_from_users_with_pred_synthetic_proportion_gt_0_3/README.md): **6,637 recordings** from the **496 profiles** listed in `predicted_synthetic_proportion_users_gt_0_3.csv`, moved out of main data.

Each partition contains a global metadata CSV, per-language CSVs, Parquet audio, TAR WAVs and JSON sidecars, and original checksums. All metadata uses the same twelve columns; WAV filenames remain `<file_id>.wav`. Selection criteria flag risk rather than establish synthetic ground truth.

Use `breadth_gt_6_all` / `breadth_gt_6_<language>` and `pred_synthetic_gt_0_3_all` / `pred_synthetic_gt_0_3_<language>` configurations, each with the `full` split. Default `all` and language configurations contain main data only.

```python
from datasets import load_dataset
main = load_dataset("psdn-ai/CROWS-multilingual", "en", split="full", streaming=True)
breadth = load_dataset("psdn-ai/CROWS-multilingual", "breadth_gt_6_en", split="full", streaming=True)
proportion = load_dataset("psdn-ai/CROWS-multilingual", "pred_synthetic_gt_0_3_en", split="full", streaming=True)
```

## Files and viewer

- `metadata.csv` is the main recording index, with exactly twelve columns.
- `archives/<language>/full-XXXXX.tar` contains original WAVs named exactly
  `<file_id>.wav` at the archive root and `<file_id>.json` metadata sidecars.
- `data/<language>/full-XXXXX.parquet` embeds the same original WAV bytes with
  an `audio` column first, followed by the twelve metadata columns for playback and filtering.
- `checksums/<language>/full-XXXXX.jsonl` records the SHA-256, byte count,
  sample rate, channel count, and frame count of each WAV.
- `release_manifest.json` records final counts and artifact checksums.

The TAR and Parquet representations contain the same recordings. Download
only the representation you need. No resampling, normalization, or transcoding
is applied when packaging the original WAV files.

Use the dataset viewer's configuration dropdown to select a language, or `all`
for the combined release. Metadata columns expose language, user ID, script ID,
and file ID alongside playable audio. The CSV is a standalone index; it is not
an AudioFolder loader for the contents of the TAR archives.

## Script prompts

**[Browse prompts by language](scripts/README.md#browse-and-download)** · **[Open the scripts viewer](https://huggingface.co/datasets/psdn-ai/CROWS-multilingual/viewer/scripts/full)** · **[Loading examples](scripts/README.md#parse-the-prompts)**

Readable pages show every prompt with its back translation and linked English content. Language-specific JSONL downloads make it easy to parse one prompt per line.

`scripts/scripts.csv` provides 51,885 unique prompts for every `prompt_id` in
the audio metadata. Join audio `prompt_id` to prompt `prompt_id`. The `scripts`
viewer configuration uses an identical Parquet copy and shows prompt content, its back translation, and the
linked English prompt ID and content. See [`scripts/README.md`](scripts/README.md)
for the exact database field mapping and handling of missing links.

## Metadata schema

Release v1.8 refreshes `semantic_score` from `files.semantic_score_std_v3` as exported on October 15, 2026. All 821,361 records matched; 811,154 scores changed and none are missing. In every audio viewer configuration, `audio` is the first column, followed by the twelve metadata fields. CSVs and TAR JSON sidecars retain their twelve-field metadata schema. See [refresh report](semantic_score_refresh_report.json).

In release v1.5, `user_id` was renamed to `profile_id` with values unchanged, and `expected_language` was removed from audio metadata.

All main and synthetic risk audio CSVs, Parquet rows, and TAR JSON sidecars use the
same twelve metadata fields. Parquet additionally contains the `audio`
feature. `script_id` has been renamed to `prompt_id`; its values are unchanged.

| Column | Parquet type | Source / meaning |
|---|---|---|
| `file_name` | string | Bare WAV filename, `<file_id>.wav` |
| `profile_id` | string | Preserved user identifier from the source filename |
| `language` | string | Preserved language code from the source filename |
| `prompt_id` | string | Former `script_id`; joins to the shared prompt table's `prompt_id` |
| `file_id` | string | Recording identifier; joins to `files.id` and embedding-table `file_id` |
| `anchor_cos_similarity` | float64, nullable | `speechbrain_spkrec_ecapa_voxceleb_embeddings_v2.anchor_similarity` |
| `duration` | float64 | `files.duration`, copied as stored |
| `whisper_large_hypothesis_transcript` | string | `files.spoken_native` |
| `english_translated_hypothesis_transcript` | string | `files.spoken_english` |
| `wer` | float64 | `files.wer_std_v3` |
| `cer` | float64 | `files.cer_std_v3` |
| `semantic_score` | float64 | `files.semantic_score_std_v3` |

```csv
file_name,profile_id,language,prompt_id,file_id,anchor_cos_similarity,duration,whisper_large_hypothesis_transcript,english_translated_hypothesis_transcript,wer,cer,semantic_score
```

Fields were joined by the exact recording IDs selected by `passing_files.csv`.
All 821,361 recordings match `files`; 1,592 have no embedding-table row, so their
`anchor_cos_similarity` is null. All other requested fields are populated.

Numeric values retain the source scale and units. No scores are recomputed.
CSV represents missing values as empty cells;
Parquet retains native nullable numeric and text types. Transcript
text is preserved, including commas, quotes, Unicode, and line breaks. Parse
CSV with a CSV reader rather than splitting on commas or physical lines.

See [`metadata_enrichment_report.json`](metadata_enrichment_report.json) for
coverage and source mappings. WAV filenames and original audio bytes remain
unchanged across all three partitions.

## Language counts

Counts below include main and both synthetic risk partitions. Their individual counts
are recorded in `release_manifest.json` and the synthetic risk folder indexes.

| Code | Language | Recordings |
|---|---|---:|
| ar | Arabic | 14,236 |
| de | German | 18,444 |
| en | English | 252,289 |
| es | Spanish | 41,704 |
| fr | French | 16,992 |
| hi | Hindi | 27,132 |
| id | Indonesian | 177,867 |
| ja | Japanese | 1,274 |
| ko | Korean | 21,009 |
| mr | Marathi | 265 |
| pt | Portuguese | 21,540 |
| ru | Russian | 69,849 |
| tr | Turkish | 10,599 |
| ur | Urdu | 38,250 |
| vi | Vietnamese | 84,752 |
| zh | Mandarin Chinese | 25,159 |

| **Total** | | **821,361** |

## Loading

```python
from datasets import load_dataset, Audio

# Select a language; use "all" for the complete dataset.
ds = load_dataset("psdn-ai/CROWS-multilingual", "en",
                  split="full", streaming=True)

# Inspect metadata and retrieve the original WAV bytes without decoding.
ds = ds.cast_column("audio", Audio(decode=False))
row = next(iter(ds))
print(row["profile_id"], row["language"], row["prompt_id"])
assert row["audio"]["path"] == row["file_name"]

# Filter by any exposed metadata column.
selected = ds.filter(lambda row: row["prompt_id"] == "YOUR_SCRIPT_ID")
```

Use a dataset commit hash in `revision=` to reproduce an exact release.
Streaming filters scan records; they do not imply an indexed random-access lookup.
Audio decoding dependencies depend on the installed Hugging Face Datasets version.

## Selection, validation, and splits

Every included recording corresponds to one unique ID in the supplied
`passing_files.csv`; that inclusion list defines this release's selection.
Metadata is parsed from source filenames of the form
`<profile_id>_<language>.<prompt_id>_<file_id>_<source_format>`.

Packaging checks the S3 object version via its ETag, preserves its bytes,
decodes every recording to check readability, validates archive member names
and Parquet row counts, and records checksums. This validates packaging and
readability, not the research labels or the selection criteria themselves.

The `full` split contains the complete release. This upload does not create
experimental train/validation/test splits or add authenticity labels. Users
should account for shared users, scripts, and related recordings when designing
and reporting evaluation splits.

### About Poseidon

Poseidon builds the training data for physical AI. Machines learn physical
skill the way apprentices always have, by watching skilled people work, and
that footage has to be created on purpose and to specification. Poseidon runs
that supply chain: it recruits skilled people and real workplaces around the
world, records their work to exact lab specifications, and refines the footage
into model-ready datasets.

## Research context and limitations

This release supports the publisher's multilingual audio research release.
The metadata supplied for this upload does not include paper bibliographic
information, detailed collection methodology, transcripts, authenticity labels,
or numerical quality/spam scores. Consult the associated research documentation
for those details; they are not inferred from filenames.

## License, Access and Attribution

The dataset is licensed under **Creative Commons Attribution-NonCommercial
4.0 International (CC BY-NC 4.0)**. See `LICENSE` and the
[official license](https://creativecommons.org/licenses/by-nc/4.0/).

When using this release, credit psdn-ai and link to
[CROWS Multilingual](https://huggingface.co/datasets/psdn-ai/CROWS-multilingual),
identify the revision used, and indicate changes as required by the license.

[**Not what you're looking for? Request a custom dataset**](https://www.psdn.ai/contact?utm_source=huggingface&utm_medium=dataset_card&utm_campaign=crows-multilingual&utm_content=custom_datasets)

## Citation

If you use this dataset, please cite:

```bibtex
@misc{poseidonai2026crowsmultilingual,
  title        = {{CROWS Multilingual}},
  author       = {{Poseidon AI, Inc.}},
  year         = {2026},
  version      = {1.8},
  publisher    = {Hugging Face},
  url          = {https://huggingface.co/datasets/psdn-ai/CROWS-multilingual},
  howpublished = {\url{https://huggingface.co/datasets/psdn-ai/CROWS-multilingual}}
}
```

## Profiles

The [profiles folder](profiles/README.md) provides 46,298 profiles with predicted synthetic submission proportions and distinct passing-language counts. Browse the `profiles` dataset configuration or download the three-column CSV, Parquet, or JSONL. Join audio metadata and profiles on `profile_id`. Reading pages are grouped by language count.
