---
library_name: transformers
tags:
- sparse
- sparse-encoder
- sentence-transformers
- sparse-retrieval
- multilingual
- learned-sparse
- cross-lingual
license: apache-2.0
pipeline_tag: sentence-similarity
language:
- aa
- en
- vi
- de
- fr
- ko
- ru
- id
- sw
- hi
- ar
- af
- bg
- bn
- ca
- cs
- da
- el
- es
- et
- fa
- fi
- gl
- gu
- he
- hr
- hu
- hy
- it
- ja
- ka
- km
- ku
- lt
- lv
- mk
- mn
- mr
- ms
- my
- nb
- nl
- 'no'
- pl
- pt
- ro
- sk
- sl
- sq
- sr
- sv
- te
- th
- tr
- uk
- ur
- yo
- zh
---
# MILCO: Learned Sparse Retrieval Across Languages via a Multilingual Connector

**Paper**: [MILCO: Learned Sparse Retrieval Across Languages via a Multilingual Connector](https://openreview.net/forum?id=Z6dVYEqurT) (ICLR 2026)

## Overview

Learned Sparse Retrieval (LSR) combines the efficiency of bi-encoders with the transparency of lexical matching, but existing approaches struggle to scale beyond English. MILCO addresses this by mapping queries and documents from different languages into a shared English lexical space via a multilingual connector. MILCO supports both **monolingual** and **cross-lingual** retrieval and has been evaluated on **39+ languages**, with the potential to generalize to additional languages supported by the underlying multilingual encoder.

MILCO is trained with a two-stage regime that combines **Sparse Alignment Pretraining** with **contrastive learning**, designed to provide representation transparency and effectiveness while mitigating semantic collapse.

We also introduce **LexEcho head**, which addresses the observation that uncommon entities/rare terms (e.g., proper nouns, code-switched terms) are often lost when projected into English. The LexEcho head augments the English lexical representation with a source-language view, preserving the original multilingual token weights alongside the projected English terms.

## Usage

### Using Transformers

#### Loading the model

```python
from transformers import AutoModel
model = AutoModel.from_pretrained("omai-research/milco-650m", trust_remote_code=True)
```

#### Encoding text (sparse tensor)

```python
# Returns a sparse COO tensor of shape [N, vocab_size]
sparse_reps = model.encode_text(["Baltimore: The Greatest City in America", "巴尔的摩：美国最伟大的城市", "Baltimore : La plus grande ville d'Amérique"])
```

#### Encoding text (token-weight dictionary)

```python
# Returns a list of {token: weight} dicts, sorted by weight descending
results = model.encode_text(["Baltimore : La plus grande ville d'Amérique", "巴尔的摩：美国最伟大的城市"], return_dict=True)
print(results[0])
# {'e_baltimore': 1.8021222352981567, 'e_maryland': 1.2527629137039185, 'e_city': 1.202409029006958, 'e_largest': 0.9440274834632874, 'e_biggest': 0.9287132620811462, 'e_america': 0.890972912311554, 'e_usa': 0.8649974465370178, 'e_urban': 0.7201237678527832, 'e_geography': 0.6369074583053589, 'e_cities': 0.5816917419433594, 'e_us': 0.42353010177612305, 'e_is': 0.35060185194015503 ..}
print(results[1])
# {'e_baltimore': 1.6522579193115234, 'e_city': 1.3217558860778809, 'e_greatest': 1.1192315816879272, 'e_usa': 0.9287132620811462, 'e_maryland': 0.8281423449516296, 'e_best': 0.817850649356842, 'e_biggest': 0.8074519634246826, 'e_us': 0.6793810129165649, 'e_great': 0.630689799785614, 'e_america': 0.5255602598190308 ...}
```
#### LexEcho: Dual-view encoding (pivot + source)

When `source_view=True`, the LexEcho head augments the pivot representation with source-language token weights. This preserves entities and terms that may not have English equivalents:

```python
results = model.encode_text(["巴尔的摩：美国最伟大的城市"], return_dict=True, source_view=True)
# Shape: [N, en_vocab_size + m_vocab_size]
# Columns [0, en_vocab_size) are pivot (English) terms
# Columns [en_vocab_size, en_vocab_size + m_vocab_size) are source (multilingual) terms
print(results[0])
# {'m_</s>': 2.09375, 'e_baltimore': 1.6522579193115234, 'e_city': 1.3217558860778809, 'e_greatest': 1.12432062625885, 'e_usa': 0.9225212931632996, 'e_maryland': 0.8247235417366028, 'e_best': 0.8143964409828186, 'e_biggest': 0.8039615750312805, 'm_伟大的': 0.77734375, 'm_:': 0.6875, 'm_美国': 0.68359375, 'e_us': 0.6734226942062378, 'e_great': 0.6265231370925903}
```

#### Query and document encoding

`encode_query` and `encode_document` are aliases for `encode_text`:

```python
q_reps = model.encode_query(queries)
d_reps = model.encode_document(documents)
scores = torch.sparse.mm(q_reps, d_reps.t())
```

#### Getting the vocabulary mapping

```python
id2term = model.get_vocab()
# {0: "e_[PAD]", 1: "e_[UNK]", ..., 30522: "m_[PAD]", ...}
# "e_" prefix = English (pivot) vocabulary
# "m_" prefix = multilingual (source) vocabulary
```

### Using Sentence Transformers

Install Sentence Transformers and PyTorch 2.6 or newer, which Transformers requires to load this `.bin` checkpoint:

```bash
pip install "sentence-transformers>=5.4.0" "torch>=2.6"
```

Each example below can be run independently.

#### Loading the model

```python
from sentence_transformers import SparseEncoder

model = SparseEncoder("omai-research/milco-650m", trust_remote_code=True)
```

#### Encoding text (sparse tensor)

```python
from sentence_transformers import SparseEncoder

model = SparseEncoder("omai-research/milco-650m", trust_remote_code=True)

texts = [
    "Baltimore: The Greatest City in America",
    "巴尔的摩：美国最伟大的城市",
    "Baltimore : La plus grande ville d'Amérique",
]
sparse_reps = model.encode(texts)
print(sparse_reps.shape, sparse_reps.layout)
# torch.Size([3, 30522]) torch.sparse_coo
```

#### Encoding text (token-weight dictionary)

Use MILCO's `_sparse_to_dicts` helper to get token weights sorted in descending order. `SparseEncoder.decode()` uses the multilingual input tokenizer, which does not describe the English output vocabulary.

```python
from sentence_transformers import SparseEncoder

model = SparseEncoder("omai-research/milco-650m", trust_remote_code=True)

texts = [
    "Baltimore : La plus grande ville d'Amérique",
    "巴尔的摩：美国最伟大的城市",
]
sparse_reps = model.encode(texts)
results = model.transformers_model._sparse_to_dicts(sparse_reps)
print(dict(list(results[0].items())[:5]))
# {'e_baltimore': 1.8038008213043213, 'e_maryland': 1.2524265050888062, 'e_city': 1.1995835304260254, 'e_largest': 0.9366427659988403, 'e_biggest': 0.9186832904815674}
print(dict(list(results[1].items())[:5]))
# {'e_baltimore': 1.6520189046859741, 'e_city': 1.3212192058563232, 'e_greatest': 1.1182334423065186, 'e_usa': 0.9234126210212708, 'e_best': 0.8151688575744629}
```

#### LexEcho: Dual-view encoding (pivot + source)

Pass `source_view=True` to include source-language token weights alongside the English pivot vocabulary. The first 30522 dimensions are pivot terms, followed by 250002 source dimensions.

```python
from sentence_transformers import SparseEncoder

model = SparseEncoder("omai-research/milco-650m", trust_remote_code=True)

sparse_reps = model.encode(["巴尔的摩：美国最伟大的城市"], source_view=True)
print(sparse_reps.shape)
# torch.Size([1, 280524])
results = model.transformers_model._sparse_to_dicts(sparse_reps)
print(dict(list(results[0].items())[:10]))
# {'m_</s>': 2.0875837802886963, 'e_baltimore': 1.6520189046859741, 'e_city': 1.3212192058563232, 'e_greatest': 1.1182334423065186, 'e_usa': 0.9234126210212708, 'e_best': 0.8151688575744629, 'e_maryland': 0.8147269487380981, 'e_biggest': 0.8038767576217651, 'm_伟大的': 0.7776944637298584, 'm_:': 0.6851922869682312}
```

## Results

MILCO achieves state-of-the-art multilingual and cross-lingual LSR performance, outperforming leading dense, sparse, and multi-vector baselines including **BGE-M3** and **Qwen3-Embed** on standard multilingual benchmarks.

With mass-based pruning to reduce document representations to only 30 active dimensions on average, MILCO 560M outperforms the similarly-sized Qwen3-Embed 0.6B (1024 dimensions) while achieving **3x lower retrieval latency** and **10x smaller index size**.

## Architecture

MILCO consists of:

- **Multilingual encoder**: A pretrained multilingual transformer that produces contextual embeddings for input text in any language.
- **Multilingual connector**: A linear layer that maps multilingual hidden states into the English encoder's hidden dimension.
- **LexEcho head**:
  - **LM head**: Borrowed from a pretrained English masked language model, produces logits over the English vocabulary. Used to generate the pivot (English) sparse representation.
  - **Echo token**: A special [ECHO] token added to the MLM head to score each input token, producing the source-language view that preserves uncommon entities that may be lost during projection into the English vocabulary.




## Configuration

| Parameter | Description |
|---|---|
| `lsr_encoder_checkpoint` | naver/splade-v3 |
| `multilingual_encoder_checkpoint` | BAAI/bge-m3-unsupervised |

## Citation

```bibtex
@inproceedings{nguyen2026milco,
  title={MILCO: Learned Sparse Retrieval Across Languages via a Multilingual Connector},
  author={Nguyen, Thong and Lei, Yibin and Ju, Jia-Huei and Yang, Eugene and Yates, Andrew},
  booktitle={International Conference on Learning Representations},
  year={2026}
}
```
