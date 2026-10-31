---
license: cc-by-4.0
task_categories:
- automatic-speech-recognition
language:
- en
- ms
- zh
- ru
- id
- ar
- ja
- ko
multilinguality:
- highly_multilingual
size_categories:
- 10K<n<100K
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
dataset_info:
  features:
  - name: audio
    dtype: audio
  - name: video_id
    dtype: string
  - name: sentence
    dtype: string
  - name: segments_en
    dtype: string
  - name: segments_ms
    dtype: string
  - name: total_speakers
    dtype: int64
  - name: sentence_en
    dtype: string
  - name: sentence_ms
    dtype: string
  - name: sentence_zh_hans
    dtype: string
  - name: sentence_zh_hant
    dtype: string
  - name: sentence_ru
    dtype: string
  - name: sentence_id
    dtype: string
  - name: sentence_ar
    dtype: string
  - name: sentence_ja
    dtype: string
  - name: sentence_ko
    dtype: string
  - name: leakage_avg
    dtype: float64
  - name: leakage_max
    dtype: float64
  - name: overlap_pct
    dtype: float64
  - name: single_speaker_pct
    dtype: float64
  - name: quality_confidence
    dtype: float64
  splits:
  - name: train
    num_bytes: 69356297972
    num_examples: 26383
  download_size: 69327852389
  dataset_size: 69356297972
---

# khursanirevo/multiturn_ks

## Dataset Description

Multiturn dialogue dataset with speaker-separated stereo audio and multi-language transcripts from 139 YouTube videos.

### Features

- **Audio**: Stereo audio with speaker separation (speaker 0 = left channel, speaker 1 = right channel)
- **Segments**: Speaker turn-level annotations with timestamps for English and Malay
- **Multi-language**: Transcripts in 9 languages (en, ms, zh-Hans, zh-Hant, ru, id, ar, ja, ko)
- **Video ID**: YouTube video identifier for each chunk
- **Chunking**: 30-second chunks with 0.5s overlap

### Columns

- `audio`: Playable stereo audio (24kHz)
- `video_id`: YouTube video identifier
- `sentence`: Full transcript for the chunk (English)
- `segments_en`: JSON list of English speaker turns `[{speaker, start, end, text}]`
- `segments_ms`: JSON list of Malay speaker turns `[{speaker, start, end, text}]`
- `total_speakers`: Number of speakers in chunk (typically 2)
- `sentence_ms`, `sentence_en`, etc.: Transcripts in each language

### Usage

```python
from datasets import load_dataset
import json

dataset = load_dataset("khursanirevo/multiturn_ks")

# Access audio and segments
chunk = dataset[0]
audio = chunk["audio"]  # Stereo audio array
video_id = chunk["video_id"]  # YouTube video ID
segments_en = json.loads(chunk["segments_en"])  # English speaker turns
segments_ms = json.loads(chunk["segments_ms"])  # Malay speaker turns

print(f"From video: {video_id}")
for seg in segments_en:
    speaker = seg['speaker']
    text = seg['text']
    print(f"Speaker {speaker} (EN): {text}")

for seg in segments_ms:
    speaker = seg['speaker']
    text = seg['text']
    print(f"Speaker {speaker} (MS): {text}")
```

### Audio Format

- **Format**: WAV (PCM)
- **Sample rate**: 24kHz
- **Channels**: 2 (stereo, speaker separation)
- **Bit depth**: 32-bit float

### Speaker Detection

Speakers are detected using RMS energy analysis:
- Channel 0 (left): Speaker 0
- Channel 1 (right): Speaker 1

### Languages

Supported languages:
- English (en)
- Malay (ms)
- Chinese Simplified (zh-Hans)
- Chinese Traditional (zh-Hant)
- Russian (ru)
- Indonesian (id)
- Arabic (ar)
- Japanese (ja)
- Korean (ko)

### Dataset Statistics

- Total videos: 139
- Total chunks: 26383
- Max chunk duration: 30s
- Overlap: 0.5s

## Source

Created from YouTube videos with dialogue separation using DialogueSidon model.

## License

CC-BY-4.0
