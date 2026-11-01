---
language:
- en
- fr
- de
- es
- it
- pt
- nl
- sv
- da
- fi
- pl
- ru
- tr
- ar
- hi
- bn
- ur
- zh
- ja
- ko
- vi

tags:
- translation
- machine-translation
- benchmark
- flores
- nlp
- translation-api

task_categories:
- translation

task_ids:
- text2text-generation

pretty_name: TranslatePlus FLORES Benchmark (2026)

configs:
  - config_name: per_sentence
    default: true
    data_files:
      - split: train
        path: "results_*.csv"
  - config_name: summary
    data_files:
      - split: train
        path: "summary.csv"

license: mit
dataset_size: 19940
---
# TranslatePlus Translation Benchmark (FLORES 2026)

This dataset contains benchmark results for **TranslatePlus Translation API** across 20 global languages using the FLORES dataset.

👉 Try the API: https://translateplus.io

---

## Methodology

* Dataset: FLORES (Facebook)
* Samples per language: 997
* Source language: English
* Target languages: Top 20 global languages
* Evaluation metrics:

  * **BLEU** (sacreBLEU)
  * **COMET** (Unbabel/wmt22-comet-da)
* Evaluation type: Reference-based (human translations)

---

## Key Results

* COMET scores up to **0.92 (near human-level quality)**
* Strong performance across European, Asian, and global languages
* Stable latency: **~0.40–0.48 seconds**
* High semantic accuracy across all tested languages

---

## Highlights

* **European languages (French, German, Swedish, Danish)** show near-human quality
* **Asian languages (Japanese, Chinese, Korean)** achieve high semantic accuracy (COMET > 0.90)
* **South Asian languages (Hindi, Urdu, Bengali)** maintain strong meaning preservation

---

## Benchmark Visualizations

### BLEU Scores (Lexical Accuracy)

![BLEU Scores](bleu_scores.png)

### COMET Scores (Semantic Quality)

![COMET Scores](comet_scores.png)

### Latency (API Performance)

![Latency](latency.png)

---

## Dataset Structure

This repo exposes **two Hub configurations** (see YAML in the dataset card):

* **`per_sentence` (default)** — `results_*.csv`: `source`, `reference`, `hypothesis`, `latency` per line
* **`summary`** — `summary.csv`: aggregate `pair`, `BLEU`, `COMET`, `Latency` per language pair

* `bleu_scores.png` → BLEU comparison chart
* `comet_scores.png` → COMET comparison chart
* `latency.png` → Latency comparison chart

Load in Python:

```python
from datasets import load_dataset

rows = load_dataset("meetsohail/translateplus-flores-benchmark", "per_sentence", split="train")
agg = load_dataset("meetsohail/translateplus-flores-benchmark", "summary", split="train")
```

---

## ⚠️ Important Notes

* BLEU scores may appear lower for languages like **Chinese, Japanese, and Korean** due to tokenization differences.
* COMET provides a more accurate measure of translation quality in such cases.
* Results are based on **standard FLORES benchmark evaluation**.

---

## Use Cases

This dataset can be used to:

* Compare translation APIs
* Evaluate multilingual AI systems
* Benchmark translation quality
* Analyze cross-language performance
* Build translation evaluation pipelines

---

## About TranslatePlus

TranslatePlus is a high-performance translation API designed for:

* Global applications
* Fast response times
* Cost-efficient scaling
* Easy API integration

👉 Learn more: https://translateplus.io

---

## License

This dataset is provided for research and benchmarking purposes.

---

## Contributing

Feel free to open issues or contribute improvements.

---

Generated using TranslatePlus Benchmarking System (2026)