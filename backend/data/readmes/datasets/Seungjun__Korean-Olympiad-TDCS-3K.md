---
license: cc-by-nc-4.0
language:
- ko
- en
task_categories:
- text-generation
pretty_name: Korean Olympiad TDCS 3K
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
dataset_info:
  features:
  - name: problem_ko
    dtype: large_string
  - name: solution_ko
    dtype: large_string
  - name: difficulty_level
    dtype: int64
  splits:
  - name: train
    num_bytes: 7983601
    num_examples: 3000
  - name: validation
    num_bytes: 819162
    num_examples: 300
  download_size: 3784957
  dataset_size: 8802763
---

# Korean Olympiad TDCS 3K

A balanced Korean Olympiad mathematics reasoning dataset derived from
[ChuGyouk/AI-MO-NuminaMath-CoT-Ko](https://huggingface.co/datasets/ChuGyouk/AI-MO-NuminaMath-CoT-Ko).

## Splits

- `train`: 3,000 rows (30 from every cluster × difficulty cell)
- `validation`: 300 rows (3 from every cluster × difficulty cell)

## Construction

- Filtered source: `olympiads`
- Problem embeddings: `Qwen/Qwen3-Embedding-4B`, 1,024 dimensions
- Problem-type clusters: 20 spherical k-means clusters
- Difficulty proxy: per-cluster quintiles of mean normalized next-token entropy from
  `LGAI-EXAONE/EXAONE-4.0-1.2B` over up to 512 generated reasoning tokens
- Benchmark decontamination: rows with at least 95% fuzzy similarity to
  [OlympiadBench-Math-Ko](https://huggingface.co/datasets/ChuGyouk/OlympiadBench-Math-Ko) were excluded before sampling
- Random seed: 42

## Important limitations

- Difficulty is model-relative uncertainty, not a human difficulty annotation.
- Most uncertainty generations reached the 512-token limit, so entropy measures the first 512 reasoning tokens rather than final-answer confidence.
- The upstream solutions are machine-generated translations/reasoning traces and may contain mathematical errors.
- Fuzzy matching reduces benchmark leakage but cannot guarantee complete decontamination.

## License

This derivative follows the upstream CC BY-NC 4.0 license.
