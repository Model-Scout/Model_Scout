---
license: cc-by-4.0
task_categories:
- text-to-speech
- automatic-speech-recognition
- audio-to-audio
- audio-classification
- text-to-audio
- voice-activity-detection
- any-to-any
tags:
- TTS
- ASR
- LID
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
  - name: gender
    dtype: string
  splits:
  - name: arabic
    num_bytes: 47548142.0
    num_examples: 100
  - name: chinese
    num_bytes: 47307900.0
    num_examples: 100
  - name: croatian
    num_bytes: 35923024.0
    num_examples: 100
  - name: czech
    num_bytes: 41969646.0
    num_examples: 100
  - name: danish
    num_bytes: 44811640.0
    num_examples: 100
  - name: dutch
    num_bytes: 47104430.0
    num_examples: 100
  - name: farsi
    num_bytes: 46839175.0
    num_examples: 100
  - name: finnish
    num_bytes: 40165057.0
    num_examples: 100
  - name: french
    num_bytes: 51776460.0
    num_examples: 100
  - name: german
    num_bytes: 55801064.0
    num_examples: 100
  - name: greek
    num_bytes: 45216947.0
    num_examples: 100
  - name: hebrew
    num_bytes: 46208162.0
    num_examples: 100
  - name: hindi
    num_bytes: 50476224.0
    num_examples: 100
  - name: hungarian
    num_bytes: 44192016.0
    num_examples: 100
  - name: italian
    num_bytes: 46838646.0
    num_examples: 100
  - name: japanese
    num_bytes: 37064261.0
    num_examples: 100
  - name: korean
    num_bytes: 47161955.0
    num_examples: 100
  - name: lithuanian
    num_bytes: 44076022.0
    num_examples: 100
  - name: norwegian
    num_bytes: 46042453.0
    num_examples: 100
  - name: polish
    num_bytes: 48412456.0
    num_examples: 100
  - name: portuguese
    num_bytes: 55752752.0
    num_examples: 100
  - name: romanian
    num_bytes: 49361834.0
    num_examples: 100
  - name: russian
    num_bytes: 51952551.0
    num_examples: 100
  - name: spanish
    num_bytes: 42633233.0
    num_examples: 100
  - name: swahili
    num_bytes: 50933114.0
    num_examples: 100
  - name: swedish
    num_bytes: 46036234.0
    num_examples: 100
  - name: turkish
    num_bytes: 47729948.0
    num_examples: 100
  - name: vietnamese
    num_bytes: 42987080.0
    num_examples: 100
  download_size: 1280190010
  dataset_size: 1302322426.0
configs:
- config_name: default
  data_files:
  - split: arabic
    path: data/arabic-*
  - split: chinese
    path: data/chinese-*
  - split: croatian
    path: data/croatian-*
  - split: czech
    path: data/czech-*
  - split: danish
    path: data/danish-*
  - split: dutch
    path: data/dutch-*
  - split: farsi
    path: data/farsi-*
  - split: finnish
    path: data/finnish-*
  - split: french
    path: data/french-*
  - split: german
    path: data/german-*
  - split: greek
    path: data/greek-*
  - split: hebrew
    path: data/hebrew-*
  - split: hindi
    path: data/hindi-*
  - split: hungarian
    path: data/hungarian-*
  - split: italian
    path: data/italian-*
  - split: japanese
    path: data/japanese-*
  - split: korean
    path: data/korean-*
  - split: lithuanian
    path: data/lithuanian-*
  - split: norwegian
    path: data/norwegian-*
  - split: polish
    path: data/polish-*
  - split: portuguese
    path: data/portuguese-*
  - split: romanian
    path: data/romanian-*
  - split: russian
    path: data/russian-*
  - split: spanish
    path: data/spanish-*
  - split: swahili
    path: data/swahili-*
  - split: swedish
    path: data/swedish-*
  - split: turkish
    path: data/turkish-*
  - split: vietnamese
    path: data/vietnamese-*
language:
- fa
- pl
- sv
- fi
- ar
- hu
- el
- ro
- cs
- sw
- fr
- hr
- en
- ko
- lb
- tr
- de
- lt
- zh
- he
- ru
- da
- ja
- nl
- pt
- it
- es
- vi
- hi
- 'no'
---



# YodaLingua-preview

**YodaLingua** is a high-quality speech dataset designed for training text-to-speech (TTS) systems, ASR models, and any application requiring clean, well-aligned audio–text pairs.  
This version contains an equal number of samples from each language (100 samples per language).

All audio clips are noise-reduced, normalized, and matched with accurate transcriptions.

## 🧾 Dataset Overview (full version)

| Property | Value |
|---------|-------|
| **Total clips** | 1,839,325 audio–transcription pairs |
| **Total duration** | ~5000 hours |
| **Speakers** | 75,793 distinct speakers |
| **Audio format** | MP3 • mono • 24 kHz • 16-bit |
| **License** | Permissive — commercial use allowed |

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

## License

This dataset is released under the [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) license.
It can be used for commercial and non-commercial purposes and attribution is not required.

---

## 🌍 Full Versions

To access the complete dataset, go to the collection:
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

## Contact

e-mail : [cyprienoucortex@gmail.com](cyprienoucortex@gmail.com)