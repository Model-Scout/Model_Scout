---
license: cc-by-4.0
pretty_name: URGENT 2026 Speech Quality Assessment
language:
- ar
- zh
- en
- fr
- de
- hi
- it
- ja
- ko
task_categories:
- audio-classification
size_categories:
- 10K<n<100K
tags:
- audio
- speech-quality
- speech-enhancement
- mos
- cmos
- subjective-evaluation
- icassp-2026
- urgent-challenge
configs:
- config_name: acr
  data_files:
  - split: test
    path: data/acr/test-*.parquet
  default: true
- config_name: ccr
  data_files:
  - split: test
    path: data/ccr/test-*.parquet
dataset_info:
- config_name: acr
  features:
  - name: sample_id
    dtype: string
  - name: audio
    dtype: audio
  - name: utterance_id
    dtype: string
  - name: system_id
    dtype: string
  - name: team_name
    dtype: string
  - name: language
    dtype: string
  - name: speaker_id
    dtype: string
  - name: text
    dtype: string
  - name: is_simulated
    dtype: bool
  - name: sample_rate
    dtype: int32
  - name: duration
    dtype: float64
  - name: mos
    dtype: float64
  - name: listener_scores
    list: int8
  splits:
  - name: test
    num_examples: 5040
    num_bytes: 574829602
- config_name: ccr
  features:
  - name: sample_id
    dtype: string
  - name: audio_a
    dtype: audio
  - name: audio_b
    dtype: audio
  - name: utterance_id
    dtype: string
  - name: system_id_a
    dtype: string
  - name: system_id_b
    dtype: string
  - name: team_name_a
    dtype: string
  - name: team_name_b
    dtype: string
  - name: language
    dtype: string
  - name: speaker_id
    dtype: string
  - name: text
    dtype: string
  - name: is_simulated
    dtype: bool
  - name: sample_rate
    dtype: int32
  - name: duration
    dtype: float64
  - name: cmos
    dtype: float64
  - name: listener_scores
    list: int8
  splits:
  - name: test
    num_examples: 12600
    num_bytes: 2872141814
---

# URGENT 2026 Speech Quality Assessment

The subjective listening-test dataset from **ICASSP 2026 URGENT Track 1: Universal Speech Enhancement**, containing **5,040 ACR samples**, **12,600 CCR comparisons**, and **141,386 individual ratings** across 840 utterances, nine languages, and six systems.

Each scored sample includes the audio, its MOS or CMOS, individual listener scores, and utterance metadata.

## Load the data

```python
from datasets import load_dataset

repo = "urgent-challenge/urgent2026-sqa"
acr = load_dataset(repo, "acr", split="test")
ccr = load_dataset(repo, "ccr", split="test")

sample = acr[0]
print(sample["sample_id"], sample["mos"], sample["listener_scores"])
audio = sample["audio"].get_all_samples()
waveform, sample_rate = audio.data, audio.sample_rate
```

Both configurations contain a single `test` split covering the complete ICASSP blind listening test.

| Configuration | Contents | Samples |
|---|---|---:|
| `acr` | Enhanced audio, MOS, and individual quality scores | 5,040 |
| `ccr` | Enhanced audio pairs, CMOS, and individual comparison scores | 12,600 |

Audio is stored as embedded mono FLAC at its native sample rate. Audio decoding uses TorchCodec; install compatible PyTorch, TorchCodec, and FFmpeg versions. To read the audio bytes with SoundFile instead:

```python
import io
import soundfile as sf
from datasets import Audio

raw_acr = acr.cast_column("audio", Audio(decode=False))
waveform, sample_rate = sf.read(io.BytesIO(raw_acr[0]["audio"]["bytes"]))
```

## ACR: absolute category rating

Listeners rate the quality of a single enhanced audio sample on a **1–5** scale, with higher scores indicating better quality. Each of the six systems has one sample for every utterance. There are **40,280 individual ratings**, with 4–16 scores per sample.

| Field | Type | Description |
|---|---|---|
| `sample_id` | string | Unique sample ID: `acr_{utterance_id}_{system_id}`. |
| `audio` | Audio | Enhanced speech from the evaluated system. |
| `utterance_id` | string | Source utterance ID, such as `fileid_1`. |
| `system_id` | string | Submission ID of the evaluated system. |
| `team_name` | string | Name of the submitting team. |
| `language` | string | ISO 639-3 language code. |
| `speaker_id` | string | Anonymous speaker grouping key. |
| `text` | string | Utterance transcript. |
| `is_simulated` | bool | Whether the source utterance was simulated. |
| `sample_rate` | int32 | Native audio sample rate in Hz. |
| `duration` | float64 | Audio duration in seconds. |
| `mos` | float64 | Mean opinion score, rounded to three decimal places. |
| `listener_scores` | list[int8] | Individual quality scores on the 1–5 scale. |

## CCR: comparison category rating

Listeners compare two systems' outputs for the same utterance on a **−3 to +3** scale. **Positive CMOS means `audio_a` is better than `audio_b`**; negative values favor `audio_b`. All 15 unordered pairs of the six systems are included for each utterance. There are **101,106 individual ratings**, with 4–20 scores per pair.

| Field | Type | Description |
|---|---|---|
| `sample_id` | string | Unique pair ID: `ccr_{utterance_id}_{system_id_a}_{system_id_b}`. |
| `audio_a` | Audio | Enhanced speech from system A. |
| `audio_b` | Audio | Enhanced speech from system B. |
| `utterance_id` | string | Source utterance ID shared by both audio signals. |
| `system_id_a` | string | Submission ID of system A. |
| `system_id_b` | string | Submission ID of system B. |
| `team_name_a` | string | Name of the team that submitted system A. |
| `team_name_b` | string | Name of the team that submitted system B. |
| `language` | string | ISO 639-3 language code. |
| `speaker_id` | string | Anonymous speaker grouping key. |
| `text` | string | Utterance transcript. |
| `is_simulated` | bool | Whether the source utterance was simulated. |
| `sample_rate` | int32 | Native sample rate of both audio signals in Hz. |
| `duration` | float64 | Duration of both audio signals in seconds. |
| `cmos` | float64 | Mean comparison score, rounded to three decimal places. Positive values favor A. |
| `listener_scores` | list[int8] | Individual comparison scores on the −3 to +3 scale, following the A/B order. |

System A has the lower numeric submission ID. If you swap A and B, negate both `cmos` and every value in `listener_scores`.

## Systems

| Submission ID | Team | Challenge rank |
|---|---|---:|
| 1412 | WR | 1 |
| 1397 | GHW | 2 |
| 1401 | subatomicseer | 3 |
| 1395 | baird | 4 |
| 1348 | RICK2000 | 5 |
| 1399 | Ali-Universal-SE | 5 |

## Languages

| Language | Code | Utterances |
|---|---|---:|
| English | eng | 163 |
| Chinese | zho | 117 |
| Arabic | ara | 80 |
| German | deu | 80 |
| French | fra | 80 |
| Hindi | hin | 80 |
| Italian | ita | 80 |
| Japanese | jpn | 80 |
| Korean | kor | 80 |

## Citation

If you use this dataset, please cite it by referencing the following paper

```bibtex
@inproceedings{urgent2026,
  title={{ICASSP 2026 URGENT Speech Enhancement Challenge}},
  author={Li, Chenda and Wang, Wei and Sach, Marvin and Zhang, Wangyou and Saijo, Kohei and Cornell, Samuele and Fu, Yihui and Ni, Zhaoheng and Fingscheidt, Tim and Watanabe, Shinji and Qian, Yanmin},
  booktitle={Proc. ICASSP 2026},
  year={2026}
}
```
