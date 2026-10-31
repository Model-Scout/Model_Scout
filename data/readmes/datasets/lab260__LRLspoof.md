---
language:
- ab
- hy
- as
- av
- az
- ba
- be
- pt
- bg
- ca
- ce
- cv
- hr
- cs
- da
- nl
- en
- fa
- fi
- fr
- ka
- gu
- hi
- hu
- is
- id
- it
- ja
- kk
- ko
- ky
- lv
- lt
- lb
- ms
- ml
- mr
- ne
- or
- os
- pl
- ru
- sl
- es
- sw
- te
- tk
- uz
- cy
- aus
- brx
- arr
- crh
- myv
- xal
- krc
- kjh
- lez
- mni
- mhr
- mdf
- nog
- raj
- tt
- tyv
- sah
license: mit
task_categories:
- audio-classification
tags:
- antispoofing
- text-to-speech
- anti-spoofing
- audio-deepfake-detection
- speech
- benchmark
- arena-ready
pretty_name: LRL spoof
size_categories:
- 1M<n<10M
configs:
- config_name: default
  data_files:
  - split: test
    path: lrl_spoof.tar.gz.part_*
viewer: false
arxiv:
- '2603.02364'
---

# LRLspoof

[![arXiv](https://img.shields.io/badge/arXiv-2603.02364-b31b1b.svg)](https://arxiv.org/abs/2603.02364)
[![Conference](https://img.shields.io/badge/INTERSPEECH-2026-1f6feb.svg)](https://arxiv.org/abs/2603.02364)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> [!IMPORTANT]
> **Official dataset for our INTERSPEECH 2026 paper**
> *"When Spoof Detectors Travel: Evaluation Across 66 Languages in the
> Low-Resource Language Spoofing Corpus"* ([arXiv:2603.02364](https://arxiv.org/abs/2603.02364)).
> This repository hosts the benchmark, evaluation protocol, and baseline
> submissions released with the paper. If you use LRLspoof, please
> [cite it](#citation).

Multilingual low-resource-language anti-spoofing benchmark: 1,304,455 TTS (spoof)
utterances across 66 languages and many TTS systems. **Spoof-only** (no bonafide).

The audio ships as the multi-part tarball `lrl_spoof.tar.gz.part_*`; download +
extract it into a `<language>/<tts_model>/<file>.wav` tree. `load_dataset` is not
the access path here (the dataset is the tarball). `data/labels.parquet`
(utterance_id + label, all spoof) exists only for arena re-verification.

## Arena scoring
Scored on **1-SRR** (`srr_complement`, lower is better) at a fixed threshold t*
**calibrated on DeepVoice**. A submission must include a `calibration` block with
the DeepVoice operating-point threshold.

## utterance_id convention
`utterance_id` = the audio file path relative to the dataset root, e.g.
`english/fastpitch/line_59.wav`. A submitter's `scores.txt` keys by this id;
emit `<utterance_id> <score>` with higher score = more bonafide.

## Citation

If you use LRLspoof, please cite our INTERSPEECH 2026 paper:

```bibtex
@inproceedings{borodin2026lrlspoof,
  title     = {When Spoof Detectors Travel: Evaluation Across 66 Languages
               in the Low-Resource Language Spoofing Corpus},
  author    = {Borodin, Kirill and Kudryavtsev, Vasiliy and Maslov, Maxim
               and Gorodnichev, Mikhail and Mkrtchian, Grach},
  booktitle = {Proc. INTERSPEECH 2026},
  year      = {2026},
  note      = {arXiv:2603.02364},
  url       = {https://arxiv.org/abs/2603.02364}
}
```

## Contact

- Email: kborodin.research@gmail.com
- Telegram: [@korallll_ai](https://t.me/korallll_ai)
