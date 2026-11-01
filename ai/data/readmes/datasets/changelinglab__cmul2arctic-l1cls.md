---
license: cc-by-nc-4.0
arxiv: 2601.14046
task_categories:
  - audio-classification
language:
  - en
  - ar
  - es
  - hi
  - ko
  - vi
  - zh
tags:
  - speech
  - accent
  - l1-classification
  - native-language-identification
size_categories:
  - 10K<n<100K
configs:
  - config_name: default
    data_files:
      - split: train
        path:
          - cmu/train/*.parquet
          - l2arctic/train/*.parquet
      - split: val
        path:
          - cmu/val/*.parquet
          - l2arctic/val/*.parquet
      - split: test
        path:
          - cmu/test/*.parquet
          - l2arctic/test/*.parquet
dataset_info:
  features:
    - name: audio
      dtype:
        audio:
          sampling_rate: 16000
    - name: corpus
      dtype: string
    - name: l1_label
      dtype: string
    - name: speaker_id
      dtype: string
    - name: utt_id
      dtype: string
  splits:
    - name: train
      num_bytes: 4541009465
      num_examples: 15714
    - name: val
      num_bytes: 2397896973
      num_examples: 7919
    - name: test
      num_bytes: 2110676527
      num_examples: 7762
  download_size: 9049582965
  dataset_size: 9049582965
---

# CMU + L2-ARCTIC Combined Dataset for L1 Classification

This dataset combines **CMU Arctic** (native English speakers) and **L2-ARCTIC** (non-native English speakers) for L1 (native language) classification research. It is redistributed for the purpose of **academic reproducibility**.

Audio is embedded in Parquet files for efficient loading via HuggingFace `datasets`.

## Dataset Description

| Subset | Source | Speakers | L1 Labels | License |
|--------|--------|----------|-----------|---------|
| `cmu/` | [CMU Arctic](http://www.festvox.org/cmu_arctic/index.html) | 4 native English speakers | `en` | CMU Arctic license (see CMU Arctic website) |
| `l2arctic/` | L2-ARCTIC | 24 non-native English speakers | `ar`, `es`, `hi`, `ko`, `vi`, `zh` | [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) |

### Splits

| Split | CMU | L2-ARCTIC | Total |
|-------|-----|-----------|-------|
| train | 2,264 | 13,450 | 15,714 |
| val | 1,132 | 6,787 | 7,919 |
| test | 1,132 | 6,630 | 7,762 |
| **Total** | **4,528** | **26,867** | **31,395** |

### Schema

| Column | Type | Description |
|--------|------|-------------|
| `audio` | struct | `{path: string, bytes: binary}` - Audio data with original relative path |
| `corpus` | string | `cmu` or `l2arctic` |
| `l1_label` | string | L1 language code (`en`, `ko`, `zh`, `ar`, `hi`, `es`, `vi`) |
| `speaker_id` | string | Speaker identifier |
| `utt_id` | string | Utterance identifier |

## License

> ⚠️ **Important**: This dataset contains data from two sources with **different licenses**.

| Folder | Source | License | Commercial Use |
|--------|--------|---------|----------------|
| `cmu/` | [CMU Arctic](http://www.festvox.org/cmu_arctic/index.html) | CMU Arctic license (see CMU Arctic website) | ✅ Allowed |
| `l2arctic/` | L2-ARCTIC | [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/legalcode) | ❌ Non-commercial only |

**Combined usage requires compliance with CC BY-NC 4.0 (non-commercial use only).**

## Usage

### Load Combined Dataset

```python
from datasets import load_dataset, Audio

# Load one split using the pre-defined split metadata
train_ds = load_dataset("y00njaekim/cmul2arctic-l1cls", split="train")

# Or load all splits at once
ds = load_dataset("y00njaekim/cmul2arctic-l1cls")

# Access a sample
sample = train_ds[0]
print(f"L1: {sample['l1_label']}, Speaker: {sample['speaker_id']}")

# Decode audio bytes
audio_bytes = sample["audio"]["bytes"]
audio_path = sample["audio"]["path"]
```

## Attribution

### CMU Arctic

- **Website**: http://www.festvox.org/cmu_arctic/index.html
- **Technical Report**: [CMU Arctic Report (PDF)](http://www.festvox.org/cmu_arctic/cmu_arctic_report.pdf)

### L2-ARCTIC

As requested by the original authors, please cite the following paper if you use L2-ARCTIC:

```bibtex
@inproceedings{zhao2018l2arctic,
    author={Guanlong {Zhao} and Sinem {Sonsaat} and Alif {Silpachai} and
            Ivana {Lucic} and Evgeny {Chukharev-Hudilainen} and John {Levis} and
            Ricardo {Gutierrez-Osuna}},
    title={L2-ARCTIC: A Non-native English Speech Corpus},
    year=2018,
    booktitle={Proc. Interspeech},
    pages={2783–2787},
    doi={10.21437/Interspeech.2018-1110},
    url={http://dx.doi.org/10.21437/Interspeech.2018-1110}
}
```

**Original Source**: https://psi.engr.tamu.edu/l2-arctic-corpus/

You can use this dataset with our benchmarking toolkit at https://github.com/changelinglab/prism
```
@misc{prism2026,
      title={PRiSM: Benchmarking Phone Realization in Speech Models}, 
      author={Shikhar Bharadwaj and Chin-Jou Li and Yoonjae Kim and Kwanghee Choi and Eunjung Yeo and Ryan Soh-Eun Shim and Hanyu Zhou and Brendon Boldt and Karen Rosero Jacome and Kalvin Chang and Darsh Agrawal and Keer Xu and Chao-Han Huck Yang and Jian Zhu and Shinji Watanabe and David R. Mortensen},
      year={2026},
      eprint={2601.14046},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2601.14046}, 
}
```

## Acknowledgments

This dataset redistribution is provided for academic reproducibility purposes. All credit for the original data collection belongs to the respective research teams at Carnegie Mellon University and Texas A&M University.
