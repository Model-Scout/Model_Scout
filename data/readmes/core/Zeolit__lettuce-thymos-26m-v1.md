---
license: apache-2.0
pipeline_tag: text-classification
tags:
  - emotion
  - multilingual
  - multi-label
  - go-emotions
  - onnx
  - int8
datasets:
  - google-research-datasets/go_emotions
  - brighter-dataset/BRIGHTER-emotion-categories
base_model: FacebookAI/xlm-roberta-large
language:
  - en
  - es
  - fr
  - de
  - pt
  - it
  - nl
  - ru
  - pl
  - uk
  - ar
  - fa
  - hi
  - bn
  - zh
  - ja
  - ko
  - vi
  - th
  - id
  - sw
  - tr
---

# lettuce-thymos-26m-v1

Multi-label emotion classification over the 28 GoEmotions labels in 22 languages.
26.5M parameters, 28 MB as int8 ONNX.

*Thymos* (θυμός) is the Homeric Greek word for the seat of emotion.

## Model description

A transformer encoder distilled from `FacebookAI/xlm-roberta-large`. Label set and
label order match `SamLowe/roberta-base-go_emotions`.

| | |
|---|---|
| Architecture | 8 layers, 384 hidden, 6 heads, FFN 1152, pre-LN |
| Position encoding | RoPE, base 10000 |
| Embedding | Factorized: 114,087 x 128, projected to 384 |
| Pooling | Masked mean |
| Parameters | 26.5M (14.6M embedding, 11.9M encoder) |
| Context | 128 tokens |
| Tokenizer | XLM-RoBERTa SentencePiece, vocabulary trimmed to 114,087 |
| Output | 28 independent sigmoid probabilities |
| File size | 28 MB int8 ONNX, 62 MB fp32 ONNX |

## Intended uses and limitations

Emotion tagging of short conversational text in 22 languages, on device or on CPU.
Multi-label: one input can carry several emotions.

Not for clinical, diagnostic or safety-critical use, and not a measure of a
person's emotional state.

Known weaknesses are listed under [Limitations](#limitations).

## How to use

```python
import json, numpy as np, onnxruntime as ort
from transformers import AutoTokenizer

tok = AutoTokenizer.from_pretrained("Zeolit/lettuce-thymos-26m-v1")
sess = ort.InferenceSession("onnx/model_quantized.onnx",
                            providers=["CPUExecutionProvider"])
meta = json.load(open("labels.json"))

enc = tok(["I'm so grateful you were there for me."], return_tensors="np")
probs = sess.run(None, {"input_ids": enc["input_ids"].astype(np.int64),
                        "attention_mask": enc["attention_mask"].astype(np.int64)})[0][0]

active = [(label, float(p))
          for label, p, t in zip(meta["labels"], probs, meta["thresholds"]) if p >= t]
```

Use the per-class thresholds in `labels.json`. A fixed 0.5 cutoff costs a large
amount of macro-F1 because the rare classes rarely reach it.

Inputs longer than 128 tokens: split into overlapping windows with stride 96, then
aggregate element-wise max for label presence, or length-weighted mean for overall
tone. `inference.py` in this repository implements this; thresholds were fitted on
single windows, so document-level aggregation is not calibrated.

Repository layout:

```
config.json               architecture config
model.safetensors         PyTorch weights
modeling_thymos.py        model definition, load with load_student(".")
inference.py              chunked inference helper
labels.json               28 labels, per-class thresholds, calibration record
tokenizer.json            XLM-RoBERTa SentencePiece, trimmed vocabulary
onnx/model.onnx           fp32 export
onnx/model_quantized.onnx int8 export
evaluation/               per-model evaluation artifacts for every table below
```

## Training data

| | |
|---|---|
| Source | GoEmotions, 58k Reddit comments, 27 emotions plus neutral |
| Splits | 43,410 train / 5,426 validation / 5,427 test |
| Translation | `facebook/m2m100_1.2B` into 21 additional languages |
| Training rows | 955,020 |

en, es, fr, de, pt, it, nl, ru, pl, uk, ar, fa, hi, bn, zh, ja, ko, vi, th, id,
sw, tr.

## Training procedure

**Teacher.** `FacebookAI/xlm-roberta-large` fine-tuned on all 22 languages.
3 epochs, batch 128, lr 1e-5 cosine with 6% warmup, layer-wise lr decay 0.9,
EMA 0.999, max length 96, bf16.

**Student.** Distilled from teacher logits. 20 epochs, batch 512, lr 3e-4, AdamW
weight decay 0.01. Loss: 0.7 per-label binary KD at temperature 2, plus 0.3
supervised. Embedding initialized from a low-rank SVD of the teacher's embedding
matrix. Checkpoint selected on threshold-free validation macro-AP.

**Thresholds.** Per class, grid searched on held-out validation folds.

**Quantization.** The embedding table is quantized to int8 with per-row scales
separately from the matmuls, since ONNX Runtime dynamic quantization does not cover
`Gather`.

## Evaluation

Five GoEmotions models sharing the same 28 labels, measured under one protocol.
Rows ordered by parameter count.

### GoEmotions

Test split of GoEmotions, machine-translated into 21 further languages,
119,394 rows. English thresholds tuned on English validation; multilingual
thresholds tuned on the pooled validation set.

| model | params | languages | English macro-F1 | 22-language macro-F1 | 22-language micro-F1 |
|---|---|---|---|---|---|
| lettuce-thymos-26m-v1 | 26.5M | 22 | 0.527 | 0.446 | 0.523 |
| joeddav/distilbert-base-uncased-go-emotions-student | 67M | 1 | 0.336 | 0.121 | 0.211 |
| SamLowe/roberta-base-go_emotions | 125M | 1 | 0.505 | 0.147 | 0.296 |
| cirimus/modernbert-base-go-emotions | 149M | 1 | 0.535 | 0.182 | 0.333 |
| cirimus/modernbert-large-go-emotions | 395M | 1 | 0.542 | 0.185 | 0.338 |

Teacher macro-F1 on the 22-language evaluation is 0.462.

Per language, this model against `SamLowe/roberta-base-go_emotions`, pooled
thresholds:

| language | baseline | this model |
|---|---|---|
| en | 0.379 | 0.522 |
| pt | 0.134 | 0.474 |
| de | 0.144 | 0.470 |
| fr | 0.141 | 0.470 |
| it | 0.139 | 0.470 |
| vi | 0.130 | 0.469 |
| pl | 0.110 | 0.466 |
| id | 0.110 | 0.461 |
| es | 0.162 | 0.457 |
| zh | 0.069 | 0.457 |
| hi | 0.075 | 0.456 |
| nl | 0.157 | 0.455 |
| ru | 0.073 | 0.452 |
| uk | 0.067 | 0.445 |
| ja | 0.103 | 0.444 |
| fa | 0.051 | 0.434 |
| ko | 0.103 | 0.431 |
| th | 0.102 | 0.427 |
| bn | 0.056 | 0.419 |
| tr | 0.094 | 0.407 |
| sw | 0.098 | 0.361 |
| ar | 0.041 | 0.354 |

### BRIGHTER

BRIGHTER (SemEval-2025 Task 11): 28 languages, text written natively in each
language, human annotated, CC-BY 4.0. No model in the table was trained on it.

The 28 GoEmotions labels are projected onto BRIGHTER's six emotions through Ekman
groups, taking the maximum within each group. Thresholds tuned on each language's
own dev split. Zero-shot across dataset, domain and label set.

Languages are grouped by whether they appear in this model's training set. Four of
the unseen languages (Makhuwa, Kinyarwanda, Tatar, Nigerian Pidgin) are also absent
from XLM-RoBERTa's pretraining corpus.

| model | params | trained langs (13) | unseen langs (15) | English |
|---|---|---|---|---|
| lettuce-thymos-26m-v1 | 26.5M | 0.427 | 0.292 | 0.502 |
| SamLowe/roberta-base-go_emotions | 125M | 0.192 | 0.152 | 0.505 |
| cirimus/modernbert-base-go-emotions | 149M | 0.250 | 0.204 | 0.520 |
| cirimus/modernbert-large-go-emotions | 395M | 0.201 | 0.144 | 0.493 |

This model per language, training languages:

| ru | es | hi | en | id | uk | ar (dz) | zh | de | pt (br) | ar (ma) | pt (mz) | sw |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.608 | 0.605 | 0.568 | 0.502 | 0.454 | 0.446 | 0.428 | 0.409 | 0.398 | 0.344 | 0.291 | 0.261 | 0.242 |

Unseen languages, highest to lowest: Romanian 0.516, Javanese 0.432, Marathi 0.414,
Sundanese 0.397, Nigerian Pidgin 0.395, Tatar 0.310, Swedish 0.287, Hausa 0.283,
Afrikaans 0.257, Igbo 0.243, Xhosa 0.240, Kinyarwanda 0.195, Yoruba 0.151,
Zulu 0.134, Makhuwa 0.121.

Systems fine-tuned on BRIGHTER's training data score 0.55 to 0.89 on this task.
Those numbers are not comparable to the zero-shot results above.

English macro-F1 on both evaluations:

| model | GoEmotions | BRIGHTER |
|---|---|---|
| SamLowe/roberta-base-go_emotions | 0.505 | 0.505 |
| cirimus/modernbert-base-go-emotions | 0.535 | 0.520 |
| lettuce-thymos-26m-v1 | 0.527 | 0.502 |
| cirimus/modernbert-large-go-emotions | 0.542 | 0.493 |

### Latency

ONNX Runtime, CPU, Intel i7-10700K, batch 1, median of 40 runs.

| threads | seq 32 | seq 64 | seq 128 |
|---|---|---|---|
| 1 | 6.4 ms | 12.2 ms | 24.6 ms |
| 2 | 3.8 ms | 7.2 ms | 13.9 ms |
| 4 | 2.7 ms | 4.7 ms | 8.9 ms |

Chunked input scales close to linearly, 12 to 14 ms per 128-token window at
2 threads.

## Limitations

`grief`, `relief`, `pride`, `nervousness` and `embarrassment` score well below the
average. GoEmotions contains 77 `grief` training examples, and macro-F1 weights that
class equally with classes that have thousands.

Arabic and Swahili trail the other languages on both evaluations. BRIGHTER tests
Arabic in Algerian and Moroccan dialects while training used Modern Standard
Arabic; the two dialects differ by 0.14.

Training domain is Reddit comments: short, informal, conversational. Literary text,
long-form writing and formal registers are out of distribution.

Output probabilities are not calibrated as absolute confidences. Decisions come
from the per-class thresholds.

Non-English training data is machine-translated. In the GoEmotions evaluation the
test data comes from the same translator, so those per-language scores measure
performance on translated text. Its 119,394 rows are 5,427 source comments rendered
in 22 languages, not 119,394 independent examples. The BRIGHTER evaluation covers
11 of the 22 languages on natively written text.

Languages outside the listed 22 rely on backbone transfer and score lower.

## License

Apache-2.0.

Upstream: GoEmotions (Apache-2.0), M2M-100 (MIT), XLM-RoBERTa (MIT).
Evaluation data: GoEmotions (Apache-2.0), BRIGHTER (CC-BY 4.0).
