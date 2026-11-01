---
task_categories:
- text-generation
language:
- ko
license: unknown
size_categories:
- 1K<=n<10K
dataset_info:
  features:
    - name: text
      dtype: string
    - name: category
      dtype: string
    - name: data-source
      dtype: string
    - name: script
      dtype: string
    - name: age-estimate
      dtype: string
    - name: license
      dtype: string
    - name: misc
      dtype: string
    - name: num_tokens
      dtype: int64
---

# babylm-ko

## Dataset Description

This dataset is part of the BabyLM multilingual collection.

### Dataset Summary

- **Language:** ko
- **Script:** Korean (Hangul + Han)
- **Category:** subtitles
- **Source:** Unknown
- **Age Estimate:** n/a
- **Number of Documents:** 7909
- **Total Tokens:** 34475400

### Tokens Per Category

- **subtitles:** 34475400 tokens

### Data Fields

- `text`: The document text
- `category`: Type of content (e.g., child-directed-speech, educational, etc.)
- `data-source`: Original source of the data
- `script`: Writing system used
- `age-estimate`: Target age or age range
- `license`: Data license
- `misc`: Additional metadata (JSON string)
- `num_tokens`: Number of tokens in the subtitle file

### Licensing Information

This dataset is licensed under: See individual files

### Citation

Please cite the original data source: Unknown
