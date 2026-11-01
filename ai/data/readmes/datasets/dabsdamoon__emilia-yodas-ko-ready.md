---
license: cc-by-4.0
language:
  - ko
task_categories:
  - text-to-speech
pretty_name: emilia-yodas-ko-ready (Korean, quality-filtered Emilia-YODAS, 24 kHz parquet)
size_categories:
  - 100K<n<1M
tags:
  - speech
  - tts
  - emilia-yodas
  - ko
gated: auto
extra_gated_heading: "Acknowledge the license and source terms to access this dataset"
extra_gated_description: "Access is granted automatically once you agree. This is a filtered subset of Emilia-YODAS (CC BY 4.0), whose recordings come from Creative Commons YouTube videos via YODAS."
extra_gated_button_content: "I agree and request access"
extra_gated_prompt: >-
  By requesting access you agree to the following. (1) You will use the data under the CC BY 4.0 license and keep the
  attribution to Emilia, YODAS and this repository in any redistribution or derivative. (2) You accept full
  responsibility for your use of the data and will not hold the authors of Emilia, YODAS or this repository liable.
  (3) If you provide colleagues with access to the data, they must first agree to these same terms. (4) You will honor
  removal requests: if a speaker or video owner asks for their recordings to be removed, you will delete the
  corresponding rows from your copies (the `speaker` column carries the source video id). (5) You will not attempt to
  identify, impersonate or clone the voice of a specific speaker in the data.
extra_gated_fields:
  I agree to the terms above: checkbox
  Intended use:
    type: select
    options:
      - Research
      - Education
      - Commercial product
      - label: Other
        value: other
---

# emilia-yodas-ko-ready

Korean speech selected from **Emilia-YODAS** (the CC BY 4.0 part of `amphion/Emilia-Dataset`), quality-filtered and repackaged as 24 kHz FLAC-in-parquet shards for TTS and aligner training.

| Item | Value |
|---|---|
| Source | Emilia-YODAS, Korean subset |
| Selection | 24 kHz · 64 kbps source MP3 only · DNSMOS ≥ 3.3 (Emilia's per-file score) · duration ≤ 15 s · measured effective bandwidth ≥ 11 kHz (LTAS −60 dB point, per file) · then the top-DNSMOS files up to a 400 h cap per language |
| Rows | 166,578 utterances · 400.0 h · 30,056 speaker labels |
| Audio | 24 kHz mono FLAC bytes in `audio` (MP3 decoded once, even-length trimmed) |
| Shards | 167 × `part-NNNNN.parquet` (≈1,000 rows each), `_manifest.json` |
| Columns | `uid`, `audio`, `num_samples`, `sampling_rate`, `text`, `phonemes`, `speaker`, `speaker_id`, `language`, `split`, noise metrics (`noise_sibilance`, `noise_env_dr`, `noise_tonal`, `noise_rms_dbfs`), pitch placeholders (`f0_*`, `f0_extractor = PENDING`), and selection metadata `dnsmos`, `bw60` (measured bandwidth, Hz), `kbps`, `src_tar`, `rank` (DNSMOS rank), `src_sec`, `clip_rate` |

`speaker` keeps the Emilia speaker label (`KO_<video>_SPEAKER_NN`); `speaker_id` is an integer block reserved per language. `split` is a per-utterance train/val assignment used by our training code. `phonemes` is an espeak-ng IPA string from our shared phonemizer.

## License and attribution

The recordings and transcripts come from Emilia-YODAS and are redistributed under **CC BY 4.0**. Please cite:

- He et al., *Emilia: An Extensive, Multilingual, and Diverse Speech Dataset for Large-Scale Speech Generation* (2024) — https://huggingface.co/datasets/amphion/Emilia-Dataset
- Li et al., *YODAS: Youtube-Oriented Dataset for Audio and Speech* (2023) — the source of the YODAS recordings (Creative Commons licensed YouTube videos)

Our selection and repackaging (quality filter, bandwidth measurement, parquet layout, phonemes, metadata) are released under the same CC BY 4.0 terms.

## Notes

- Effective bandwidth of 64 kbps MP3 sources tops out near 11.25 kHz (encoder low-pass), so ≥ 12 kHz material does not exist in this source; the 11 kHz gate keeps the full-band files.
- DNSMOS is the per-file score shipped with Emilia; it was not recomputed.
- Pitch (`f0_crepe`) columns are placeholders (`PENDING`) in this release.

## Access terms

This repository is gated with automatic approval. Requesting access means agreeing to use the data under CC BY 4.0 with attribution to Emilia, YODAS and this repository, to take responsibility for your own use, to pass these terms on to anyone you share the data with, to honor removal requests from speakers or video owners (the `speaker` column carries the source video id), and not to identify, impersonate or clone specific speakers. These mirror the access terms of the upstream `amphion/Emilia-Dataset`.
