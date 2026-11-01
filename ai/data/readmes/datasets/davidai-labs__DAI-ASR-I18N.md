---
pretty_name: DAI-ASR-I18N
license: other
license_name: dai-asr-i18n-dua
license_link: https://huggingface.co/datasets/davidai-labs/DAI-ASR-I18N/blob/main/DATA_USE_AGREEMENT.md
language: [ar, bn, de, en, es, fr, hi, id, it, ja, ko, mr, pt, ru, ta, te, th, tl, tr, vi, zh]
task_categories: [automatic-speech-recognition]
tags: [speech, asr, diarization, multilingual, conversational, i18n, benchmark, evaluation]
size_categories: [1K<n<10K]
extra_gated_prompt: >-
  Access to DAI-ASR-I18N is granted on request under the DAI-ASR-I18N Data Use Agreement (evaluation,
  benchmarking and non-commercial research; evaluation of commercial models is permitted). The data
  contains recordings of identifiable people. You agree to the Data Use Agreement: no training use of
  any kind, no re-identification, no redistribution, and deletion of specific recordings within 30 days
  when a removal request is propagated to you.
extra_gated_fields:
  Name: text
  Institutional Email: text
  Affiliation: text
  Country: country
  Intended use (evaluation, benchmarking or research): text
  I agree to the Data Use Agreement, including that the dataset is never used to train, fine-tune or optimize any model: checkbox
  I agree not to attempt re-identification of any speaker: checkbox
  I agree not to redistribute, and to honor propagated deletion requests: checkbox
---

# Dataset Card for DAI-ASR-I18N

- **Publication:** https://research.withdavid.ai/blog/dai-asr-i18n
- **GitHub repo:** https://github.com/withdavid-ai/dai-asr-i18n

DAI-ASR-I18N is a benchmark from David AI for speech recognition and speaker diarization on everyday
two-speaker conversations across 21 languages. In the audio corpus, each speaker is recorded on a separate
channel, and each clip includes human-verified, speaker-attributed verbatim transcripts. The conversations
are unscripted and capture natural speech patterns, including interjections and backchanneling. To make the
benchmark reproducible and support open speech research, we release a frozen public dataset containing about
two hours of audio per language.

- **Dataset Owner:** David AI Labs
- **Languages:** 21 (listed below)
- **License:** custom Data Use Agreement (`license: other`); see [Access and licensing](#access-and-licensing)
- **Release snapshot:** `2026-09-26`
- **Scoring code and methodology:** the David AI's DAI-ASR-I18N repository, released under the MIT License.

## Supported tasks and metrics

- **Automatic speech recognition.** The public headline metric is **WER** for every benchmark language
  except Chinese, Japanese, Korean, and Thai, which use **CER**. Reference and hypothesis text are normalized
  with the same deterministic per-language policy. For speaker-attributed transcription accuracy we report
  **cpWER**/**cpCER**.
- **Speaker diarization.** Diarization uses **DER** with its miss, false-alarm, and speaker-confusion
  components, plus speaker-count metrics.

## Languages

Arabic (ar), Bengali (bn), Chinese (zh), English (en), French (fr), German (de), Hindi (hi), Indonesian
(id), Italian (it), Japanese (ja), Korean (ko), Marathi (mr), Portuguese (pt), Russian (ru), Spanish (es),
Tagalog (tl), Tamil (ta), Telugu (te), Thai (th), Turkish (tr), and Vietnamese (vi).

## Dataset statistics

| Statistic | Public release |
|---|---:|
| Clips | 1,035 |
| Total two-channel audio duration | 42.1 hours |
| Speaker channels | 2,070 (2 per clip) |
| Approximate speaker-channel duration | 84.2 hours |
| Languages | 21 |
| Distinct speakers | 682 |
| Speaker-channel gender (weighted by speaker channel) | 54.4% female, 44.3% male, 1.2% undisclosed |

## Splits

- **Public evaluation set (released here):** about two hours per language across 21 languages.
- **Private held-out set (not released):** retained to reduce training-data contamination and kept private.

## Dataset structure

The dataset is delivered as **per-clip audio files** plus a **metadata and transcript table** (one row per
clip, keyed by `sample_id`). Each clip provides two per-speaker channels (`ch1`, `ch2`), each a
single-channel (mono) track, delivered as lossless **FLAC** under `audio/<sample_id>/{ch1,ch2}.flac`, at
its native source sample rate (16, 24, 32, or 44.1 kHz; 16-bit). A mixed-speaker mono track is not shipped;
we provide the code in our repo for mixing. The table below carries the metadata and the transcript.

Metadata and transcript columns:

- **Metadata:** `sample_id` (a stable namespaced UUID — `uuid5` — of the source id), `language`, `locale`,
  `duration_type` (short ≤6 min / long ≥14 min), `duration_s`, `n_speakers`, `topic`,
  `overlap_type` (low <10% / medium 10–20% / high ≥20%), `clip_overlap_frac`, `speaker1_gender`,
  `speaker2_gender`, `speaker1_id`, `speaker2_id`, `benchmark_set`. `speaker1_id` and `speaker2_id` are
  stable namespaced UUIDs (`uuid5`, same namespace as `sample_id`) for the two speakers: a speaker keeps
  the same id across every clip they appear in, so clips can be grouped by speaker, but the id cannot be
  linked back to any real identity. No real speaker identity is released.
- **Transcript:** `word_alignments`, the human-verified, speaker-attributed transcript carrying both the
  reference **text** and its **word-level timing**, as a list of per-segment structs
  `{speaker, start, end, timing_source, words:[{start, end, text}]}`. The reference text for WER/CER/cpWER
  is the sequence of `words[].text`; the `start`/`end` on each word carry the timing for DER.

`word_alignments` carries the word-level text and timestamps, produced by language-specific forced
alignment with a MeetEval character-based pseudo-timing fallback for segments whose forced alignment
failed (`timing_source: "pseudo"`; otherwise the acoustic forced timing is retained).

```json
{
  "sample_id": "e007337e-293e-5296-aaee-3f05b85c5658",
  "language": "en",
  "locale": "en-US",
  "duration_type": "long",
  "duration_s": 120.4,
  "n_speakers": 2,
  "topic": "...",
  "overlap_type": "low",
  "clip_overlap_frac": 0.07,
  "speaker1_gender": "female",
  "speaker2_gender": "male",
  "speaker1_id": "54984bde-f203-5146-ab7f-28a346faa5ec",
  "speaker2_id": "b9b671d4-a2bc-5c3d-8b15-169462340343",
  "benchmark_set": "public",
  "word_alignments": [
    {"speaker": 1, "start": 0.42, "end": 2.81, "timing_source": null,
     "words": [{"start": 0.42, "end": 0.71, "text": "..."}]},
    {"speaker": 2, "start": 2.95, "end": 4.10, "timing_source": "pseudo",
     "words": [{"start": 2.95, "end": 3.30, "text": "..."}]}
  ]
}
```

## Dataset creation

- **Source data.** Natural two-party conversations recorded per speaker channel by contributors engaged for
  data collection.
- **Transcripts.** Human-verified verbatim transcripts, speaker-attributed at the segment level.
- **Word-level timestamps.** We used language-specific forced-alignment algorithms to obtain word-level
  timestamps for the transcript in order to evaluate time-based metrics (DER). Segments whose forced
  alignment failed fall back to MeetEval character-based pseudo timing, recorded as `timing_source: "pseudo"`.

## Data access and privacy

Recipients must follow the approved Data Use Agreement and all privacy laws applicable to their processing.

Do not attempt to identify, locate, or contact a speaker. Report suspected sensitive-content or consent
issues to **research@withdavid.ai**. The release's consent-withdrawal and erasure procedure, including
recipient-notification obligations, is defined in the Data Use Agreement.

Important notes:

- **Evaluation only, never training.** This is a test benchmark, not training data. Evaluating commercial models
  is permitted; using the data to train, fine-tune or optimize any model is prohibited.
- **Coverage and balance.** Balanced to about two hours per language and roughly balanced by gender.
- **Data collection.** The data collection process follows a rigorous standard under applicable privacy laws;
  individual contributors are compensated at a fair market rate in their local regions.

## Access and licensing

- **Data:** access is gated and granted under the **DAI-ASR-I18N Data Use Agreement, version 1.1, dated
  2026-10-02** (`license: other`). The agreement permits evaluating and benchmarking models, including
  commercial models, and non-commercial research. It prohibits any training use, re-identification,
  speaker or biometric identification, and redistribution, and requires recipients to delete withdrawn
  recordings within 30 days of notice. Requesting Hub access does not replace the agreement; access is granted only
  after the required agreement and review steps are complete.
- **Code:** the evaluation harness and scoring code are released separately under the **MIT License** in the
  David AI ASR Bench repository (`https://github.com/withdavid-ai/dai-asr-i18n`).

## Citation

```bibtex
@techreport{davidai2026dai-asr-i18n,
  title       = {DAI-ASR-I18N: A Multilingual, Dual-Channel Conversational Benchmark for Speech Recognition and Speaker Diarization},
  author      = {{David AI}},
  institution = {David AI},
  year        = {2026},
  url         = {https://research.withdavid.ai/},
}
```
