---
license: other
task_categories:
- translation
- audio-to-audio
language:
- ar
- es
- fr
- hi
- id
- ja
- ko
- pt
- ru
- th
- tr
- vi
- en
tags:
- speech2speech
pretty_name: SoundHarvest
size_categories:
- 1K<n<10K
---

## Data Format

The dataset is organized in the following structure:

```yaml
dataset/
├── video_id_1/
│ ├── audio_language_1.wav
│ ├── audio_language_2.wav
│ ├── subtitle_language_1.vtt
│ ├── subtitle_language_2.vtt
│ └── unmatched/
│ └── ...
├── video_id_2/
│ ├── ...
└── ...
```

Original version with the channel (MrBeast) will contain 487 hours 27 minutes 59 seconds of audio files.

## Limitations

- **Copyright**: Please be aware of copyright restrictions when using this dataset. Ensure that you have the necessary permissions to use the audio and subtitle data for your intended purposes.

- **Inaccuracies**: While efforts have been made to align audio and subtitles accurately, there may be occasional mismatches or inaccuracies in the dataset. We recommend verifying the quality and alignment of the data for your specific use case.

## Generating Dataset

For generating the dataset launch:
1. `generate_urls.py` - to generate video URLs based on `channel_urls.txt`
2. `generate_dataset.py` - for generating dataset (can take **a lot** of time...)
3. `polish_dataset.py` - for cleaning the folders without any useful data

## Usage

The SoundHarvest dataset can be utilized for a variety of applications, including:

### 1. Automatic Speech Recognition (ASR)

Train ASR models to convert spoken language into text. SoundHarvest provides diverse language samples, making it suitable for multilingual ASR tasks.

### 2. Multilingual Natural Language Processing (NLP)

Leverage the dataset for multilingual NLP tasks, such as:

- Speech sentiment analysis.
- Language identification.

### 3. Linguistic Research and Analysis

Conduct linguistic research and analysis to explore various aspects of languages, including phonetics, dialects, and language evolution.

### 4. Speech-to-Speech Translation

Use the dataset to develop and evaluate speech-to-speech translation models. Translate spoken content from one language to another, expanding the dataset's applications to cross-lingual communication.

## Acknowledgments

We would like to express our gratitude to the YouTube content creators for providing valuable multilingual audio content that makes this dataset possible.