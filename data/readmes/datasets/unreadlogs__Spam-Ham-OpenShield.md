---
license: cc-by-nc-4.0
language:
- ar
- bn
- zh
- en
- fr
- de
- hi
- id
- ja
- jv
- ko
- mr
- no
- pt
- pa
- ru
- es
- sv
- tr
- uk
- ur
multilinguality:
- multilingual
tags:
- text-classification
- spam-detection
- multilingual
- cybersecurity
- phish-detection
pretty_name: OpenShield Multilingual Dataset
size_categories:
- 100K<n<1M
task_categories:
- text-classification
extra_gated_prompt: "By accessing this dataset, you agree to use it strictly for academic, research, benchmarking, or security evaluation purposes under CC-BY-NC 4.0 terms."
extra_gated_auto_prompt: true
---

# 🛡️ OpenShield Multilingual Dataset

> **Summary:** A massive multilingual spam/ham classification dataset containing **~190,000 samples** spanning **21 languages** formatted in JSON Lines (`.jsonl`).

### ⚡ Access Status: Auto-Approved Gated Access
> **Instant Access:** This repository uses Hugging Face gated access to track research usage. **Access requests are set to AUTO-APPROVED**. Simply log in, agree to the conditions, and access is granted immediately.

---

## 📌 Dataset Overview

**OpenShield** is a multilingual text classification benchmark designed to evaluate and train spam detection filters, guardrails, and language models across diverse global languages.

* **Total Samples:** ~190,000
* **Format:** JSON Lines (`.jsonl`)
* **Languages (21):** Arabic (`ar`), Bengali (`bn`), Chinese (`zh`), English (`en`), French (`fr`), German (`de`), Hindi (`hi`), Indonesian (`id`), Japanese (`ja`), Javanese (`jv`), Korean (`ko`), Marathi (`mr`), Norwegian (`no`), Portuguese (`pt`), Punjabi (`pa`), Russian (`ru`), Spanish (`es`), Swedish (`sv`), Turkish (`tr`), Ukrainian (`uk`), Urdu (`ur`)
* **Task:** Binary Text Classification (`ham` vs. `spam`)

---

## 📂 Repository Structure

The files are split per language into dedicated `.jsonl` files inside the repository:

```text
├── dataset/
│   ├── arabic.jsonl
│   ├── bengali.jsonl
│   ├── chinese.jsonl
│   ├── english.jsonl
│   ├── french.jsonl
│   ├── german.jsonl
│   ├── hindi.jsonl
│   ├── indonesian.jsonl
│   ├── japanese.jsonl
│   ├── javanese.jsonl
│   ├── korean.jsonl
│   ├── marathi.jsonl
│   ├── norwegian.jsonl
│   ├── portuguese.jsonl
│   ├── punjabi.jsonl
│   ├── russian.jsonl
│   ├── spanish.jsonl
│   ├── swedish.jsonl
│   ├── turkish.jsonl
│   ├── ukrainian.jsonl
│   └── urdu.jsonl

```

---

## 🔍 Data Format & Fields

Each entry is a JSON object with the following fields:

| Field | Type | Description |
| --- | --- | --- |
| `id` | `string` | Unique record identifier |
| `text` | `string` | Content of the message or communication | 
| `lang` | `string` | ISO 639-1 language code | 
| `label` | `int` | Classification label (`0`: Ham, `1`: Spam) |

### Sample Record

```json
{"id": "abc-0001", "text": " -- ", "lang": "zh", "label": 0}

```

---

## 🚀 Loading the Dataset

### Option 1: Load a Specific Language

```python
from datasets import load_dataset

# Load English subset
dataset_en = load_dataset(
    "json",
    data_files="https://huggingface.co/datasets/unreadlogs/OpenShield-Dataset/resolve/main/dataset/english.jsonl",
    token=True
)

print(dataset_en["train"][0])

```

### Option 2: Load All Languages Combined

```python
from datasets import load_dataset

# Load all language files into a single unified dataset
dataset_all = load_dataset(
    "json",
    data_files="https://huggingface.co/datasets/unreadlogs/OpenShield-Dataset/resolve/main/dataset/*.jsonl",
    token=True
)

print(f"Total samples loaded: {len(dataset_all['train'])}")

```

---

## ⚖️ License & Attribution

This dataset is distributed under the **[Creative Commons Attribution-NonCommercial 4.0 International (CC-BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/)** license.

* **Non-Commercial:** May not be used for direct commercial exploitation without prior authorization.
* **Intended Use:** Academic research, security benchmarking, evaluation of anti-spam and content filtering models.
* **Takedown & Removal:** If you believe any subset includes copyrighted material or personal data you wish removed, please open a thread in the Community Discussions tab.

