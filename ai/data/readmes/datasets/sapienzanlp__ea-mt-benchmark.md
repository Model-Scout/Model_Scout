---
license: cc-by-sa-4.0
task_categories:
  - text-generation
language:
  - en
  - ar
  - de
  - es
  - fr
  - it
  - ja
  - ko
  - th
  - tr
  - zh
size_categories:
  - 10K<n<100K
configs:
- config_name: en-it
  data_files:
    - split: sample
      path: data/sample/it_IT.jsonl
    - split: validation
      path: data/validation/it_IT.jsonl
    - split: test
      path: data/test/it_IT.jsonl
- config_name: en-ar
  data_files:
    - split: sample
      path: data/sample/ar_AE.jsonl
    - split: validation
      path: data/validation/ar_AE.jsonl
    - split: test
      path: data/test/ar_AE.jsonl
- config_name: en-de
  data_files:
    - split: sample
      path: data/sample/de_DE.jsonl
    - split: validation
      path: data/validation/de_DE.jsonl
    - split: test
      path: data/test/de_DE.jsonl
- config_name: en-es
  data_files:
    - split: sample
      path: data/sample/es_ES.jsonl
    - split: validation
      path: data/validation/es_ES.jsonl
    - split: test
      path: data/test/es_ES.jsonl
- config_name: en-fr
  data_files:
    - split: sample
      path: data/sample/fr_FR.jsonl
    - split: validation
      path: data/validation/fr_FR.jsonl
    - split: test
      path: data/test/fr_FR.jsonl
- config_name: en-ja
  data_files:
    - split: sample
      path: data/sample/ja_JP.jsonl
    - split: validation
      path: data/validation/ja_JP.jsonl
    - split: test
      path: data/test/ja_JP.jsonl
- config_name: en-ko
  data_files:
    - split: sample
      path: data/sample/ko_KR.jsonl
    - split: validation
      path: data/validation/ko_KR.jsonl
    - split: test
      path: data/test/ko_KR.jsonl
- config_name: en-th
  data_files:
    - split: sample
      path: data/sample/th_TH.jsonl
    - split: validation
      path: data/validation/th_TH.jsonl
    - split: test
      path: data/test/th_TH.jsonl
- config_name: en-tr
  data_files:
    - split: sample
      path: data/sample/tr_TR.jsonl
    - split: validation
      path: data/validation/tr_TR.jsonl
    - split: test
      path: data/test/tr_TR.jsonl
- config_name: en-zh
  data_files:
    - split: sample
      path: data/sample/zh_TW.jsonl
    - split: validation
      path: data/validation/zh_TW.jsonl
    - split: test
      path: data/test/zh_TW.jsonl
---

# Dataset Card for EA-MT

EA-MT (Entity-Aware Machine Translation) is a multilingual benchmark for evaluating the capabilities of Large Language Models (LLMs) and Machine Translation (MT) models in translating simple sentences with potentially challenging entity mentions, e.g., entities for which a word-for-word translation may not be accurate.

Here is an example of a simple sentence with a challenging entity mention:
* *English*: "What is the plot of **The Catcher in the Rye**?"
* *Italian*:
  * Word-for-word translation (incorrect): "Qual è la trama del **Cacciatore nella segale**?"
  * Correct translation: "Qual è la trama de **Il giovane Holden**?"

> Note: In the example above, the correct translation of "The Catcher in the Rye" is "Il giovane Holden" in Italian, which roughly translates to "The Young Holden."

You can find more information about this task here:
* Paper (coming soon!)
* [Website](https://sapienzanlp.github.io/ea-mt/)
* [Leaderboard](https://huggingface.co/spaces/sapienzanlp/ea-mt-leaderboard)

## Languages

The dataset is available in the following languages pairs:
- `en-ar`: English - Arabic
- `en-zh`: English - Chinese
- `en-fr`: English - French
- `en-de`: English - German
- `en-it`: English - Italian
- `en-ja`: English - Japanese
- `en-ko`: English - Korean
- `en-es`: English - Spanish
- `en-th`: English - Thai
- `en-tr`: English - Turkish
- `en-zh`: English - Chinese (Traditional)

## How To Use

You can use this benchmark in Hugging Face Datasets by specifying the language pair you want to use. For example, to load the English-Italian dataset, you can use the following configuration:

```python
from datasets import load_dataset

# Load the English-Italian dataset ("en-it")
dataset = load_dataset("sapienzanlp/ea-mt-benchmark", "en-it")

# Iterate over the "sample" split and print the source sentence and the first target translation.
for example in dataset["sample"]:
    print(example["source"])
    print(example["targets"][0])
    print()
```

This will load the English-Italian dataset and print the source sentence and the target translation.

### Data format

The dataset is available in the following splits:
* `sample`: A small sample of the dataset for quick testing and debugging.
* `validation`: A validation set for fine-tuning and hyperparameter tuning.
* `test`: A test set for evaluating the model's performance.

Each example in the dataset has the following format:
```json
{
  "id": "Q1422318_1",
  "wikidata_id": "Q1422318",
  "entity_types": [
    "Artwork",
    "Book"
  ],
  "source": "Who is the author of the novel The Dark Tower: The Gunslinger?",
  "targets": [
    {
      "translation": "Chi è l'autore del romanzo L'ultimo cavaliere?",
      "mention": "L'ultimo cavaliere"
    }
  ],
  "source_locale": "en",
  "target_locale": "it"
}
```

Each example contains the following fields:
- `id`: A unique identifier for the example.
- `wikidata_id`: The Wikidata ID of the entity mentioned in the source sentence.
- `entity_types`: The types of the entity mentioned in the source sentence.
- `source`: The source sentence in English.
- `targets`: A list of target translations in the target language. Each target translation contains the following fields:
  - `translation`: The target translation.
  - `mention`: The entity mention in the target translation.
- `source_locale`: The source language code.
- `target_locale`: The target language code.

> Note: This is a multi-reference translation dataset, meaning that each example has multiple valid translations. The translations are provided as a list of target translations in the `targets` field. A model's output is considered correct if it generates any of the valid translations for a given example.

## License

The dataset is released under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

## Citation

If you use this benchmark in your work, please cite the following papers:

```bibtex
@inproceedings{ea-mt-benchmark,
    title       = "{S}em{E}val-2025 Task 2: Entity-Aware Machine Translation",
    author      = "Simone Conia and Min Li and Roberto Navigli and Saloni Potdar",
    booktitle   = "Proceedings of the 19th International Workshop on Semantic Evaluation (SemEval-2025)",
    year        = "2025",
    publisher   = "Association for Computational Linguistics",
}
```

```bibtex
@inproceedings{conia-etal-2024-towards,
    title = "Towards Cross-Cultural Machine Translation with Retrieval-Augmented Generation from Multilingual Knowledge Graphs",
    author = "Conia, Simone  and
      Lee, Daniel  and
      Li, Min  and
      Minhas, Umar Farooq  and
      Potdar, Saloni  and
      Li, Yunyao",
    booktitle = "Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing",
    month = nov,
    year = "2024",
    address = "Miami, Florida, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.emnlp-main.914/",
    doi = "10.18653/v1/2024.emnlp-main.914",
    pages = "16343--16360",
}
```
