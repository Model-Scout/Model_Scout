---
language:
- en
- zh
- ml
- ja
- hi
- ko
- te
- ta
- pa
- fr
- bn
- kn
- ar
- th
- de
- es
pretty_name: MISP-M3SD
license: apache-2.0
task_categories:
- audio-classification
tags:
- speaker-diarization
- audio-visual
- multimodal
- multilingual
- dataset
- robust-speech-processing
- in-the-wild
---
# MISP-M3SD


## Dataset Summary

**MISP-M3SD** is a large-scale **multimodal**, **multi-scenario**, and **multilingual** dataset for **robust speaker diarization**, constructed from in-the-wild online videos. It contains more than **770 hours** of synchronised audio-visual recordings, covering **14 scenarios** and **16 languages**.

The dataset is designed to support the development of speaker diarization systems with stronger **cross-domain generalisation** under realistic conditions, including background noise, reverberation, overlapping speech, off-screen speech, motion blur, unstable speaker visibility, and camera switching.

To enable scalable construction, MISP-M3SD is built through a largely automated pipeline, including:

1. multilingual multi-scenario media acquisition,
2. data cleaning and preprocessing, and
3. cross-modal consistency-guided annotation with selective manual verification.


## Access

To use MISP-M3SD:

1. Download [`audio.zip`](./audio.zip) together with all split files ([`audio.z01`](./audio.z01), [`audio.z02`](./audio.z02), [`audio.z03`](./audio.z03), [`audio.z04`](./audio.z04), [`audio.z05`](./audio.z05), [`audio.z06`](./audio.z06));
2. Extract the audio archive to obtain the released WAV files;
3. Use [`oracle.rttm`](./oracle.rttm) as the final diarization annotation file;
4. Because of storage limitations, the videos are not distributed as a complete packaged archive. Instead, we provide metadata for each source video, including the corresponding video ID, in [`video_information.xlsx`](./video_information.xlsx), together with video download scripts in the GitHub repository. This allows users to retrieve the videos directly from the original platforms. 

## Key Features

- **Large scale**: 770.55 hours of synchronised audio-visual recordings
- **Multilingual**: 16 languages
- **Multi-scenario**: 14 scenarios
- **Rich interaction complexity**: 7,276 speakers in total, with 5.30 speakers per sample on average
- **Rich metadata**: includes source video identifiers, duration, title, description, language, and scenario
- **Realistic conditions**: collected from in-the-wild online videos
- **Reliable annotation**: cross-modal consistency-guided annotation with selective manual verification
- **Practical release format**: audio and annotations are directly provided, while source videos can be retrieved through released scripts and video IDs

## Scenarios

MISP-M3SD covers 14 scenarios:

- Lesson
- Interview
- News
- Debate
- Discussion
- Conversation
- Job Interview
- Meeting
- Lecture
- Tutorial
- Entertainment Vlog
- Home Interaction
- Dinner Party
- Other

The scenario distribution is diverse but naturally uneven, reflecting the characteristics of publicly accessible online videos rather than an artificially balanced design.

## Data Splits

The dataset is divided into **train / dev / eval** splits at the sample level, with the split assignment for each sample provided in [`split.txt`](./split.txt).

| Split | #Samples | Duration (h) | Avg. Duration (min) | Median Duration (min) | Speech Activity (h) | #Speakers | Avg. Speakers | #Languages | #Scenarios |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Train | 1272 | 716.54 | 33.80 | 18.38 | 656.17 | 6756 | 5.31 | 14 | 14 |
| Dev | 50 | 27.10 | 32.52 | 28.42 | 25.71 | 275 | 5.50 | 11 | 13 |
| Eval | 50 | 26.91 | 32.30 | 29.62 | 25.04 | 245 | 4.90 | 11 | 13 |
| Total | 1372 | 770.55 | 33.70 | 20.98 | 706.91 | 7276 | 5.30 | 16 | 14 |

The splits are constructed to preserve the diversity of the full dataset in terms of scenario, language, duration, speaker-number distribution, and overlap characteristics.


A comparison with representative audio-visual speaker diarization datasets is shown below.

| Dataset | Scenarios | #Samples | Speakers | Duration (h) | Speech (%) | Noise | Languages |
|---|---|---:|---|---:|---:|---|---|
| AMI | Meetings | 170 | 3-5 | 100 | 80.91 | No | EN |
| AVDIAR | Chat | 27 | 1-4 | 0.35 | 82.6 | No | EN, FR |
| AVA-AVD | Daily Activities | 351 | 2-24 | 29.25 | 45.95 | Yes | EN, FR, ZH, DE, KO, ES |
| MSDWild | Vlogs | 3143 | 2-10 | 80 | 91.29 | Yes | EN, ZH, TH, KO, JA, DE, PT, AR |
| MISP2021&2022 | Conversations | 373 | 2-6 | 121 | 92.30 | Yes | CN |
| **MISP-M3SD** | Lesson, Interview, News, Debate, Meeting, Home Interaction, etc. | **1372** | **1-19** | **770.55** | **91.74** | **Yes** | **EN, ZH, ML, JA, HI, KO, TE, TA, PA, etc.** |

Compared with previous datasets, MISP-M3SD provides:

- substantially larger scale
- broader scenario coverage
- richer multilingual content
- more realistic in-the-wild conditions
- a scalable construction pipeline for robust multimodal diarization research