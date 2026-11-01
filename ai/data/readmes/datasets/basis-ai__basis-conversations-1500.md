---
pretty_name: "Basis Conversations"
license: other
license_name: basis-data-license-1.0
license_link: LICENSE
language:
- ar
- de
- en
- es
- fr
- he
- hi
- it
- ja
- ka
- kk
- ko
- nl
- pl
- pt
- ru
- tr
- uk
- xh
- xmf
- zh
- zu
language_creators:
- crowdsourced
annotations_creators:
- machine-generated
- crowdsourced
multilinguality: multilingual
source_datasets:
- original
task_categories:
- automatic-speech-recognition
- audio-classification
tags:
- audio
- conversational
- multi-speaker
- full-duplex
- turn-taking
- speaker-tracks
- word-alignment
- laughter
- backchannel
size_categories:
- 10K<n<100K
configs:
- config_name: default
  data_files:
  - split: train
    path:
    - "ar/metadata.jsonl"
    - "ar/audio/*/*.flac"
    - "de/metadata.jsonl"
    - "de/audio/*/*.flac"
    - "en/metadata.jsonl"
    - "en/audio/*/*.flac"
    - "es/metadata.jsonl"
    - "es/audio/*/*.flac"
    - "fr/metadata.jsonl"
    - "fr/audio/*/*.flac"
    - "he/metadata.jsonl"
    - "he/audio/*/*.flac"
    - "hi/metadata.jsonl"
    - "hi/audio/*/*.flac"
    - "it/metadata.jsonl"
    - "it/audio/*/*.flac"
    - "ja/metadata.jsonl"
    - "ja/audio/*/*.flac"
    - "ka/metadata.jsonl"
    - "ka/audio/*/*.flac"
    - "kk/metadata.jsonl"
    - "kk/audio/*/*.flac"
    - "ko/metadata.jsonl"
    - "ko/audio/*/*.flac"
    - "nl/metadata.jsonl"
    - "nl/audio/*/*.flac"
    - "pl/metadata.jsonl"
    - "pl/audio/*/*.flac"
    - "pt/metadata.jsonl"
    - "pt/audio/*/*.flac"
    - "ru/metadata.jsonl"
    - "ru/audio/*/*.flac"
    - "tr/metadata.jsonl"
    - "tr/audio/*/*.flac"
    - "uk/metadata.jsonl"
    - "uk/audio/*/*.flac"
    - "xh/metadata.jsonl"
    - "xh/audio/*/*.flac"
    - "xmf/metadata.jsonl"
    - "xmf/audio/*/*.flac"
    - "zh/metadata.jsonl"
    - "zh/audio/*/*.flac"
    - "zu/metadata.jsonl"
    - "zu/audio/*/*.flac"
- config_name: ar
  data_files:
  - split: train
    path:
    - "ar/metadata.jsonl"
    - "ar/audio/*/*.flac"
- config_name: de
  data_files:
  - split: train
    path:
    - "de/metadata.jsonl"
    - "de/audio/*/*.flac"
- config_name: en
  data_files:
  - split: train
    path:
    - "en/metadata.jsonl"
    - "en/audio/*/*.flac"
- config_name: es
  data_files:
  - split: train
    path:
    - "es/metadata.jsonl"
    - "es/audio/*/*.flac"
- config_name: fr
  data_files:
  - split: train
    path:
    - "fr/metadata.jsonl"
    - "fr/audio/*/*.flac"
- config_name: he
  data_files:
  - split: train
    path:
    - "he/metadata.jsonl"
    - "he/audio/*/*.flac"
- config_name: hi
  data_files:
  - split: train
    path:
    - "hi/metadata.jsonl"
    - "hi/audio/*/*.flac"
- config_name: it
  data_files:
  - split: train
    path:
    - "it/metadata.jsonl"
    - "it/audio/*/*.flac"
- config_name: ja
  data_files:
  - split: train
    path:
    - "ja/metadata.jsonl"
    - "ja/audio/*/*.flac"
- config_name: ka
  data_files:
  - split: train
    path:
    - "ka/metadata.jsonl"
    - "ka/audio/*/*.flac"
- config_name: kk
  data_files:
  - split: train
    path:
    - "kk/metadata.jsonl"
    - "kk/audio/*/*.flac"
- config_name: ko
  data_files:
  - split: train
    path:
    - "ko/metadata.jsonl"
    - "ko/audio/*/*.flac"
- config_name: nl
  data_files:
  - split: train
    path:
    - "nl/metadata.jsonl"
    - "nl/audio/*/*.flac"
- config_name: pl
  data_files:
  - split: train
    path:
    - "pl/metadata.jsonl"
    - "pl/audio/*/*.flac"
- config_name: pt
  data_files:
  - split: train
    path:
    - "pt/metadata.jsonl"
    - "pt/audio/*/*.flac"
- config_name: ru
  data_files:
  - split: train
    path:
    - "ru/metadata.jsonl"
    - "ru/audio/*/*.flac"
- config_name: tr
  data_files:
  - split: train
    path:
    - "tr/metadata.jsonl"
    - "tr/audio/*/*.flac"
- config_name: uk
  data_files:
  - split: train
    path:
    - "uk/metadata.jsonl"
    - "uk/audio/*/*.flac"
- config_name: xh
  data_files:
  - split: train
    path:
    - "xh/metadata.jsonl"
    - "xh/audio/*/*.flac"
- config_name: xmf
  data_files:
  - split: train
    path:
    - "xmf/metadata.jsonl"
    - "xmf/audio/*/*.flac"
- config_name: zh
  data_files:
  - split: train
    path:
    - "zh/metadata.jsonl"
    - "zh/audio/*/*.flac"
- config_name: zu
  data_files:
  - split: train
    path:
    - "zu/metadata.jsonl"
    - "zu/audio/*/*.flac"
extra_gated_heading: "Request access"
extra_gated_description: "Listen to samples at https://withbasis.co/open/conversations-1500#listen. Requests are reviewed by a person."
extra_gated_prompt: "This dataset contains recordings of real people. By requesting access you agree not to try to identify, locate or contact any speaker, not to use the data to impersonate a specific person, not to reconstruct anything that was removed, and to use it under the terms in the LICENSE file."
extra_gated_fields:
  Name: text
  Institution: text
  Work email: text
  Role/position: text
  I agree to the terms above: checkbox
extra_gated_button_content: "Request access"
---
# Dataset Card for Basis Conversations 1500

<img src="basis-conversations-1500.gif" alt="Basis Conversations 1500" style="border-radius: 16px;" />

[![Blog + Samples](https://img.shields.io/badge/%F0%9F%93%B0-Blog%20%2B%20Samples-0ea5e9)](https://withbasis.co/open/conversations-1500)
[![Basis](https://img.shields.io/badge/%F0%9F%8F%A0-Basis-8b5cf6)](https://withbasis.co)
[![Contact](https://img.shields.io/badge/%E2%9C%89%EF%B8%8F-Contact-green)](mailto:data@withbasis.co)

**Listen first: [sample conversations](https://withbasis.co/open/conversations-1500)**

## Overview

Basis Conversations 1500 is a multi-party, multilingual, full duplex conversational speech dataset. Each conversation includes up to 4 simultaneous speakers, each with channel-separated, 48 kHz audio. The median conversation lasts 33 minutes and 2,645 unique speakers are represented.

**Multi-party:** a conversation seats between two and four people at a time; participants come and go over the course of the conversation.

**Multilingual:** Speakers from 33 countries speaking 22 languages (some never before included in public conversational speech data at any scale).

**Highly annotated:** about 100 hours of conversations are human annotated (113k human judgements from 7,362 labelers) for categories of backchannels, interruptions, speaker addressee moments, pauses, laughter, repairs and self-repairs (disfluencies).


### Languages

| Locale | Hours | Conversations | Speakers | Human-annotated hours |
|---|---|---|---|---|
| Arabic (ar-EG, ar-JO, ar-LB, ar-MA, ar-SA) | 279.2 | 418 | 530 | 12.7 |
| Chinese (zh-TW) | 15.3 | 17 | 35 | |
| Dutch (nl-NL) | 2.2 | 8 | 15 | 0.1 |
| English (en-AU, en-GB, en-NZ, en-US) | 174.4 | 200 | 418 | 21.5 |
| French (fr-FR) | 5.3 | 17 | 23 | 1.0 |
| Georgian (ka-GE) | 47.2 | 83 | 102 | 5.2 |
| German (de-DE) | 7.7 | 15 | 13 | 1.1 |
| Hebrew (he-IL) | 25.0 | 50 | 63 | |
| Hindi (hi-IN) | 182.2 | 204 | 202 | 10.1 |
| Italian (it-IT) | 11.8 | 22 | 47 | 3.8 |
| Japanese (ja-JP) | 42.7 | 51 | 62 | |
| Kazakh (kk-KZ) | 32.1 | 60 | 109 | |
| Korean (ko-KR) | 9.5 | 28 | 35 | |
| Mingrelian (xmf-GE) | 1.3 | 2 | 4 | |
| Polish (pl-PL) | 4.1 | 11 | 15 | 1.6 |
| Portuguese (pt-BR, pt-PT) | 114.1 | 121 | 177 | 16.2 |
| Russian (ru-BY, ru-KZ) | 28.5 | 61 | 86 | 0.2 |
| Spanish (es-AR, es-CL, es-CO, es-EC, es-ES, es-MX) | 481.2 | 487 | 578 | 20.6 |
| Turkish (tr-TR) | 19.6 | 27 | 40 | 3.2 |
| Ukrainian (uk-UA) | 0.3 | 3 | 5 | 0.2 |
| Xhosa (xh-ZA) | 10.5 | 12 | 51 | |
| Zulu (zu-ZA) | 7.6 | 10 | 39 | |
| **Total** | **1,502.0** | **1,907** | **2,645** | **97.5** |

## How to Use

If wanted, transcripts, annotations and speaker metadata can be inspected without downloading audio:

```python
from huggingface_hub import snapshot_download
local_dir = snapshot_download(
    repo_id="basis-ai/basis-conversations-1500", repo_type="dataset",
    allow_patterns=["*.jsonl", "*.json", "*.md", "manifests/*", "LICENSE", "CHECKSUMS.sha256"],
)
```

To add one language's audio, include `"es/audio/*/*"` (every file under `audio/` is one speaker's track). The repository is approximately 253 GB. `manifests/lhotse/` loads with `lhotse.RecordingSet.from_jsonl` and `SupervisionSet.from_jsonl` (channels 0 to N−1 are the speaker tracks).

Loading with 🤗 Datasets (install the audio extra first: `pip install "datasets[audio]"`):

```python
from datasets import load_dataset, Audio
import soundfile as sf

ds = load_dataset("basis-ai/basis-conversations-1500", "es", split="train")   # one row per speaker track
ds = ds.cast_column("audio", Audio(decode=False))   # tracks run from 2 to 250 minutes: keep them undecoded and read windows
row = ds[0]
with sf.SoundFile(row["audio"]["path"]) as f:
    f.seek(120 * 48000)
    window = f.read(30 * 48000)   # 30 seconds starting at 2:00
```


## Dataset Structure

Conversations are grouped by language. Sometimes conversations are cut into sub-segments or temporarily muted to remove PII amongst other reasons. The segments of a common conversation share a clock, and we report the length of the redacted gap (`gap_before`).


```text
<lang>/
├── segments.jsonl                       one line per segment: transcript, speakers, human judgments, machine labels
├── human_judgments.jsonl                one line per human judgment, with its segment
├── machine_labels.jsonl                 one line per machine label, with its segment
├── metadata.jsonl                       one line per speaker track: the table the dataset viewer shows
└── audio/<conversation_id>/
    ├── <stem>.<speaker_id>.flac         one track per speaker, same clock (the stem is the segment's file stem, not its id; paths are on the segment row)
    └── …
speakers.jsonl        one line per speaker
manifests/lhotse/     recordings.jsonl and supervisions.jsonl
FIELDS.md             every field of every file, one line each
ANNOTATIONS.md        every label and question defined, with its criterion and how it was made
dataset_info.json     per-language statistics and the list of annotated conversations
LICENSE
```

### Dataset Statistics

| Item | Value |
|---|---|
| Languages | 22 |
| Conversations | 1,907 |
| Segments | 2,396 |
| Conversation audio | approximately 1,502 hours |
| Speakers | 2,645 |
| Speakers per conversation | 2 to 30 over a conversation's length (median 5; 77 % of conversations have 2 to 8); four on the call at a time, 94 % of hours with 3 or more |
| Mean segment duration | 37.6 minutes (median 26.1) |
| Audio files | 13,682 FLAC speaker tracks |
| Human judgments | 113,096 |
| Machine labels | 41,021 |

### Audio

FLAC, 16-bit, mono, 48 kHz, as recorded: no denoising, no loudness normalisation. Every file under `audio/` is one speaker's own microphone, cut and muted on the segment's shared clock: every track of a segment starts at the same instant and has the same length, so time 0 is the same instant in all of them and a time on any row indexes every track. To hear the call, sum the tracks on that clock (scale by the number of tracks or normalise: a unity sum of 16-bit tracks clips). In a few cases, we mute small spans of audio for privacy or other reasons, which are reported on the segment.


### Transcripts

For convenience, we report transcripts for each segment, which were produced either by real-time speech-to-text providers or backfilled after the fact. The transcripts are provided as a convenience for finding or filtering moments of interest, but are often noisy and can be inaccurate, especially for real-time transcription for worse-supported languages (we do not recommend supervising on the provided transcripts for training!). We mark a row `slur_suspected` when a list of slurs and group-hate phrases matches it; the audio and the words are left as heard.

```json
{"speaker": "spk_f1b3650242be", "start": 2117.02, "end": 2119.14,
 "text": "وزي كذا، بس طبعاً نفس اللي مو قلت لك",
 "words": [{"word": "وزي", "start": 2117.02, "end": 2117.16}, "…"]}
```

### Annotations

Using a combination of waveform analysis, offline audio models, and LLMs as judges on transcriptions, we machine-label a number of events of interest in a sub-set of the conversations. For some of these label types, we have humans vote on which category the instance falls into (including "wrongly labeled"). For this reason, we aim to over-label (fewer false negatives) for machine-labels before passing along to the human annotators. In this release, 23,751 judged moments in 148 conversations across 14 languages are included, with 113,096 votes in their tallies (about five per moment) from 7,362 annotators; a moment whose settled answer was that the event was not there is left out.

For laughter and backchannels, we only include the machine labels that people confirmed. For the other events (overlaps included), the machine labels are included as is, so if you want a checked set, use the human-judged moments.

| Event | Machine labels | Human-judged moments | Human options |
|---|---:|---:|---|
| backchannel: a short sound from a listener while someone else holds the floor | 5,580 | 7,807 | affirming · amused or surprised · sympathy · frustration · ordinary speech · background noise · other · inaudible |
| laughter | 5,946 acoustic, plus 2,939 social laughter and 1,500 humor from the transcript | 6,080 | at their own line · at someone else's line · awkward · ordinary speech · background noise · other |
| overlap: two people talking at once | 10,228 | 7,372 | cooperative · competitive · simultaneous start · unclear · no overlap |
| pause: a silence after a speaker stops | 868 | 504 | holding the turn · finished, normal gap · finished, awkward gap · inaudible · other |
| repair: a listener's response to trouble hearing or understanding | 384 other-initiated, plus 528 outcomes and 104 breakdowns | 267 | repeat request · clarification request · confirmation check · no trouble · inaudible |
| self-repair: a speaker's own disfluency | 1,064, plus 525 disfluency | 1,080 | filler · repeat · self-correction · restart · abandoned · none · inaudible |
| addressee: who a line was said to | 2,092 directed speech | 641 | one of the speakers · everyone · unclear · inaudible |
| other machine-only labels: agreement, pushback, turn management, collaborative completion, topic changes and endings, and social acts (self-disclosure, greetings, apologies, and others) | 9,263 | — | — |

### Speakers

`speakers.jsonl` has one line per speaker; the same person carries the same `speaker` id in every segment, so a speaker-disjoint split is a filter on this field.

| Field | Type | Description |
|---|---|---|
| `speaker` | string | Stable anonymous identifier. |
| `gender` | string | `male`, `female` or `other`, as declared at signup. |
| `age_band` | string | `18-24` … `65+`, from the age declared at signup. |
| `countries` | list | Country of the speaker (ISO 3166-1 alpha-2). |
| `languages` | list | Languages of the conversations they appear in. |
| `conversations`, `segments` | int, int | How many conversations and segments they appear in. |

On a segment, each speaker entry repeats `gender`, `age_band` and `country`, and adds `on_call` (the stretches during which the speaker was connected to the call and recording) and `audio` (the highest frequency the track carries, in Hz, where measured).

## Dataset Creation

### Recording

Conversations were recorded in a mobile and web app over live calls. Participants were matched with strangers who speak the same language, up to four to a room at a time, with people joining and leaving over the call, and talked about whatever they wanted for as long as they liked. Each participant's device recorded its own microphone. Recording environments and microphone conditions vary across speakers and are measured per track. We filter out conversations with very poor audio defects, while still retaining some with noisy though real-life conditions to be useful for robust training/eval situations.

### Consent and Privacy

Every participant agreed at signup to be recorded and to license their recordings for AI training, including resale to third parties and training of speech recognition, text-to-speech and voice-cloning systems, and waived their right of publicity for AI training. To the best of our knowledge, we mute spoken personal details (full names given for contact, phone numbers, addresses, handles, email addresses) in every file and their rows kept as placeholders. We additionally take extra effort to remove suspected minors from any and all conversations, by running offline models to detect underage voices, monitoring transcripts, and instructing other participants to report suspected minors.


Suspected hate speech is flagged on the row and left in the audio. Speaker identifiers are salted and stable; no names, account identifiers or contact data are in the release. Demographics are self-reported at signup and never inferred from audio.


## Additional Information

### Licensing

The terms are in `LICENSE`. Custom licenses are available on request: [data@withbasis.co](mailto:data@withbasis.co).

### Citation

```bibtex
@misc{basis2026conversations1500,
  title     = {Basis Conversations 1500},
  author    = {{Basis}},
  year      = {2026},
  publisher = {Hugging Face},
  url       = {https://huggingface.co/datasets/basis-ai/basis-conversations-1500}
}
```
