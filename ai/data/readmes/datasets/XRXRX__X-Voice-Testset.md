---
license: other
license_name: custom-license
license_link: LICENSE
task_categories:
- text-to-speech
- automatic-speech-recognition
language:
- bg
- cs
- da
- de
- el
- en
- es
- et
- fi
- fr
- hr
- hu
- id
- it
- ja
- ko
- lt
- lv
- mt
- nl
- pl
- pt
- ro
- ru
- sk
- sl
- sv
- th
- vi
- zh
---

<h1 align="center">X-Voice Multilingual Test Set</h1>
<h3 align="center">High-Fidelity Test Set for Multilingual Text-to-Speech across 30 Languages</h3>


This test set is built as part of the research: **X-Voice: One Speaker, 30+ Languages with Zero-Shot Voice Cloning**, serving as the evaluation benchmark for our model.

## Dataset Summary
- **30 languages**
  - **European**: bg (Bulgarian), cs (Czech), da (Danish), de (German), el (Greek), en (English), es (Spanish), et (Estonian), fi (Finnish), fr (French), hr (Croatian), hu (Hungarian),  it (Italian),  lt (Lithuanian), lv (Latvian), mt (Maltese), nl (Dutch), pl (Polish), pt (Portuguese), ro (Romanian), ru (Russian), sk (Slovak), sl (Slovenian), sv (Swedish).
  - **Asian**: id (Indonesian), ja (Japanese), ko (Korean), th (Thai), vi (Vietnamese), zh (Chinese).
- **500 utterances per language** from **over 100 speakers** (15,000 utterances in total).
- Audio format: **24kHz mono WAV**.
- Each sample includes human-recorded **ground-truth audio**.
- Primarily constructed from **Common Voice**. Vietnamese data from Dolly-Audio, Korean from Emilia, Croatian from ParlaSpeech-HR.

## Curation Pipeline
1. Temporal and speaking rate filtering
2. Silero VAD for speech segmentation and silence trimming
3. ECAPA-TDNN speaker verification (cosine similarity ≥ 0.6) to ensure consistent speakers between prompt and reference audio

## Data Structure
```
X-Voice-TestSet/zero_shot
├── bg/
│   ├── ground_truth/  # 📂 Folder for human-recorded ground-truth audio
│   ├── waveform/      # 📂 Folder for prompt reference audio
│   ├── gt_wav.scp     # 📄 Index file for ground-truth audio (utt_id /path/to/gt.wav)
│   ├── prompt_text    # 📄 Prompt text file (utt_id prompt_content)
│   ├── prompt_wav.scp # 📄 Index file for prompt audio (utt_id /path/to/prompt.wav)
│   └── text           # 📄 Target text file (utt_id target_content)
├── cs/
│   └── ...            # Same structure as bg/
├── da/
│   └── ...
...
└── zh/
    └── ...            # Same structure as bg/
```
## License

**This dataset contains data from multiple sources, each with its own license.**
Users must comply with the license of each individual sub-dataset they use.

| Dataset | License | Commercial Use |
|---|---|---|
| CommonVoice | CC0-1.0 | Yes |
| ParlaSpeech-HR | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) | Yes |
| Emilia | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | Yes |
| Dolly-Audio | [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) | No |

## Citation
If you use this benchmark, please cite our work.
