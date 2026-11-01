---
pretty_name: "TTS Voice: 20,000 Hours of 48kHz Global Conversational Audio"
license: other
license_name: datoric-commercial
license_link: LICENSE.md
language:
  - en
  - es
  - zh
  - hi
  - ar
  - pt
  - fr
  - de
  - ja
  - ko
  - it
  - ru
  - id
  - vi
  - th
  - tr
  - bn
  - ur
  - ta
  - te
  - mr
  - nl
  - pl
  - ms
  - sw
  - tl
  - ug
  - hmn
  - ceb
  - tzm
  - bo
  - nso
  - gn
  - mad
task_categories:
  - text-to-speech
  - automatic-speech-recognition
  - audio-classification
tags:
  - tts
  - speech-synthesis
  - voice-cloning
  - conversational-speech
  - 48khz
  - multilingual
  - low-resource-languages
  - speaker-modeling
  - voice-agents
size_categories:
  - 1M<n<10M
extra_gated_heading: "Request sample access"
extra_gated_prompt: >-
  This listing is a preview. The production dataset (20,000 hours of 48kHz
  conversational speech across 30+ languages) is rights-cleared and delivered
  directly under a commercial license. Approved requesters get the full
  metadata schema and data dictionary in this repository, and can request a
  review package with real audio samples, transcripts, and QA summaries.
  Requests are reviewed within 1 business day.
extra_gated_fields:
  Full name: text
  Work email: text
  Company: text
  Company website: text
  Your role:
    type: select
    options:
      - Founder / Executive
      - Research Scientist
      - ML Engineer
      - Data / Procurement Lead
      - Other
  What are you building or training?: text
  Languages of interest: text
  Data volume you are evaluating:
    type: select
    options:
      - Evaluation sample only
      - Under 1,000 hours
      - 1,000 to 5,000 hours
      - 5,000+ hours / full dataset
      - Custom collection
  Purchase timeline:
    type: select
    options:
      - Immediate
      - 1 to 3 months
      - 3 to 6 months
      - Exploring
  Country: country
  I agree to be contacted by Datoric about samples, licensing, and custom data collection: checkbox
extra_gated_button_content: "Request sample access"
---

# TTS Voice Dataset

**20,000 hours of high-fidelity 48kHz conversational audio across 30+ global, regional, and underrepresented languages, built for text-to-speech, voice cloning, and multilingual speech AI.**

> This repository is a specification and preview listing. The production dataset is rights-cleared and delivered directly to buyers. [Request access](#how-to-evaluate-this-dataset) to see the full schema and get real audio samples.

## Overview

The TTS Voice Dataset is a 20,000-hour collection of high-fidelity 48kHz conversational audio recorded globally across numerous languages, regions, accents, and speaker profiles. It is designed for text-to-speech, voice cloning, speech synthesis, conversational AI, speaker modeling, multilingual speech training, and voice agent development.

The collection emphasizes natural spoken dialogue rather than scripted or robotic recordings, which is what makes it useful for building expressive, human-like voices for real conversational products. The 48kHz audio quality supports high-fidelity voice modeling, while the conversational recordings teach models realistic pacing, tone, turn-taking, emotion, pronunciation variation, and speaker expressiveness.

## At a glance

| | |
|---|---|
| Total volume | 20,000 hours |
| Sample rate | 48kHz, WAV/PCM where available |
| Bit depth | 16-bit or 24-bit depending on subset |
| Languages | 30+ global, regional, and underrepresented |
| Speech type | Natural conversational dialogue, not only read speech |
| Speakers | Diverse age buckets, genders, accents, native and non-native profiles where available |

## Language distribution

| Tier | Share | Hours | Languages |
|---|---|---|---|
| English + major accents | 30% | 6,000 | American, British, Canadian, Australian English |
| Major commercial languages | 35% | 7,000 | Spanish, Mandarin Chinese, Hindi, Arabic, Portuguese, French, German, Japanese, Korean, Italian, Russian |
| High-growth regional | 20% | 4,000 | Indonesian, Vietnamese, Thai, Turkish, Bengali, Urdu, Tamil, Telugu, Marathi, Dutch, Polish, Malay, Swahili |
| Low-resource / long-tail | 15% | 3,000 | Tagalog, Uyghur, Hmong, Cebuano, Tamazight, Tibetan, Sepedi, Guarani, Madurese, Bouyei |

Long-tail coverage is the hard part of multilingual voice sourcing; this dataset was structured to balance commercial usefulness with genuine linguistic diversity.

## Technical specifications

- **Annotation coverage:** language, locale, accent, speaker count, transcript availability, diarization availability, quality score, noise level, topic category
- **TTS-specific fields:** clean speech seconds, expressive speech seconds, text normalization availability, pronunciation metadata where available
- **Audio QA metrics:** SNR, loudness LUFS, clipping percentage, silence percentage, background noise level, transcript quality score where available
- **Buyer evaluation metrics:** transcript WER by subset where available, diarization error rate by subset where available, speaker consistency, pronunciation coverage, phoneme coverage, expressive range
- **Delivery format:** WAV audio, CSV metadata, optional JSON transcripts and diarization files

## Metadata schema

The gated file `annotation_schema.json` in this repository contains the full per-recording metadata schema with an illustrative example record, including audio QA fields (SNR, LUFS, clipping, silence) and TTS-specific fields (clean/expressive seconds, normalization availability).

## How to evaluate this dataset

1. **Request access** using the form above. Requests are reviewed within 1 business day.
2. On approval you get the gated files in this repository: full metadata schema, data dictionary, and access instructions.
3. **Request a review package** and we deliver real 48kHz audio samples in your target languages, transcripts, metadata CSVs, QA summaries, and licensing documentation within 2 business days.

All samples are delivered with structured CSV metadata and JSON annotation files where available. Buyer review packages include representative media files, metadata samples, annotation schema, QA summaries, and data dictionary documentation.

## Licensing

The production dataset is rights-cleared for commercial AI training and licensed directly by Datoric, with documented contributor consent and chain-of-custody. Subset (by language, accent, or hours), exclusive, and custom-collection options are available.

## About Datoric

Datoric supplies rights-cleared, spec-exact training data for frontier AI labs and enterprise model teams: expressive multilingual voice, computer-use traces, egocentric and industrial video, human manipulation data, robot episodes, and gameplay trajectories. We also run managed collection pipelines for custom specifications.

**Contact:** nikhil@arzule.com
