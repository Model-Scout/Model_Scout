---
license: other
license_name: mixed-see-license-section
task_categories:
  - audio-to-audio
language:
  - en
  - ko
tags:
  - speech-separation
  - source-separation
  - cocktail-party
  - bilingual
  - english
  - korean
  - speech
pretty_name: MuSSeD Multilingual Speech Separation Dataset
size_categories:
  - 10K<n<100K
dataset_info:
  - config_name: 2spk
    features:
      - name: audio
        dtype: audio
      - name: file_id
        dtype: string
      - name: speaker_type
        dtype: string
      - name: meta
        dtype: string
    splits:
      - name: train
        num_bytes: 2161230124
        num_examples: 10000
      - name: dev
        num_bytes: 281341657.3
        num_examples: 1300
      - name: test
        num_bytes: 288195834.9
        num_examples: 1300
    download_size: 2704697738
    dataset_size: 2730767616.2000003
  - config_name: 3spk
    features:
      - name: audio
        dtype: audio
      - name: file_id
        dtype: string
      - name: speaker_type
        dtype: string
      - name: meta
        dtype: string
    splits:
      - name: train
        num_bytes: 2608317239
        num_examples: 10000
      - name: dev
        num_bytes: 337024379.8
        num_examples: 1300
      - name: test
        num_bytes: 331952820.8
        num_examples: 1300
    download_size: 3196579806
    dataset_size: 3277294439.6000004
  - config_name: 4spk
    features:
      - name: audio
        dtype: audio
      - name: file_id
        dtype: string
      - name: speaker_type
        dtype: string
      - name: meta
        dtype: string
    splits:
      - name: train
        num_bytes: 2958162977
        num_examples: 10000
      - name: dev
        num_bytes: 378898175.9
        num_examples: 1300
      - name: test
        num_bytes: 375917477.9
        num_examples: 1300
    download_size: 3610134728
    dataset_size: 3712978630.8
configs:
  - config_name: 2spk
    data_files:
      - split: train
        path: 2spk/train-*
      - split: dev
        path: 2spk/dev-*
      - split: test
        path: 2spk/test-*
  - config_name: 3spk
    data_files:
      - split: train
        path: 3spk/train-*
      - split: dev
        path: 3spk/dev-*
      - split: test
        path: 3spk/test-*
  - config_name: 4spk
    data_files:
      - split: train
        path: 4spk/train-*
      - split: dev
        path: 4spk/dev-*
      - split: test
        path: 4spk/test-*
---

# MuSSeD: Multilingual Speech Separation Dataset (English, Korean)

A bilingual **speech-separation** corpus of synthetic multi-speaker mixtures built from
English ([LibriTTS-R](https://www.openslr.org/141/)) and Korean read-speech sources ([AI-Hub Multi-Speaker Speech Synthesis corpus](https://www.aihub.or.kr/aihubdata/data/view.do?dataSetSn=542)).
Each mixture concatenates/overlaps **2, 3, or 4** single-speaker utterances, and every
mixture ships with rich per-speaker JSON metadata (speaker id, gender, language,
timing, transcription, overlap ratio, source utterance id).

- **Audio:** 16 kHz, mono, 16-bit PCM WAV
- **Mixtures:** 37,800 total — 30,000 train / 3,900 dev / 3,900 test
- **Speaker counts:** 2spk, 3spk, 4spk
- **Total duration:** ≈ 82.5 h (train ≈ 65.4 h, dev ≈ 8.5 h, test ≈ 8.6 h)
- **Languages:** English (`ENG`) + Korean (`KOR`), including bilingual mixtures
- **Speakers:** 514 speakers

---

## Reliability & Verification

MuSSeD is built for leakage-free, representative evaluation: splits are speaker-disjoint, 
dev/test mirror the train distribution, overlap spans the full difficulty range, and every mixture ships with complete 
per-speaker ground truth — each property is summarized below.

### 1. Speaker-disjoint splits

Speaker identity is parsed directly from the mixture filename (the token after each
`EN_`/`KO_` tag) and cross-checked between splits.

| Split | Unique speakers |
|-------|----------------:|
| train | 326 |
| dev   | 100 |
| test  | 88  |
| **total** | **514** (322 EN + 192 KO) |

### 2. Representative splits

The dev and test splits follow the same distributions as train for the properties
that matter for separation difficulty — bilingual share and overlap share are nearly
identical across splits, so validation/test numbers are representative of the training
distribution.

<img src="./figure/split_consistency.png" width="75%">

### 3. Controlled, full-range overlap

Overlap is not concentrated at one difficulty. Mixtures span the full range from
clean (no overlap) to fully overlapped, with the harder end growing as speaker count
increases (2-4 spk), which is the expected and desired behaviour.

<img src="./figure/overlap_distribution.png" width="70%">

### 4. Metadata

Every mixture has a paired JSON with per-speaker ground truth,
enabling exact, reproducible analysis of language / gender / overlap / timing.

---

## Composition

The share of bilingual mixtures grows with speaker count, while English-only /
Korean-only mixtures remain represented at every count:

<img src="./figure/language_composition.png" width="65%">

Across the 514 unique speakers, the male / female balance is:

<img src="./figure/gender_ratio.png" width="65%">

---

## Dataset Structure

```
MuSSeD-EnKo/
├── train/ {2spk,3spk,4spk}/
│   ├── raw/   <mixture_id>.wav
│   └── json/  <mixture_id>.json
├── dev/   {2spk,3spk,4spk}/ {raw,json}/
└── test/  {2spk,3spk,4spk}/ {raw,json}/
```

**Filename convention.** A mixture filename is the concatenation of its source
utterance ids, each of the form `EN_<spk>_...` or `KO_<spk>_...` — e.g. a 4spk file
`KO_5801_..._KO_5487_..._KO_5495_..._KO_5396_....wav` encodes speakers KO_5801,
KO_5487, KO_5495, KO_5396.

### JSON

```json
{
  "mixture_id": "EN_260_123286_000027_000001_EN_4992_41806_000003_000002",
  "speaker_count": 2,
  "overlapped_ratio": 0.0,
  "total_length_sec": 14.44,
  "speakers": [
    {
      "speaker_id": "260",
      "speaker_name": "Brad Bush",
      "gender": "Male",
      "language": "ENG",
      "length_sec": 2.48,
      "start_time_sec": 0.0,
      "end_time_sec": 2.48,
      "transcription": "I had rather not disturb him while he is quiet.",
      "original_file_id": "/test-clean/260/123286/260_123286_000027_000001"
    }
  ]
}
```

---

## Usage

```python
from datasets import load_dataset
import json

# config = "2spk" | "3spk" | "4spk"
ds = load_dataset("syshim/MuSSeD-EnKo", "2spk", split="test")

ex      = ds[0]
audio   = ex["audio"]              # {"array": np.ndarray, "sampling_rate": 16000}
meta    = json.loads(ex["meta"])   # per-mixture ground truth
n_src   = meta["speaker_count"]
overlap = meta["overlapped_ratio"]
langs   = [s["language"] for s in meta["speakers"]]
# ... train / evaluate your separation model ...
```

---

## License

This dataset is derived from multiple sources:

- **English audio** originates from **LibriTTS-R** (CC BY 4.0).
- **Korean audio** originates from a Multi-speaker Speech Synthesis Data by National Information Society Agency (NIA)

Because of these mixed terms the top-level tag is set to `other`.

## Citation

If you use this dataset, please cite LibriTTS-R, the Korean source corpus, and this release:
```bibtex
@misc{mousse2026,
  title  = {MOUSSE: MULTILINGUALOVERLAPPEDSPEECHSEPARATIONWITHPREDICTIVE UNCERTAINTYESTIMATION},
  year   = {2026}
}
```
