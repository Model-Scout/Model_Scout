---
language:
- ko
license: other
task_categories:
- text-generation
arxiv: 2512.18834
configs:
- config_name: minhash_deduped
  data_files:
  - split: train
    path: minhash_deduped/**/*.parquet
- config_name: quality_filtered
  data_files:
  - split: train
    path: quality_filtered/**/*.parquet
- config_name: matched
  data_files:
  - split: train
    path: consensus/*.parquet
default: minhash_deduped
---

<p align="center">
  <a href="https://huggingface.co/collections/AdaMLLab/mixminmatch">
    <img src="https://img.shields.io/badge/🤗_Collection-MixMinMatch-blue" alt="MixMinMatch Collection">
  </a>
</p>

KorMix ([https://arxiv.org/abs/2512.18834](https://arxiv.org/abs/2512.18834)) is a Korean pretraining corpus built by combining five publicly available Korean datasets, applying Korean-specific quality filtering, and performing cross-dataset deduplication.

## Subsets

| Subset | Description |
|--------|-------------|
| `quality_filtered` | Quality-filtered data before deduplication |
| `minhash_deduped` | Document-level MinHash deduplication |
| `matched` | Documents appearing in 2+ source datasets |

The matched subset uses cross-dataset agreement as a signal for quality.

## Usage

```python
from datasets import load_dataset

ds = load_dataset("AdaMLLab/KorMix", "minhash_deduped")
ds = load_dataset("AdaMLLab/KorMix", "quality_filtered")
ds = load_dataset("AdaMLLab/KorMix", "matched")
```

## Sources

- FineWeb-2 (`HuggingFaceFW/fineweb-2`, `kor_Hang`)
- HPLT 2.0 (`HPLT/HPLT2.0_cleaned`, `kor_Hang`)
- CulturaX (`uonlp/CulturaX`, `ko`)
- C4 (`allenai/c4`, `ko`)
- FinePDFs (`HuggingFaceFW/finepdfs`, `kor_Hang`)

## Pipeline

1. Quality filtering with Korean-specific thresholds (Hangul script ratio, no-space-language adjustments for word-level metrics, repetition patterns)
2. Document-level MinHash deduplication (5-gram shingles, 14 bands, 8 hashes per band, similarity threshold 0.8)
3. Cross-source matching to identify documents appearing in 2+ independent sources

## Citation

```bib
@misc{alrashed2025mixminmatch,
      title={Mix, MinHash, and Match: Cross-Source Agreement for Multilingual Pretraining Datasets},
      author={Sultan Alrashed and Francesco Orabona},
      year={2025},
      eprint={2512.18834v2},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2512.18834v2},
}
```

## License

See individual source dataset licenses.
