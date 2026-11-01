---
pretty_name: "Quranic Translation Audio Data"
language:
- ar
- zh
- de
- id
- it
- ko
- fr
- pt
- ru
- bn
- bs
- en
- fa
- ur
license: apache-2.0
task_categories:
- audio-to-audio
- text-to-speech
- automatic-speech-recognition
tags:
- quran
- islam
- translation
- multilingual
- audio
- opus
- protobuf
---

<p align="center">
  <img src="/datasets/zaibihassan/Quranic-Translation-Audio-Data/resolve/main/banner.png" alt="Quranic Translation Audio Data Banner" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Audio%20Format-Opus%20(32kbps)-blueviolet?style=for-the-badge&logo=opus" alt="Opus Format">
  <img src="https://img.shields.io/badge/Timing%20Format-Protocol%20Buffers-violet?style=for-the-badge" alt="Protobuf">
  <img src="https://img.shields.io/badge/Total%20Translations-51-emerald?style=for-the-badge" alt="Total Translations">
  <img src="https://img.shields.io/badge/License-Apache%202.0-orange?style=for-the-badge" alt="License">
</p>

---

## Overview

**Quranic Translation Audio Data** is a highly curated, standardized, and streaming-optimized multilingual audio dataset containing the complete recitation of translation audios and commentaries of the Holy Quran across **51 different translation directories**. 

Every audio track has been meticulously converted from heavy .mp3 source files into the modern, high-fidelity **Opus (.opus)** format at a streaming-optimized bitrate of **32kbps**. Alongside the audio, the dataset includes highly efficient **Protocol Buffer (.pb)** files containing word-by-word/verse-by-verse timing data for real-time syncing. This ensures crystal-clear vocal clarity while achieving maximum compression and immediate playback alignment-making it ideal for:
- Mobile apps and offline Quranic platforms
- Low-bandwidth/edge-computing applications
- Multilingual Text-to-Speech (TTS) alignment and Speech Recognition (ASR) research
   
  ---
    ## Key Features

<ul>
  <li><b>High Vocal Fidelity</b>: Audio processed using the advanced Opus interactive audio codec, providing warm and natural voice tones despite the highly compressed size.</li>
<li><b>Minimal Footprint</b>: By standardizing to 32kbps Opus, the entire dataset footprint is reduced by up to <b>65-75%</b> compared to standard MP3 formats, saving gigabytes of storage and bandwidth.</li>
<li><b>Protocol Buffer Timing</b>: Binary .pb timing files are ~33% smaller than JSON and parse instantly in any language, enabling word-by-word karaoke-style highlighting.</li>
<li><b>100% Complete</b>: Each language contains all 114 Surahs (chapters) from the Holy Quran, ensuring complete coverage without missing gaps.</li>
<li><b>Perfect Organization</b>: Standardized 3-digit naming format (001.opus/.pb to 114.opus/.pb) mapped cleanly inside individual language folders.</li>
</ul>

---

## Dataset Structure

The dataset is organized cleanly into 51 folders, each representing a specific language translation or commentary. Inside each directory, the audio and timing files are structured as follows:

```
Quranic-Translation-Audio-Data/
+- arabic_Abdullah_Al-Asmari_Commentary/
|  +- 001.opus
|  +- 001.pb
|  +- ...
+- english_sahih_international/
|  +- 001.opus
|  +- 001.pb
|  +- ...
+- urdu_mufti_taqi_usmani/
   +- 001.opus
   +- 001.pb
   +- ...
```