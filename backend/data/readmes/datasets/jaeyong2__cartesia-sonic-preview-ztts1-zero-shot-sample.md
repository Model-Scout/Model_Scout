---
license: other
license_name: ztts1-eval-derived
task_categories:
- text-to-speech
language:
- en
- zh
- ko
- ja
- es
- ru
- de
tags:
- tts
- zero-shot-tts
- speech-evaluation
size_categories:
- n<1K
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*.parquet
dataset_info:
  features:
  - name: utt
    dtype: string
  - name: language
    dtype: string
  - name: audio
    dtype: audio
  - name: reference_audio
    dtype: audio
  - name: target_text
    dtype: string
  - name: prompt_text
    dtype: string
  - name: asr_transcript
    dtype: string
  - name: wer
    dtype: float32
  - name: cer
    dtype: float32
  - name: sim
    dtype: float32
  - name: audio_seconds
    dtype: float32
  - name: reference_seconds
    dtype: float32
  - name: reference_voice
    dtype: string
  - name: model_id
    dtype: string
  - name: mode
    dtype: string
  splits:
  - name: train
    num_examples: 700
---

# Cartesia Sonic on ZTTS1 zero-shot — sample with reference audio

100 utterances per language (700 rows) from the
zero-shot subsets of ZTTS1-Eval, synthesized with Cartesia Sonic (preview) in
voice-cloning mode.

Unlike the full set, **every row carries the reference recording as well as the
synthesized clip**, so a take can be compared against the voice it was cloning
without checking out the benchmark.

## Columns

| column | meaning |
|---|---|
| `audio` | the clip the model produced |
| `reference_audio` | the recording it was cloning |
| `target_text` | what the model was asked to say |
| `prompt_text` | what the reference recording says |
| `asr_transcript` | Whisper-large-v3 transcript of `audio` |
| `wer`, `cer` | error of `asr_transcript` against `target_text`, in percent |
| `sim` | WavLM speaker similarity between `audio` and `reference_audio` |
| `audio_seconds`, `reference_seconds` | durations, for spotting runaway or truncated takes |
| `reference_voice` | id of the reference clip |

For Chinese and Japanese read `cer`, not `wer`: the reference text is
word-segmented while the transcript is not, so word error is near 100 even for
a clean clip.

## Usage

```python
from datasets import load_dataset

ds = load_dataset("jaeyong2/cartesia-sonic-preview-ztts1-zero-shot-sample", split="train")
row = ds[0]
row["audio"]["array"]            # what the model said
row["reference_audio"]["array"]  # the voice it was imitating
```

## Provenance

Text and reference recordings come from
[ZTTS1-Eval](https://github.com/Zyphra/ZTTS1-Eval) zero-shot subsets. Scores
were computed with Whisper-large-v3 (WER/CER) and WavLM-base-plus-sv
(similarity).
