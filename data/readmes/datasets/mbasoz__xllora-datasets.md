---
pretty_name: XL-LoRA Multilingual Triplet Dataset
license: cc-by-4.0
task_categories:
- sentence-similarity
- text-retrieval
language:
- afr
- af
- hin
- hi
- tel
- te
- mar
- mr
- ind
- id
- hau
- ha
- kor
- ko
configs:
- config_name: afr
  data_files: xllora-afrikaans.csv
- config_name: hin
  data_files: xllora-hindi.csv
- config_name: tel
  data_files: xllora-telugu.csv
- config_name: mar
  data_files: xllora-marathi.csv
- config_name: ind
  data_files: xllora-indonesian.csv
- config_name: hau
  data_files: xllora-hausa.csv
- config_name: kor
  data_files: xllora-korean.csv
---

# XL-LoRA Multilingual Triplet Dataset

This dataset contains multilingual sentence triplets generated using the **XL-LoRA** method described in the paper:

**[Bootstrapping Embeddings for Low Resource Languages](https://arxiv.org/abs/2603.01732)**

Each subset corresponds to a language and can be loaded using its **ISO 639-3 language code**.

## Dataset Structure

All subsets share the same column schema:

| Column | Description |
|------|-------------|
| `sent0` | Anchor sentence in the target language |
| `sent1` | Positive sentence in English |
| `hard_neg` | Hard negative sentence in English |

The dataset is designed for **contrastive training of multilingual sentence embeddings**.

Anchor sentences are written in the **target language**, while both positive and hard negative sentences are in **English**.

## Available Subsets

| Language | ISO 639-3 Code | File |
|---------|---------------|------|
| Afrikaans | `afr` | `xllora-afrikaans.csv` |
| Hindi | `hin` | `xllora-hindi.csv` |
| Telugu | `tel` | `xllora-telugu.csv` |
| Marathi | `mar` | `xllora-marathi.csv` |
| Indonesian | `ind` | `xllora-indonesian.csv` |
| Hausa | `hau` | `xllora-hausa.csv` |
| Korean | `kor` | `xllora-korean.csv` |


## Usage

Load a specific language subset:

```python
from datasets import load_dataset

dataset = load_dataset("mbasoz/xllora-datasets", "afr")

print(dataset["train"][0])
```


## Related Resources

- **Paper:** [Bootstrapping Embeddings for Low Resource Languages](https://arxiv.org/abs/2603.01732)
- **Code:** https://github.com/mbasoz/xllora-embedding  

## Citation

If you use this dataset, please cite:

```
@article{basoz2026bootstrappingembeddings,
  title={Bootstrapping Embeddings for Low Resource Languages},
  author={Merve Basoz and Andrew Horne and Mattia Opper},
  year={2026},
  eprint={2603.01732},
  archivePrefix={arXiv},
  primaryClass={cs.CL},
  url={https://arxiv.org/abs/2603.01732},
  note={Accepted to the LoResLM Workshop at EACL 2026}
}
```