# ODAQ: Open Dataset of Audio Quality

A collection of audio signals with subjective scores of perceived quality.

### ODAQ Dataset (Open Dataset of Audio Quality)

The **ODAQ dataset** is a unique collection of audio signals accompanied by subjective scores of perceived quality. It was created to address the scarcity of such data, which is essential for audio research.

ODAQ contains **240 audio samples** with corresponding quality scores, obtained through a MUSHRA listening test conducted in parallel at Fraunhofer IIS (Germany) and Netflix, Inc. (USA). The audio samples are processed versions of original audio material, which includes:
* Stereo audio at 44.1 or 48 kHz sampling frequency.
* 14 music excerpts (8 of which are solo recordings).
* 11 excerpts from movie-like soundtracks with dialogues, music, and sound effects.

---

### Highlights
* Each audio sample was rated by **26 expert listeners** (after post-screening).
* The audio samples were processed by **6 method classes** at 5 different quality levels, plus anchor conditions.
* The processing methods were designed to generate quality degradations commonly encountered in audio coding and source separation.
* The diversity of processing conditions, the wide range of quality levels, and the pool of international listeners make ODAQ particularly well-suited for further research into the prediction and analysis of perceived audio quality.

---

### Package Structure
The dataset is organized into several folders for easy navigation:
* `ODAQ_unprocessed`: Contains the original, unprocessed audio material.
* `ODAQ_listening_test`: Contains the audio samples used in the test and the results (both individual .xml files and an aggregated .csv table).
* `ODAQ_training`: Contains the audio samples used during the training phase of the listening test.
* `listening_test_instructions`: Contains the instructions provided to the participants.
* `ODAQ_DE_raw_outputs`: Contains the raw outputs of the separation systems used for the "Dialogue Enhancement" scenario.

---

### License and Citation
The ODAQ dataset has a **mixed Creative Commons license (CC BY, CC BY-NC, and CC0)**. For full details, please refer to the `_license_disclaimer.txt` and `_detailed_license.csv` files included in the package.

## ICASSP 2024

Please refer to [our ICASSP 2024 paper][id] for full details about the listening test and please cite it if you find this dataset useful:
```
@inproceedings{Torcoli2024ODAQ,
author = {Torcoli, M. and Wu, C. W. and Dick, S. and Williams, P. A. and Halimeh, M. M. and Wolcott, W. and Habets, E. A. P.},
year = {2024},
month = {April},
title = {{ODAQ}: Open Dataset of Audio Quality},
address = {Seoul, Korea},
booktitle={IEEE International Conference on Acoustics Speech and Signal Processing (ICASSP)}
}
```
---

**Useful Links:**
* **Paper**: https://arxiv.org/abs/2401.00197
* **GitHub Project Page**: https://github.com/Fraunhofer-IIS/ODAQ/
* **Listening Test App**: https://github.com/Netflix-Skunkworks/listening-test-app

출처: Kaggle (davidventurino/odaq-open-dataset-of-audio-quality)
태그: music, signal processing, deep learning, audio, audio classification
라이선스: Other (specified in description)
수정일: 2025-09-13T10:32:56.817Z
