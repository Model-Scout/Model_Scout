---
license: apache-2.0
task_categories:
- text-classification
language:
- ko
tags:
- medical
- NER
- Korean
- Bio-medical
pretty_name: KBMC
size_categories:
- 1K<n<10K
---


## Dataset Summary

This dataset is the first open-source medical Named Entity Recognition (NER) dataset in Korean language.

## Dataset Structure

### Data Instances

Each row in the `KBMC.tsv` file contains a sentence with its corresponding named entities (Disease, Body, and Treatement).

### Data Fields

- `sentence`: The sentence text.
- `tags`: The named entities in the sentence.

## Licensing Information

The dataset is provided under the Apache 2.0 License.

## Citation

Please cite the dataset as follows:

```bibtex
@misc{byun2024korean,
      title={Korean Bio-Medical Corpus (KBMC) for Medical Named Entity Recognition}, 
      author={Sungjoo Byun and Jiseung Hong and Sumin Park and Dongjun Jang and Jean Seo and Minseok Kim and Chaeyoung Oh and Hyopil Shin},
      year={2024},
      eprint={2403.16158},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
