---
task_categories:
- audio-classification
- automatic-speech-recognition
- text-to-speech
language:
- zh
- en
- ja
- ko
pretty_name: StarRail Voice
dataset_info:
  features:
  - name: audio
    dtype: audio
  - name: ingame_filename
    dtype: string
  - name: transcription
    dtype: string
  - name: language
    dtype: string
  - name: speaker
    dtype: string
  - name: voice_type
    dtype: string
  splits:
  - name: train
    num_bytes: 233254812029
    num_examples: 403437
  download_size: 241437714402
  dataset_size: 233254812029
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

# StarRail Voice

StarRail Voice is a dataset of voice lines from the popular game [Honkai: Star Rail](https://hsr.hoyoverse.com/).

Hugging Face 🤗  [StarRail-Voice](https://huggingface.co/datasets/simon3000/starrail-voice)

ModelScope [StarRail-Voice](https://modelscope.cn/datasets/simono/starrail-voice)

<!-- STATS -->
Last update at `2026-07-16`, game version `4.4.0`

`403437` wavs

`60164` without speaker (15%)

`61375` without transcription (15%)

`57869` without inGameFilename (14%)
<!-- STATS_END -->

## Dataset Details

### Dataset Description

The dataset contains voice lines from the game's characters in multiple languages, including Chinese, English, Japanese, and Korean.

The voice lines are spoken by the characters in the game and cover a wide range of topics, including greetings, combat, and story dialogue.

- **Language(s) (NLP):** Chinese, English, Japanese, Korean

## Dataset Creation

### Source Data

The data was obtained by unpacking the [Honkai: Star Rail](https://hsr.hoyoverse.com/) game.

#### Data Collection and Processing

Please refer to [StarRail-Voice](https://github.com/simon300000/starrail-voice) and [bnnm/wwiser-utils#15](https://github.com/bnnm/wwiser-utils/pull/15#issuecomment-1962182022) for more information on how the data was processed.

#### Who are the source data producers?

The source data producers are the developers of the game, HoYoverse.

### Annotations

The dataset contains official annotations from the game, including language, speaker name, and transcription.

## Bias, Risks, and Limitations

Annotations are incomplete. Some voice lines are missing speaker names and transcriptions.

Annotations are not guaranteed to be completely accurate.

Speakers and transcriptions may contain markups and placeholders, for example: `Hey, here you are, {NICKNAME}! Did you hear that? These two masters just called me a swordplay genius.`

### Recommendations

Users should be made aware of the risks, biases and limitations of the dataset.

Speaker names can be partially inferred from the ingame filenames.

## Licensing Information

Copyright © COGNOSPHERE. All Rights Reserved.
