---
pretty_name: "Audio-Video Conversations: 4,000 Hours of Synchronized Speech & Video"
license: other
license_name: datoric-commercial
license_link: LICENSE.md
language:
  - en
  - es
  - pt
  - zh
  - hi
  - ar
  - fr
  - de
  - ja
  - ko
  - id
  - vi
  - th
  - tr
  - tl
  - it
  - nl
  - ms
  - ur
  - ta
  - te
task_categories:
  - automatic-speech-recognition
  - video-classification
tags:
  - multimodal
  - audio-video
  - lip-sync
  - avatars
  - talking-heads
  - emotion-recognition
  - turn-taking
  - paralinguistics
  - conversational
  - multilingual
size_categories:
  - 100K<n<1M
extra_gated_heading: "Request sample access"
extra_gated_prompt: >-
  This listing is a preview. The production dataset (4,000 hours of
  synchronized conversational speech and video across 20+ languages) is
  rights-cleared and delivered directly under a commercial license. Approved
  requesters get the full annotation schema and data dictionary in this
  repository, and can request a review package with real audio-video samples
  and QA summaries. Requests are reviewed within 1 business day.
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
      - Under 500 hours
      - 500 to 2,000 hours
      - 2,000+ hours / full dataset
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

# Audio-Video Conversational Dataset

**4,000 hours of synchronized speech and video of natural conversations: face movement, mouth motion, gestures, turn-taking, emotion, laughter, and interruptions across 20+ languages.**

> This repository is a specification and preview listing. The production dataset is rights-cleared and delivered directly to buyers. [Request access](#how-to-evaluate-this-dataset) to see the full schema and get real samples.

## Overview

The Audio-Video Conversational Dataset is a 4,000-hour collection of synchronized speech and video recordings of people having natural conversations across diverse speakers, languages, accents, environments, and interaction styles. It is designed for multimodal voice agents, avatar systems, lip-sync models, emotion recognition, paralinguistic understanding, conversational video models, audio-video MLLM training, and human interaction world modeling.

Each recording pairs conversational audio with synchronized video capturing face movement, mouth motion, gestures, eye gaze, facial expressions, pauses, laughter, interruptions, overlapping speech, and turn-taking behavior. Models learn not only what is being said, but how speech is visually and socially expressed through timing, facial behavior, body language, and interaction dynamics.

## At a glance

| | |
|---|---|
| Total volume | 4,000 hours |
| Video quality | 1080p+ where available |
| Audio quality | 48kHz where available |
| Languages | 20+ |
| Modality | Synchronized audio + video, natural multi-speaker conversation |
| Key phenomena | Turn-taking, overlapping speech, laughter, interruptions, gesture, gaze, emotion |

## Language distribution

| Region | Share |
|---|---|
| English + major accents | 25% |
| Spanish and Portuguese | 15% |
| East Asian languages | 15% |
| South Asian languages | 12% |
| European languages | 10% |
| Southeast Asian languages | 10% |
| Arabic and MENA regional speech | 8% |
| Long-tail / underrepresented | 5% |

Coverage includes English, Spanish, Portuguese, Mandarin Chinese, Hindi, Arabic, French, German, Japanese, Korean, Indonesian, Vietnamese, Thai, Turkish, Tagalog, Italian, Dutch, Malay, Urdu, Tamil, Telugu, and additional regional or underrepresented languages depending on subset.

## Technical specifications

- **Annotation coverage:** transcript segments, speaker turns, timestamps, face visibility, mouth visibility, gesture labels, emotion or tone labels, laughter events, interruption events, overlapping speech, speaker role, audio-video sync quality, QA review
- **Buyer evaluation metrics:** audio-video sync drift, face visibility percentage, mouth visibility percentage, transcript quality, diarization quality, paralinguistic event coverage
- **QA metrics:** sync validation, face/mouth visibility checks, audio clarity score, video exposure/blur score, annotation review
- **Delivery format:** MP4 video, WAV audio track where separated, CSV metadata, JSON annotations, transcript files

## Annotation schema

The gated file `annotation_schema.json` in this repository contains the full recording schema with an illustrative example record, including speaker-turn structure, paralinguistic event annotations, and sync-quality metrics.

## How to evaluate this dataset

1. **Request access** using the form above. Requests are reviewed within 1 business day.
2. On approval you get the gated files in this repository: full annotation schema, data dictionary, and access instructions.
3. **Request a review package** and we deliver real synchronized audio-video samples in your target languages, transcripts, JSON annotations, QA summaries, and licensing documentation within 2 business days.

All samples are delivered with structured CSV metadata and JSON annotation files where available. Buyer review packages include representative media files, metadata samples, annotation schema, QA summaries, and data dictionary documentation.

## Licensing

The production dataset is rights-cleared for commercial AI training and licensed directly by Datoric, with documented on-camera contributor consent and chain-of-custody. Subset (by language or hours), exclusive, and custom-collection options are available.

## About Datoric

Datoric supplies rights-cleared, spec-exact training data for frontier AI labs and enterprise model teams: expressive multilingual voice, audio-video conversation, egocentric and industrial video, human manipulation data, robot episodes, computer-use traces, and gameplay trajectories. We also run managed collection pipelines for custom specifications.

**Contact:** nikhil@arzule.com
