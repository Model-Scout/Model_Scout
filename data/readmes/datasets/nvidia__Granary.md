---
license: cc-by-4.0
task_categories:
- automatic-speech-recognition
- translation
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
- it
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
- uk
pretty_name: Granary
size_categories:
- 10M<n<100M
tags:
- granary
- multilingual
- nemo
configs:
- config_name: sv_voxpopuli
  data_files:
  - path: sv/voxpopuli/sv_asr.jsonl
    split: asr
  - path: sv/voxpopuli/sv_ast-en.jsonl
    split: ast
- config_name: sv_ytc
  data_files:
  - path: sv/ytc/sv_asr.jsonl
    split: asr
  - path: sv/ytc/sv_ast-en.jsonl
    split: ast
- config_name: mt_voxpopuli
  data_files:
  - path: mt/voxpopuli/mt_ast-en.jsonl
    split: ast
  - path: mt/voxpopuli/mt_asr.jsonl
    split: asr
- config_name: sk_voxpopuli
  data_files:
  - path: sk/voxpopuli/sk_asr.jsonl
    split: asr
  - path: sk/voxpopuli/sk_ast-en.jsonl
    split: ast
- config_name: sk_ytc
  data_files:
  - path: sk/ytc/sk_asr.jsonl
    split: asr
  - path: sk/ytc/sk_ast-en.jsonl
    split: ast
- config_name: it_voxpopuli
  data_files:
  - path: it/voxpopuli/it_asr.jsonl
    split: asr
  - path: it/voxpopuli/it_ast-en.jsonl
    split: ast
- config_name: it_ytc
  data_files:
  - path: it/ytc/it_asr.jsonl
    split: asr
  - path: it/ytc/it_ast-en.jsonl
    split: ast
- config_name: en_voxpopuli
  data_files:
  - path: en/voxpopuli/en_asr.jsonl
    split: asr
- config_name: en_ytc
  data_files:
  - path: en/ytc/en_asr.jsonl
    split: asr
- config_name: en_librilight
  data_files:
  - path: en/librilight/en_asr.jsonl
    split: asr
- config_name: en_yodas
  data_files:
  - path: en/yodas/en_asr.jsonl
    split: asr
- config_name: pt_voxpopuli
  data_files:
  - path: pt/voxpopuli/pt_ast-en.jsonl
    split: ast
  - path: pt/voxpopuli/pt_asr.jsonl
    split: asr
- config_name: pt_ytc
  data_files:
  - path: pt/ytc/pt_ast-en.jsonl
    split: ast
  - path: pt/ytc/pt_asr.jsonl
    split: asr
- config_name: lv_voxpopuli
  data_files:
  - path: lv/voxpopuli/lv_ast-en.jsonl
    split: ast
  - path: lv/voxpopuli/lv_asr.jsonl
    split: asr
- config_name: lv_ytc
  data_files:
  - path: lv/ytc/lv_ast-en.jsonl
    split: ast
  - path: lv/ytc/lv_asr.jsonl
    split: asr
- config_name: ro_voxpopuli
  data_files:
  - path: ro/voxpopuli/ro_ast-en.jsonl
    split: ast
  - path: ro/voxpopuli/ro_asr.jsonl
    split: asr
- config_name: ro_ytc
  data_files:
  - path: ro/ytc/ro_ast-en.jsonl
    split: ast
  - path: ro/ytc/ro_asr.jsonl
    split: asr
- config_name: pl_voxpopuli
  data_files:
  - path: pl/voxpopuli/pl_asr.jsonl
    split: asr
  - path: pl/voxpopuli/pl_ast-en.jsonl
    split: ast
- config_name: pl_ytc
  data_files:
  - path: pl/ytc/pl_asr.jsonl
    split: asr
  - path: pl/ytc/pl_ast-en.jsonl
    split: ast
- config_name: sl_voxpopuli
  data_files:
  - path: sl/voxpopuli/sl_ast-en.jsonl
    split: ast
  - path: sl/voxpopuli/sl_asr.jsonl
    split: asr
- config_name: sl_ytc
  data_files:
  - path: sl/ytc/sl_ast-en.jsonl
    split: ast
  - path: sl/ytc/sl_asr.jsonl
    split: asr
- config_name: cs_voxpopuli
  data_files:
  - path: cs/voxpopuli/cs_asr.jsonl
    split: asr
  - path: cs/voxpopuli/cs_ast-en.jsonl
    split: ast
- config_name: cs_ytc
  data_files:
  - path: cs/ytc/cs_asr.jsonl
    split: asr
  - path: cs/ytc/cs_ast-en.jsonl
    split: ast
- config_name: cs_yodas
  data_files:
  - path: cs/yodas/cs_asr.jsonl
    split: asr
  - path: cs/yodas/cs_ast-en.jsonl
    split: ast
- config_name: el_voxpopuli
  data_files:
  - path: el/voxpopuli/el_asr.jsonl
    split: asr
  - path: el/voxpopuli/el_ast-en.jsonl
    split: ast
- config_name: el_ytc
  data_files:
  - path: el/ytc/el_asr.jsonl
    split: asr
  - path: el/ytc/el_ast-en.jsonl
    split: ast
- config_name: hu_voxpopuli
  data_files:
  - path: hu/voxpopuli/hu_asr.jsonl
    split: asr
  - path: hu/voxpopuli/hu_ast-en.jsonl
    split: ast
- config_name: hu_ytc
  data_files:
  - path: hu/ytc/hu_asr.jsonl
    split: asr
  - path: hu/ytc/hu_ast-en.jsonl
    split: ast
- config_name: lt_voxpopuli
  data_files:
  - path: lt/voxpopuli/lt_asr.jsonl
    split: asr
  - path: lt/voxpopuli/lt_ast-en.jsonl
    split: ast
- config_name: lt_ytc
  data_files:
  - path: lt/ytc/lt_asr.jsonl
    split: asr
  - path: lt/ytc/lt_ast-en.jsonl
    split: ast
- config_name: et_voxpopuli
  data_files:
  - path: et/voxpopuli/et_asr.jsonl
    split: asr
  - path: et/voxpopuli/et_ast-en.jsonl
    split: ast
- config_name: et_ytc
  data_files:
  - path: et/ytc/et_asr.jsonl
    split: asr
  - path: et/ytc/et_ast-en.jsonl
    split: ast
- config_name: fr_voxpopuli
  data_files:
  - path: fr/voxpopuli/fr_ast-en.jsonl
    split: ast
  - path: fr/voxpopuli/fr_asr.jsonl
    split: asr
- config_name: fr_ytc
  data_files:
  - path: fr/ytc/fr_ast-en.jsonl
    split: ast
  - path: fr/ytc/fr_asr.jsonl
    split: asr
- config_name: da_voxpopuli
  data_files:
  - path: da/voxpopuli/da_asr.jsonl
    split: asr
  - path: da/voxpopuli/da_ast-en.jsonl
    split: ast
- config_name: da_ytc
  data_files:
  - path: da/ytc/da_asr.jsonl
    split: asr
  - path: da/ytc/da_ast-en.jsonl
    split: ast
- config_name: da_yodas
  data_files:
  - path: da/yodas/da_asr.jsonl
    split: asr
  - path: da/yodas/da_ast-en.jsonl
    split: ast
- config_name: bg_voxpopuli
  data_files:
  - path: bg/voxpopuli/bg_asr.jsonl
    split: asr
  - path: bg/voxpopuli/bg_ast-en.jsonl
    split: ast
- config_name: bg_ytc
  data_files:
  - path: bg/ytc/bg_asr.jsonl
    split: asr
  - path: bg/ytc/bg_ast-en.jsonl
    split: ast
- config_name: bg_yodas
  data_files:
  - path: bg/yodas/bg_asr.jsonl
    split: asr
  - path: bg/yodas/bg_ast-en.jsonl
    split: ast
- config_name: es_voxpopuli
  data_files:
  - path: es/voxpopuli/es_asr.jsonl
    split: asr
  - path: es/voxpopuli/es_ast-en.jsonl
    split: ast
- config_name: es_ytc
  data_files:
  - path: es/ytc/es_asr.jsonl
    split: asr
  - path: es/ytc/es_ast-en.jsonl
    split: ast
- config_name: nl_voxpopuli
  data_files:
  - path: nl/voxpopuli/nl_ast-en.jsonl
    split: ast
  - path: nl/voxpopuli/nl_asr.jsonl
    split: asr
- config_name: nl_ytc
  data_files:
  - path: nl/ytc/nl_ast-en.jsonl
    split: ast
  - path: nl/ytc/nl_asr.jsonl
    split: asr
- config_name: hr_voxpopuli
  data_files:
  - path: hr/voxpopuli/hr_ast-en.jsonl
    split: ast
  - path: hr/voxpopuli/hr_asr.jsonl
    split: asr
- config_name: hr_ytc
  data_files:
  - path: hr/ytc/hr_ast-en.jsonl
    split: ast
  - path: hr/ytc/hr_asr.jsonl
    split: asr
- config_name: fi_voxpopuli
  data_files:
  - path: fi/voxpopuli/fi_asr.jsonl
    split: asr
  - path: fi/voxpopuli/fi_ast-en.jsonl
    split: ast
- config_name: fi_ytc
  data_files:
  - path: fi/ytc/fi_asr.jsonl
    split: asr
  - path: fi/ytc/fi_ast-en.jsonl
    split: ast
- config_name: uk_ytc
  data_files:
  - path: uk/ytc/uk_asr.jsonl
    split: asr
  - path: uk/ytc/uk_ast-en.jsonl
    split: ast
- config_name: de_voxpopuli
  data_files:
  - path: de/voxpopuli/de_asr.jsonl
    split: asr
  - path: de/voxpopuli/de_ast-en.jsonl
    split: ast
- config_name: de_ytc
  data_files:
  - path: de/ytc/de_asr.jsonl
    split: asr
  - path: de/ytc/de_ast-en.jsonl
    split: ast
- config_name: de_yodas
  data_files:
  - path: de/yodas/de_asr.jsonl
    split: asr
  - path: de/yodas/de_ast-en.jsonl
    split: ast
- config_name: sv
  data_files:
  - path:
    - sv/voxpopuli/sv_asr.jsonl
    - sv/ytc/sv_asr.jsonl
    split: asr
  - path:
    - sv/voxpopuli/sv_ast-en.jsonl
    - sv/ytc/sv_ast-en.jsonl
    split: ast
- config_name: mt
  data_files:
  - path:
    - mt/voxpopuli/mt_ast-en.jsonl
    split: ast
  - path:
    - mt/voxpopuli/mt_asr.jsonl
    split: asr
- config_name: sk
  data_files:
  - path:
    - sk/voxpopuli/sk_asr.jsonl
    - sk/ytc/sk_asr.jsonl
    split: asr
  - path:
    - sk/voxpopuli/sk_ast-en.jsonl
    - sk/ytc/sk_ast-en.jsonl
    split: ast
- config_name: it
  data_files:
  - path:
    - it/voxpopuli/it_asr.jsonl
    - it/ytc/it_asr.jsonl
    split: asr
  - path:
    - it/voxpopuli/it_ast-en.jsonl
    - it/ytc/it_ast-en.jsonl
    split: ast
- config_name: en
  data_files:
  - path:
    - en/voxpopuli/en_asr.jsonl
    - en/ytc/en_asr.jsonl
    - en/librilight/en_asr.jsonl
    - en/yodas/en_asr.jsonl
    split: asr
- config_name: pt
  data_files:
  - path:
    - pt/voxpopuli/pt_ast-en.jsonl
    - pt/ytc/pt_ast-en.jsonl
    split: ast
  - path:
    - pt/voxpopuli/pt_asr.jsonl
    - pt/ytc/pt_asr.jsonl
    split: asr
- config_name: lv
  data_files:
  - path:
    - lv/voxpopuli/lv_ast-en.jsonl
    - lv/ytc/lv_ast-en.jsonl
    split: ast
  - path:
    - lv/voxpopuli/lv_asr.jsonl
    - lv/ytc/lv_asr.jsonl
    split: asr
- config_name: ro
  data_files:
  - path:
    - ro/voxpopuli/ro_ast-en.jsonl
    - ro/ytc/ro_ast-en.jsonl
    split: ast
  - path:
    - ro/voxpopuli/ro_asr.jsonl
    - ro/ytc/ro_asr.jsonl
    split: asr
- config_name: pl
  data_files:
  - path:
    - pl/voxpopuli/pl_asr.jsonl
    - pl/ytc/pl_asr.jsonl
    split: asr
  - path:
    - pl/voxpopuli/pl_ast-en.jsonl
    - pl/ytc/pl_ast-en.jsonl
    split: ast
- config_name: sl
  data_files:
  - path:
    - sl/voxpopuli/sl_ast-en.jsonl
    - sl/ytc/sl_ast-en.jsonl
    split: ast
  - path:
    - sl/voxpopuli/sl_asr.jsonl
    - sl/ytc/sl_asr.jsonl
    split: asr
- config_name: cs
  data_files:
  - path:
    - cs/voxpopuli/cs_asr.jsonl
    - cs/ytc/cs_asr.jsonl
    - cs/yodas/cs_asr.jsonl
    split: asr
  - path:
    - cs/voxpopuli/cs_ast-en.jsonl
    - cs/ytc/cs_ast-en.jsonl
    - cs/yodas/cs_ast-en.jsonl
    split: ast
- config_name: el
  data_files:
  - path:
    - el/voxpopuli/el_asr.jsonl
    - el/ytc/el_asr.jsonl
    split: asr
  - path:
    - el/voxpopuli/el_ast-en.jsonl
    - el/ytc/el_ast-en.jsonl
    split: ast
- config_name: hu
  data_files:
  - path:
    - hu/voxpopuli/hu_asr.jsonl
    - hu/ytc/hu_asr.jsonl
    split: asr
  - path:
    - hu/voxpopuli/hu_ast-en.jsonl
    - hu/ytc/hu_ast-en.jsonl
    split: ast
- config_name: lt
  data_files:
  - path:
    - lt/voxpopuli/lt_asr.jsonl
    - lt/ytc/lt_asr.jsonl
    split: asr
  - path:
    - lt/voxpopuli/lt_ast-en.jsonl
    - lt/ytc/lt_ast-en.jsonl
    split: ast
- config_name: et
  data_files:
  - path:
    - et/voxpopuli/et_asr.jsonl
    - et/ytc/et_asr.jsonl
    split: asr
  - path:
    - et/voxpopuli/et_ast-en.jsonl
    - et/ytc/et_ast-en.jsonl
    split: ast
- config_name: fr
  data_files:
  - path:
    - fr/voxpopuli/fr_ast-en.jsonl
    - fr/ytc/fr_ast-en.jsonl
    split: ast
  - path:
    - fr/voxpopuli/fr_asr.jsonl
    - fr/ytc/fr_asr.jsonl
    split: asr
- config_name: da
  data_files:
  - path:
    - da/voxpopuli/da_asr.jsonl
    - da/ytc/da_asr.jsonl
    - da/yodas/da_asr.jsonl
    split: asr
  - path:
    - da/voxpopuli/da_ast-en.jsonl
    - da/ytc/da_ast-en.jsonl
    - da/yodas/da_ast-en.jsonl
    split: ast
- config_name: bg
  data_files:
  - path:
    - bg/voxpopuli/bg_asr.jsonl
    - bg/ytc/bg_asr.jsonl
    - bg/yodas/bg_asr.jsonl
    split: asr
  - path:
    - bg/voxpopuli/bg_ast-en.jsonl
    - bg/ytc/bg_ast-en.jsonl
    - bg/yodas/bg_ast-en.jsonl
    split: ast
- config_name: es
  data_files:
  - path:
    - es/voxpopuli/es_asr.jsonl
    - es/ytc/es_asr.jsonl
    split: asr
  - path:
    - es/voxpopuli/es_ast-en.jsonl
    - es/ytc/es_ast-en.jsonl
    split: ast
- config_name: nl
  data_files:
  - path:
    - nl/voxpopuli/nl_ast-en.jsonl
    - nl/ytc/nl_ast-en.jsonl
    split: ast
  - path:
    - nl/voxpopuli/nl_asr.jsonl
    - nl/ytc/nl_asr.jsonl
    split: asr
- config_name: hr
  data_files:
  - path:
    - hr/voxpopuli/hr_ast-en.jsonl
    - hr/ytc/hr_ast-en.jsonl
    split: ast
  - path:
    - hr/voxpopuli/hr_asr.jsonl
    - hr/ytc/hr_asr.jsonl
    split: asr
- config_name: fi
  data_files:
  - path:
    - fi/voxpopuli/fi_asr.jsonl
    - fi/ytc/fi_asr.jsonl
    split: asr
  - path:
    - fi/voxpopuli/fi_ast-en.jsonl
    - fi/ytc/fi_ast-en.jsonl
    split: ast
- config_name: uk
  data_files:
  - path:
    - uk/ytc/uk_asr.jsonl
    split: asr
  - path:
    - uk/ytc/uk_ast-en.jsonl
    split: ast
- config_name: de
  data_files:
  - path:
    - de/voxpopuli/de_asr.jsonl
    - de/ytc/de_asr.jsonl
    - de/yodas/de_asr.jsonl
    split: asr
  - path:
    - de/voxpopuli/de_ast-en.jsonl
    - de/ytc/de_ast-en.jsonl
    - de/yodas/de_ast-en.jsonl
    split: ast
---

# Granary: Speech Recognition and Translation Dataset in 25 European Languages

**Granary** is a large-scale, open-source multilingual speech dataset covering 25 European languages for Automatic Speech Recognition (ASR) and Automatic Speech Translation (AST) tasks. 

<div align="center">

| | |
|:---:|:---:|
| <img src="granary-icon.png" alt="Granary Icon" width="300"/> | <img src="granary_overview_figure_transparent.png" alt="Granary Overview" width="400"/> |

</div>


## Overview

Granary addresses the scarcity of high-quality speech data for low-resource languages by consolidating multiple datasets under a unified framework:

- **🗣️ ~1M hours** of high-quality pseudo-labeled ASR speech data across **25 languages** 
- **📊 Two main tasks**: ASR (transcription) and AST (X→English translation)  
- **🔧 Open-source pipeline** [NeMo SDP Granary pipeline](https://github.com/NVIDIA/NeMo-speech-data-processor/tree/main/dataset_configs/multilingual/granary) for generating similar datasets for additional languages
- **🤝 Collaborative effort** between [NVIDIA NeMo](https://github.com/NVIDIA/NeMo), [CMU](https://arxiv.org/pdf/2406.00899v1), and [FBK](https://huggingface.co/datasets/FBK-MT/mosel) teams

### Supported Languages
Bulgarian, Czech, Danish, German, Greek, English, Spanish, Estonian, Finnish, French, Croatian, Hungarian, Italian, Lithuanian, Latvian, Maltese, Dutch, Polish, Portuguese, Romanian, Slovak, Slovenian, Swedish, Ukrainian, Russian. 

## Pipeline & Quality

Granary employs a sophisticated two-stage processing pipeline ensuring high-quality, consistent data across all sources:

### Stage 1: ASR Processing  
1. **Audio Segmentation**: VAD + forced alignment for optimal chunks
2. **Two-Pass Inference**: Whisper-large-v3 with language ID verification
3. **Quality Filtering**: Remove hallucinations, invalid characters, low-quality segments
4. **P&C Restoration**: Qwen-2.5-7B for punctuation/capitalization normalization

### Stage 2: AST Processing
1. **Translation**: EuroLLM-9B for X→English translation from ASR outputs
2. **Quality Estimation**: Automatic scoring and confidence filtering
3. **Consistency Checks**: Length ratios, language ID validation, semantic coherence

This repository consolidates access to all Granary speech corpora with labels from different sources ([YODAS-Granary](https://huggingface.co/datasets/espnet/yodas-granary), [MOSEL](https://huggingface.co/datasets/FBK-MT/mosel)) in NeMo manifests format. 

Refer to this [blog](https://nvidia-nemo.github.io/blog/2025/08/13/granary-data-for-fine-tune/) on how to use Granary data for fine-tuning NeMo models.

## Dataset Components

> **⚠️ Important**: This repository provides manifests (metadata), not audio files. You need to download the original corpora and organize audio files in the structure below for the manifests to work.

Granary consolidates speech data from multiple high-quality sources. Refer to [this info](https://huggingface.co/datasets/nvidia/Granary/blob/main/Data_Downloading.md) on how to download these corpora from the sources and place in `<corpora/language>` format. 

### Primary Dataset Sources

#### 1. YODAS-Granary 
- **Repository**: [`espnet/yodas-granary`](https://huggingface.co/datasets/espnet/yodas-granary)
- **Content**: Direct-access speech data with embedded audio files (192k hours)
- **Sources**: YODAS2 
- **Languages**: 23 European languages

#### 2. MOSEL (Multi-corpus Collection)
- **Repository**: [`FBK-MT/mosel`](https://huggingface.co/datasets/FBK-MT/mosel) 
- **Content**: High-quality transcriptions for existing audio corpora (451k hours)
- **Sources**: VoxPopuli + YouTube-Commons + LibriLight
- **Languages**: 24 European languages + English


## Repository Structure

This repository contains **NeMo JSONL manifests** organized by language and corpus. For HuggingFace datasets usage, see the [Quick Start](#quick-start) section.

```
nvidia/granary/
├── <language>/                    # ISO 639-1 language codes (bg, de, en, etc.)
│   ├── yodas/                     # YODAS-Granary NeMo manifests
│   │   ├── <lang>_asr.jsonl       # ASR task manifests
│   │   └── <lang>_ast-en.jsonl    # AST task manifests (non-English only)
│   ├── voxpopuli/                 # VoxPopuli NeMo manifests (from MOSEL)
│   │   ├── <lang>_asr.jsonl
│   │   └── <lang>_ast-en.jsonl
│   ├── ytc/                       # YouTube-Commons NeMo manifests (from MOSEL)
│   │   ├── <lang>_asr.jsonl
│   │   └── <lang>_ast-en.jsonl
│   └── librilight/                # LibriLight NeMo manifests (English only)
│       └── en_asr.jsonl
```

### Data Organization
- **By Language**: Each language has its own directory with all available corpora
- **By Corpus**: Within each language, data is organized by source corpus
- **By Task**: ASR and AST manifests are clearly separated

## 🚀 Quick Start

### Prerequisites: Audio File Organization

**Required Audio Directory Structure:**
```
your_audio_directory/
├── yodas/              # YODAS-Granary audio (download from HuggingFace)
│   └── <language>/
│       └── *.wav       
├── voxpopuli/          # VoxPopuli audio (download separately)
│   └── <language>/
│       └── *.flac       
├── ytc/                # YouTube-Commons audio (download separately)
│   └── <language>/
│       └── *.wav       
└── librilight/         # LibriLight audio (English only)
    └── en/
        └── *.flac      
```


Once audio files are organized in `<corpus>/<language>/` format, you can access all Granary data with `load_dataset`. 


```python
from datasets import load_dataset

# 🌍 Language-level access (combines ALL corpora for a language)
ds = load_dataset("nvidia/granary", "de")                    # All German data (ASR + AST)
ds = load_dataset("nvidia/granary", "de", split="asr")       # All German ASR (YODAS + VoxPopuli + YTC)
ds = load_dataset("nvidia/granary", "de", split="ast")       # All German→English AST

# 🎯 Corpus-specific access
ds = load_dataset("nvidia/granary", "de_yodas")             # Only German YODAS data
ds = load_dataset("nvidia/granary", "de_voxpopuli")         # Only German VoxPopuli data
ds = load_dataset("nvidia/granary", "en_librilight")        # Only English LibriLight data

# 📡 Streaming for large datasets
ds = load_dataset("nvidia/granary", "de", streaming=True)   # Stream all German data
ds = load_dataset("nvidia/granary", "en", streaming=True)   # Stream all English data
```

**Available Configurations:**
- **76 total configurations** across 25 languages and 4 corpora
- **Language-level**: `de`, `en`, `fr`, `es`, `it`, etc. (24 configs)
- **Corpus-specific**: `de_yodas`, `de_voxpopuli`, `en_librilight`, etc. (52 configs)

## 📊 Data Sample Structure

Each sample in the dataset contains the following fields:

```python
{
    "audio_filepath": str,      # Path to audio file (e.g., "yodas/de/audio.wav")
    "text": str,               # Source language transcription 
    "duration": float,         # Duration in seconds
    "source_lang": str,        # Source language code (e.g., "de")
    "target_lang": str,        # Target language ("de" for ASR, "en" for AST)
    "taskname": str,           # Task type: "asr" or "ast"
    "utt_id": str,             # Unique utterance identifier
    "original_source_id": str, # Original audio/video ID
    "dataset_source": str,     # Corpus source: "yodas", "voxpopuli", "ytc", "librilight"
    "answer": str              # Target text (transcription for ASR, English translation for AST)
}
```

**What You Get by Configuration:**
- **`load_dataset("nvidia/granary", "de")`**: Mix of ASR + AST samples from all German corpora
- **`load_dataset("nvidia/granary", "de", split="asr")`**: Only ASR samples (German transcriptions)
- **`load_dataset("nvidia/granary", "de", split="ast")`**: Only AST samples (German→English translations)
- **`load_dataset("nvidia/granary", "de_yodas")`**: Only YODAS corpus data for German

## 🔧 NeMo Integration

For users of the [NVIDIA NeMo toolkit](https://github.com/NVIDIA/NeMo), ready-to-use manifest files are provided once audio is organized in `<corpus>/<language>/` format:

### Direct Usage
```python
# Use any manifest with NeMo toolkit for training/inference
manifest_path = "de/yodas/de_asr.jsonl"        # YODAS German ASR
manifest_path = "de/voxpopuli/de_asr.jsonl"    # VoxPopuli German ASR  
manifest_path = "de/voxpopuli/de_ast-en.jsonl" # VoxPopuli German→English AST

# See NeMo ASR/AST documentation for training examples:
# https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/
```

### Audio File Organization

Ensure your audio files match the manifest `audio_filepath` entries:

```
your_audio_directory/
├── yodas/              # YODAS-Granary audio (from HF download)
│   └── <language>/
│       └── *.wav       
├── voxpopuli/          # VoxPopuli audio (download separately)
│   └── <language>/
│       └── *.flac       
├── ytc/                # YouTube-Commons audio (download separately)
│   └── <language>/
│       └── *.wav       
└── librilight/         # LibriLight audio (download separately)
    └── en/
        └── *.flac      
```

### WebDataset Conversion

For large-scale training, convert to optimized WebDataset format:

```bash
git clone https://github.com/NeMo.git
cd NeMo

python scripts/speech_recognition/convert_to_tarred_audio_dataset.py \
    --manifest_path=<path to the manifest file> \
    --target_dir=<path to output directory> \
    --num_shards=<number of tarfiles that will contain the audio> \
    --max_duration=<float representing maximum duration of audio samples> \
    --min_duration=<float representing minimum duration of audio samples> \
    --shuffle --shuffle_seed=1 \
    --sort_in_shards \
    --force_codec=flac \
    --workers=-1
```

Then you can leverage [lhotse with NeMo](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/datasets.html#lhotse-dataloading) to train efficently. 

### Generate Datasets for New Languages

You may also use the complete Granary pipeline to create similar datasets for additional languages:

```bash
# Use the full Granary processing pipeline via NeMo-speech-data-processor
git clone https://github.com/NVIDIA/NeMo-speech-data-processor.git
cd NeMo-speech-data-processor

# Configure for your target language and audio source
python main.py \
  --config-path=dataset_configs/multilingual/granary/ \
  --config-name=granary_pipeline.yaml \
  params.target_language="your_language" \
  params.audio_source="your_audio_corpus"
```

The pipeline includes:
- **ASR Processing**: Long-form segmentation, two-pass Whisper inference, language ID verification, robust filtering, P&C restoration
- **AST Processing**: EuroLLM-9B translation, quality estimation filtering, cross-lingual validation
- **Quality Control**: Hallucination detection, character rate filtering, metadata consistency checks

## 📊 Dataset Statistics

### Consolidated Overview
| Task | Languages | Total Hours | Description |
|------|-----------|-------------|-------------|
| **ASR** | 25 | ~643k | Speech recognition (transcription) |
| **AST** | 24 (non-English) | ~351k | Speech translation to English |


### Cross-Corpus Distribution
| Source | Languages | Filtered Hours | Data Access | Audio Format |
|--------|-----------|----------------|-------------|--------------|
| **YODAS** | 23 | 192,172 | Direct HF download | 16kHz WAV (embedded) |
| **VoxPopuli** | 24 | 206,116 | Transcriptions + separate audio | FLAC |
| **YouTube-Commons** | 24 | 122,475 | Transcriptions + separate audio | WAV |
| **LibriLight** | 1 (EN) | ~23,500 | Transcriptions + separate audio | FLAC |
| **Total** | 25 | 643,238 | Multiple access methods | Mixed formats |

## 📚 Citation

```bibtex
@misc{koluguri2025granaryspeechrecognitiontranslation,
      title={Granary: Speech Recognition and Translation Dataset in 25 European Languages}, 
      author={Nithin Rao Koluguri and Monica Sekoyan and George Zelenfroynd and Sasha Meister and Shuoyang Ding and Sofia Kostandian and He Huang and Nikolay Karpov and Jagadeesh Balam and Vitaly Lavrukhin and Yifan Peng and Sara Papi and Marco Gaido and Alessio Brutti and Boris Ginsburg},
      year={2025},
      eprint={2505.13404},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2505.13404}, 
}
```

## 📄 License

- **YODAS-Granary**: CC-BY-3.0 ([source](https://huggingface.co/datasets/espnet/yodas-granary))
- **MOSEL**: CC-BY-4.0 ([source](https://huggingface.co/datasets/FBK-MT/mosel))
- **Original Audio Corpora**: See respective source licenses (VoxPopuli, LibriLight, YouTube-Commons)

## 🤝 Acknowledgments

Granary is a collaborative effort between:
- **NVIDIA NeMo Team**: Pipeline development, NeMo integration, and dataset consolidation
- **Carnegie Mellon University (CMU)**: YODAS dataset contribution and curation
- **Fondazione Bruno Kessler (FBK)**: MOSEL corpus processing and YouTube-Commons integration

## 🔗 Related Links

- 📊 **Datasets**: [YODAS-Granary](https://huggingface.co/datasets/espnet/yodas-granary) • [MOSEL](https://huggingface.co/datasets/FBK-MT/mosel)
- 🛠️ **Training**: [NVIDIA NeMo Toolkit](https://github.com/NVIDIA/NeMo) • [NeMo ASR Documentation](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/)
- 🔧 **Pipeline**: [NeMo-speech-data-processor](https://github.com/NVIDIA/NeMo-speech-data-processor/tree/main/dataset_configs/multilingual/granary)
- 🔬 **Publication**: [Paper (arXiv:2505.13404)](https://arxiv.org/abs/2505.13404)

---

