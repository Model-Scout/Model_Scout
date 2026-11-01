---
language:
- ar
- ja
- ko
- tr
- vi
license: other
task_categories:
- text-to-speech
- automatic-speech-recognition
pretty_name: Multilingual TTS/ASR Aggregated Dataset
size_categories:
- 100K<n<1M
configs:
- config_name: default
  data_files:
  - split: arabic
    path: data/arabic/*.parquet
  - split: japanese
    path: data/japanese/*.parquet
  - split: korean
    path: data/korean/*.parquet
  - split: turkish
    path: data/turkish/*.parquet
  - split: vietnamese
    path: data/vietnamese/*.parquet
dataset_info:
  features:
  - name: audio
    dtype:
      audio:
        sampling_rate: 22050
  - name: text
    dtype: string
  - name: duration
    dtype: float32
  - name: sampling_rate
    dtype: int32
  - name: language
    dtype: string
  - name: dialect
    dtype: string
  - name: speaker_id
    dtype: string
  - name: gender
    dtype: string
  - name: dataset_name
    dtype: string
  - name: split
    dtype: string
  - name: uid
    dtype: string
  - name: rms
    dtype: float32
  - name: lufs
    dtype: float32
  - name: snr
    dtype: float32
---

# Multilingual TTS/ASR Aggregated Dataset

Cleaned, deduplicated and loudness-normalized Arabic, Japanese, Korean, Turkish, and Vietnamese speech. The training columns are `audio` (16-bit PCM WAV, 22050 Hz) and `text`; the remaining columns contain quality and provenance metadata.
