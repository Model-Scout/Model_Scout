---
license: apache-2.0
library_name: sentence-transformers
pipeline_tag: sentence-similarity
base_model: ibm-granite/granite-embedding-311m-multilingual-r2
tags:
  - sentence-transformers
  - feature-extraction
  - sentence-similarity
  - embeddings
  - retrieval
  - multilingual
  - matryoshka
  - roleplay
  - memory
  - onnx
  - int8
language:
  - ar
  - de
  - en
  - es
  - fr
  - hi
  - it
  - ja
  - ko
  - nl
  - pl
  - pt
  - ru
  - tr
  - zh
datasets:
  - hotchpotch/wikipedia-multilingual-synthetic-ir-query
  - nthakur/swim-ir-cross-lingual
  - nthakur/swim-ir-monolingual
  - HuggingFaceFW/finewiki
  - sentence-transformers/parallel-sentences-wikimatrix
  - sentence-transformers/parallel-sentences-tatoeba
  - sentence-transformers/parallel-sentences-europarl
  - flax-sentence-embeddings/stackexchange_title_body_jsonl
  - tomaarsen/natural-questions-hard-negatives
  - sentence-transformers/hotpotqa
  - sentence-transformers/squad
  - sentence-transformers/miracl
  - sentence-transformers/mr-tydi
  - SkelterLabsInc/JaQuAD
  - deepset/germanquad
  - deepset/germandpr
  - PlanTL-GOB-ES/SQAC
  - ipipan/polqa
  - CohereLabs/aya_dataset
  - OpenAssistant/oasst2
  - sentence-transformers/simple-wiki
  - deepmind/narrativeqa
  - hotchpotch/bekko-embedding-hard-negatives
  - google/Synthetic-Persona-Chat
---

# lettuce-eidos-768d-v5

Multilingual embedding model for conversational memory retrieval in 15 languages.
768-dimensional output with Matryoshka truncation to 64, 4,096-token context,
60M active parameters per token, 262 MB as int8 ONNX.

It is the memory model of [LettuceAI](https://lettuceai.app) and succeeds
[`Zeolit/lettuce-emb-768d-v4`](https://huggingface.co/Zeolit/lettuce-emb-768d-v4).

*Eidos* (εἶδος) is the Greek word for form: the shape of a thing that remains
recognisable however it is described.

## Model description

A 12-layer student pruned from `ibm-granite/granite-embedding-311m-multilingual-r2`
(22 layers) and trained by self-distillation from the unpruned model, together
with contrastive retrieval objectives on general and roleplay data.

| | |
|---|---|
| Architecture | ModernBERT, 12 layers (6 global attention, 6 sliding window 128), 768 hidden, 12 heads, FFN 1152 |
| Layers kept from base | 0, 1, 2, 5, 6, 9, 10, 15, 16, 18, 19, 21 |
| Parameters | 262M total: 201M vocabulary table, 60M transformer |
| Vocabulary | 262,152 tokens (granite multilingual r2 tokenizer) |
| Pooling | CLS token, L2 normalized |
| Output | 768 dimensions; Matryoshka 512 / 384 / 256 / 128 / 64 |
| Context | 4,096 tokens (trained); base supports 32K |
| Prompts | none; queries and documents are encoded the same way |
| Files | 262 MB int8 ONNX, 1,046 MB fp32 ONNX |

## Intended uses and limitations

Retrieval of short conversational memories (chat turns, roleplay events, notes)
from a user's own history, on device or on CPU. Works for queries and memories in
different languages.

Raw cosine similarities are high for this model, including for unrelated text.
Ranking is unaffected, but **do not apply fixed thresholds tuned for other models**;
use `calibration.json` (see [Score calibration](#score-calibration)).

Known weaknesses are listed under [Limitations](#limitations).

## How to use

### Sentence Transformers

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("Zeolit/lettuce-eidos-768d-v5")
# model = SentenceTransformer("Zeolit/lettuce-eidos-768d-v5", truncate_dim=256)

query = "Aria: The mill looks quiet tonight.\nUser: Do you remember where you hid the sword?"
memories = [
    "Elara hid the sword in the old stone well behind the mill, under a loose slab.",
    "Elara took her sword to the village blacksmith to have it sharpened.",
    "Apple prices at the market went up again this week.",
]
q = model.encode(query)
m = model.encode(memories)
print(model.similarity(q, m))
```

Requires a `transformers` release with ModernBERT `layer_types` support
(the checkpoint was saved with transformers 5.17).

### ONNX Runtime

Pooling and normalization are inside the graph; the output `embedding` is the
final 768-dimensional unit vector.

```python
import json, numpy as np, onnxruntime as ort
from tokenizers import Tokenizer

tok = Tokenizer.from_file("tokenizer.json")
tok.enable_truncation(4096)
tok.enable_padding()
sess = ort.InferenceSession("onnx/model_quantized.onnx", providers=["CPUExecutionProvider"])
cal = json.load(open("calibration.json"))

def embed(texts, dim=768):
    enc = tok.encode_batch(texts)
    e = sess.run(None, {
        "input_ids": np.array([x.ids for x in enc], dtype=np.int64),
        "attention_mask": np.array([x.attention_mask for x in enc], dtype=np.int64),
    })[0][:, :dim]
    return e / np.linalg.norm(e, axis=1, keepdims=True)   # re-normalize after truncation

def shown_score(cosine, dim=768):
    c = cal["dims"][str(dim)]
    return np.clip(c["a"] * cosine + c["b"], 0.0, 1.0)

q = embed([query])
m = embed(memories)
scores = shown_score(m @ q[0])
keep = scores >= cal["default_threshold"]
```

Repository layout:

```
config.json                 ModernBERT config (12 layers)
model.safetensors           PyTorch weights, fp32
tokenizer.json              tokenizer
modules.json, 1_Pooling/    Sentence Transformers config (CLS pooling + normalize)
onnx/model.onnx             fp32 export, pooling + normalization in graph
onnx/model_quantized.onnx   int8 export (dynamic quantization)
calibration.json            per-dimension score mapping and thresholds
evaluation/results.json     every number in this card
```

## Training data

All general-purpose training data is under licences that permit commercial use
and derivative works (CC-BY, CC-BY-SA, Apache-2.0, MIT, or free of copyright
restrictions). Non-commercial and no-derivatives datasets, web-scraped third-party
content, and outputs of models whose terms restrict training were excluded.

**General retrieval, 11.06M pairs after filtering, 18 sources:**

| Source | Licence | Content | Languages |
|---|---|---|---|
| `hotchpotch/wikipedia-multilingual-synthetic-ir-query` | CC-BY-SA 4.0 | query → Wikipedia passage / long document | 11 |
| `nthakur/swim-ir-cross-lingual`, `swim-ir-monolingual` | CC-BY-SA 4.0 | question → passage, incl. cross-lingual | 10 |
| `HuggingFaceFW/finewiki` (own pairs) | CC-BY-SA 4.0 | title → lead, paragraph pairs, long articles | 15 |
| `parallel-sentences-wikimatrix` / `-tatoeba` / `-europarl` | CC-BY-SA / CC-BY 2.0 FR / no copyright restriction | en ↔ xx parallel sentences | 14 pairs |
| `stackexchange_title_body_jsonl` | CC-BY-SA 4.0 | forum title → body | en |
| Natural Questions (hard negatives), HotpotQA, SQuAD | CC-BY-SA | human-labelled question → passage | en |
| MIRACL, Mr. TyDi | Apache-2.0 | human-labelled, with negatives | 9 |
| JaQuAD, GermanQuAD, GermanDPR, SQAC, PolQA | CC-BY-SA 3.0/4.0, CC-BY 4.0 | human-written question → paragraph | ja, de, es, pl |
| Aya dataset, OASST2 | Apache-2.0 | human-written request → answer | 15 |
| Simple Wiki, NarrativeQA | CC-BY-SA, Apache-2.0 | paraphrase, question → summary | en |
| `bekko-embedding-hard-negatives` (Wikipedia subsets only) | CC-BY-SA | query + 15 hard negatives | 11 |

**Roleplay and chat memory, ~580k pairs:**

- Generated with `google/gemma-4-26B-A4B-it`: 10,000 scenarios per language,
  150,000 in total, built from independent axes (relationship, concern, memory
  type, voice, setting). Each scenario yields two memories about the same two
  characters describing different events (each the other's hard negative), a
  direct recall question per memory, and a context-enriched query per memory
  (previous character message + user message). 30% of non-English scenarios are
  cross-lingual (query in the target language, memory in English). Outputs are
  validated for structure, length, script and language. 5% of scenarios are held
  out as whole units for evaluation.
- 60,000 English pairs cut without a model from the persona dialogues used for
  v4 (opening → passage, passage with two turns removed → rest). Passages used as
  answers in the evaluation benchmark are excluded.

## Training procedure

**Pruning.** Greedy backward layer elimination on the base model: remove one layer
at a time, choosing the layer whose removal best preserves the cosine between the
pruned and full model's embeddings, with at least 6 global-attention layers kept.
Cosine to the full model before training: 0.936.

**Teacher pass.** The full base model scores every pair. Inconsistent pairs are
dropped, the easiest 30% are thinned, and hard negatives are mined per query with a
scale-free false-negative guard (a candidate is rejected if it scores within 25%
of the positive–background gap of the positive), then sieved with
`BAAI/bge-reranker-v2-m3`. Negatives are re-mined with the stage-1 model before
stage 2.

**Losses.** InfoNCE with GradCache and teacher-guided false-negative masking;
self-distillation to the teacher's embeddings and in-batch similarity matrix;
listwise KL to teacher scores over mined negatives (stages 2–3). All losses are
applied at every Matryoshka dimension. Distillation weight 15 on general data, 3 on
roleplay data.

| Stage | Steps | Max length | Batch | Roleplay share |
|---|---|---|---|---|
| 1 | 4,000 | 256 | 1,024 | 30% |
| 2 | 3,000 | 512 | 192, 7 hard negatives | 25% |
| 3 | 1,500 | 4,096 | 32 long / 512 short replay | 20% |

Learning rates 5e-5 / 2e-5 / 1e-5, temperature 0.03, warmup 5%. The release is the
last stage-3 checkpoint.

**Quantization.** ONNX Runtime dynamic int8 quantization. On a 500-query roleplay
eval, recall@1 goes from 0.972 (fp32) to 0.958 (int8) at 768 dimensions and from
0.964 to 0.940 at 64; mean cosine between int8 and fp32 embeddings is 0.991.

## Evaluation

Four models under one protocol: this model, v4, `hotchpotch/bekko-embedding-v1-a25m`
and the unpruned base `ibm-granite/granite-embedding-311m-multilingual-r2`.
PyTorch fp32 unless stated. Raw numbers are in `evaluation/results.json`.

### Roleplay memory (v4 benchmark)

5,000 deterministic queries. Persona-prefix queries (the opening 30% of a dialogue
window retrieves the window) and summary queries. v4's published numbers reproduce
(Tier B recall@1 0.513 against 0.512 published).

| Model | 500 passages R@1 | R@5 | **144k passages R@1** | R@5 |
|---|---|---|---|---|
| lettuce-eidos-768d-v5 | **0.926** | **0.986** | **0.725** | **0.903** |
| lettuce-emb-768d-v4 | 0.902 | 0.948 | 0.513 | 0.769 |
| bekko-embedding-v1-a25m | 0.916 | 0.974 | 0.535 | 0.763 |
| granite-311m-multilingual-r2 | 0.864 | 0.962 | 0.460 | 0.669 |

Persona-prefix subset of the 144k haystack: v5 0.866, v4 0.245.

Both v4 and v5 were trained on the persona corpus this benchmark is built from
(v5 with benchmark answers excluded). Read it as in-distribution.

### Matryoshka (144k haystack, recall@1)

| Dimensions | 64 | 128 | 256 | 384 | 512 | 768 |
|---|---|---|---|---|---|---|
| v5 | **0.661** | **0.709** | **0.717** | **0.724** | **0.724** | **0.725** |
| v4 | 0.425 | 0.487 | 0.504 | | 0.509 | 0.513 |

### Multilingual chat memory (held-out, recall@1)

25,364 queries (direct questions and context-enriched queries) over 12,682
memories from the held-out 5% of generated scenarios. Every scenario contains two
memories about the same characters, so the best wrong answer is a deliberate
near-duplicate.

| Model | all | ar | de | en | es | fr | hi | it | ja | ko | nl | pl | pt | ru | tr | zh |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v5 | **0.232** | 0.240 | 0.207 | 0.260 | 0.238 | 0.218 | 0.228 | 0.202 | 0.272 | 0.301 | 0.226 | 0.171 | 0.239 | 0.191 | 0.228 | 0.269 |
| v4 | 0.025 | 0.010 | 0.038 | 0.079 | 0.038 | 0.018 | 0.014 | 0.019 | 0.026 | 0.013 | 0.034 | 0.008 | 0.030 | 0.006 | 0.032 | 0.018 |
| bekko-a25m | 0.095 | 0.101 | 0.103 | 0.092 | 0.092 | 0.070 | 0.102 | 0.074 | 0.133 | 0.152 | 0.096 | 0.048 | 0.094 | 0.056 | 0.101 | 0.129 |
| granite-311m | 0.081 | 0.109 | 0.057 | 0.095 | 0.071 | 0.050 | 0.106 | 0.044 | 0.138 | 0.117 | 0.061 | 0.044 | 0.073 | 0.052 | 0.098 | 0.119 |

This test comes from the same generator as the roleplay training data (different
scenarios), so it is also in-distribution for v5.

### STSBenchmark

Spearman 0.784 (v4: 0.819).

## Score calibration

Unrelated text scores a median raw cosine of about 0.65 with this model.
`calibration.json` gives, per Matryoshka dimension, a linear map

```
shown = clamp(a * cosine + b, 0, 1)
```

fitted on the held-out multilingual chat-memory test so that the median unrelated
memory maps to 0.20 and the point where 2% of unrelated memories pass maps to 0.50.
After mapping, use 0.50 as the default threshold and 0.35 as a permissive fallback
(about 10% of unrelated memories pass).

| Dimension | a | b | correct memories kept at 0.50 | at 0.35 |
|---|---|---|---|---|
| 768 | 2.3810 | −1.3810 | 92.5% | 99.1% |
| 512 | 2.2901 | −1.2863 | 92.6% | 99.2% |
| 384 | 2.2556 | −1.2549 | 92.6% | 99.1% |
| 256 | 2.2388 | −1.2440 | 92.4% | 99.1% |
| 128 | 2.2388 | −1.2664 | 91.8% | 98.9% |
| 64 | 1.9481 | −1.0058 | 89.0% | 98.0% |

Thresholds only remove unrelated memories. Near-duplicates of the correct memory
score as high as the correct one and are separated by ranking, not by threshold.

## Limitations

- Tuned for short conversational memories. Retrieval of book-length documents is
  weaker than v4.
- Sentence-similarity grading (STS) is lower than v4.
- Multilingual chat-memory recall@1 of 0.232 leaves most near-duplicate cases
  unresolved on the first result.
- All benchmarks above were built by us and are in-distribution. No public
  retrieval benchmark (e.g. MMTEB) has been run yet.
- The int8 file is larger than v4's (262 MB vs 138 MB) because of the multilingual
  vocabulary; compute per token is about half of v4's.

## License

Apache-2.0. The base model is Apache-2.0. Training data licences are listed above;
CC-BY and CC-BY-SA sources are credited here as required.
