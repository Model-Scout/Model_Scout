---
dataset_info:
  features:
  - name: id
    dtype: string
  - name: audio
    dtype:
      audio:
        sampling_rate: 48000
        mono: false
  - name: duration_s
    dtype: float32
  - name: language_a
    dtype: string
  - name: language_b
    dtype: string
  - name: corpus_a
    dtype: string
  - name: corpus_b
    dtype: string
  - name: speaker_a
    dtype: string
  - name: speaker_b
    dtype: string
  - name: license_a
    dtype: string
  - name: license_b
    dtype: string
  - name: non_commercial
    dtype: bool
  - name: n_turns
    dtype: int32
  - name: n_backchannels
    dtype: int32
  - name: segments_a
    sequence:
    - name: start
      dtype: float32
    - name: end
      dtype: float32
    - name: kind
      dtype: string
  - name: segments_b
    sequence:
    - name: start
      dtype: float32
    - name: end
      dtype: float32
    - name: kind
      dtype: string
  - name: sources
    sequence:
    - name: channel
      dtype: int8
    - name: at_s
      dtype: float32
    - name: corpus
      dtype: string
    - name: file
      dtype: string
    - name: from_s
      dtype: float32
    - name: to_s
      dtype: float32
  splits:
  - name: train
    num_bytes: 80613079464.0
    num_examples: 84340
  - name: test
    num_bytes: 243732657.0
    num_examples: 253
  download_size: 80597974511
  dataset_size: 80856812121.0
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
pretty_name: Synthetic Stereo Calls
language:
- af
- as
- ca
- crh
- de
- ee
- en
- es
- eu
- gl
- gu
- ha
- hi
- ja
- jv
- km
- kn
- ko
- ln
- ml
- mr
- my
- ne
- pl
- st
- su
- ta
- te
- tn
- tw
- uk
- xh
- yo
- zh
license_name: per-channel
size_categories:
- 10K<n<100K
license_link: LICENSE.md
license: other
task_categories:
- audio-to-audio
tags:
- speech
- telephony
- call-centre
- speech-enhancement
- stereo
- conversation
- synthetic
---

# Synthetic Stereo Calls

Two-party calls made from clean studio speech. Each call has two channels at 48 kHz, one party per channel, the way a call
centre records a call in stereo. The channels are clean, so you degrade them yourself.

We built these calls to train [CallEnhancer](https://huggingface.co/Scicom-intl/CallEnhancer) on recordings that hold both
parties in one channel. A model trained to remove cross-talk also learns to remove the quieter party of such a recording.
Mixing the two channels of these calls, degrading them, and asking for both parties back teaches it the difference.

| | train | test |
|---|---:|---:|
| calls | 84,340 | 253 |
| hours | 702.7 | 2.1 |
| speakers | 701 | 102 |
| languages | 31 | 30 |

Each call is 20 to 40 s long. Test speakers do not appear in train. For a corpus with a single speaker, the test calls use
other recordings of that speaker.

![one call](https://huggingface.co/datasets/Scicom-intl/Synthetic-Stereo-Calls/resolve/main/assets/fig_stereo_example_legs.png)
![one call degraded](https://huggingface.co/datasets/Scicom-intl/Synthetic-Stereo-Calls/resolve/main/assets/fig_stereo_example_input.png)

*One test call, both parties from Google Tamil (OpenSLR 65). Top: the two clean channels with party A set 10 dB under party
B, as 20 ms levels. Bottom: the same call in one channel after our training degradation (two lines), as a
spectrogram.*

## What a call is

- Channel 1 is party A and channel 2 is party B. Each party is one speaker of one corpus.
- A party talks in talkspurts. A talkspurt is a phrase of that speaker's recordings, cut at a word gap when it runs longer
  than the drawn length. The rest of the sentence carries on in the party's next talkspurt, so each party reads its
  sentences in order.
- Between its phrases a channel is digital silence.
- Both parties sit at one speech level: the 90th percentile of 20 ms frames at -22 dBFS. Nothing is mixed in, so you choose
  the level gap between the parties when you mix them.
- A backchannel ("yeah", "mm-hmm", "okay") is one of the speaker's own recorded interjections where the corpus has them
  (EARS). Otherwise it is the first words of one of the speaker's phrases.

## Turn-taking copied from real calls

We measured how the two parties take turns in 3,878 real two-channel call-centre calls (229 hours,
not released, aggregates only). A talkspurt is one party's speech with gaps under 200 ms closed. The generator draws every
talkspurt length, the number of talkspurts in a turn, the pause inside a turn, the gap or overlap when the turn passes, and
the backchannels from those calls. The table compares medians, measured the same way on both sides at 8 kHz.

| median | real calls | synthetic, clean | synthetic, after a phone line |
|---|---:|---:|---:|
| talkspurt (s) | 0.80 | 0.70 | 0.74 |
| pause inside a turn (s) | 0.36 | 0.40 | 0.40 |
| gap when the turn passes (s) | 0.24 | 0.32 | 0.24 |
| turn (s) | 1.64 | 1.48 | 1.58 |
| backchannel (s) | 0.28 | 0.36 | 0.40 |
| backchannels per minute | 5.9 | 4.6 | 5.1 |
| share of time a party talks | 0.42 | 0.36 | 0.37 |
| both parties talking | 0.057 | 0.047 | 0.058 |
| neither party talking | 0.222 | 0.314 | 0.299 |
| switches that overlap | 27 % | 21 % | 28 % |

After the line, talkspurts run 8 % shorter and turns 4 % shorter than in real calls at the median, and the calls hold more silence: neither party talks for 30 % of the time, against 22 %.

| | |
|---|---|
| ![talkspurt](https://huggingface.co/datasets/Scicom-intl/Synthetic-Stereo-Calls/resolve/main/assets/fig_stereo_spurt.png) | ![gap](https://huggingface.co/datasets/Scicom-intl/Synthetic-Stereo-Calls/resolve/main/assets/fig_stereo_gap.png) |
| ![turn](https://huggingface.co/datasets/Scicom-intl/Synthetic-Stereo-Calls/resolve/main/assets/fig_stereo_turn.png) | ![pause](https://huggingface.co/datasets/Scicom-intl/Synthetic-Stereo-Calls/resolve/main/assets/fig_stereo_pause.png) |

## After a phone line

To check that a degraded call looks like a real one, we passed each channel through our training degradation as its own
phone line (codec, band limit, line noise, background noise) and measured it with the same statistics as 116
legs of 58 real calls. A real leg holds its party's speech 38 % of the time at the
median, a synthetic channel 37 %, and a single-speaker training clip
70 %. Envelope SNR: 50.9 dB real, 51.4 dB
synthetic. Noise floor: -80.9 dBFS real, -78.0 dBFS synthetic. In
18 % of synthetic channels the degradation adds no noise, so the pauses stay digitally silent; every real leg has
a line floor.

| | |
|---|---|
| ![speech share](https://huggingface.co/datasets/Scicom-intl/Synthetic-Stereo-Calls/resolve/main/assets/fig_stereo_active.png) | ![snr](https://huggingface.co/datasets/Scicom-intl/Synthetic-Stereo-Calls/resolve/main/assets/fig_stereo_snr.png) |
| ![floor](https://huggingface.co/datasets/Scicom-intl/Synthetic-Stereo-Calls/resolve/main/assets/fig_stereo_floor.png) | ![spectrum](https://huggingface.co/datasets/Scicom-intl/Synthetic-Stereo-Calls/resolve/main/assets/fig_stereo_ltas.png) |

The speech-level gap between the two parties of a real call has a median of 9.2 dB over
3,878 calls. We draw our training gaps from that distribution, up to 30 dB.

![gaps](https://huggingface.co/datasets/Scicom-intl/Synthetic-Stereo-Calls/resolve/main/assets/fig_stereo_gaps.png)

## How clean

A recording is used only if it passes every check:

- no run of three samples at full scale (no clipping);
- at least 55 dB from the speech level (the 90th-percentile 20 ms frame) down to the noise under the speech (the quietest
  2 % of the 10 ms frames that are not digital silence);
- a DNSMOS background score of at least 3.8 where the source publishes one;
- energy up to at least 18 kHz;
- a real recording: no restored or synthetic speech, no podcasts, no home-recorded audiobooks, no whispered, sung, shouted
  or non-verbal takes.

| corpus | license | languages | speakers | channels | speech hours | source |
|---|---|---|---:|---:|---:|---|
| Google UK and Ireland English (OpenSLR 83) | CC BY-SA 4.0 | en | 28 | 21,797 | 73.2 | [link](https://www.openslr.org/83/) |
| EARS | CC BY-NC 4.0 | en | 28 | 18,751 | 69.4 | [link](https://github.com/facebookresearch/ears_dataset) |
| DAPS | CC BY-NC 4.0 | en | 18 | 14,067 | 51.3 | [link](https://zenodo.org/records/4660670) |
| Expresso (read) | CC BY-NC 4.0 | en | 4 | 13,865 | 43.2 | [link](https://huggingface.co/datasets/ylacombe/expresso) |
| Google Nigerian English (OpenSLR 70) | CC BY-SA 4.0 | en | 19 | 9,539 | 32.1 | [link](https://www.openslr.org/70/) |
| AISHELL-3 | Apache 2.0 | zh | 61 | 4,028 | 13.7 | [link](https://www.openslr.org/93/) |
| Google Peruvian Spanish (OpenSLR 73) | CC BY-SA 4.0 | es | 17 | 3,224 | 10.5 | [link](https://www.openslr.org/73/) |
| Google South African languages (OpenSLR 32) | CC BY-SA 4.0 | af/st/tn/xh | 37 | 3,102 | 10.5 | [link](https://www.openslr.org/32/) |
| Google Gujarati (OpenSLR 78) | CC BY-SA 4.0 | gu | 34 | 3,016 | 10.3 | [link](https://www.openslr.org/78/) |
| Google Sundanese (OpenSLR 44) | CC BY-SA 4.0 | su | 30 | 3,018 | 10.3 | [link](https://www.openslr.org/44/) |
| Google Marathi (OpenSLR 64) | CC BY-SA 4.0 | mr | 9 | 3,011 | 10.3 | [link](https://www.openslr.org/64/) |
| Google Javanese (OpenSLR 41) | CC BY-SA 4.0 | jv | 23 | 3,005 | 10.2 | [link](https://www.openslr.org/41/) |
| Google Chilean Spanish (OpenSLR 71) | CC BY-SA 4.0 | es | 18 | 3,153 | 10.2 | [link](https://www.openslr.org/71/) |
| Google Burmese (OpenSLR 80) | CC BY-SA 4.0 | my | 13 | 3,007 | 10.2 | [link](https://www.openslr.org/80/) |
| Google Malayalam (OpenSLR 63) | CC BY-SA 4.0 | ml | 35 | 3,018 | 10.1 | [link](https://www.openslr.org/63/) |
| Google Nepali (OpenSLR 43) | CC BY-SA 4.0 | ne | 16 | 2,966 | 10.1 | [link](https://www.openslr.org/43/) |
| Google Galician (OpenSLR 77) | CC BY-SA 4.0 | gl | 28 | 2,998 | 10.0 | [link](https://www.openslr.org/77/) |
| Google Colombian Spanish (OpenSLR 72) | CC BY-SA 4.0 | es | 15 | 3,073 | 9.9 | [link](https://www.openslr.org/72/) |
| Google Basque (OpenSLR 76) | CC BY-SA 4.0 | eu | 29 | 2,967 | 9.9 | [link](https://www.openslr.org/76/) |
| Google Catalan (OpenSLR 69) | CC BY-SA 4.0 | ca | 24 | 2,987 | 9.9 | [link](https://www.openslr.org/69/) |
| Google Tamil (OpenSLR 65) | CC BY-SA 4.0 | ta | 44 | 2,956 | 9.9 | [link](https://www.openslr.org/65/) |
| Google Khmer (OpenSLR 42) | CC BY-SA 4.0 | km | 11 | 2,897 | 9.7 | [link](https://www.openslr.org/42/) |
| Google Telugu (OpenSLR 66) | CC BY-SA 4.0 | te | 39 | 2,854 | 9.3 | [link](https://www.openslr.org/66/) |
| Google Venezuelan Spanish (OpenSLR 75) | CC BY-SA 4.0 | es | 11 | 2,417 | 8.0 | [link](https://www.openslr.org/75/) |
| Google Argentinian Spanish (OpenSLR 61) | CC BY-SA 4.0 | es | 24 | 2,353 | 7.8 | [link](https://www.openslr.org/61/) |
| Google Kannada (OpenSLR 79) | CC BY-SA 4.0 | kn | 46 | 2,205 | 7.4 | [link](https://www.openslr.org/79/) |
| BibleTTS (ewe) | CC BY-SA 4.0 | ee | 1 | 1,617 | 5.8 | [link](https://masakhane-io.github.io/bibleTTS/) |
| BibleTTS (lingala) | CC BY-SA 4.0 | ln | 1 | 1,594 | 5.6 | [link](https://masakhane-io.github.io/bibleTTS/) |
| BibleTTS (yoruba) | CC BY-SA 4.0 | yo | 1 | 1,571 | 5.5 | [link](https://masakhane-io.github.io/bibleTTS/) |
| BibleTTS (asante-twi) | CC BY-SA 4.0 | tw | 1 | 1,562 | 5.3 | [link](https://masakhane-io.github.io/bibleTTS/) |
| JSUT (basic5000) | JSUT terms of use | ja | 1 | 1,556 | 5.3 | [link](https://sites.google.com/site/shinnosuketakamichi/publication/jsut) |
| BibleTTS (akuapem-twi) | CC BY-SA 4.0 | tw | 1 | 1,542 | 5.3 | [link](https://masakhane-io.github.io/bibleTTS/) |
| IndicTTS Hindi | not stated | hi | 1 | 1,495 | 5.2 | [link](https://huggingface.co/datasets/SPRINGLab/IndicTTS-Hindi) |
| Thorsten-Voice | CC0 1.0 | de | 1 | 1,599 | 5.2 | [link](https://huggingface.co/datasets/Thorsten-Voice/TV-44kHz-Full) |
| KSS | CC BY-NC-SA 4.0 | ko | 1 | 1,601 | 5.2 | [link](https://www.kaggle.com/datasets/bryanpark/korean-single-speaker-speech-dataset) |
| Crimean Tatar TTS (Sevil) | Apache 2.0 | crh | 1 | 1,446 | 5.1 | [link](https://huggingface.co/datasets/speech-uk/tts-crh-sevil) |
| BibleTTS (hausa) | CC BY-SA 4.0 | ha | 1 | 1,546 | 5.1 | [link](https://masakhane-io.github.io/bibleTTS/) |
| IndicTTS Assamese | not stated | as | 1 | 1,566 | 4.9 | [link](https://huggingface.co/datasets/SPRINGLab/IndicTTS_Assamese) |
| IISc Hindi (female) | CC BY 4.0 | hi | 1 | 1,500 | 4.9 | [link](https://huggingface.co/datasets/somu9/iisc_mono_hindi_female) |
| OpenTTS (Oleksa) | Apache 2.0 | uk | 1 | 1,594 | 4.8 | [link](https://huggingface.co/datasets/speech-uk/opentts-oleksa) |
| Google Yoruba (OpenSLR 86) | CC BY-SA 4.0 | yo | 18 | 1,465 | 4.7 | [link](https://www.openslr.org/86/) |
| Crimean Tatar TTS (Abibullah) | Apache 2.0 | crh | 1 | 1,518 | 4.7 | [link](https://huggingface.co/datasets/speech-uk/tts-crh-abibullah) |
| MC Speech | CC0 1.0 | pl | 1 | 1,549 | 4.6 | [link](https://huggingface.co/datasets/czyzi0/the-mc-speech-dataset) |
| Google Puerto Rican Spanish (OpenSLR 74) | CC BY-SA 4.0 | es | 5 | 1,146 | 3.8 | [link](https://www.openslr.org/74/) |
| IndicTTS Kannada | not stated | kn | 1 | 939 | 3.4 | [link](https://huggingface.co/datasets/SPRINGLab/IndicTTS_Kannada) |

## Columns

| column | what |
|---|---|
| `audio` | the call, two channels at 48 kHz (decode with `Audio(mono=False)` or read the FLAC bytes with soundfile) |
| `duration_s` | length in seconds |
| `language_a`, `language_b` | language of each party |
| `corpus_a`, `corpus_b` | source corpus of each party |
| `speaker_a`, `speaker_b` | speaker of each party, unique across corpora |
| `license_a`, `license_b` | license of each channel's source |
| `non_commercial` | true when either channel is not cleared for commercial use (a non-commercial license, or terms that are research-only or not stated) |
| `n_turns`, `n_backchannels` | turns and backchannels in the call |
| `segments_a`, `segments_b` | where each party talks: start, end (s), `speech` or `backchannel` |
| `sources` | every placed phrase: channel, time in the call, corpus, source file, start and end in that file |

## Use

```python
from datasets import load_dataset, Audio
ds = load_dataset("Scicom-intl/Synthetic-Stereo-Calls", split="train", streaming=True).cast_column("audio", Audio(mono=False))
row = next(iter(ds))
a, b = row["audio"]["array"]                  # party A, party B: 48 kHz, equal speech level
gap_db = 9.0                                  # put party B 9 dB under party A
mono = a + b * 10 ** (-gap_db / 20)           # one channel holding both parties: degrade this as your input
target = mono                                 # and keep both parties in the target
```

The `audio` feature is stored with `mono=False`; the cast only makes that explicit. To use only calls whose two channels
are both cleared for commercial use, keep the rows where `non_commercial` is false.

## Licenses

A channel is one speaker's recordings, cut into phrases and re-timed. It keeps the license of its source corpus, given in
`license_a` and `license_b`. A call holds two channels: use it only as both licenses allow. Non-commercial (NC) sources
make a call non-commercial, and share-alike (SA) sources ask that what you share from them carries the same license. JSUT
comes with its own terms of use, and the IndicTTS copies we used state no license: check them before you use those calls.
`non_commercial` is true for every call with an NC, JSUT or IndicTTS channel. The arrangement, the timing and the
metadata are ours and are released under CC BY 4.0.

## Not included

Our training set also has calls with our in-house studio voices. Those recordings are private, so those calls are not
here, and this is why there is no Malay.

## Credits

The speech belongs to the authors of the corpora in the table. Please cite them. The turn-taking statistics come from real
call-centre calls measured by Scicom (MSC) Berhad.
