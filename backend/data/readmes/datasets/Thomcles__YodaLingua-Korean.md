---
license: cc-by-4.0
language:
- ko
task_categories:
- text-to-speech
- automatic-speech-recognition
- audio-to-audio
- audio-classification
- text-to-audio
- voice-activity-detection
tags:
- TTS
- korean
pretty_name: YodaLingua
dataset_info:
  features:
  - name: __key__
    dtype: string
  - name: mp3
    dtype:
      audio:
        sampling_rate: 24000
  - name: text
    dtype: string
  - name: language
    dtype: string
  - name: speaker_id
    dtype: string
  - name: dnsmos
    dtype: float64
  splits:
  - name: train
    num_bytes: 2106507698.094
    num_examples: 53903
  download_size: 2078749186
  dataset_size: 2106507698.094
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
extra_gated_prompt: >-
  Get access this dataset by contacting me via email:
  [cyprienoucortex@gmail.com](cyprienoucortex@gmail.com)
---



  # YodaLingua-Korean

**YodaLingua** is a high-quality speech dataset designed for training text-to-speech (TTS) systems, ASR models, and any application requiring clean, well-aligned audio–text pairs.  
This release contains the **Korean** portion of the multilingual YodaLingua collection.

## 🧾 Dataset Overview

| Property | Value |
|---------|-------|
| **Total clips** | 53,903 audio–transcription pairs |
| **Total duration** | 143 hours |
| **Speakers** | 2,219 distinct speakers |
| **Audio format** | MP3 • mono • 24 kHz • 16-bit |
| **License** | Permissive — commercial use allowed |

All audio clips are noise-reduced, normalized, and matched with accurate transcriptions.

---

## Data Fields

Each entry in the dataset contains the following fields:

| Field | Description |
|------|------------|
| `__key__` | Unique identifier for each sample. |
| `audio` | Path to the audio file associated with the sample (MP3 format). |
| `text` | Ground-truth transcription of the audio segment. |
| `language` | Language code following ISO 639 standards. |
| `speaker_id` | Unique identifier assigned to each speaker. Multiple audio can share the same speaker ID. |
| `dnsmos` | DNSMOS P.835 Overall (OVRL) score estimating perceptual speech quality; higher values indicate cleaner and more intelligible audio. |


---

## 🌍 Multilingual Versions

Other languages are available in the YodaLingua multilingual collection:  
👉 https://huggingface.co/collections/Thomcles/yodalingua

---

We apply a multi-stage pipeline to ensure maximum data quality:

### **1. Standardization**
- Convert to WAV  
- Mono channel  
- Resample to **24 kHz**  
- **16-bit** sample width  
- Normalize to **–20 dBFS** (with volume correction between –3 and +3 dB)

### **2. Noise Reduction**
Advanced denoising applied to improve clarity and remove background artifacts.

### **3. Speaker Diarization**
Segment long recordings by speaker to improve diversity and ensure speaker-consistent utterances.

### **4. Voice Activity Detection (VAD)**
Merge consecutive VAD segments from the same speaker into clean utterances of **3–30 s**.

### **5. Transcription**
State-of-the-art ASR models produce accurate text transcripts.

### **6. Quality Filtering**
Clips are filtered using **DNSMOS P.835 OVRL**; only samples with a score **> 2.4** are retained.


## 📚 Loading the Dataset

```python
from datasets import load_dataset

ds = load_dataset("Thomcles/YodaLingua-Korean")
```

---

## Contact

e-mail : [cyprienoucortex@gmail.com](cyprienoucortex@gmail.com)