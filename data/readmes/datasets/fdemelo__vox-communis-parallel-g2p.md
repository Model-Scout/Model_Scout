---
language:
- ab
- am
- ba
- be
- bg
- bn
- ca
- cs
- cv
- ckb
- dv
- el
- eu
- gn
- ha
- hi
- hsb
- hu
- hy
- id
- it
- ja
- ka
- kk
- ko
- ky
- lt
- mk
- mn
- mr
- mt
- nl
- or
- pa
- pl
- pt
- ro
- ru
- rw
- sk
- sl
- sq
- sr
- sv
- sw
- ta
- th
- tk
- tr
- ug
- uk
- uz
- vi
- yo
- yue
- zh
tags:
- G2P
- Grapheme-to-phoneme
- Phonetics
- Linguistics
- Corpus
size_categories:
- n<1K
pretty_name: VXC
license: cc0-1.0
---

# VoxCommunis Parallel G2P dataset

This dataset was derived from the [VoxCommunis Corpus](https://huggingface.co/datasets/pacscilab/VoxCommunis) to provide pairs of utterances along with their
corresponding phonemes, side by side, as to ease the training of *grapheme-to-phoneme* (G2P) models.

The original VoxCommunis Corpus features force-aligned TextGrids with phone- and word-level segmentations derived from the [Mozilla Common Voice Corpus](https://commonvoice.mozilla.org/en/datasets).
The lexicons were developed using Epitran, the XPF Corpus, Charsiu, and some custom dictionaries. Manual correction was also applied by VoxCommunis.

The source TextGrids were used to collect the utterance duration, and pairs of time-aligned sentences along with their corresponding phonemes.
The phoneme set type, Epitran (`epi`), XPF (`xpf`), Charsiu (`chr`), and others (`vxc`, `cvu`) were inferred from the TextGrid file names.
Those collected attributes were then joined with the VoxCommunis `speaker_files` on a per language basis.

**Note**: Word separation is marked by the `|` character in the phonetic sentences.

The derived dataset herein inherits the distribution license from The Mozilla Common Voice Corpus, the VoxCommunis Corpus, and so is free to download and use
under a *CC0* license.
