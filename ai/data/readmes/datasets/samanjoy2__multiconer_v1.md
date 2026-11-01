---
pretty_name: "MultiCoNER v1"
license: "cc-by-4.0"
task_categories: ["token-classification"]
language: ["bn", "de", "en", "es", "fa", "hi", "ko", "nl", "ru", "tr", "zh"]
tags: ["named-entity-recognition", "ner", "multilingual", "multiconer", "semeval-2022"]
---

# MultiCoNER v1

MultiCoNER v1 is a multilingual dataset for complex named entity recognition.

This repository is an unofficial convenience mirror created to make the publicly available dataset easier to access through Hugging Face. I did not create or own this dataset. All credit belongs to the original MultiCoNER authors and the organizers of SemEval-2022 Task 11.

## Entity types

The dataset uses BIO annotations for six entity types: Person (`PER`), Location (`LOC`), Group (`GRP`), Corporation (`CORP`), Product (`PROD`), and Creative Work (`CW`).

## Data format

The files are provided in CoNLL format. Each line contains a token and its named entity label, while empty lines separate samples.

## Download

```python
from huggingface_hub import snapshot_download

dataset_path = snapshot_download(
    repo_id="samanjoy2/multiconer_v1",
    repo_type="dataset"
)
```

## License

The original dataset is distributed under the Creative Commons Attribution 4.0 International license.

## Citation

```bibtex
@inproceedings{malmasi-etal-2022-multiconer,
    title = "{M}ulti{C}o{NER}: A Large-scale Multilingual Dataset for Complex Named Entity Recognition",
    author = "Malmasi, Shervin and Fang, Anjie and Fetahu, Besnik and Kar, Sudipta and Rokhlenko, Oleg",
    booktitle = "Proceedings of the 29th International Conference on Computational Linguistics",
    year = "2022",
    pages = "3798--3809",
    url = "https://aclanthology.org/2022.coling-1.334/"
}
```

This repository is only a convenience mirror. Please cite the original dataset authors.
