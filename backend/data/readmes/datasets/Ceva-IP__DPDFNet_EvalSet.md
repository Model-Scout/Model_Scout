---
pretty_name: DPDFNet - Evaluation Set
tags:
- audio
- speech
- speech-enhancement
- noise-suppression
- evaluation
language:
- ar
- nl
- fr
- de
- hu
- ko
- pl
- pt
- ru
- es
- tr
- vi
license: apache-2.0
size_categories:
- 1K<n<10K
---

# DPDFNet: Evaluation Set

A **multilingual, long-form, low-SNR** evaluation set introduced in the paper **“DPDFNet: Boosting DeepFilterNet2 via Dual-Path RNN”**.

## At a glance

- **12 languages**: arabic, dutch, french, german, hungarian, korean, polish, portuguese, russian, spanish, turkish, vietnamese
- **9 noise scenes**: airport, car, office, pub, rain, restaurant, street, subway, train
- **SNR (dB)**: 0 / 5 / 10  
- **Duration**: ~2.5 minutes per clip (includes **speech-free intervals**)  
- **Size**: **324 clips** (~**13.5 hours**)

## What you get

This repo is meant for **evaluation**, and it includes:

- **Noisy mixtures**
- **Clean references**
- **Enhanced outputs** from the models reported in the paper (ours and open-source)

## Recommended use

Use this set to evaluate:
- **Causal / streaming** enhancement models on long recordings
- Robustness to **silence → speech transitions**, **non-stationary noises**, and **multilingual** speech
- Stability on clips that may contain **multiple speakers** within a single recording

## Citation

If you use this evaluation set, please cite the DPDFNet paper:

```bibtex
@article{rika2025dpdfnet,
  title   = {DPDFNet: Boosting DeepFilterNet2 via Dual-Path RNN},
  author  = {Rika, Daniel and Sapir, Nino and Gus, Ido},
  year    = {2025}
}
```