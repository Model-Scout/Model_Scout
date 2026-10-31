---
license: cc-by-nc-sa-4.0
task_categories:
- text-to-audio
- text-to-speech
language:
- zh
- en
- fr
- ja
- ko
- es
- de
- ru
- it
tags:
- singing
- audio
- croissant
pretty_name: a
size_categories:
- 1B<n<10B
configs:
- config_name: meta
  data_files: processed/All/metadata.json
---

#  GTSinger: A Global Multi-Technique Singing Corpus with Realistic Music Scores for All Singing Tasks

#### Yu Zhang*, Changhao Pan*, Wenxiang Guo*, Ruiqi Li, Zhiyuan Zhu, Jialei Wang, Wenhao Xu, Jingyu Lu, Zhiqing Hong, Chuxin Wang, LiChao Zhang, Jinzheng He, Ziyue Jiang, Yuxin Chen, Chen Yang, Jiecheng Zhou, Xinyu Cheng, Zhou Zhao | Zhejiang University

Dataset of [GTSinger (NeurIPS 2024 Spotlight)](https://arxiv.org/abs/2409.13832): A Global Multi-Technique Singing Corpus with Realistic Music Scores for All Singing Tasks.

[![arXiv](https://img.shields.io/badge/arXiv-Paper-<COLOR>.svg)](https://arxiv.org/abs/2409.13832) 
[![GitHub](https://img.shields.io/badge/GitHub-Repo-black.svg)](https://github.com/AaronZ345/GTSinger)
[![weixin](https://img.shields.io/badge/-WeChat@机器之心-000000?logo=wechat&logoColor=07C160)](https://mp.weixin.qq.com/s/B1Iqr-24l57f0MslzYEslA)
[![weixin](https://img.shields.io/badge/-WeChat@PaperWeekly-000000?logo=wechat&logoColor=07C160)](https://mp.weixin.qq.com/s/6RLdUzJM5PItklKUTTNz2w)
[![zhihu](https://img.shields.io/badge/-知乎-000000?logo=zhihu&logoColor=0084FF)](https://zhuanlan.zhihu.com/p/993933492)
[![Google Drive](https://img.shields.io/badge/Google%20Drive-Link-blue?logo=googledrive&logoColor=white)](https://drive.google.com/drive/folders/1xcdvCxNAEEfJElt7sEP-xT8dMKxn1_Lz?usp=drive_link)

We introduce GTSinger, a large Global, multi-Technique, free-to-use, high-quality singing corpus with realistic music scores, designed for all singing tasks, along with its benchmarks.

We provide the **full corpus for free** in this repository. 

And `metadata.json` and `phone_set.json` are also offered for each language in `processed`. **Note: you should change the wav_fn for each segment to your own absolute path! And you can use metadata of multiple languages by concat their data! We will provide the metadata for other languages soon!**

Besides, we also provide our dataset on [Google Drive](https://drive.google.com/drive/folders/1xcdvCxNAEEfJElt7sEP-xT8dMKxn1_Lz?usp=drive_link).

Moreover, you can visit our [Demo Page](https://aaronz345.github.io/GTSingerDemo) for the audio samples of our dataset as well as the results of our benchmarks.

## Updates

- 2025.02: We released all processed data of GTSinger and refined 7/9 languages!
- 2024.10: We refine the paired speech data of each language!
- 2024.10: We released the processed data of Chinese, English, Spanish, German, Russian!
- 2024.09: We released the full dataset of GTSinger!
- 2024.09: GTSinger is accepted by NeurIPS 2024 (Spotlight)!

## Key Features

- **80.59 hours of singing voices** in GTSinger are recorded in professional studios by skilled singers, ensuring **high quality and clarity**, forming the largest recorded singing dataset.
- Contributed by **20 singers** across **nine widely spoken languages** (Chinese, English, Japanese, Korean, Russian, Spanish, French, German, and Italian) and all four vocal ranges, GTSinger enables zero-shot SVS and style transfer models to learn diverse timbres and styles.
- GTSinger provides **controlled comparison** and **phoneme-level annotations** of **six singing techniques** (mixed voice, falsetto, breathy, pharyngeal, vibrato, and glissando) for songs, thereby facilitating singing technique modeling, recognition, and control.
- Unlike fine-grained music scores, GTSinger features **realistic music scores** with regular note duration, assisting singing models in learning and adapting to real-world musical composition.
- The dataset includes **manual phoneme-to-audio alignments, global style labels** (singing method, emotion, range, and pace), and **16.16 hours of paired speech**, ensuring comprehensive annotations and broad task suitability.

## Dataset

### Where to download

Through this repo you can access our **full dataset** (audio along with TextGrid, json, musicxml) and **processed data** (metadata.json, phone_set.json, spker_set.json) on Hugging Face **for free**! Hope our data is helpful for your research.

Besides, we also provide our dataset on [![Google Drive](https://img.shields.io/badge/Google%20Drive-Link-blue?logo=googledrive&logoColor=white)](https://drive.google.com/drive/folders/1xcdvCxNAEEfJElt7sEP-xT8dMKxn1_Lz?usp=drive_link).

**Please note that, if you are using GTSinger, it means that you have accepted the terms of [license](./dataset_license.md).**

### Data Architecture

Our dataset is organized hierarchically. 

It presents nine top-level folders, each corresponding to a distinct language. 

Within each language folder, there are five sub-folders, each representing a specific singing technique.

These technique folders contain numerous song entries, with each song further divided into several controlled comparison groups: a control group (natural singing without the specific technique), and a technique group (densely employing the specific technique).

Our singing voices and speech are recorded at a 48kHz sampling rate with 24-bit resolution in WAV format. 

Alignments and annotations are provided in TextGrid files, including word boundaries, phoneme boundaries, phoneme-level annotations for six techniques, and global style labels (singing method, emotion, pace, and range). 

We also provide realistic music scores in musicxml format.

Notably, we provide an additional JSON file for each singing voice, facilitating data parsing and processing for singing models.

Here is the data structure of our dataset:

```
.
├── Chinese
│   ├── ZH-Alto-1
│   └── ZH-Tenor-1
├── English
│   ├── EN-Alto-1
│   │   ├── Breathy
│   │   ├── Glissando
│   │   │   └── my love
│   │   │       ├── Control_Group
│   │   │       ├── Glissando_Group
│   │   │       └── Paired_Speech_Group
│   │   ├── Mixed_Voice_and_Falsetto
│   │   ├── Pharyngeal
│   │   └── Vibrato
│   ├── EN-Alto-2
│   │   ├── Breathy
│   │   ├── Glissando
│   │   ├── Mixed_Voice_and_Falsetto
│   │   ├── Pharyngeal
│   │   └── Vibrato
│   └── EN-Tenor-1
│       ├── Breathy
│       ├── Glissando
│       ├── Mixed_Voice_and_Falsetto
│       ├── Pharyngeal
│       └── Vibrato
├── French
│   ├── FR-Soprano-1
│   └── FR-Tenor-1
├── German
│   ├── DE-Soprano-1
│   └── DE-Tenor-1
├── Italian
│   ├── IT-Bass-1
│   ├── IT-Bass-2
│   └── IT-Soprano-1
├── Japanese
│   ├── JA-Soprano-1
│   └── JA-Tenor-1
├── Korean
│   ├── KO-Soprano-1
│   ├── KO-Soprano-2
│   └── KO-Tenor-1
├── Russian
│   └── RU-Alto-1
└── Spanish
    ├── ES-Bass-1
    └── ES-Soprano-1
```

## Citations ##

If you find this code useful in your research, please cite our work:
```bib
@article{zhang2024gtsinger,
  title={Gtsinger: A global multi-technique singing corpus with realistic music scores for all singing tasks},
  author={Zhang, Yu and Pan, Changhao and Guo, Wenxiang and Li, Ruiqi and Zhu, Zhiyuan and Wang, Jialei and Xu, Wenhao and Lu, Jingyu and Hong, Zhiqing and Wang, Chuxin and others},
  journal={arXiv preprint arXiv:2409.13832},
  year={2024}
}
```

## Disclaimer ##

Any organization or individual is prohibited from using any technology mentioned in this paper to generate someone's singing without his/her consent, including but not limited to government leaders, political figures, and celebrities. If you do not comply with this item, you could be in violation of copyright laws.