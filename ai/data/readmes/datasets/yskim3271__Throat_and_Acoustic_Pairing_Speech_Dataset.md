---
license: cc-by-4.0
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: dev
    path: data/dev-*
  - split: test
    path: data/test-*
dataset_info:
- config_name: default
  features:
  - name: gender
    dtype: string
  - name: speaker_id
    dtype: string
  - name: sentence_id
    dtype: string
  - name: text
    dtype: string
  - name: duration
    dtype: float32
  - name: audio.throat_microphone
    dtype: audio
  - name: audio.acoustic_microphone
    dtype: audio
  - name: normalized_text
    dtype: string
  splits:
  - name: train
    num_bytes: 4868539208
    num_examples: 4000
  - name: dev
    num_bytes: 1152997554
    num_examples: 1000
  - name: test
    num_bytes: 1190844664
    num_examples: 1000
  download_size: 7025122286
  dataset_size: 7212381426
language:
- ko
---

# TAPS: Throat and Acoustic Paired Speech Dataset

## 1. DATASET SUMMARY
**The Throat and Acoustic Paired Speech (TAPS) dataset** is a standardized corpus designed for deep learning-based speech enhancement, specifically targeting throat microphone recordings. Throat microphones effectively suppress background noise but suffer from high-frequency attenuation due to the low-pass filtering effect of the skin and tissue. **The dataset provides paired recordings from 60 native Korean speakers, captured simultaneously using a throat microphone (accelerometer-based) and an acoustic microphone.**
This dataset facilitates speech enhancement research by enabling the development of models that recover lost high-frequency components and improve intelligibility. Additionally, we introduce a mismatch correction technique to align signals from the two microphones, which enhances model training.

___

## 2. Dataset Usage
To use the TAPS dataset, follow the steps below:
### 2.1	Loading the dataset
You can load the dataset from Hugging Face as follows:

```python
from datasets import load_dataset
dataset = load_dataset("yskim3271/Throat_and_Acoustic_Pairing_Speech_Dataset")
print(dataset)
```

### Example output:
```python
 DatasetDict({
     train: Dataset({
         features: ['gender', 'speaker_id', 'sentence_id', 'text', 'duration', 'audio.throat_microphone', 'audio.acoustic_microphone', 'normalized_text'],
         num_rows: 4000
     })
     dev: Dataset({
         features: ['gender', 'speaker_id', 'sentence_id', 'text', 'duration', 'audio.throat_microphone', 'audio.acoustic_microphone', 'normalized_text'],
         num_rows: 1000
     })
     test: Dataset({
         features: ['gender', 'speaker_id', 'sentence_id', 'text', 'duration', 'audio.throat_microphone', 'audio.acoustic_microphone', 'normalized_text'],
         num_rows: 1000
     })
 })
```

## 2.2 Accessing a sample
Each dataset entry consists of metadata and paired audio recordings. You can access a sample as follows:

```python
sample = dataset["train"][0]  # Get the first sample
print(f"Gender: {sample['gender']}")
print(f"Speaker ID: {sample['speaker_id']}")
print(f"Sentence ID: {sample['sentence_id']}")
print(f"Text: {sample['text']}")
print(f"Duration: {sample['duration']} sec")
print(f"Throat Microphone Audio Path: {sample['audio.throat_microphone']['path']}")
print(f"Acoustic Microphone Audio Path: {sample['audio.acoustic_microphone']['path']}")
```

## 2.3 Using Text and Normalized Text Fields
The dataset includes both `text` (orthographic transcript) and `normalized_text` (pronunciation-oriented transcript) fields for all splits.

### Normalized Text Details
`normalized_text` is a pronunciation-oriented Hangul transcription manually produced by listening to the acoustic microphone recording.
- Numbers are converted into their Korean spoken forms.
- Latin alphabet sequences (e.g., acronyms) and measurement units are converted into their Korean spoken forms.
- All non-Hangul special characters are removed or replaced with their spoken equivalents.

Note: Because `normalized_text` is based on manual auditory transcription of the acoustic recording, it may differ from `text`, which preserves the original written form.

#### Example usage:
```python
sample = dataset["train"][0]
print(f"Original text: {sample['text']}")
print(f"Normalized text: {sample['normalized_text']}")

# Output:
# Original text: 충남 예산군이 이달부터 '2022년 찾아가는 어린이 생활안전 교육'을 실시하고 있다
# Normalized text: 충남 예선군이 이달부터 이천 이십 이 년 찾아가는 어린이 생활안전 교육을 실시하고 있다
```
___

## 3. Links and Details
- **Project website:** [Link](http://taps.postech.ac.kr)
- **Point of contact:** Yunsik Kim (ys.kim@postech.ac.kr)
- **Collected by:** Intelligent Semiconductor and Wearable Devices (ISWD) of the Pohang University of Science and Technology (POSTECH)
- **Language:** Korean
- **Download size:** 7.03 GB
- **Total audio duration:** 15.3 hours
- **Number of speech utterances:** 6,000
___

## 4. Citataion
The BibTeX entry for the dataset is currently being prepared.
___

## 5. DATASET STRUCTURE & STATISTICS
- Training Set (40 speakers, 4,000 utterances, 10.2 hours)
- Development Set (10 speakers, 1,000 utterances, 2.5 hours)
- Test Set (10 speakers, 1,000 utterances, 2.6 hours)
- Each set is gender-balanced (50% male, 50% female).
- No speaker overlap across train/dev/test sets.

| Dataset Type | Train | Dev | Test |
|:---------------|:------------|:--------------|:-----------|
| **Number of Speakers** | 40 | 10 | 10 |
| **Number of male speakers** | 20 | 5 | 5 |
| **Mean / standard deviation of the speaker age** | 28.5 / 7.3 | 25.6 / 3.0 | 26.2 / 1.4 |
| **Number of utterances** | 4,000 | 1,000 | 1,000 |
| **Total length of utterances (hours)** | 10.2 | 2.5 | 2.6 |
| **Max / average / min length of utterances (s)** | 26.3 / 9.1 / 3.2 | 17.9 / 9.0 / 3.3 | 16.6 / 9.3 / 4.2 |
___

## 6. DATA FIELDS

Each dataset entry contains:
- **`gender`:** Speaker's gender (male/female).
- **`speaker_id`:** Unique speaker identifier (e.g., "p01").
- **`sentence_id`:** Utterance index (e.g., "u30").
- **`text`:** Original transcription.
- **`duration`:** Length of the audio sample.
- **`audio.throat_microphone`:** Throat microphone signal.
- **`audio.acoustic_microphone`:** Acoustic microphone signal.
- **`normalized_text`:** Pronunciation-oriented Hangul transcription manually produced by listening to the acoustic microphone recording. Numbers, Latin alphabet sequences, and measurement units are converted into their Korean spoken forms, and all non-Hangul special characters are removed or replaced with their spoken equivalents. It may differ from `text` (orthographic transcript).
___
## 7. DATASET CREATION
### 7.1 Hardware System for Audio Data Collection
The hardware system simultaneously records signals from a throat microphone and an acoustic microphone, ensuring synchronization.
- **Throat microphone:** The TDK IIM-42652 MEMS accelerometer captures neck surface vibrations (8 kHz, 16-bit resolution).
<p align="left">
  <img src="https://cdn-uploads.huggingface.co/production/uploads/6787e5b7d2d1062c364f53b1/hXlThD1DEhXHN90cvXHSJ.png"  style="object-fit:contain; width:500px; height:250px;">
</p>
- **Acoustic microphone:** The CUI Devices CMM-4030D-261 MEMS microphone records audio (16 kHz, 24-bit resolution) and is integrated into a peripheral board.
<p align="left">
  <img src="https://cdn-uploads.huggingface.co/production/uploads/6787e5b7d2d1062c364f53b1/1NVYVMWfTHjqJCWmSWNXP.png" style="object-fit:contain; width:500px; height:250px;">
</p>
- **MCU and data transmission:** The STM32F301C8T6 MCU processes signals via SPI (throat microphone) and I²S (acoustic microphone). Data is transmitted to a laptop in real-time through UART communication.
<p align="left">
  <img src="https://cdn-uploads.huggingface.co/production/uploads/6787e5b7d2d1062c364f53b1/d5f79nQd1XXWAH6ij5-rq.png" style="object-fit:contain; width:500px; height:250px;">
</p>

### 7.2 Sensors Positioning and Recording Environment
- **Throat microphone placement:** Attached to the supraglottic area of the neck.
- **Acoustic microphone position:** 30 cm in front of the speaker.
- **Recording conditions:** Conducted in a controlled, semi-soundproof environment to minimize ambient noise.
- **Head rest:** A headrest was used to maintain a consistent head position during recording.
- **Nylon filter:** A nylon pop filter was placed between the speaker and the acoustic microphone to minimize plosive sounds.
- **Scripts for Utterances:** Sentences were displayed on a screen for participants to read.
<p align="left">
  <img src="https://cdn-uploads.huggingface.co/production/uploads/6787e5b7d2d1062c364f53b1/7J4JspKHyKt4xNcws16fV.png" style="object-fit:contain; width:714px; height:400px;">
</p>

### 7.3 Python-based Software for Data Recordings
The custom-built software facilitates real-time data recording, monitoring, and synchronization of throat and acoustic microphone signals.
- **Interface overview:** The software displays live waveforms, spectrograms, and synchronization metrics (e.g., SNR, shift values).
- **Shift analysis:** Visualizations include a shift plot to monitor synchronization between the microphones and a shift histogram for statistical analysis.
- **Recording control:** Users can manage recordings using controls for file navigation (e.g., Prev, Next, Skip).
- **Real-time feedback:** Signal quality is monitored with metrics like SNR and synchronization shifts.

### 7.4 Recorded Audio Data Post-Processing
- **Noise reduction:** Applied Demucs model to suppress background noise in the acoustic microphone recordings.
- **Mismatch correction:** Aligned throat and acoustic microphone signals using cross-correlation.
- **Silent segment trimming:** Removed leading/trailing silence.

### 7.5 Personal and Sensitive Information
- No personally identifiable information is included.
- Ethical approval: Institutional Review Board (IRB) approval from POSTECH.
- Consent: All participants provided written informed consent.

___
## 8. POTENTIAL APPLICATIONS OF THE DATASET
The TAPS dataset enables various speech processing tasks, including:
- **Speech enhancement:** Improving the intelligibility and quality of throat microphone recordings by recovering high-frequency components.
- **Automatic speech recognition (ASR):** Enhancing throat microphone speech for better transcription accuracy in noisy environments.
- **Speaker Verification:** Exploring the effectiveness of throat microphone recordings for identity verification in challenging acoustic environments.
