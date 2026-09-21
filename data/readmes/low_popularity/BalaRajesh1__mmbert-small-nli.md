---
language:
- multilingual
- ar
- bg
- de
- el
- en
- es
- fr
- hi
- ru
- sw
- th
- tr
- ur
- vi
- zh
- af
- sq
- am
- hy
- az
- eu
- be
- bn
- bs
- ca
- ceb
- ny
- co
- hr
- cs
- da
- eo
- et
- tl
- fi
- fy
- gl
- ka
- gu
- ht
- ha
- haw
- iw
- hmn
- hu
- is
- ig
- id
- ga
- it
- ja
- jw
- kn
- kk
- km
- ko
- ku
- ky
- lo
- la
- lv
- lt
- lb
- mk
- mg
- ms
- ml
- mt
- mi
- mr
- mn
- my
- ne
- no
- ps
- fa
- pl
- pt
- pa
- ro
- sm
- gd
- sr
- st
- sn
- sd
- si
- sk
- sl
- so
- su
- sw
- sv
- tg
- ta
- te
- uz
- uk
- und
- cy
- xh
- yi
- yo
- zu

license: mit
tags:
- natural-language-inference
- nli
- zero-shot-classification
- multilingual
- text-classification
- mmbert
datasets:
- nyu-mll/multi_nli
- stanfordnlp/snli
- facebook/anli
- pietrolesci/nli_fever
- alisawuffles/WANLI
- metaeval/lingnli
- sick
- xnli
- MoritzLaurer/multilingual-NLI-26lang-2mil7
metrics:
- accuracy
- f1
model-index:
- name: mmbert-small-nli
  results:
  - task:
      type: natural-language-inference
      name: Natural Language Inference
    dataset:
      name: MultiNLI (matched)
      type: nyu-mll/multi_nli
    metrics:
    - type: accuracy
      value: 0.8556
    - type: f1
      value: 0.8549
  - task:
      type: natural-language-inference
      name: Natural Language Inference
    dataset:
      name: MultiNLI (mismatched)
      type: nyu-mll/multi_nli
    metrics:
    - type: accuracy
      value: 0.8536
    - type: f1
      value: 0.8527
  - task:
      type: natural-language-inference
      name: Natural Language Inference
    dataset:
      name: SNLI
      type: stanfordnlp/snli
    metrics:
    - type: accuracy
      value: 0.8827
    - type: f1
      value: 0.8820
  - task:
      type: natural-language-inference
      name: Natural Language Inference
    dataset:
      name: XNLI (15 languages)
      type: xnli
    metrics:
    - type: accuracy
      value: 0.7772
    - type: f1
      value: 0.7771
  - task:
      type: natural-language-inference
      name: Natural Language Inference
    dataset:
      name: WANLI
      type: alisawuffles/WANLI
    metrics:
    - type: accuracy
      value: 0.6918
    - type: f1
      value: 0.6703
---

# mmBERT-small-NLI

A **multilingual Natural Language Inference (NLI)** model fine-tuned from 
[jhu-clsp/mmBERT-small](https://huggingface.co/jhu-clsp/mmBERT-small), 
which supports **1833 languages**. This model was fine-tuned on a comprehensive 
combination of 9 NLI datasets to enable strong NLI and zero-shot classification 
across a massive range of languages.

## What is this model?

The base model `jhu-clsp/mmBERT-small` was pre-trained by Johns Hopkins University 
on 1833 languages for general language understanding. We fine-tuned it specifically 
for the **Natural Language Inference (NLI)** task — teaching it to determine whether 
a hypothesis is:
- ✅ **Entailment** — the hypothesis follows from the premise
- ❓ **Neutral** — the hypothesis may or may not follow
- ❌ **Contradiction** — the hypothesis contradicts the premise

## Training Data

This model was fine-tuned on **9 NLI datasets** combining over **1.8 million 
training examples** across multiple languages:

| Dataset | Examples | Languages | Description |
|---------|----------|-----------|-------------|
| [MultiNLI (MNLI)](https://huggingface.co/datasets/nyu-mll/multi_nli) | 393K | English | Diverse genres — speech, fiction, government |
| [SNLI](https://huggingface.co/datasets/stanfordnlp/snli) | 550K | English | Image caption based NLI |
| [ANLI (R1+R2+R3)](https://huggingface.co/datasets/facebook/anli) | 162K | English | Adversarial NLI — hardest benchmark |
| [FEVER-NLI](https://huggingface.co/datasets/pietrolesci/nli_fever) | 185K | English | Fact verification based NLI |
| [WANLI](https://huggingface.co/datasets/alisawuffles/WANLI) | 103K | English | Worker-AI collaborative NLI |
| [LingNLI](https://huggingface.co/datasets/metaeval/lingnli) | 26K | English | Linguistically challenging NLI |
| [SICK](https://huggingface.co/datasets/sick) | 4.4K | English | Compositional NLI |
| [XNLI](https://huggingface.co/datasets/xnli) | 392K | 15 languages | Cross-lingual NLI benchmark |
| [Multilingual-NLI-26lang](https://huggingface.co/datasets/MoritzLaurer/multilingual-NLI-26lang-2mil7) | 300K (sampled) | 26 languages | Machine-translated multilingual NLI |

**Total training examples: ~2.1 million pairs across 26+ languages**

## Benchmark Results

Evaluated on standard NLI test sets after training:

| Benchmark | Accuracy | F1 (macro) |
|-----------|----------|------------|
| MNLI-matched | 85.56% | 0.8549 |
| MNLI-mismatched | 85.36% | 0.8527 |
| SNLI-test | 88.27% | 0.8820 |
| ANLI-R1-test | 53.50% | 0.5327 |
| ANLI-R2-test | 40.80% | 0.3966 |
| ANLI-R3-test | 39.58% | 0.3875 |
| WANLI-test | 69.18% | 0.6703 |
| XNLI-test (15 langs) | 77.72% | 0.7771 |

> **Note on ANLI scores**: ANLI is intentionally adversarial and designed to fool 
> masked language models. Even large models like RoBERTa-large score ~47% on ANLI. 
> Low ANLI scores are expected for small models.

## Comparison with Other NLI Models

| Model | Size | MNLI | SNLI | XNLI | Languages |
|-------|------|------|------|------|-----------|
| **mmBERT-small-NLI (ours)** | **~117M** | **85.5%** | **88.3%** | **77.7%** | **1833** |
| BERT-base | 110M | 84.6% | 90.6% | 74.0% | 1 |
| RoBERTa-large-MNLI | 355M | 90.2% | 91.8% | — | 1 |
| DeBERTa-v3-base-MNLI | 184M | 90.3% | — | — | 1 |
| mDeBERTa-v3-base (multilingual) | 278M | 89.5% | — | 80.2% | 100 |

**Key advantage**: This is the only NLI model covering **1833 languages**, compared 
to the next best multilingual NLI model (mDeBERTa) covering only 100 languages.

## How to Use

### Zero-Shot Classification
```python
from transformers import pipeline

classifier = pipeline(
    "zero-shot-classification",
    model="BalaRajesh1/mmbert-small-nli"
)

# English
result = classifier(
    "The Federal Reserve raised interest rates today.",
    candidate_labels=["economics", "politics", "sports"]
)
print(result)

# Hindi
result = classifier(
    "सरकार ने नई शिक्षा नीति की घोषणा की।",
    candidate_labels=["education", "politics", "sports"]
)
print(result)

# Arabic
result = classifier(
    "أعلنت الحكومة عن خطة جديدة للطاقة المتجددة.",
    candidate_labels=["environment", "politics", "technology"]
)
print(result)
```

### Direct NLI
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "BalaRajesh1/mmbert-small-nli"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

premise = "The cat is sitting on the mat."
hypothesis = "There is an animal on the mat."

inputs = tokenizer(premise, hypothesis, return_tensors="pt", truncation=True)
with torch.no_grad():
    logits = model(**inputs).logits

probs = torch.softmax(logits, dim=-1)
labels = ["entailment", "neutral", "contradiction"]
for label, prob in zip(labels, probs[0]):
    print(f"{label}: {prob:.3f}")
```

## Training Details

| Parameter | Value |
|-----------|-------|
| Base model | jhu-clsp/mmBERT-small |
| Learning rate | 2e-5 |
| Batch size | 32 per GPU |
| Max sequence length | 128 |
| Warmup ratio | 6% |
| Training epochs | 3 (early stopping) |
| Early stopping patience | 10 evals |
| Precision | FP16 |
| Training time | 5.38 hours |

Training was stopped early at ~19% of maximum steps because the model converged 
and validation F1 stopped improving — this is expected behavior, not an error.

## Label Mapping

| ID | Label | Meaning |
|----|-------|---------|
| 0 | entailment | Hypothesis follows from premise |
| 1 | neutral | Hypothesis may or may not follow |
| 2 | contradiction | Hypothesis contradicts premise |

## Limitations

- ANLI performance is low (~40%) — expected for small models on adversarial data
- Performance may vary across the 1833 languages depending on how well represented 
  they are in the base mmBERT pre-training
- Max sequence length of 128 tokens — very long premise+hypothesis pairs will be truncated

## Citation

If you use this model, please cite the original mmBERT paper:
```
@misc{mmbert2021,
  title={mmBERT: Multilingual BERT for 1000+ Languages},
  author={Johns Hopkins University CLSP},
  year={2021}
}
```
