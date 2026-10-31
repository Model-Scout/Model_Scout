---
language:
- ko
license:
- cc-by-4.0
task_categories:
- automatic-speech-recognition
- text-to-speech
pretty_name: Korean Full-Duplex Synthetic Dataset Preview
size_categories:
- n<1K
tags:
- full-duplex
- spoken-dialogue
- synthetic
configs:
- config_name: representative
  data_files:
  - split: train
    path: data/representative.jsonl
---

# Korean Full-Duplex Synthetic Dataset Preview

## Overview

Public preview of a Korean full-duplex synthetic speech dataset. This
repository contains 100 conversations sampled from a corpus of 89,273
conversations (2,000.5 hours); it does not publish the full corpus audio.

## Preview contents

- 100 conversation WAV files
- `data/representative.jsonl`
- 24 kHz, mono, 16-bit PCM
- Events: `normal`, `barge_in`, `backchannel`, `cutoff_by_user`

## Annotation format

Each conversation includes:

- `conversation_id`: conversation identifier
- `events[].speaker`: `user` or `assistant`
- `events[].text`: utterance text
- `events[].start_sec`, `events[].end_sec`: dialogue-timeline timestamps
- `events[].event_type`: `normal`, `barge_in`, `backchannel`, or `cutoff_by_user`
- `label_sequence`: round-level interaction labels

## Full-corpus statistics

- Text dialogues: 729,635
- Text utterances: 10,694,922
- Materialized conversations: 89,273
- Materialized duration: 2,000.5 hours

The 2,000.5-hour duration is the measured sum of the materialized conversation
WAV durations.

## Generation, license, and attribution

- User speech: [CosyVoice3](https://github.com/FunAudioLLM/CosyVoice)
- Assistant speech: [Qwen3-TTS 1.7B](https://github.com/QwenLM/Qwen3-TTS)
- Voice conditioning source: [Zeroth-Korean](https://huggingface.co/datasets/kresnik/zeroth_korean), CC BY 4.0
- Preview license: CC BY 4.0

## Contact

- mukss0909056@snu.ac.kr

