---
task_categories:
- text-to-speech
- automatic-speech-recognition
language:
- ar
- de
- en
- es
- fr
- hi
- id
- it
- ja
- ko
- nl
- pl
- pt
- ru
- tr
- vi
- zh
size_categories:
- 1M<n<10M
tags:
- speech-synthesis
- voice-cloning
- dubbing
- cross-lingual
- expressive-tts
configs:
- config_name: ambient_v3
  data_files:
  - split: train
    path: ambient_v3/train-*
- config_name: one_speaker
  data_files:
  - split: train
    path: data/train-*.parquet
- config_name: music_sfx_step2
  data_files:
  - split: train
    path: music_sfx_step2/train-*.parquet
- config_name: dynamic_sfx_step2
  data_files:
  - split: train
    path: dynamic_sfx_step2/train-*.parquet
- config_name: ambient_v4
  data_files:
  - split: train
    path: ambient_v4/train-*.parquet
- config_name: dynamic_sfx_step3
  data_files:
  - split: train
    path: dynamic_sfx_step3/train-*.parquet
- config_name: music_sfx_step3
  data_files:
  - split: train
    path: music_sfx_step3/train-*.parquet
- config_name: wavcaps_bg
  data_files:
  - split: train
    path: wavcaps_bg/train-*.parquet
- config_name: multispeaker
  data_files:
  - split: train
    path: multispeaker/train-*.parquet
---

# translation_dataset

Synthetic, expressive, multilingual speech for **cross-lingual dubbing** research.
Each example pairs a style-annotated text with generated audio that clones an English
reference voice: **the voice stays the same, the language changes**.

- ~1.9M examples in the `one_speaker` config
- 17 languages
- ~900 distinct reference speakers

## Samples

Each sample shows the generated audio followed by the English reference voice that
conditioned it.

### English (`en`)

<audio controls src="https://huggingface.co/datasets/mlinmg/translation_dataset/resolve/main/samples/en.mp3"></audio>
<audio controls src="https://huggingface.co/datasets/mlinmg/translation_dataset/resolve/main/samples/en_reference.flac"></audio>

### Italian (`it`)

<audio controls src="https://huggingface.co/datasets/mlinmg/translation_dataset/resolve/main/samples/it.mp3"></audio>
<audio controls src="https://huggingface.co/datasets/mlinmg/translation_dataset/resolve/main/samples/it_reference.flac"></audio>

### Russian (`ru`)

<audio controls src="https://huggingface.co/datasets/mlinmg/translation_dataset/resolve/main/samples/ru.mp3"></audio>
<audio controls src="https://huggingface.co/datasets/mlinmg/translation_dataset/resolve/main/samples/ru_reference.flac"></audio>

### Arabic (`ar`)

<audio controls src="https://huggingface.co/datasets/mlinmg/translation_dataset/resolve/main/samples/ar.mp3"></audio>
<audio controls src="https://huggingface.co/datasets/mlinmg/translation_dataset/resolve/main/samples/ar_reference.flac"></audio>

### Chinese (`zh`)

<audio controls src="https://huggingface.co/datasets/mlinmg/translation_dataset/resolve/main/samples/zh.mp3"></audio>
<audio controls src="https://huggingface.co/datasets/mlinmg/translation_dataset/resolve/main/samples/zh_reference.flac"></audio>

### Japanese (`ja`)

<audio controls src="https://huggingface.co/datasets/mlinmg/translation_dataset/resolve/main/samples/ja.mp3"></audio>
<audio controls src="https://huggingface.co/datasets/mlinmg/translation_dataset/resolve/main/samples/ja_reference.flac"></audio>

### Korean (`ko`)

<audio controls src="https://huggingface.co/datasets/mlinmg/translation_dataset/resolve/main/samples/ko.mp3"></audio>
<audio controls src="https://huggingface.co/datasets/mlinmg/translation_dataset/resolve/main/samples/ko_reference.flac"></audio>

### Hindi (`hi`)

<audio controls src="https://huggingface.co/datasets/mlinmg/translation_dataset/resolve/main/samples/hi.mp3"></audio>
<audio controls src="https://huggingface.co/datasets/mlinmg/translation_dataset/resolve/main/samples/hi_reference.flac"></audio>

## Configs

All nine subsets below are registered as loadable configurations with a `train` split.

| Config | Content | Parquet files |
|---|---|---:|
| `one_speaker` | Single-speaker synthetic speech with reference audio and text | 1,913 |
| `multispeaker` | Multispeaker synthetic speech with reference audio and text | 537 |
| `ambient_v3` | Ambient-background audio with transcription, prompt and profile | 241 |
| `ambient_v4` | Regenerated ambient backgrounds; generation is currently stopped | 358 |
| `music_sfx_step2` | Multispeaker scenes with separate voice, music, SFX, background and mixed audio | 1,053 |
| `dynamic_sfx_step2` | Multispeaker scenes with dynamic SFX and separate audio stems | 1,052 |
| `music_sfx_step3` | Available Step 2 music scenes with regenerated backgrounds | 80 |
| `dynamic_sfx_step3` | Available Step 2 dynamic-SFX scenes with regenerated backgrounds | 54 |
| `wavcaps_bg` | Recorded BBC + Freesound backgrounds in one tagged table, including crowd/babble | 216 |

File counts reflect the repository snapshot inspected on 2026-09-26; they are not
row counts. Some generation runs were stopped before exhausting their source data,
so Step 3 and ambient_v4 should not be assumed to cover all rows in earlier versions.
WavCaps publication is complete: 33,409 recordings, approximately 1,959 hours.

### Load any subset

```python
from datasets import load_dataset

ds = load_dataset(
    "mlinmg/translation_dataset", "multispeaker", split="train", streaming=True
)
# Replace "multispeaker" with any config name in the table above.
```

### Multispeaker and background fields

`multispeaker` contains `id` (string), `language`, `transcription`, `references`
(a list of reference audio bytes and text), and `generated_audio` (bytes/path).
The original `one_speaker` IDs are integers; do not assume all configs share an ID type.

The four `music_sfx_step2/3` and `dynamic_sfx_step2/3` configs additionally contain
`duration_seconds`, `n_speakers`, `bg_prompt`, `bg_profile`, and separate
`generated_audio`, `sfx_audio`, `music_audio`, `bg_audio`, `mixed_audio` columns.
Their references also retain `speaker_id`, `source`, `revision`, and `sha256`.

`ambient_v3` and `ambient_v4` contain `id`, `language`, `transcription`, `bg_prompt`,
`bg_profile`, and `bg_audio`. They do not expose the separate multispeaker stems.
`wavcaps_bg` has a distinct schema with `source`, `tags`, `caption`, and provenance;
see its dedicated section below. Schemas are declared in the YAML `dataset_info`.

## Structure (`one_speaker`)

| field | type | description |
|---|---|---|
| `id` | `int` | utterance ID; the same `id` appears once per language, linking parallel translations |
| `language` | `string` | ISO 639-1 code |
| `transcription` | `string` | text with inline style directives |
| `references` | `list<struct>` | reference voices, `{audio, text}` |
| `generated_audio` | `Audio` | synthesized speech |

Background configs add fields such as `bg_prompt`, `bg_profile`, `bg_audio`, and, for
multi-speaker configs, separate `sfx_audio`, `music_audio` and `mixed_audio` stems.

### Style directives

Transcriptions contain bracketed prosodic cues that are meant to be performed, not read:

```
[inhale] So, the detective... [soft voice] just looked at the file
[long pause] and then he [gasp] he said it. [angry] It w-w-wasn't a robbery.
[shouting] It was an ambush!!!
```

Stuttering, syllabic emphasis and repeated punctuation are also used as intensity cues.
These cues are requests to the synthesizer and are not verified perceptual annotations.

## Loading

```python
from datasets import load_dataset

ds = load_dataset("mlinmg/translation_dataset", "one_speaker", split="train", streaming=True)
ex = next(iter(ds))
```

The dataset is several hundred GB; streaming is recommended.

## Limitations

- **Synthetic configs:** their audio is synthetic and should not be treated as recorded human speech. `wavcaps_bg` contains recorded-source assets; see its section below.
- **English-only reference voices**, so target-language accents may be influenced by
  the source timbre.
- Intelligibility, speaker fidelity and background quality have not been exhaustively
  validated. Synthesis artifacts may be present.
- **License to be determined.**



## Recorded WavCaps backgrounds (`wavcaps_bg`)

One combined train table containing BBC and Freesound background candidates from
`cvssp/WavCaps` at revision `0930ec11ded28fa0eaa910fde2f6fc3538acbeac`.
These are recorded-source assets, distinct from the synthetic configs above.
Publication is complete; `wavcaps_bg/PUBLICATION_COMPLETE.json` records the verified shards.

`bg_audio` contains the original encoded audio, with no resampling or normalization.
`id` is prefixed by source; `source` is `bbc` or `freesound`. Full source metadata
and original IDs are retained in `source_metadata_json`. `duration` is measured in
seconds; `sha256` hashes the original encoded audio; `source_revision` pins provenance.

Filter using the list-valued `tags` column: `nature`, `urban`, `indoor_mechanical`,
`crowd` (including chatter/babble), `ambience`, and `music_mentioned`.
Tags come from source captions/metadata, not an acoustic classifier. Crowd, babble
and environmental music are allowed. Candidates are at least 15 seconds long.
Decoded audio integrity and byte preservation are checked, but this does not
certify perceptual quality or speech-free backgrounds:
`acoustic_background_validation` is false for every row.

```python
from datasets import load_dataset
ds = load_dataset("mlinmg/translation_dataset", "wavcaps_bg", split="train", streaming=True)
crowd = ds.filter(lambda row: "crowd" in row["tags"])
bbc = ds.filter(lambda row: row["source"] == "bbc")
```
