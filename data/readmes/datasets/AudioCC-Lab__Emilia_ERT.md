---
language: [de, en, fr, ja, ko, zh]
license: cc-by-nc-4.0
pretty_name: Emilia ERT
size_categories:
- 1M<n<10M
---

# Emilia ERT

## Dataset summary

Emilia ERT contains **9,310,186 speech segments totaling 26,133.85 hours** in six languages, distributed as **666 audio TAR shards** and a single **34-column metadata table**, `metrics.scp`. The data originate from [Emilia dataset](https://huggingface.co/datasets/amphion/Emilia-Dataset) and were selected using the **SQA+SED filtering strategy described in the accompanying paper**, combining speech quality assessment (SQA) and sound event detection (SED). Existing transcripts and automatic audio metrics are included.



| Language | Code | Segments | Duration (hours) | TAR shards |
| --- | --- | ---: | ---: | ---: |
| German | de | 166,600 | 433.62 | 10 |
| English | en | 4,619,380 | 13,370.38 | 333 |
| French | fr | 78,751 | 191.89 | 12 |
| Japanese | ja | 203,264 | 391.90 | 27 |
| Korean | ko | 11,640 | 30.20 | 1 |
| Chinese | zh | 4,230,551 | 11,715.86 | 283 |
| **Total** | | **9,310,186** | **26,133.85** | **666** |

Durations are sums of the `length(s)` values in the released `metrics.scp`, converted to hours and rounded to two decimal places. All 9,310,186 records have numeric duration values.

Audio archives occupy 665,879,367,680 bytes; `metrics.scp` occupies 6,134,693,898 bytes. No held-out evaluation split is provided. Define appropriate speaker/source-disjoint splits for experiments.

<!-- ## Data source and filtering

The source collection is `emilia_complete`, derived from the original [Emilia dataset](https://huggingface.co/datasets/amphion/Emilia-Dataset). This release contains the data retained after applying the paper's **SQA+SED** filtering strategy: SQA provides speech-quality measurements, while SED provides sound-event information used in the selection. The source is recorded as `Emilia_complete` in the `datasets` column. Emilia-YODAS is not included.

Release preparation preserved the already selected audio and its metadata; it did not rerun the filtering strategy. The duration statistics above describe this filtered release. -->



## Files and audio addressing

```text
.
├── audio/
│   ├── DE-B000000.tar
│   ├── EN-B000000.tar
│   └── ...
├── metrics.scp
├── SHA256SUMS
├── LICENSE
└── README.md
```

`metrics.scp` is a UTF-8, TAB-separated table with a header, despite its extension. It is not a conventional two-column Kaldi SCP. Column order, values, precision, and source missing-value markers were preserved; only `path` was converted to a repository-relative locator:

```text
audio/DE-B000000.tar:512:154989
```

The components are **TAR path : byte offset : byte length**. The offset points to the encoded MP3 payload, not the TAR header. Archive members retain their local numeric names; `uid` supplies the original-style Emilia identifier. Archives were retained byte-for-byte without re-encoding during release preparation. Do not recompress or rebuild them while using these offsets.

## Metadata fields

Types describe valid values; all cells are stored as text. Handle missing or nonnumeric markers explicitly rather than converting them to zero. Related outputs are grouped into a single metric entry below; column numbers refer to the unchanged 34-column SCP schema.

| # | Field | Type / unit | Meaning |
| ---: | --- | --- | --- |
| 1 | `datasets` | string | Local source label; `Emilia_complete` throughout this release. |
| 2 | `uid` | string | Segment identifier, e.g. `DE_B00008_S00023_W000000`; the prefix identifies the source language. |
| 3 | `fs` | integer, Hz | Sample rate recorded in the source manifest. Scoring models may internally resample audio. |
| 4 | `path` | string | Relative TAR path, payload offset, and payload length, separated by colons. |
| 5 | `length(s)` | float, seconds | Segment duration from the source table. |
| 6 | `silerovad` | float, fraction | Silero VAD detected-speech duration divided by total duration. |
| 7 | `webrtcvad` | float, fraction | Speech fraction estimated by the WebRTC VAD workflow. |
| 8 | `transcript` | string | Automatic transcript from the local WhisperX workflow; not a verified human transcription. |
| 9 | `confidence` | float, score | Mean of available WhisperX aligned-word scores in the inspected implementation; not a calibrated probability of transcript correctness. |
| 10 | `dnsmos` | float, predicted MOS | DNSMOS overall quality output (`DNSMOS_OVRL`). |
| 11 | `scoreq` | float, model score | SCOREQ speech-quality estimate on the model's native scale. |
| 12–14 | `squim_pesq`, `squim_sisdr`, `squim_stoi` | float; PESQ score, SI-SDR in dB, STOI score | Non-intrusive estimates of perceptual speech quality (PESQ), scale-invariant signal-to-distortion ratio (SI-SDR), and short-time objective intelligibility (STOI), respectively. These are model predictions without a clean reference. |
| 15 | `srmr` | float, ratio | Speech-to-reverberation modulation energy ratio, a non-intrusive reverberation-related measure. |
| 16 | `vqscore` | float, model score | VQScore non-intrusive speech-quality estimate. |
| 17 | `wadasnr` | float, dB | Signal-to-noise ratio estimated using waveform amplitude distribution analysis (WADA-SNR). |
| 18 | `distillmos` | float, predicted MOS | DistillMOS speech-quality estimate. |
| 19 | `utmos` | float, predicted MOS | UTMOS speech-quality estimate. |
| 20 | `dnsmos_pro` | float, model score | DNSMOS Pro quality output retained from the local scoring workflow. |
| 21 | `nisqa` | float, predicted MOS | NISQA overall quality estimate (`NISQA_MOS`). |
| 22–28 | `sigmos_ovrl`, `sigmos_col`, `sigmos_disc`, `sigmos_loud`, `sigmos_noise`, `sigmos_reverb`, `sigmos_sig` | float, predicted quality ratings | Ratings for overall quality, coloration, discontinuity, loudness, background noise, reverberation, and speech-signal quality, respectively. These are predicted quality dimensions, not physical impairment measurements. |
| 29 | `ced` | float, probability score | Maximum CED probability over the workflow's selected noise/event classes. |
| 30 | `flexsed` | float, probability score | Maximum FlexSED probability over selected noise/event prompts and time frames in the inspected workflow. |
| 31 | `panns` | float, probability score | Maximum PANNs clip-level probability over selected classes at AudioSet. |
| 32 | `beats` | string | BEATs highest-scoring selected non-speech event label followed by its score, e.g. `Inside, small room 0.0067`. Split from the right to extract the final numeric score. |
| 33–34 | `speaker_count`, `overlap_ratio` | integer count; float fraction | Both are derived from Sortformer diarization outputs. `speaker_count` respents the number of speakers in the audio and `overlap_ratio` represents the degree of overlap between the speakers. |



## Usage

Download `metrics.scp` and the required shards, then parse with an explicit TAB delimiter. Plain whitespace splitting would corrupt transcripts and event labels.

```python
import csv
from pathlib import Path

root = Path("/path/to/Emilia_ERT")
with (root / "metrics.scp").open(encoding="utf-8", newline="") as f:
    row = next(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))

relative, offset, size = row["path"].rsplit(":", 2)
with (root / relative).open("rb") as f:
    f.seek(int(offset))
    audio_bytes = f.read(int(size))
assert len(audio_bytes) == int(size)
print(row["uid"], row["transcript"])

# Optional MP3 decoding with a compatible libsndfile installation:
# import io
# import soundfile as sf
# waveform, sample_rate = sf.read(io.BytesIO(audio_bytes))
```



## License and access review


[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/legalcode.en) permits noncommercial sharing and adaptation within the licensor's rights, subject to attribution, a license reference, retention of supplied notices, and indication of changes. It does not independently clear third-party rights. See [LICENSE](LICENSE) for the attribution notice.
