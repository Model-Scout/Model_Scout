---
dataset_info:
- config_name: acoustic_atlas
  features:
  - name: id
    dtype: string
  - name: number
    dtype: string
  - name: section_id
    dtype: string
  - name: section_title
    dtype: string
  - name: type
    dtype: string
  - name: points
    dtype: float64
  - name: context
    dtype: string
  - name: prompt
    dtype: string
  - name: options
    list: string
  - name: blanks
    list: string
  - name: matching
    dtype: string
  - name: grading
    dtype: string
  - name: images
    list: image
  - name: image_alts
    list: string
  splits:
  - name: test
    num_bytes: 15250294
    num_examples: 48
  download_size: 15250761
  dataset_size: 15250294
- config_name: control_blank_image
  features:
  - name: id
    dtype: string
  - name: number
    dtype: string
  - name: section_id
    dtype: string
  - name: section_title
    dtype: string
  - name: type
    dtype: string
  - name: points
    dtype: float64
  - name: context
    dtype: string
  - name: prompt
    dtype: string
  - name: options
    list: string
  - name: blanks
    list: string
  - name: matching
    dtype: string
  - name: grading
    dtype: string
  - name: images
    list: image
  - name: image_alts
    list: string
  splits:
  - name: test
    num_bytes: 360050
    num_examples: 48
  download_size: 359777
  dataset_size: 360050
- config_name: control_mel_shuffled
  features:
  - name: id
    dtype: string
  - name: number
    dtype: string
  - name: section_id
    dtype: string
  - name: section_title
    dtype: string
  - name: type
    dtype: string
  - name: points
    dtype: float64
  - name: context
    dtype: string
  - name: prompt
    dtype: string
  - name: options
    list: string
  - name: blanks
    list: string
  - name: matching
    dtype: string
  - name: grading
    dtype: string
  - name: images
    list: image
  - name: image_alts
    list: string
  splits:
  - name: test
    num_bytes: 5495837
    num_examples: 48
  download_size: 5495898
  dataset_size: 5495837
- config_name: control_no_image
  features:
  - name: id
    dtype: string
  - name: number
    dtype: string
  - name: section_id
    dtype: string
  - name: section_title
    dtype: string
  - name: type
    dtype: string
  - name: points
    dtype: float64
  - name: context
    dtype: string
  - name: prompt
    dtype: string
  - name: options
    list: string
  - name: blanks
    list: string
  - name: matching
    dtype: string
  - name: grading
    dtype: string
  - name: images
    list: image
  - name: image_alts
    list: string
  splits:
  - name: test
    num_bytes: 13100
    num_examples: 48
  download_size: 13603
  dataset_size: 13100
- config_name: cqt
  features:
  - name: id
    dtype: string
  - name: number
    dtype: string
  - name: section_id
    dtype: string
  - name: section_title
    dtype: string
  - name: type
    dtype: string
  - name: points
    dtype: float64
  - name: context
    dtype: string
  - name: prompt
    dtype: string
  - name: options
    list: string
  - name: blanks
    list: string
  - name: matching
    dtype: string
  - name: grading
    dtype: string
  - name: images
    list: image
  - name: image_alts
    list: string
  splits:
  - name: test
    num_bytes: 14615183
    num_examples: 48
  download_size: 14615600
  dataset_size: 14615183
- config_name: erb
  features:
  - name: id
    dtype: string
  - name: number
    dtype: string
  - name: section_id
    dtype: string
  - name: section_title
    dtype: string
  - name: type
    dtype: string
  - name: points
    dtype: float64
  - name: context
    dtype: string
  - name: prompt
    dtype: string
  - name: options
    list: string
  - name: blanks
    list: string
  - name: matching
    dtype: string
  - name: grading
    dtype: string
  - name: images
    list: image
  - name: image_alts
    list: string
  splits:
  - name: test
    num_bytes: 3134692
    num_examples: 48
  download_size: 3134600
  dataset_size: 3134692
- config_name: mel
  features:
  - name: id
    dtype: string
  - name: number
    dtype: string
  - name: section_id
    dtype: string
  - name: section_title
    dtype: string
  - name: type
    dtype: string
  - name: points
    dtype: float64
  - name: context
    dtype: string
  - name: prompt
    dtype: string
  - name: options
    list: string
  - name: blanks
    list: string
  - name: matching
    dtype: string
  - name: grading
    dtype: string
  - name: images
    list: image
  - name: image_alts
    list: string
  splits:
  - name: test
    num_bytes: 5495837
    num_examples: 48
  download_size: 5495942
  dataset_size: 5495837
- config_name: mel_periodicity
  features:
  - name: id
    dtype: string
  - name: number
    dtype: string
  - name: section_id
    dtype: string
  - name: section_title
    dtype: string
  - name: type
    dtype: string
  - name: points
    dtype: float64
  - name: context
    dtype: string
  - name: prompt
    dtype: string
  - name: options
    list: string
  - name: blanks
    list: string
  - name: matching
    dtype: string
  - name: grading
    dtype: string
  - name: images
    list: image
  - name: image_alts
    list: string
  splits:
  - name: test
    num_bytes: 14218554
    num_examples: 48
  download_size: 14218979
  dataset_size: 14218554
- config_name: modulation
  features:
  - name: id
    dtype: string
  - name: number
    dtype: string
  - name: section_id
    dtype: string
  - name: section_title
    dtype: string
  - name: type
    dtype: string
  - name: points
    dtype: float64
  - name: context
    dtype: string
  - name: prompt
    dtype: string
  - name: options
    list: string
  - name: blanks
    list: string
  - name: matching
    dtype: string
  - name: grading
    dtype: string
  - name: images
    list: image
  - name: image_alts
    list: string
  splits:
  - name: test
    num_bytes: 3530256
    num_examples: 48
  download_size: 3530164
  dataset_size: 3530256
- config_name: multires_stft
  features:
  - name: id
    dtype: string
  - name: number
    dtype: string
  - name: section_id
    dtype: string
  - name: section_title
    dtype: string
  - name: type
    dtype: string
  - name: points
    dtype: float64
  - name: context
    dtype: string
  - name: prompt
    dtype: string
  - name: options
    list: string
  - name: blanks
    list: string
  - name: matching
    dtype: string
  - name: grading
    dtype: string
  - name: images
    list: image
  - name: image_alts
    list: string
  splits:
  - name: test
    num_bytes: 30603752
    num_examples: 48
  download_size: 30604795
  dataset_size: 30603752
- config_name: periodicity
  features:
  - name: id
    dtype: string
  - name: number
    dtype: string
  - name: section_id
    dtype: string
  - name: section_title
    dtype: string
  - name: type
    dtype: string
  - name: points
    dtype: float64
  - name: context
    dtype: string
  - name: prompt
    dtype: string
  - name: options
    list: string
  - name: blanks
    list: string
  - name: matching
    dtype: string
  - name: grading
    dtype: string
  - name: images
    list: image
  - name: image_alts
    list: string
  splits:
  - name: test
    num_bytes: 11783058
    num_examples: 48
  download_size: 11783419
  dataset_size: 11783058
- config_name: prosody_voice
  features:
  - name: id
    dtype: string
  - name: number
    dtype: string
  - name: section_id
    dtype: string
  - name: section_title
    dtype: string
  - name: type
    dtype: string
  - name: points
    dtype: float64
  - name: context
    dtype: string
  - name: prompt
    dtype: string
  - name: options
    list: string
  - name: blanks
    list: string
  - name: matching
    dtype: string
  - name: grading
    dtype: string
  - name: images
    list: image
  - name: image_alts
    list: string
  splits:
  - name: test
    num_bytes: 5825214
    num_examples: 48
  download_size: 5825227
  dataset_size: 5825214
- config_name: reassigned
  features:
  - name: id
    dtype: string
  - name: number
    dtype: string
  - name: section_id
    dtype: string
  - name: section_title
    dtype: string
  - name: type
    dtype: string
  - name: points
    dtype: float64
  - name: context
    dtype: string
  - name: prompt
    dtype: string
  - name: options
    list: string
  - name: blanks
    list: string
  - name: matching
    dtype: string
  - name: grading
    dtype: string
  - name: images
    list: image
  - name: image_alts
    list: string
  splits:
  - name: test
    num_bytes: 13740021
    num_examples: 48
  download_size: 13740492
  dataset_size: 13740021
- config_name: scalogram
  features:
  - name: id
    dtype: string
  - name: number
    dtype: string
  - name: section_id
    dtype: string
  - name: section_title
    dtype: string
  - name: type
    dtype: string
  - name: points
    dtype: float64
  - name: context
    dtype: string
  - name: prompt
    dtype: string
  - name: options
    list: string
  - name: blanks
    list: string
  - name: matching
    dtype: string
  - name: grading
    dtype: string
  - name: images
    list: image
  - name: image_alts
    list: string
  splits:
  - name: test
    num_bytes: 8408513
    num_examples: 48
  download_size: 8408774
  dataset_size: 8408513
- config_name: source_filter
  features:
  - name: id
    dtype: string
  - name: number
    dtype: string
  - name: section_id
    dtype: string
  - name: section_title
    dtype: string
  - name: type
    dtype: string
  - name: points
    dtype: float64
  - name: context
    dtype: string
  - name: prompt
    dtype: string
  - name: options
    list: string
  - name: blanks
    list: string
  - name: matching
    dtype: string
  - name: grading
    dtype: string
  - name: images
    list: image
  - name: image_alts
    list: string
  splits:
  - name: test
    num_bytes: 8917521
    num_examples: 48
  download_size: 8917786
  dataset_size: 8917521
- config_name: speech_atlas
  features:
  - name: id
    dtype: string
  - name: number
    dtype: string
  - name: section_id
    dtype: string
  - name: section_title
    dtype: string
  - name: type
    dtype: string
  - name: points
    dtype: float64
  - name: context
    dtype: string
  - name: prompt
    dtype: string
  - name: options
    list: string
  - name: blanks
    list: string
  - name: matching
    dtype: string
  - name: grading
    dtype: string
  - name: images
    list: image
  - name: image_alts
    list: string
  splits:
  - name: test
    num_bytes: 9966888
    num_examples: 48
  download_size: 9967149
  dataset_size: 9966888
- config_name: stft
  features:
  - name: id
    dtype: string
  - name: number
    dtype: string
  - name: section_id
    dtype: string
  - name: section_title
    dtype: string
  - name: type
    dtype: string
  - name: points
    dtype: float64
  - name: context
    dtype: string
  - name: prompt
    dtype: string
  - name: options
    list: string
  - name: blanks
    list: string
  - name: matching
    dtype: string
  - name: grading
    dtype: string
  - name: images
    list: image
  - name: image_alts
    list: string
  splits:
  - name: test
    num_bytes: 14936105
    num_examples: 48
  download_size: 14936576
  dataset_size: 14936105
- config_name: waveform
  features:
  - name: id
    dtype: string
  - name: number
    dtype: string
  - name: section_id
    dtype: string
  - name: section_title
    dtype: string
  - name: type
    dtype: string
  - name: points
    dtype: float64
  - name: context
    dtype: string
  - name: prompt
    dtype: string
  - name: options
    list: string
  - name: blanks
    list: string
  - name: matching
    dtype: string
  - name: grading
    dtype: string
  - name: images
    list: image
  - name: image_alts
    list: string
  splits:
  - name: test
    num_bytes: 3435058
    num_examples: 48
  download_size: 3434966
  dataset_size: 3435058
- config_name: waveform_mel
  features:
  - name: id
    dtype: string
  - name: number
    dtype: string
  - name: section_id
    dtype: string
  - name: section_title
    dtype: string
  - name: type
    dtype: string
  - name: points
    dtype: float64
  - name: context
    dtype: string
  - name: prompt
    dtype: string
  - name: options
    list: string
  - name: blanks
    list: string
  - name: matching
    dtype: string
  - name: grading
    dtype: string
  - name: images
    list: image
  - name: image_alts
    list: string
  splits:
  - name: test
    num_bytes: 7557012
    num_examples: 48
  download_size: 7557182
  dataset_size: 7557012
configs:
- config_name: acoustic_atlas
  data_files:
  - split: test
    path: acoustic_atlas/test-*
- config_name: control_blank_image
  data_files:
  - split: test
    path: control_blank_image/test-*
- config_name: control_mel_shuffled
  data_files:
  - split: test
    path: control_mel_shuffled/test-*
- config_name: control_no_image
  data_files:
  - split: test
    path: control_no_image/test-*
- config_name: cqt
  data_files:
  - split: test
    path: cqt/test-*
- config_name: erb
  data_files:
  - split: test
    path: erb/test-*
- config_name: mel
  data_files:
  - split: test
    path: mel/test-*
- config_name: mel_periodicity
  data_files:
  - split: test
    path: mel_periodicity/test-*
- config_name: modulation
  data_files:
  - split: test
    path: modulation/test-*
- config_name: multires_stft
  data_files:
  - split: test
    path: multires_stft/test-*
- config_name: periodicity
  data_files:
  - split: test
    path: periodicity/test-*
- config_name: prosody_voice
  data_files:
  - split: test
    path: prosody_voice/test-*
- config_name: reassigned
  data_files:
  - split: test
    path: reassigned/test-*
- config_name: scalogram
  data_files:
  - split: test
    path: scalogram/test-*
- config_name: source_filter
  data_files:
  - split: test
    path: source_filter/test-*
- config_name: speech_atlas
  data_files:
  - split: test
    path: speech_atlas/test-*
- config_name: stft
  data_files:
  - split: test
    path: stft/test-*
- config_name: waveform
  data_files:
  - split: test
    path: waveform/test-*
- config_name: waveform_mel
  data_files:
  - split: test
    path: waveform_mel/test-*
language:
- en
- de
- es
- fr
- zh
- ja
- ko
- ar
license: other
task_categories:
- question-answering
pretty_name: AuraBench
tags:
- audio
- vision-language
- spectrogram
- benchmark
- any-to-bench
- signal-processing
- exam
---
# AuraBench Dataset Card

## Summary

AuraBench contains 48 canonical audio questions rendered under 16 deterministic
signal-processing image conditions. Every condition uses the same source waveform,
question, options, and deterministic answer key. Three additional controls remove the
image, replace it with a uniform blank image, or permute mel images within each task
family.

The shuffled-image control uses a deterministic semantic derangement within each
compatible choice set: no image remains on its source question, no image crosses to a
different option vocabulary, and every source image's ground-truth label differs from
the target question's answer. Its taker-visible exam identity matches the ordinary Mel
condition, so the model is not told that image labels have been permuted.

Evaluated models receive image and text inputs only. The Any-to-Bench bundles do not
contain audio files, transcripts, source filenames, corpus labels, or descriptive alt
text.

## Tasks

| Family | Questions | Labels |
|---|---:|---|
| Speaker category | 8 | corpus-provided female / male label |
| Language identification | 8 | English, German, Spanish, French, Mandarin Chinese, Japanese, Korean, Arabic |
| Sound-event classification | 8 | dog, rain, footsteps, keyboard, clock, helicopter, siren, glass |
| Phonetic content | 8 | four English vowels and two complete Mandarin aspiration pairs |
| Lexical recognition | 8 | isolated English digits |
| Emotional expression | 8 | happy, sad, angry, fearful, crossed with two actors |

All questions are single-choice and worth one point. Grading is deterministic.

Public question IDs are opaque random identifiers. They carry no family, source, or
ordinal meaning, and display numbers are omitted. Within each family, question order
is shuffled; every question has its own pinned option permutation; and correct-option
positions are counterbalanced for comparable choice sets. The same audited public
layout is used across every image condition to preserve paired evaluation.

## Evaluation integrity

The published Any-to-Bench bundles include `grading.json` so results can be reproduced.
That file must never be staged into the taker's workspace. For agentic CLI takers, a private
HOME, disabled web search, blocked shell network, and Codex `workspace-write` mode are still
insufficient by themselves: `workspace-write` permits reads elsewhere on the host, including
the source bundle and previous run outputs.

The reference AuraBench runner therefore applies an outer OS-level filesystem policy. The
taker can read and write its current ephemeral a2b run root and can read the pinned Codex
runtime, but it cannot read the project directory, other a2b workspaces, mounted volumes, or
network mounts, and cannot write outside its current run root. OS canaries verify these
boundaries before benchmark execution. See `scripts/hermetic-bin/codex` and
`scripts/run_matrix`.

The corrected reference matrix contains 38 condition-effort pairs and 76 model runs, all with
48/48 coverage and zero schema errors. The hidden shuffled-Mel control scores 7/48 and 10/48
for sol low/medium, compared with the former impossible 48/48 result obtained when host answer
keys were readable. Detailed results and SHA-256 digests are in `results/summary.json`.

## Image conditions

Atomic conditions are waveform, linear STFT, mel spectrogram, CQT,
multi-resolution STFT, reassigned spectrogram, wavelet scalogram, ERB cochleagram,
periodicity maps, modulation energy, source/filter tracks, and a prosody/voice-quality
dashboard. Combination conditions are waveform+mel, mel+periodicity, a speech atlas,
and a general acoustic atlas.

All transformations are classical DSP. AuraBench does not use ASR, neural audio
encoders, neural classifiers, learned embeddings, neural denoisers, or neural source
separation.

## Source corpora and licenses

| Corpus | Used for | Upstream license |
|---|---|---|
| [RAVDESS speech](https://zenodo.org/records/1188976) | speaker category, emotion | CC BY-NC-SA 4.0 |
| [FLEURS](https://huggingface.co/datasets/google/fleurs) | language identification | CC BY 4.0 |
| [ESC-50](https://github.com/karoldvl/ESC-50) | sound events | CC BY-NC 3.0; per-clip attribution remains applicable |
| [Hillenbrand et al. vowels](https://github.com/santiagobarreda/hillenbrand_et_al_1995) | vowel classification | hosted with permission in an MIT-licensed repository |
| [Yali-Lower](https://huggingface.co/datasets/ntnu-smil/yali-lower) | Mandarin consonants | GPL 3.0 or later |
| [Free Spoken Digit Dataset](https://github.com/Jakobovski/free-spoken-digit-dataset) | spoken digits | CC BY-SA 4.0 |

The corpus licenses remain applicable to canonical audio and derived images. This
repository's MIT license covers AuraBench code and original metadata only; it does not
replace upstream data licenses. See `data/provenance/audio_manifest.json` for the
source ID, citation, license string, source hash, and canonical hash of every item.

## Preprocessing

Each source is decoded to mono, DC-centered, resampled to 16 kHz with a polyphase
filter, peak-normalized to 0.98, center-cropped only when longer than the family target,
and right-padded with zeros when shorter. Canonical files are PCM16 WAV. Target lengths
are 1 second for phonetic and digit items, 4 seconds for speaker and emotion items, 5
seconds for sound events, and 10 seconds for language identification.

No sample was selected or removed based on a model's performance. FLEURS transcript
fields are deliberately discarded during ingestion.

## Known source properties

- RAVDESS emotional expressions are acted speech rather than spontaneous emotion.
- Speaker-category ground truth is the source corpus's binary metadata label; it is not
  a claim about gender identity inferred from voice.
- ESC-50 documents that some upstream clips may contain class-dependent preprocessing.
- Hillenbrand items are `/hVd/` syllables rather than isolated steady-state vowels.
- A representation may be undefined for a signal. Unreliable F0 and formant estimates
  remain blank rather than being replaced by a fallback estimate.

## Bundle layout

Each directory under `benchmark/bundles/` is a complete Any-to-Bench bundle containing
`exam.json`, `answer_schema.json`, `grading.json`, `manifest.json`, `aurabench.json`,
and any required image assets. `aurabench.json` records the image-to-question mapping,
including the deliberate permutation used by the shuffled-image control, using only
opaque public IDs. `config/public_layout.yaml` pins the reproducible question and option
permutations and records the answer-shortcut audit score.
