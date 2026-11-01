---
license: openrail
task_categories:
- feature-extraction
language:
- ko
- hi
- he
- gv
- tzh
- mdh
- lss
tags:
- audio
- speech
- prosody
- acoustics
- linguistics
- phonetics
- voice-analytics
- multilingual
pretty_name: Alexandria Voice Corpus — Multilingual Macro-Prosody Telemetry (v1.1 Replacement)
size_categories:
- 10K<n<100K
---

# Alexandria Voice Corpus — Multilingual Macro-Prosody Telemetry

**Version 1.1 — Replacement release**

This pack supersedes the earlier Korean & Hindi two-language release. That release was built on a pipeline with several unresolved quality-gate bugs (documented below). This version corrects all known issues and expands to seven typologically diverse languages.

No audio is included. This is a structured acoustic feature dataset for linguistic research, speech technology, and cross-linguistic prosody analysis.

Enterprise & Commercial Licensing

This 7-language prosody dataset is a free, open sample of Moonscape Software’s feature-extraction pipeline released under Open RAIL license. Moonscape Software also maintains a proprietary, commercially-cleared 1.2 million row Cross-Linguistic Macro Prosody Index. For enterprise licensing, bulk data access, or commercial applications, please contact: moonscapesoftware@gmail.com

---

## What changed from the previous release

The earlier `korean_cv24` and `hindi_cv24` files in the two-language pack were generated before three gate-level bugs were resolved:

| Bug | Effect on data |
|---|---|
| **BUG-029** — Missing C50 floor on T2 gate | High-reverb recordings admitted to STUDIO tier. Clips recorded in tiled bathrooms or reverberant rooms were incorrectly marked T2, inflating that tier and contaminating features like F0 smoothness and spectral tilt. |
| **BUG-030** — Missing speech-ratio floor on T2 gate | Sparse/silence-heavy clips admitted to STUDIO tier. Clips where >70% of the audio was ambient room tone were stamped T2. This inflated articulation_rate and skewed nPVI values. |
| **High-SNR branch C50 fix** | The fast path for very loud recordings (SNR ≥ 35 dB) also lacked the C50 floor, so a loud reverberant recording could bypass the room quality check entirely. |

All three are fixed in this release. The full T2 gate now requires simultaneously: SNR ≥ 25 dB **and** C50 ≥ 20 dB **and** speech_ratio ≥ 0.30. Tier labels have been retroactively corrected across all ledgers.

If you downloaded the previous pack, please replace both files.
---
License updated to Open RAIL. 

## License and Acceptable Use Policy (OpenRAIL)

This dataset is released under an **OpenRAIL (Responsible AI License)** framework. By downloading, accessing, or using this dataset, you explicitly agree to the following Permitted and Forbidden uses.

**Permitted Uses:**
You are encouraged to use this de-identified macro-prosody telemetry data for:
* Linguistic and cross-linguistic prosody research.
* Acoustic feature analysis and statistical modeling.
* Training and evaluating deepfake detection, anti-spoofing, or synthetic audio identification models.

**Strictly Forbidden Uses:**
Because this dataset contains extracted acoustic features and voice physics telemetry, the following use cases are strictly prohibited to protect biometric privacy:
1. **Speaker Re-Identification:** You may not attempt to reverse-engineer, unmask, re-link, or re-identify any individual speaker from this data, nor may you attempt to reconstruct the original source audio.
2. **Biometric Surveillance:** You may not use this data to develop, train, fine-tune, or enhance any biometric identification system, real-time tracking software, or law enforcement surveillance tool.
3. **Speech Synthesis / Voice Cloning:** You may not use this telemetry data to train, condition, or fine-tune generative Text-to-Speech (TTS), Voice Conversion (VC), or other synthetic voice generation models.

*Failure to comply with these behavioral restrictions immediately terminates your license to use this dataset.*


---

## Dataset Details

### Dataset Description

- **Curated by:** MoonScape Software
- **Version:** 1.1
- **Languages:** Korean, Hindi, Hebrew, Manx, Tzeltal, Maguindanao, Lasi
- **Source corpora:** Mozilla Common Voice CV24 (CC0-1.0) and Spontaneous Speech SPS2 (CC0-1.0)
- **License:** OpenRAIL
- **Total clips:** 58,830
- **Anonymization standard:** `moonscape_k5_v1`

### What is macro-prosody telemetry?

Macro-prosody refers to the suprasegmental properties of speech — pitch contour, rhythm, intensity, voice quality — measured at the utterance level. Each row in this dataset is one spoken clip with 30+ acoustic features extracted from it.

This is distinct from transcription, phoneme alignment, or word-level data. It is designed for population-level acoustic analysis, cross-linguistic typology research, and training prosody-aware speech models.

---

## Language Coverage

| Language | Code | Family | Corpus | Speech type | Clips | T1% | MetaGender% | Notes |
|---|---|---|---|---|---|---|---|---|
| Korean | `ko` | Koreanic (isolate) | CV24 | Scripted | 6,805 | 68% | 61% | Replacement for v1.0 |
| Hindi | `hi` | Indo-Aryan | CV24 | Scripted | 18,435 | 67% | 55% | Replacement for v1.0 |
| Hebrew | `he` | Semitic | CV24 | Scripted | 5,455 | 73% | 93% | Strong demographic metadata; heavily male-skewed (see notes) |
| Manx | `gv` | Celtic (Goidelic) | CV24 | Scripted | 6,579 | 98% | 0% | Near-extinct revival language; near-entirely PRISTINE quality |
| Tzeltal | `tzh` | Mayan | CV24 | Scripted | 5,585 | 57% | 68% | All meta-gender records are female (see notes) |
| Maguindanao | `mdh` | Austronesian | SPS2 | Spontaneous | 5,536 | 33% | 0% | No TSV demographics; gender is pitch-inferred only |
| Lasi | `lss` | Indo-Iranian (Sindhi) | SPS2 | Spontaneous | 10,435 | 59% | 0% | Large spontaneous corpus; no TSV demographics |

**Total: 58,830 clips** (395 suppressed by k-anonymity, 0.7% suppression rate)

### Typological notes

This pack was selected to span typologically distinct language families and speech types:

- **Korean** is a language isolate with phrase-final focus marking and complex mora timing — a useful contrast to the stress-timed Indo-Aryan languages.
- **Hindi** is the largest corpus here and provides strong statistical power for Indo-Aryan prosody baselines.
- **Hebrew** is a VSO Semitic language with root-and-pattern morphology; the high metadata coverage makes it useful for demographic-stratified analyses.
- **Manx** is a Celtic revival language with a tiny native speaker community. The 98% PRISTINE rate reflects the controlled recording conditions of motivated community contributors.
- **Tzeltal** is a Mayan language with ergative-absolutive alignment and a distinctive tonal register system. It is rarely represented in acoustic datasets.
- **Maguindanao** (SPS2) is spontaneous speech from a Philippine Austronesian language. The T2-heavy distribution reflects the naturalistic recording conditions of the SPS2 corpus.
- **Lasi** (SPS2) is a Sindhi variety spoken in Balochistan. Shorter median clip duration (3.4s vs 5–6s for CV24 languages) reflects the spontaneous speech format.

---

## Dataset Structure

Each Parquet file contains one row per utterance. Files are Snappy-compressed.

### Column reference

| Column | Type | Description |
|---|---|---|
| `clip_id` | string | Anonymized sequential ID (e.g. `korean_cv24_004521`) |
| `lang_code` | string | BCP-47 language code |
| `lang_name` | string | Language name |
| `corpus_id` | string | Source corpus (`cv24` or `sps2`) |
| `speech_type` | string | `scripted` or `spontaneous` |
| `tier` | int | Quality tier: 1 (PRISTINE) or 2 (STUDIO). T3/T4 suppressed at export. |
| `tier_label` | string | `PRISTINE` or `STUDIO` |
| `duration_ms` | int | Clip duration bucketed to nearest 100ms |
| `gender` | string | `male` / `female` / `other` / `unknown` |
| `gender_source` | string | `meta` (self-reported) / `inferred` (pitch-based) / `unknown` |
| `age` | string | Age bracket from CV metadata (where available; blank for SPS2) |
| `syllable_count_approx` | int | Approximate syllable count (vowel-count proxy; transcript removed) |
| `pitch_mean` | float32 | Mean F0 (Hz) |
| `pitch_std` | float32 | F0 standard deviation (Hz) |
| `pitch_range` | float32 | F0 range max–min (Hz) |
| `pitch_velocity_max` | float32 | Maximum rate of F0 change (Hz/s) |
| `intensity_mean` | float32 | Mean RMS intensity (dB) |
| `intensity_max` | float32 | Peak intensity (dB) |
| `intensity_range` | float32 | Dynamic range (dB) |
| `intensity_velocity_max` | float32 | Maximum rate of intensity change |
| `hnr_mean` | float32 | Harmonics-to-noise ratio (dB) |
| `cpps` | float32 | Cepstral peak prominence smoothed (breathiness) |
| `jitter_local` | float32 | Cycle-to-cycle pitch perturbation |
| `shimmer_local` | float32 | Cycle-to-cycle amplitude perturbation |
| `spectral_centroid_mean` | float32 | Mean spectral centroid (Hz) |
| `spectral_tilt` | float32 | Spectral slope (voice effort indicator) |
| `mfcc_delta_mean` | float32 | Mean MFCC delta (rate of spectral change) |
| `zcr_mean` | float32 | Zero-crossing rate |
| `teo_mean` | float32 | Teager energy operator mean |
| `teo_std` | float32 | Teager energy operator std dev |
| `f1_mean` | float32 | First formant mean (Hz) |
| `f2_mean` | float32 | Second formant mean (Hz) |
| `f3_mean` | float32 | Third formant mean (Hz) |
| `formant_dispersion` | float32 | F3–F1 dispersion (Hz) |
| `npvi` | float32 | Normalized pairwise variability index (rhythm) |
| `articulation_rate` | float32 | Syllables per second (speech intervals only) |
| `snr_median` | float32 | Median SNR (Brouhaha) |
| `c50_median` | float32 | Median C50 clarity (Brouhaha) |
| `speech_ratio` | float32 | Proportion of clip containing voiced speech |
| `emotion_score` | float32 | Brouhaha emotional arousal proxy |
| `dialect_tag` | string | Accent/dialect slug from CV metadata (where available; blank for SPS2) |
| `sample_type` | string | `core` (cream-selected) or null |


### Quality tiers

Clips were graded using [Brouhaha](https://github.com/marianne-m/brouhaha-vad) acoustic scoring. The T2 gate requires **all three** conditions simultaneously (corrected in v1.1):

| Tier | Label | SNR | C50 | Speech ratio | Description |
|---|---|---|---|---|---|
| T1 | PRISTINE | ≥ 35 dB | ≥ 35 dB | ≥ 0.30 | Studio/near-studio quality |
| T2 | STUDIO | ≥ 25 dB | ≥ 20 dB | ≥ 0.30 | Clean field recording, low reverb |
| T3 | WILD | ≥ 10 dB | any | ≥ 0.10 | Usable but noisy — **not exported** |
| T4 | TRASH | < 10 dB | any | < 0.10 | Rejected — **not exported** |

Only T1 and T2 clips appear in this dataset. T3 and T4 are excluded at export.

### Files

```
korean_cv24.parquet         6,805 rows   ~600 KB
hindi_cv24.parquet         18,435 rows   ~1.1 MB
hebrew_cv24.parquet         5,455 rows   ~475 KB
manx_cv24.parquet           6,579 rows   ~440 KB
tzeltal_cv24.parquet        5,585 rows   ~500 KB
mdn_cv24.parquet            5,536 rows   ~500 KB
lasi_cv24.parquet          10,435 rows   ~860 KB
```

---

## Dataset Creation

### Curation Rationale

This release addresses two gaps: the quality-gate bugs in the initial Korean/Hindi release, and the absence of any low-resource, non-Western language representation in the initial pack. Tzeltal, Manx, Lasi, and Maguindanao are rarely seen in structured acoustic datasets. The SPS2 spontaneous speech languages (Maguindanao, Lasi) provide a direct contrast to the CV24 scripted speech languages within this same release.

### Source Data

#### Processing Pipeline

1. MP3 source audio converted to 16 kHz mono WAV (ffmpeg, −20 dBFS normalization)
2. Quality grading via Brouhaha (SNR, C50, VAD) — T1/T2 retained only
3. Tier retroactively corrected post BUG-029/030 fix via `regrade_tiers.py`
4. Acoustic feature extraction via Parselmouth/Praat at 16 kHz
5. Cream selection (demographically balanced 25-minute representative subset per language) recorded in `sample_type` field
6. Anonymization and precision degradation applied at export

#### Source Data Producers

CV24 recordings were made by volunteer contributors to the Mozilla Common Voice project under CC0. SPS2 recordings were collected by the Mozilla Spontaneous Speech project under CC0. Contributors self-reported demographic metadata where willing; many rows will have blank age/accent fields.

### Anonymization — `moonscape_k5_v1`

- Original Mozilla filenames replaced with sequential anonymized clip IDs (mapping kept internal, never distributed)
- Transcripts removed entirely (approximate syllable count provided as proxy)
- All continuous acoustic variables truncated to 2 decimal places, stored as float32
- Duration bucketed to nearest 100ms
- K-anonymity at k=5 on `{gender, age_bucket, duration_bucket}` — rows in groups smaller than k=5 suppressed (395 rows suppressed across 7 languages, 0.7%)

---

## Bias, Risks, and Limitations

**Gender coverage varies significantly by language.** Hebrew has 93% self-reported gender metadata but is heavily male-skewed (4,982 male vs 95 female meta-labeled records). Tzeltal has 68% metadata coverage but all meta-labeled records are female — this reflects the contributor demographics of the CV24 Tzeltal community at time of collection, not the language population. Manx, Maguindanao, and Lasi have 0% self-reported gender; all gender labels are pitch-inferred and should be treated accordingly. Always inspect `gender_source` before demographic analyses.

**Scripted vs spontaneous speech are not directly comparable.** CV24 (Korean, Hindi, Hebrew, Manx, Tzeltal) is read speech from volunteer recordings of prompted sentences. SPS2 (Maguindanao, Lasi) is spontaneous conversational speech. Articulation rate, pause rate, nPVI, and pitch dynamics will differ systematically between the two corpus types — this is a real typological signal but also a corpus-type confound. The `speech_type` and `corpus_id` columns allow you to stratify analyses accordingly.

**Recording conditions are uncontrolled for CV24.** Common Voice contributors record at home on personal devices. Acoustic conditions vary widely; the quality gate reduces but does not eliminate this variance. Manx is an exception — the 98% PRISTINE rate suggests a tightly controlled recording campaign by the community.

**Lasi and Maguindanao lack TSV demographic metadata.** The SPS2 corpus was released without validated speaker demographic files. Age, accent, and dialect fields will be blank for these languages. Gender is pitch-inferred only.

**Formant data (F1/F2/F3) is present but may be unreliable for tonal languages.** The Parselmouth formant tracker can produce artifacts in tonal contexts. Cross-validate against known formant benchmarks before using F1/F2/F3 for Korean, Tzeltal, or Maguindanao.

**Prohibited use:** Do not attempt to use this dataset for speaker identification, speaker re-linking to source audio, or any form of individual re-identification. This is prohibited regardless of technical feasibility and violates the terms of use.

### Recommendations

Use `gender_source == 'meta'` to filter to self-reported labels for any demographic analysis. Use `corpus_id` to separate scripted from spontaneous comparisons. For rhythm typology work, `npvi` and `articulation_rate` are the most reliable features in this release. Treat `intensity_mean` and `intensity_max` with caution — Mozilla applies normalization during encoding which compresses the true dynamic range.

---

## Citation

```bibtex
@dataset{alexandria_multilingual_prosody_v1_1_2026,
  title     = {Alexandria Voice Corpus --- Multilingual Macro-Prosody Telemetry v1.1},
  author    = {MoonScape Software},
  year      = {2026},
  license   = {OpenRAIL},
  note      = {Derived from Mozilla Common Voice CV24 and Spontaneous Speech SPS2 (CC0).
               Acoustic features extracted via Parselmouth/Praat. v1.1 corrects
               quality-gate bugs BUG-029, BUG-030, and high-SNR C50 bypass present
               in the earlier Korean/Hindi release.}
}

@misc{mozilla_common_voice,
  title     = {Common Voice: A Massively-Multilingual Speech Corpus},
  author    = {Ardila, Rosana and others},
  year      = {2020},
  url       = {https://commonvoice.mozilla.org}
}
```

---

## Glossary

| Term | Definition |
|---|---|
| **F0 / pitch_mean** | Fundamental frequency — perceived pitch, Hz |
| **HNR** | Harmonics-to-noise ratio — higher = cleaner, more periodic voice |
| **CPPS** | Cepstral peak prominence smoothed — lower = breathier voice |
| **nPVI** | Normalized pairwise variability index — durational variability between adjacent syllables; higher in stress-timed languages |
| **C50** | Clarity metric — higher = less reverb/echo |
| **SNR** | Signal-to-noise ratio — higher = cleaner recording |
| **Brouhaha** | Quality scoring model: [github.com/marianne-m/brouhaha-vad](https://github.com/marianne-m/brouhaha-vad) |
| **T1 / PRISTINE** | SNR ≥ 35, C50 ≥ 35, speech_ratio ≥ 0.30 |
| **T2 / STUDIO** | SNR ≥ 25, C50 ≥ 20, speech_ratio ≥ 0.30 (all three required simultaneously) |
| **moonscape_k5_v1** | Anonymization: k=5 suppression + sequential IDs + 2dp truncation + 100ms duration bucketing |
| **CV24** | Mozilla Common Voice 24.0 — scripted read speech |
| **SPS2** | Mozilla Spontaneous Speech 2.0 — unscripted conversational speech |

---

## Contact

Chris - Founder and Lead Systems Design
moonscapesoftware@gmail.com