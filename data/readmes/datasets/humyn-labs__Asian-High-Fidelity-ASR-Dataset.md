---
license: cc-by-4.0
dataset_info:
  features:
  - name: language
    dtype: string
  - name: file_name
    dtype: string
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: transcript_json
    dtype: string
  - name: type
    dtype: string
  splits:
  - name: train
    num_bytes: 2099204670
    num_examples: 242
  download_size: 1898685319
  dataset_size: 2099204670
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
task_categories:
- automatic-speech-recognition
- audio-classification
language:
- ar
- ko
- vi
size_categories:
- n<1K
tags:
- ASR
- single-speaker
- multi-speaker
- natural-speech
- ai-research
---
## Dataset Overview

This dataset contains high-quality conversational audio samples curated for **Automatic Speech Recognition** tasks in Vietnamese, Korean, Arabic and Filipino.

The dataset includes:

* Paired **audio + transcripts**
* Natural, non-scripted conversational speech
* Single-speaker & Dual-speaker interactions

### Audio Specifications

* **Sampling Rate:** 16 kHz – 24 kHz
* **Bit Depth:** 16-bit
* **Audio Type:** Non-scripted conversational speech

---

## Supported Languages

| Language                 | Variant                          |
| ------------------------ | -------------------------------- |
| Vietnamese               | Regional conversational variants |
| Filipino (Tagalog-based) | Standard & colloquial speech     |
| Arabic                   | Modern Standard Arabic           |
| Korean                   | Modern Standard Korean           |
---

## Speaker Representation
* Natural, spontaneous dialogue
* Balanced gender representation

---

# Dataset Creation Methodology

## Data Collection

Speech data was collected from native speakers across multiple regions:

### Vietnam

* Urban and semi-urban communities
* Regional dialect diversity coverage

### Philippines

* Metro and non-metro regions
* Standard and colloquial Filipino usage

### Arabic
* Cross-regional accent variation
* Modern Standard Arabic and spoken dialect balance

### Korean
* Metro and non-metro regions
* Regional dialect diversity coverage

---

## Recording Setup

* Non-scripted, dual-speaker conversations
* Duration: **10–30 minutes per recording**
* Topics include:

  * Business
  * Finance
  * Politics
  * Everyday life discussions
  * Social topics

---

## Transcription Process

* Manual transcription by native speakers
* Reviewed for linguistic accuracy
* Preserves:

  * Conversational fillers
  * Natural pauses
---

# Dataset Intended Purpose

## Intended Uses

This dataset is designed for:

* Training and fine-tuning **Automatic Speech Recognition** models
* Conversational ASR benchmarking
* Speaker turn detection and interruption modeling
* Informal speech modeling
* Conversational AI research
* Academic and open-source research

---

## Out-of-Scope Uses

This dataset is **not intended for**:

* Safety-critical or real-time production systems without additional validation
* Commercial deployment without proper attribution and compliance with **CC BY 4.0**
* Medical, clinical, legal, or diagnostic applications

---

# License

This dataset is released under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.

---

# 📬 Contact

For dataset-related queries, please contact:

**[[support@humynlabs.ai](mailto:support@humynlabs.ai)]**