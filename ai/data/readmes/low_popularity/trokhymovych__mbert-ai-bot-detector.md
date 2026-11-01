---
library_name: transformers
tags:
- text-classification
- bot-detection
- social-media
- multilingual
base_model: bert-base-multilingual-cased
license: apache-2.0
language:
- ar
- bg
- ca
- zh
- en
- fr
- de
- el
- it
- ja
- ko
- fa
- pl
- pt
- ru
- es
- uk
pipeline_tag: text-classification
---

# mbert-ai-bot-detector

A multilingual BERT model fine-tuned for **AI-powered social bots detection**. 
Given a text from social media communication, the model outputs a probability score indicating whether the text was written by a bot (LABEL_1) or a human (LABEL_0). 
User-level decisions are made by aggregating scores across multiple texts (≥20 recommended).

## Model Details

### Model Description

- **Model type:** Sequence classification (binary)
- **Base model:** `bert-base-multilingual-cased`
- **Language(s):** Multilingual (104 languages), fine-tuned primarily on Arabic, Bulgarian, Catalan, Chinese, English, French, German, Greek, Italian, Japanese, Korean, Persian, Polish, Portuguese, Russian, Spanish, Ukrainian
- **Labels:** `LABEL_0` = human, `LABEL_1` = bot/generated
- **License:** Apache-2.0

## Uses

### User-Level Inference (recommended)

Aggregate text scores per user for account-level bot detection:

```python
import numpy as np
from transformers import pipeline

BATCH_SIZE = 128
MAX_LENGTH = 512

clf = pipeline("text-classification", model="trokhymovych/mbert-ai-bot-detector", batch_size=BATCH_SIZE, device=0)

def user_bot_score(clf, texts: list[str], threshold: float = 0.4) -> dict:
    """Returns probability of class 1 (bot/generated) for each text."""
    # Sort by length so batches are roughly the same size to reduce padding overhead
    order = np.argsort([len(t) for t in texts])[::-1]
    sorted_texts = [texts[i] for i in order]

    raw = []
    tokenizer_kwargs = {"truncation": True, "max_length": MAX_LENGTH}
    for i in range(0, len(sorted_texts), BATCH_SIZE * 10):
        batch = sorted_texts[i : i + BATCH_SIZE * 10]
        raw += clf(batch, **tokenizer_kwargs)

    # Restore original order and extract P(class=1)
    scores = np.empty(len(texts))
    for rank, orig_idx in enumerate(order):
        r = raw[rank]
        scores[orig_idx] = r["score"] if r["label"] == "LABEL_1" else 1 - r["score"]

    mean_score = np.mean(scores)
    
    return {"text_scores": scores, "user_scores": mean_score, "is_bot": mean_score >= threshold}
```

### Direct Use (not recommended)

Score individual text for bot-like language patterns:

```python
from transformers import pipeline

clf = pipeline("text-classification", model="trokhymovych/mbert-ai-bot-detector")
result = clf("This is a text to classify.")
# {'label': 'LABEL_1', 'score': 0.87}
```

**Note: Single-text predictions are less reliable and should be used with caution.**

## Bias, Risks, and Limitations

- User-level scores depend on having multiple texts; single-text predictions are less reliable
- Performance may degrade on languages underrepresented in mBERT pretraining data
- Bot detection is an adversarial problem; sophisticated bots may evade detection
- The model reflects patterns in training data; populations or writing styles not represented there may be misclassified

### Out-of-Scope Use

- Long-form documents (model is optimized for short social media posts)
- Authoritative legal or moderation decisions without human review
- Languages significantly underrepresented in mBERT's pretraining

### Recommendations

Use user-level aggregation (mean over ≥20 texts) rather than single-text decisions. 
Calibrate the decision threshold on your target domain using Precision/Recall tradeoffs before deployment.
Based on the Fox-8-23 dataset, we recommend a decision threshold of 0.4. 

<div style="display: flex; gap: 10px;">
  <img src="imgs/fox8_all.png" width="48%"/>
  <img src="imgs/fox8_20.png" width="48%"/>
</div>



## Evaluation
### Metrics
Model is evaluated at the **user level** on [Fox-8-23 dataset](https://zenodo.org/records/8035290).  

The evaluation dataset was not used during training, the same as any posts from the dataset platform (Twitter). 
Training data was artificially created using adversarial generation. 
Text scores are averaged per user.

### Results

| Model | Fox-8-23 AUC |
|---|---|
| GEC score | 0.811±0.009 |
| Binocular | 0.688±0.011 |
| FastDetect | 0.672±0.012 |
| OSM-Det | 0.861±0.008 |
| mbert-ai-bot-detector | **0.989±0.002** |

## Citation

```
@misc{trokhymovych2026adversarial,
      title={Adversarial Creation and Detection of AI-Generated Social Bot Content}, 
      author={Mykola Trokhymovych and Ricardo Baeza-Yates and Alessandro Flammini and Diego Saez-Trumper and Filippo Menczer},
      year={2026},
      eprint={2606.07219},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2606.07219}, 
}
```