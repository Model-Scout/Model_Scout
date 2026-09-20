---
language:
  - en
  - ru
  - uk
  - de
  - es
  - am
  - zh
  - ar
  - hi
  - it
  - fr
  - he
  - ja
  - tt
license: openrail++
library_name: transformers
base_model:
  - distilbert/distilbert-base-multilingual-cased
datasets:
- gravitee-io/textdetox-multilingual-toxicity-dataset
pipeline_tag: text-classification
tags:
  - toxicity
  - distilbert
  - gravitee-io
  - ai-gateway
---
# distillbert-multilingual-toxicity-classifier

This is a DistilBERT-based multilingual toxicity classifier fine-tuned using the [gravitee-io/textdetox-multilingual-toxicity-dataset](https://huggingface.co/datasets/gravitee-io/textdetox-multilingual-toxicity-dataset). The model supports a wide range of languages and is trained for toxicity classification ("not-toxic", "toxic").

We perform an 85/15 train-test split per language based on the `textdetox` dataset. All credits go to the authors of the original corpora.

## Performance Overview

### Original model

| Language   | Validation F1 | Training F1 |   ΔF1   |
|------------|---------------|-------------|---------|
| Russian    | 0.9572        | 0.9897      | -0.0324 |
| English    | 0.9528        | 0.9853      | -0.0325 |
| Hindi      | 0.9248        | 0.9599      | -0.0351 |
| Armenian   | 0.6513        | 0.6915      | -0.0402 |
| French     | 0.9446        | 0.9874      | -0.0428 |
| Tatar      | 0.9200        | 0.9682      | -0.0482 |
| Ukrainian  | 0.8997        | 0.9511      | -0.0514 |
| Japanese   | 0.8658        | 0.9253      | -0.0595 |
| German     | 0.8904        | 0.9547      | -0.0643 |
| Spanish    | 0.8564        | 0.9399      | -0.0835 |
| Chinese    | 0.6865        | 0.7807      | -0.0942 |
| Arabic     | 0.7563        | 0.8550      | -0.0987 |
| Italian    | 0.8223        | 0.9271      | -0.1048 |
| Hinglish   | 0.7234        | 0.8533      | -0.1299 |
| Hebrew     | 0.6455        | 0.8441      | -0.1987 |

### Quantized model (ONNX)

| Language  | Val F1 | Quantized Val F1 | Δ Val F1    | Train F1 | Quantized Train F1 | Δ Train F1  |
|-----------|--------|------------------|-------------|----------|--------------------|-------------|
| Russian   | 0.9572 | 0.9609           | **+0.0037** | 0.9897   | 0.9875             | **−0.0022** |
| English   | 0.9528 | 0.9495           | **−0.0033** | 0.9853   | 0.9857             | **+0.0004** |
| German    | 0.8904 | 0.8842           | **−0.0062** | 0.9547   | 0.9369             | **−0.0178** |
| Hindi     | 0.9248 | 0.8940           | **−0.0300** | 0.9599   | 0.9335             | **−0.0264** |
| French    | 0.9446 | 0.9351           | **−0.0095** | 0.9874   | 0.9814             | **−0.0060** |
| Japanese  | 0.8658 | 0.8584           | **−0.0074** | 0.9253   | 0.9081             | **−0.0172** |
| Ukrainian | 0.8997 | 0.8988           | **−0.0009** | 0.9511   | 0.9476             | **−0.0035** |
| Tatar     | 0.9200 | 0.9148           | **−0.0052** | 0.9682   | 0.9631             | **−0.0051** |
| Amharic   | 0.6513 | 0.6377           | **−0.0136** | 0.6915   | 0.6863             | **−0.0052** |
| Spanish   | 0.8564 | 0.8439           | **−0.0125** | 0.9399   | 0.9273             | **−0.0126** |
| Chinese   | 0.6865 | 0.6697           | **−0.0168** | 0.7807   | 0.7596             | **−0.0211** |
| Arabic    | 0.7563 | 0.7535           | **−0.0028** | 0.8550   | 0.8481             | **−0.0069** |
| Italian   | 0.8223 | 0.8033           | **−0.0190** | 0.9271   | 0.9193             | **−0.0078** |
| Hinglish  | 0.7234 | 0.7260           | **+0.0026** | 0.8533   | 0.8436             | **−0.0097** |
| Hebrew    | 0.6455 | 0.6190           | **−0.0265** | 0.8441   | 0.8204             | **−0.0237** |


 The quantized model maintains high accuracy and generalization on the evaluation set, 
 with negligible performance loss for most languages.

## 🤗 Usage

```python
from transformers import AutoTokenizer
from optimum.onnxruntime import ORTModelForSequenceClassification
import numpy as np

# Load model and tokenizer using optimum
model = ORTModelForSequenceClassification.from_pretrained(
 "gravitee-io/distilbert-multilingual-toxicity-classifier",
 file_name="model.quant.onnx"
)
tokenizer = AutoTokenizer.from_pretrained("gravitee-io/distilbert-multilingual-toxicity-classifier")

# Tokenize input
text = "Your text here"
inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)

# Run inference
outputs = model(**inputs)
logits = outputs.logits

# Optional: convert to probabilities
probs = 1 / (1 + np.exp(-logits))
print(probs)
```

## Github Repository

You can check details on how the model was fine-tuned and evaluated on the [Github Repository](https://github.com/gravitee-io-labs/gravitee-distilbert-multilingual-toxicity-classifier)

## License

This model is licensed under [OpenRAIL++](LICENSE)

## Citation

```bibtex
@inproceedings{dementieva2024overview,
  title={Overview of the Multilingual Text Detoxification Task at PAN 2024},
  author={Dementieva, Daryna and Moskovskiy, Daniil and Babakov, Nikolay and Ayele, Abinew Ali and Rizwan, Naquee and Schneider, Frolian and Wang, Xintog and Yimam, Seid Muhie and Ustalov, Dmitry and Stakovskii, Elisei and Smirnova, Alisa and Elnagar, Ashraf and Mukherjee, Animesh and Panchenko, Alexander},
  booktitle={Working Notes of CLEF 2024 - Conference and Labs of the Evaluation Forum},
  editor={Guglielmo Faggioli and Nicola Ferro and Petra Galu{{s}}{{c}}{'a}kov{'a} and Alba Garc{'i}a Seco de Herrera},
  year={2024},
  organization={CEUR-WS.org}
}

@inproceedings{dementieva-etal-2024-toxicity,
  title = "Toxicity Classification in {U}krainian",
  author = "Dementieva, Daryna and Khylenko, Valeriia and Babakov, Nikolay and Groh, Georg",
  booktitle = "Proceedings of the 8th Workshop on Online Abuse and Harms (WOAH 2024)",
  month = jun,
  year = "2024",
  address = "Mexico City, Mexico",
  publisher = "Association for Computational Linguistics",
  url = "https://aclanthology.org/2024.woah-1.19/",
  doi = "10.18653/v1/2024.woah-1.19",
  pages = "244--255"
}

@inproceedings{DBLP:conf/ecir/BevendorffCCDEFFKMMPPRRSSSTUWZ24,
  author = {Janek Bevendorff and et al.},
  title = {Overview of {PAN} 2024: Multi-author Writing Style Analysis, Multilingual Text Detoxification, Oppositional Thinking Analysis, and Generative {AI} Authorship Verification - Extended Abstract},
  booktitle = {ECIR 2024, Glasgow, UK, March 24-28, 2024, Proceedings, Part {VI}},
  series = {Lecture Notes in Computer Science},
  volume = {14613},
  pages = {3--10},
  publisher = {Springer},
  year = {2024},
  doi = {10.1007/978-3-031-56072-9_1}
}
```
