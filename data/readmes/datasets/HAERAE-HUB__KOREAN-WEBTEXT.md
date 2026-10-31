---
language:
- ko
dataset_info:
  features:
  - name: text
    dtype: string
  - name: source
    dtype: string
  - name: token_count
    dtype: int64
  - name: __index_level_0__
    dtype: int64
  splits:
  - name: train
    num_bytes: 8555372905
    num_examples: 1284879
  download_size: 4472792071
  dataset_size: 8555372905
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

# KOREAN-WEBTEXT

**KOREAN-WEBTEXT** is a high-quality Korean language corpus consisting of 2.2 billion tokens. The data has been collected from the following sources:

- **cc100**
- **oscar-corpus/OSCAR-2201**
- **oscar-corpus/OSCAR-2109**
- **oscar-corpus/OSCAR-2301**
- **ontocord/CulturaY**
- **Additional credible internet sources collected by out team**

(We are working to add more sources)

The dataset undergoes rigorous filtering at both the sentence and document levels to ensure quality of text data. Additionally, simple deduplication processes are applied to further refine the dataset.

## Dataset Structure

### Sentence-Level Filters

The following filters are applied at the sentence level:

1. **Repetition Check**: The ratio of repetition for any word in a line should not exceed 0.2.
2. **Punctuation Check**: Lines must end with one of these punctuation marks: `.`, `?`, `]`, or `"`.
3. **Token Count Check**: The line must contain more than 16 tokens.
4. **Character Count Check**: The line must contain more than 32 characters.

### Document-Level Filters

The following filters are applied at the document level:

1. **Token Count Check**: Documents must contain more than 512 tokens.
2. **Stopwords Removal**: Documents containing any of the following stopwords are removed:
   ```python
   stopwords = [
       'www', 'http', '...', 'ㅋㅋㅋ', '약관', 'is', '카지노', '토토', '\u3000',
       '■', '▲', '010', '.kr', '@', '마사지', '스웨디시', '대선'
   ]
   ```

### Deduplication Processes

To ensure data uniqueness, the following deduplication steps are applied:

1. **Exact Deduplication**: Removal of exact duplicate lines.
2. **First 15 Tokens Deduplication**: Removal of lines with identical first 15 tokens.
3. **Last 15 Tokens Deduplication**: Removal of lines with identical last 15 tokens.

## Usage

While the dataset may be small for pretraining models due to its size, we expect it to be better suited for ablation studies.

### Examples

#### Loading the Dataset

To load and use the dataset, you can use the following example code:

```python
import datasets

dataset = datasets.load_dataset('HAERAE-HUB/KOREAN-WEBTEXT-1B')
```

## Citation

If you use this dataset in your research, please cite it as follows:

```
@dataset{KOREAN-WEBTEXT,
  title={KOREAN-WEBTEXT: A High-Quality Korean Language Corpus},
  author={HAERAE-Team},
  year={2024},
  howpublished={\url{https://huggingface.co/datasets/HAERAE-HUB/KOREAN-WEBTEXT}},
}
```

## Contact

For more information or questions about the dataset, please contact the maintainers at [spthsrbwls123@yonsei.ac.kr].

---
