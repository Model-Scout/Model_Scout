---
language:
- multilingual
- af
- am
- ar
- as
- az
- be
- bg
- bn
- br
- bs
- ca
- cs
- cy
- da
- de
- el
- en
- eo
- es
- et
- eu
- fa
- fi
- fr
- fy
- ga
- gd
- gl
- gu
- ha
- he
- hi
- hr
- hu
- hy
- id
- is
- it
- ja
- jv
- ka
- kk
- km
- kn
- ko
- ku
- ky
- la
- lo
- lt
- lv
- mg
- mk
- ml
- mn
- mr
- ms
- my
- ne
- nl
- 'no'
- om
- or
- pa
- pl
- ps
- pt
- ro
- ru
- sa
- sd
- si
- sk
- sl
- so
- sq
- sr
- su
- sv
- sw
- ta
- te
- th
- tl
- tr
- ug
- uk
- ur
- uz
- vi
- xh
- yi
- zh
base_model: intfloat/multilingual-e5-small
library_name: sentence-transformers
tags:
  - sentence-transformers
  - feature-extraction
  - sentence-similarity
  - mteb
  - lora
  - peft
---

# turkish_focused-multilingual-e5-small (V4 LoRA)

This is a domain adapted embedding model based on `intfloat/multilingual-e5-small`. It has been fine-tuned using **Low-Rank Adaptation (LoRA)** to significantly boost Turkish-language retrieval and cross-lingual alignment while strictly preserving the base model's English scientific and factoid retrieval capabilities.

## 🚀 Architecture & Training
To avoid catastrophic forgetting of pre-trained weights, this model utilizes Low-Rank Adaptation (LoRA) via PEFT. Only the attention matrices (`query`, `key`, `value`, `dense`) were adapted, keeping base representations stable.
* **Base Model:** `intfloat/multilingual-e5-small`
* **LoRA Config:** $r=16$, $\alpha=32$, dropout $= 0.05$
* **Epochs:** 1.5
* **Batch Size:** 160
* **Learning Rate:** 3e-5 (warmup: 281 steps)
* **Hardware:** Local NVIDIA GeForce RTX 4060 (8GB VRAM)

## 📚 Training Dataset Composition (300,000 Pairs)
The model was trained on a balanced ~300k-pair corpus designed to blend general QA, instruction-following, and specialized Turkish retrieval:

* **English Retention Corpus (100,000 pairs):**
  * `rajpurkar/squad`
  * `yahma/alpaca-cleaned`
  * `databricks/databricks-dolly-15k`
* **Turkish General Corpus (150,000 pairs):**
  * `boun-tabi/squad_tr`
  * `merve/turkish_instructions`
  * `atasoglu/databricks-dolly-15k-tr`
* **Targeted Turkish Corpus (50,000 pairs):**
  * **30,000 pairs:** `trmteb/turkish_embedding_model_training_data`
  * **10,000 pairs:** `AhiskaAI/Ahiska-Turkish-Language-Dataset` (passages paired with synthetic queries generated via `gpt-5.6-luna` and local LLM inference)
  * **10,000 pairs:** `NumanKaanKaratas/turkish-sentences` (passages paired with synthetic queries generated via `gpt-5.6-luna` and local LLM inference)

## 📊 MTEB Benchmark Evaluation
Evaluated across 11 tasks comparing the merged LoRA model against the original `intfloat/multilingual-e5-small` base:

| Task | `base_e5` | `my_custom_e5_lora` | Delta |
| :--- | :--- | :--- | :--- |
| **BelebeleRetrieval** | 0.7632 | 0.8262 | **+0.0630** |
| **STS17** | 0.6133 | 0.6563 | **+0.0430** |
| **STS22.v2** | 0.6428 | 0.6734 | **+0.0306** |
| **MKQARetrieval** | 0.0938 | 0.1039 | **+0.0101** |
| **TurkishMovieSentiment** | 0.6827 | 0.6810 | -0.0017 |
| **TurHistQuadRetrieval** | 0.4329 | 0.4310 | -0.0019 |
| **STSBenchmark** | 0.8359 | 0.8329 | -0.0030 |
| **XQuADRetrieval** | 0.9755 | 0.9668 | -0.0087 |
| **NFCorpus** | 0.3050 | 0.2908 | -0.0142 |
| **TurkishProductSentiment** | 0.5873 | 0.5679 | -0.0194 |
| **SciFact** | 0.6694 | 0.6480 | -0.0214 |

## 💻 Usage
The PEFT adapter matrices have been fused directly into the base weights (`merge_and_unload()`), allowing direct usage via `sentence-transformers` without needing `peft`:

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("Yigit-Karaman/turkish_focused-multilingual-e5-small")

# E5 models require query/passage prefixes
query = "query: Bilgi erişimi modellerinde LoRA nasıl çalışır?"
doc = "passage: Düşük dereceli uyarlama (LoRA), temel ağırlıkları dondurup dikkat katmanlarına eğitilebilir matrisler ekleyerek çalışır."

embeddings = model.encode([query, doc], normalize_embeddings=True)
similarity = embeddings[0] @ embeddings[1]

print(f"Cosine Similarity: {similarity:.4f}")