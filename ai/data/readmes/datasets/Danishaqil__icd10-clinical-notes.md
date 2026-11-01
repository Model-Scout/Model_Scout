---
license: cc-by-4.0
language:
- en
- sv
- de
- fr
- es
- it
- pt
- nl
- pl
- ro
- hu
- cs
- el
- bg
- da
- fi
- sk
- hr
- lt
- sl
- lv
- et
- mt
- ga
- zh
- ar
- hi
- ja
- ko
- ru
- tr
- vi
- id
- th
tags:
- medical
- icd-10
- clinical-nlp
- diagnosis-coding
- healthcare
- multilingual
task_categories:
- text-classification
pretty_name: ICD-10 Multilingual Clinical Notes
size_categories:
- 1K<n<10K
---

# ICD-10 Multilingual Clinical Notes Dataset

A comprehensive multilingual dataset of ICD-10 diagnosis codes with clinical journal notes in 34 languages.

**Author:** Birger Moëll, Department of Linguistics and Philology, Uppsala University

## Dataset Description

This dataset provides ICD-10 codes with:
- **Official diagnosis names** in 34 languages (24 EU + 10 major world languages)
- **Sample clinical journal notes** (English and Swedish)
- **Train/test splits** for classifier training

### Languages

| EU Official (24) | Major World (10) |
|------------------|------------------|
| English, Swedish, German, French, Spanish, Italian, Portuguese, Dutch, Polish, Romanian, Hungarian, Czech, Greek, Bulgarian, Danish, Finnish, Slovak, Croatian, Lithuanian, Slovenian, Latvian, Estonian, Maltese, Irish | Chinese, Arabic, Hindi, Japanese, Korean, Russian, Turkish, Vietnamese, Indonesian, Thai |

## Model Performance

| Method | Accuracy |
|--------|----------|
| Sentence Embeddings (multilingual-MiniLM) | See metrics.json |
| TF-IDF + Logistic Regression | See metrics.json |

## Dataset Structure

```python
{
    "id": "I10_en",
    "code": "I10",
    "language": "en",
    "name": "Essential hypertension",
    "journal_note": "BP 158/96 x3 readings. No end-organ damage...",
    "label": 25
}
```

### ICD-10 Categories Included

- **Infectious diseases** (A00-B99): Cholera, Gastroenteritis, TB, Sepsis, HIV
- **Neoplasms** (C00-D49): Colon, Lung, Breast, Prostate cancer
- **Blood diseases** (D50-D89): Iron deficiency anemia
- **Endocrine** (E00-E89): Hypothyroidism, Diabetes T1/T2, Obesity, Hyperlipidemia
- **Mental disorders** (F00-F99): Alcohol disorders, Depression, Anxiety
- **Nervous system** (G00-G99): Parkinson, Alzheimer, MS, Epilepsy, Migraine
- **Circulatory** (I00-I99): Hypertension, Angina, MI, CAD, AF, Heart failure, Stroke
- **Respiratory** (J00-J99): URI, Pneumonia, COPD, Asthma
- **Digestive** (K00-K93): GERD, Gastritis, Gallstones
- **Musculoskeletal** (M00-M99): Knee OA, Back pain, Osteoporosis
- **Genitourinary** (N00-N99): CKD, UTI
- **Pregnancy** (O00-O99): Gestational diabetes
- **Symptoms** (R00-R99): Cough, Abdominal pain, Headache, Fatigue
- **Injury** (S00-T98): Head injury, Forearm/Femur fractures
- **Health factors** (Z00-Z99): General exam, Immunization

## Usage

### Loading

```python
from datasets import load_dataset

dataset = load_dataset("birgermoell/icd10-clinical-notes")

# Filter by language
english = dataset.filter(lambda x: x["language"] == "en")
swedish = dataset.filter(lambda x: x["language"] == "sv")
german = dataset.filter(lambda x: x["language"] == "de")
```

### Classification with Embeddings

```python
from sentence_transformers import SentenceTransformer
import pickle

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
text = "Patient with chest pain and elevated troponin"
embedding = model.encode([text])

with open("model/embedding_classifier.pkl", "rb") as f:
    clf = pickle.load(f)

prediction = clf.predict(embedding)
print(f"Predicted ICD-10: {prediction[0]}")
```

## Adding Languages

The dataset is designed for easy extension. Edit `icd10_full_dataset.py`:

```python
ICD10_CODES = {
    "I10": {
        "en": "Essential hypertension",
        "sv": "Essentiell hypertoni",
        "new_lang": "Translation here",  # Add new language
    },
    ...
}
```

## Files

```
data/train.jsonl          # Training data (80%)
data/test.jsonl           # Test data (20%)
data/metadata.json        # Dataset statistics
model/embedding_classifier.pkl   # Trained embedding classifier
model/tfidf_classifier.pkl       # TF-IDF classifier
model/metrics.json        # Accuracy metrics
```

## Citation

```bibtex
@dataset{moell2025icd10multilingual,
  author = {Moëll, Birger},
  title = {ICD-10 Multilingual Clinical Notes Dataset},
  year = {2025},
  publisher = {Hugging Face},
  institution = {Department of Linguistics and Philology, Uppsala University},
  url = {https://huggingface.co/datasets/birgermoell/icd10-clinical-notes}
}
```

## License

CC-BY-4.0

## Disclaimer

This dataset is for research and educational purposes. Journal notes are synthetic examples and should not be used for clinical decision-making. Always consult official ICD-10 documentation for clinical coding.

## Contact

Birger Moëll
Department of Linguistics and Philology
Uppsala University
https://www.uu.se/en/department/linguistics-and-philology
