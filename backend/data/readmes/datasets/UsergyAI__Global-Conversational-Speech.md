---
language:
- zh
- en
- pt
- es
- fr
- ja
- ko
- yue
- de
- it
pretty_name: "Global Conversational Speech — Healthcare, Meetings, Call Centers"
license: other
license_name: commercial-license
license_link: https://usergy.ai/contact
task_categories:
- automatic-speech-recognition
- audio-classification
tags:
- audio
- speech
- conversational
- healthcare
- medical
- multilingual
- native-speakers
- stereo
- channel-separated
- speaker-diarization
- asr
- transcription
- meetings
- call-center
- professional-recording
size_categories:
- 100K<n<1M
annotations_creators:
- machine-generated
- expert-generated
language_creators:
- crowdsourced
extra_gated_prompt: |
  ## Commercial Dataset Access
  
  This dataset is available for **commercial licensing**. 
  
  By requesting access, you'll receive:
  - Full dataset specifications and sample files
  - Pricing information ($65/hour)
  - Direct contact with our team
  
  We typically respond within 24 hours.
extra_gated_fields:
  Name: text
  Company: text
  Email: text
  "Intended Use Case": text
---

# Global Conversational Speech Dataset

**305 hours. 18 locales. Real conversations.**

Not scraped from YouTube. Not recorded by anonymous crowds who don't speak the language. Every conversation in this dataset traces back to verified native speakers we know by name.

---

## The [Human] Standard

Most speech datasets are built the same way: scrape the internet, hire anonymous contractors, run it through automated QC, ship it. The result? Models that are confidently wrong.

We built this dataset differently.

- **Native speakers only** — Every recording made by verified speakers in their native language
- **Real conversations** — Unscripted, natural dialogue between two people who actually know how to talk to each other
- **Channel-separated stereo** — Each speaker on their own channel, ready for diarization training
- **Full traceability** — Every file links back to the person who recorded it

This is the [human] standard for AI data.

---

## Dataset Overview

| Metric | Value |
|--------|-------|
| **Total Duration** | 305 hours |
| **Total Files** | 928 |
| **Total Size** | ~199 GB |
| **Locales** | 18 |
| **Domains** | Healthcare, Meetings, Call Centers |
| **Format** | WAV, PCM, Stereo |
| **Sample Rate** | 44.1 kHz / 48 kHz |
| **Speakers per File** | 2 (98.6% of files) |
| **Transcripts** | 100% coverage, word-level timestamps |

---

## Audio Specifications

- **Format:** WAV (PCM 16-bit / 24-bit lossless)
- **Sample Rate:** 44.1 kHz or 48 kHz
- **Channels:** Stereo (2-channel, speaker-separated)
- **Recording Platform:** Zencastr / Riverside (professional remote recording)
- **SNR:** 45-51 dB (studio-quality)
- **Speech Type:** Natural, unscripted conversational dialogue
- **Typical Duration:** 10-60 minutes per recording

All audio files are professionally recorded with channel separation — Speaker A on left channel, Speaker B on right channel. Ready for speaker diarization training out of the box.

---

## Supported Languages

| Locale | Language | Hours | Domain Focus |
|--------|----------|-------|--------------|
| zh-CN | Chinese (Mandarin) | 34h | Healthcare, Meetings |
| en-US | English (US) | 31h | Healthcare, Meetings |
| pt-PT | Portuguese (Portugal) | 30h | Healthcare |
| pt-BR | Portuguese (Brazil) | 30h | Healthcare |
| es-MX | Spanish (Mexico) | 28h | Healthcare, Meetings |
| en-GB | English (UK) | 26h | Healthcare |
| fr-FR | French (France) | 25h | Healthcare, Meetings |
| ja-JP | Japanese | 20h | Healthcare, Meetings |
| ko-KR | Korean | 18h | Healthcare |
| yue-HK | Cantonese | 15h | Healthcare |
| de-DE | German | 14h | Healthcare |
| it-IT | Italian | 12h | Healthcare |
| es-ES | Spanish (Spain) | 10h | Meetings |
| en-AU | English (Australia) | 8h | Call Centers |
| en-IN | English (India) | 6h | Call Centers |
| hi-IN | Hindi | 5h | Call Centers |
| fr-CA | French (Canada) | 4h | Call Centers |
| es-AR | Spanish (Argentina) | 4h | Meetings |

---

## Domain Breakdown

### Healthcare (205 hours)
Medical conversations across specialties: general practice consultations, mental health sessions, dental discussions, specialist referrals. Recorded with healthcare professionals and patients discussing real (simulated) medical scenarios.

**Subdomains:** General Medicine, Mental Health, Dentistry, Cardiology, Pediatrics, Geriatrics

### Meetings (81 hours)
Business and professional conversations: team discussions, project planning, client calls, interview scenarios. Natural back-and-forth dialogue with interruptions, crosstalk, and real conversational dynamics.

**Subdomains:** Business Strategy, Project Management, Sales Calls, HR Interviews

### Call Centers (19 hours)
Customer service scenarios: support calls, complaint handling, booking and scheduling. Simulated but realistic call center interactions with appropriate pacing and turn-taking.

**Subdomains:** Technical Support, Customer Service, Booking, Complaints

---

## Transcription Details

Every audio file includes:

- **Full verbatim transcript** — Including fillers, false starts, and disfluencies
- **Word-level timestamps** — Start and end time for every word
- **Speaker diarization** — Speaker labels (Speaker A / Speaker B) for every segment
- **Confidence scores** — Per-word confidence from ASR model

**Transcription Process:**
1. Primary transcription via ElevenLabs Scribe v2
2. Secondary pass with Whisper Large v3
3. Human verification for samples

**Format:** JSON with structured segments

```json
{
  "segments": [
    {
      "start": "00:00:01.240",
      "end": "00:00:05.890",
      "speaker": "Speaker A",
      "text": "Good morning, thanks for coming in today.",
      "words": [
        {"word": "Good", "start": 1.24, "end": 1.48, "confidence": 0.98},
        {"word": "morning", "start": 1.52, "end": 1.89, "confidence": 0.99}
      ]
    }
  ]
}
```

---

## Dataset Creation Methodology

### Recording Process

All recordings were conducted via professional remote recording platforms (Zencastr and Riverside) that capture each participant on separate audio tracks. This ensures:

- **Clean channel separation** — No bleed between speakers
- **Consistent quality** — Platform handles audio optimization
- **Natural conversation** — Participants in comfortable environments

### Contributor Selection

Contributors were recruited through our verified community network of 300,000+ members. Selection criteria:

- Native speaker of target language
- Clear speech without heavy regional accents (unless specifically required)
- Comfortable with conversational topics
- Passed audio quality screening

### Quality Assurance

Multi-stage QC pipeline:

1. **Automated checks:** Duration, sample rate, channel count, SNR
2. **Language verification:** Confirmed correct language via speech recognition
3. **Content review:** Spot-checked for topic adherence and quality
4. **Transcript validation:** Compared ASR output against audio samples

---

## Intended Uses

This dataset is designed for:

- ✅ Training and fine-tuning **Automatic Speech Recognition (ASR)** models
- ✅ **Speaker diarization** research and model development
- ✅ **Conversational AI** training (natural dialogue patterns)
- ✅ **Healthcare NLP** applications (medical conversation understanding)
- ✅ **Multilingual ASR** benchmarking
- ✅ **Speech-to-text** model evaluation
- ✅ Academic and commercial research

---

## Out-of-Scope Uses

This dataset is **not** intended for:

- ❌ Real-time, safety-critical medical diagnosis systems
- ❌ Biometric speaker identification without consent
- ❌ Training voice cloning systems without proper licensing
- ❌ Any application that violates applicable privacy laws

---

## Why UsergyAI?

We spent years inside the world's largest AI data companies. We saw how datasets actually get built — the shortcuts, the anonymous crowds, the "quality checks" that catch formatting errors but miss meaning.

Then we built something different.

**300,000+ verified community members.** Not anonymous contractors. Real people with real expertise who come back because we never lied to them about what a project paid or what it required.

**Full traceability.** Every data point traces back to a person we know. Not a user ID. A person.

**The [human] standard.** Because AI is only as good as its data, and data is only as good as the people who create it.

---

## Contact

For licensing inquiries, custom datasets, or questions:

**Swaroop** (Founder)  
📧 swaroop@usergy.ai  
🌐 [usergy.ai](https://usergy.ai)

---

*The [human] standard for AI data.*

---

## Citation

```bibtex
@dataset{usergyai_conversational_speech_2026,
  author = {UsergyAI},
  title = {Global Conversational Speech Dataset},
  year = {2026},
  publisher = {Hugging Face},
  url = {https://huggingface.co/datasets/UsergyAI/Global-Conversational-Speech}
}
```
