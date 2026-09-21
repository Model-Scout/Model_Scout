---
language:
- ko
- en
license: apache-2.0
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- retrieval
- korean
- matryoshka
- rag
pipeline_tag: sentence-similarity
library_name: sentence-transformers
base_model:
- Snowflake/snowflake-arctic-embed-l-v2.0
---

# Frony Embed Arctic V2.5 (0.6B)

A Korean-first text embedding model for retrieval, built on Snowflake/snowflake-arctic-embed-l-v2.0. It targets single-stage retrieval where the top-1 hit matters — RAG pipelines that feed one or two passages directly to an LLM, FAQ matching, semantic search over Korean documents. It handles Korean↔English cross-lingual retrieval and was explicitly tuned for Markdown-formatted passages, which is how most modern RAG chunks actually look.

**At a glance**

| | |
|---|---|
| Base model | `Snowflake/snowflake-arctic-embed-l-v2.0` |
| Parameters | ~568M |
| Architecture | Bi-encoder, single-vector dense retrieval (mean pooling) |
| Dimensions | 1024, or 512 via Matryoshka truncation (both directly trained) |
| Max sequence length | 8192 tokens (**512 recommended** — see note below) |
| Similarity | Cosine (outputs are L2-normalized) |
| Languages | Korean, English (ko→ko, ko→en, en→ko) |
| Training data | about 500K query–passage pairs |
| Training | 3 stages — multi-vector → self-distillation → hard negatives |
| Training hardware | Single GPU, 46GB VRAM |
| License | Apache-2.0 (see *License and attribution*) |

> **Note on sequence length.** The base model accepts up to 8192 tokens, but training and evaluation were done at shorter lengths. Quality is only guaranteed up to **512 tokens**. Chunk accordingly.

---

## Usage
 
```bash
pip install -U sentence-transformers
```
 
The model distinguishes queries from passages using the special tokens `<Q>` and
`<P>`. **These are required** — retrieval quality degrades noticeably without
them. They are registered as prompts in the published model, so `prompt_name`
adds them for you.
 
```python
import torch.nn.functional as F
from sentence_transformers import SentenceTransformer
 
model = SentenceTransformer("FronyAI/frony-embed-arctic-ko-0.6B-v2.5")
 
queries = [
    "대한민국의 수도는 어디입니까?",
    "What is the largest port city in South Korea?",
]
passages = [
    "서울은 대한민국의 수도이며, 정치와 경제의 중심지이다.",
    "Busan is South Korea's largest port city, located on the southeastern coast.",
]
 
q = model.encode(queries,  prompt_name="query",   convert_to_tensor=True)
p = model.encode(passages, prompt_name="passage", convert_to_tensor=True)
 
# Outputs are L2-normalized already, so cosine similarity is a plain dot product.
scores = q @ p.T                      # [2, 2]
#           p0 (서울)  p1 (Busan)
#   q0        0.6026      0.3363
#   q1        0.2030      0.8143
 
# 512 dimensions (Matryoshka): slice the first 512, then re-normalize.
# Truncating a unit vector leaves it shorter than unit length, and skipping the
# second normalization distorts every score that follows. Truncate queries and
# passages to the same width — mixing widths produces meaningless scores.
q512 = F.normalize(q[:, :512], p=2, dim=-1)
p512 = F.normalize(p[:, :512], p=2, dim=-1)
scores_512 = q512 @ p512.T            # [2, 2]
#           p0 (서울)  p1 (Busan)
#   q0        0.5913      0.3466
#   q1        0.1592      0.8073
 
# Outside sentence-transformers, write the tokens inline instead:
#   "<Q>대한민국의 수도는 어디입니까?"
#   "<P>서울은 대한민국의 수도이며, 정치와 경제의 중심지이다."
```
 
The correct pairs are (q0, p0) and (q1, p1), and both widths rank them first.
Scores shown are from a single reference run — expect small differences across
hardware and dtype, and compare the ordering rather than the exact digits.
 
> **512 is the only supported truncation.** Stage 3 trains the full
> 1024-dimension output and the 512-dimension prefix jointly, with equal weight.
> Narrower widths such as 256 or 128 were never part of the training objective
> and are not expected to hold up.

---

## Training

Training runs in three sequential stages, each initialized from the previous stage's checkpoint:

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 620 406" width="620" height="406" role="img" font-family="ui-sans-serif, system-ui, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif">
  <title>Three-stage training pipeline</title>
  <desc>Training starts from the base model snowflake-arctic-embed-l-v2.0 and proceeds through three sequential stages: Stage 1 multi-vector training, Stage 2 dense transfer via self-distillation, and Stage 3 hard-negative fine-tuning. The result is this model, frony-embed-arctic-ko-0.6B-v2.5. Each stage initializes from the previous stage's checkpoint.</desc>

  <defs>
    <marker id="d" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M1 1L9 5L1 9" fill="none" stroke="#8A8A80" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
    </marker>
  </defs>

  <rect x="0" y="0" width="620" height="406" fill="#FAFAF7"/>

  <!-- base model -->
  <rect x="210" y="25" width="200" height="40" rx="20" fill="#EFEFEA" stroke="#D2D2C8"/>
  <text x="310" y="45" text-anchor="middle" dominant-baseline="central" font-size="15" font-weight="600" fill="#4A4A44">Base model</text>

  <line x1="310" y1="68" x2="310" y2="84" stroke="#8A8A80" stroke-width="1.4" marker-end="url(#d)"/>

  <!-- stage 1 -->
  <rect x="60" y="87" width="500" height="54" rx="12" fill="#E3DDEF" stroke="#6B4FA0"/>
  <text x="85" y="114" dominant-baseline="central" font-size="13" font-weight="600" fill="#6B4FA0">Stage1: Align</text>
  <text x="200" y="114" dominant-baseline="central" font-size="15" font-weight="600" fill="#33254F">Multi-vector training</text>

  <line x1="310" y1="144" x2="310" y2="160" stroke="#8A8A80" stroke-width="1.4" marker-end="url(#d)"/>

  <!-- stage 2 -->
  <rect x="60" y="163" width="500" height="54" rx="12" fill="#D9E9E5" stroke="#2E7D6F"/>
  <text x="85" y="190" dominant-baseline="central" font-size="13" font-weight="600" fill="#2E7D6F">Stage2: Distill</text>
  <text x="200" y="190" dominant-baseline="central" font-size="15" font-weight="600" fill="#173F38">Dense transfer via self-distillation</text>

  <line x1="310" y1="220" x2="310" y2="236" stroke="#8A8A80" stroke-width="1.4" marker-end="url(#d)"/>

  <!-- stage 3 -->
  <rect x="60" y="239" width="500" height="54" rx="12" fill="#F5DFD8" stroke="#C4553D"/>
  <text x="85" y="266" dominant-baseline="central" font-size="13" font-weight="600" fill="#C4553D">Stage3: Refine</text>
  <text x="200" y="266" dominant-baseline="central" font-size="15" font-weight="600" fill="#7A3527">Hard-negative fine-tuning</text>

  <line x1="310" y1="296" x2="310" y2="312" stroke="#8A8A80" stroke-width="1.4" marker-end="url(#d)"/>

  <!-- this model -->
  <rect x="210" y="315" width="200" height="40" rx="20" fill="#2F2F2A" stroke="#2F2F2A"/>
  <text x="310" y="335" text-anchor="middle" dominant-baseline="central" font-size="15" font-weight="600" fill="#FAFAF7">This model</text>

  <text x="310" y="384" text-anchor="middle" font-size="12" fill="#6B6B63">Each stage initializes from the previous stage's checkpoint.</text>
</svg>

The reasoning behind the order: preliminary experiments showed multi-vector (late-interaction) retrieval consistently outperforming dense retrieval on our data. Rather than ship a multi-vector model — which costs far more at index and query time — we train that objective first, then transfer what it learned into a single-vector representation, and finally sharpen the result against hard negatives.

### Shared setup

Common across all three stages:

| | |
|---|---|
| Pooling | Mean pooling over tokens, attention-mask weighted |
| Max sequence length | 512 |
| Temperature | 0.02 |
| Loss | InfoNCE (cross-entropy over similarity scores) |
| Optimizer | 8-bit AdamW (`bitsandbytes`) |
| Schedule | Polynomial decay, `power=1.0` |
| Weight decay | 1e-3, excluding biases and LayerNorm |
| Precision | fp16 |
| Gradient accumulation | 4 |
| Gradient clipping | 1.0 |
| Framework | PyTorch Lightning |

The validation set is held fixed across all three stages, so loss curves are directly comparable from one stage to the next.

**Query and passage tokens.** `<Q>` and `<P>` are added to the vocabulary as genuine special tokens in Stage 1, with the embedding matrix resized accordingly, and their embeddings are trained through all three stages. They are not string prefixes in the manner of `"query: "` — they are single learned tokens, which is why they cost one token rather than several and why omitting them degrades retrieval noticeably.

---

### Stage 1: Align — Multi-vector training

Late-interaction retrieval consistently beat dense retrieval in preliminary experiments on our data, but shipping a multi-vector model would multiply index and query cost — so this stage trains that objective first, to produce something worth transferring into a single vector later. Scoring is ColBERT-style MaxSim over the full token sequence with no pooling, trained with InfoNCE over in-batch negatives. `<Q>` and `<P>` are added here as genuine special tokens with the embedding matrix resized, and train through all three stages.

Because token-by-token similarity matrices make large batches expensive — and batch size is what determines the number of in-batch negatives — each step maintains a FIFO queue of the four most recent passage batches, giving a negative pool of 32 from a batch of 8. Queued passages are re-encoded rather than cached, so gradients flow through all 32: a memory-for-compute trade, not a memory bank in the MoCo sense (He et al., 2020, arXiv:1911.05722). Note that gradient accumulation 4 over batch size 8 also yields 32, but that number is unrelated — it affects only optimizer step frequency. Gradient caching (Gao et al., 2021, arXiv:2101.06983) solves the same problem more efficiently by decoupling pool size from activation memory, and is the most direct path to widening the pool in a future version.

**Configuration**

| | |
|---|---|
| Initialized from | `snowflake-arctic-embed-l-v2.0` |
| Batch size | 8 |
| Negative pool | 32 passages (8 × 4 queued batches) |
| Learning rate | 1e-5 → 1e-6 |
| Warmup | 5% of total steps |

---

### Stage 2: Distill — Dense transfer via self-distillation

This stage moves what Stage 1 learned into the pooled single-vector representation the released model actually uses at inference. Batching, learning rate, and negative pool carry over unchanged; only the objective changes — the pooled vector becomes the thing being trained, and token-level scoring shifts from training target to teacher.

The first version optimized dense objectives alone, and the token loss began climbing partway through training: Stage 1's multi-vector ability was decaying under dense-only optimization. That matters because the distillation targets come from that same token-level scoring, so degrading it degrades the signal being distilled. The fix was to keep a small auxiliary hard-label loss on the token vectors — minor in weight next to the dense terms, and there only to anchor the representation distillation depends on. This is why the pipeline has three stages rather than two.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 630 318" role="img" font-family="ui-sans-serif, system-ui, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif">
  <title>Stage 2 self-distillation: three loss terms combined into one objective</title>
  <desc>A single encoder forward pass feeds two representations. A dense vector is produced by mean pooling, while the token vectors are left unpooled, one per token. Three loss terms follow: a hard-label loss on the dense vector, a distillation loss scoring the dense vector against soft targets from the token vectors, and a hard-label loss on the token vectors. The three are combined as a weighted average into one scalar total loss.</desc>

  <defs>
    <marker id="g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M1 1L9 5L1 9" fill="none" stroke="#8A8A80" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
    </marker>
    <marker id="c" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M1 1L9 5L1 9" fill="none" stroke="#C4553D" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
    </marker>
  </defs>

  <rect x="0" y="0" width="630" height="318" fill="#FAFAF7"/>

  <!-- encoder -->
  <rect x="18" y="80" width="105" height="160" rx="12" fill="#EFEFEA" stroke="#D2D2C8"/>
  <text x="70" y="152" text-anchor="middle" font-size="13" font-weight="600" fill="#1A1A18">encoder</text>
  <text x="70" y="170" text-anchor="middle" font-size="11" fill="#6B6B63">one pass</text>

  <path d="M125 160 H136" fill="none" stroke="#8A8A80" stroke-width="1.4"/>
  <path d="M136 160 V110 H146" fill="none" stroke="#8A8A80" stroke-width="1.4" marker-end="url(#g)"/>
  <path d="M136 160 V210 H146" fill="none" stroke="#8A8A80" stroke-width="1.4" marker-end="url(#g)"/>

  <!-- dense vector -->
  <rect x="150" y="80" width="140" height="60" rx="12" fill="#D9E9E5" stroke="#2E7D6F"/>
  <text x="220" y="104" text-anchor="middle" font-size="13" font-weight="600" fill="#173F38">dense vector</text>
  <text x="220" y="122" text-anchor="middle" font-size="11" fill="#3F6E64">mean pooled</text>

  <!-- token vectors -->
  <rect x="150" y="180" width="140" height="60" rx="12" fill="#E3DDEF" stroke="#6B4FA0"/>
  <text x="220" y="204" text-anchor="middle" font-size="13" font-weight="600" fill="#33254F">token vectors</text>
  <text x="220" y="222" text-anchor="middle" font-size="11" fill="#5A4A78">one per token</text>

  <!-- dense fan-out -->
  <path d="M292 110 H303" fill="none" stroke="#8A8A80" stroke-width="1.4"/>
  <path d="M303 110 V80 H313" fill="none" stroke="#8A8A80" stroke-width="1.4" marker-end="url(#g)"/>
  <path d="M303 110 V150 H313" fill="none" stroke="#8A8A80" stroke-width="1.4" marker-end="url(#g)"/>

  <!-- token fan-out -->
  <path d="M292 210 H303" fill="none" stroke="#8A8A80" stroke-width="1.4"/>
  <path d="M303 210 V240 H313" fill="none" stroke="#8A8A80" stroke-width="1.4" marker-end="url(#g)"/>
  <path d="M303 210 V170 H313" fill="none" stroke="#C4553D" stroke-width="1.6" marker-end="url(#c)"/>

  <!-- dense loss -->
  <rect x="317" y="50" width="150" height="60" rx="12" fill="#D9E9E5" stroke="#2E7D6F"/>
  <text x="392" y="74" text-anchor="middle" font-size="13" font-weight="600" fill="#173F38">dense loss</text>
  <text x="392" y="92" text-anchor="middle" font-size="11" fill="#3F6E64">hard labels</text>

  <!-- distillation loss -->
  <rect x="317" y="130" width="150" height="60" rx="12" fill="#F5DFD8" stroke="#C4553D"/>
  <text x="392" y="154" text-anchor="middle" font-size="13" font-weight="600" fill="#7A3527">distillation loss</text>
  <text x="392" y="172" text-anchor="middle" font-size="11" fill="#A8452F">soft targets</text>

  <!-- token loss -->
  <rect x="317" y="210" width="150" height="60" rx="12" fill="#E3DDEF" stroke="#6B4FA0"/>
  <text x="392" y="234" text-anchor="middle" font-size="13" font-weight="600" fill="#33254F">token loss</text>
  <text x="392" y="252" text-anchor="middle" font-size="11" fill="#5A4A78">hard labels</text>

  <!-- merge into total -->
  <path d="M469 80 H480 V160" fill="none" stroke="#8A8A80" stroke-width="1.4"/>
  <path d="M469 240 H480 V160" fill="none" stroke="#8A8A80" stroke-width="1.4"/>
  <path d="M469 160 H490" fill="none" stroke="#8A8A80" stroke-width="1.4" marker-end="url(#g)"/>
  <text x="553" y="121" text-anchor="middle" font-size="11" font-weight="600" fill="#6B6B63">weighted average</text>

  <!-- total loss -->
  <rect x="494" y="130" width="118" height="60" rx="12" fill="#2F2F2A" stroke="#2F2F2A"/>
  <text x="553" y="154" text-anchor="middle" font-size="13" font-weight="600" fill="#FAFAF7">total loss</text>
  <text x="553" y="172" text-anchor="middle" font-size="11" fill="#BFBFB4">one scalar</text>

  <text x="315" y="296" text-anchor="middle" font-size="11" fill="#6B6B63">The token loss keeps the representation that produces the soft targets from decaying.</text>
</svg>

**How the two representations work.** No separate teacher model is involved. A
single forward pass produces one set of hidden states, and two representations
are read off it — the **dense vector**, produced by mean pooling and scored by
dot product, and the **token vectors**, left unpooled and scored by the same
MaxSim as Stage 1. Both come from the same encoder in the same step, so the
model teaches itself.

Three terms combine as a weighted sum, dominated by the dense loss, with the
distillation and token terms carrying small auxiliary weights. The distillation
term supplies the dense vector with soft targets drawn from the token vectors'
score distribution, so the dense representation is pulled toward the ranking
that multi-vector scoring produces rather than only toward the correct answer.
Both representations receive gradient from that term, which makes it a
consistency constraint between the two rather than one-way transfer from a
frozen teacher.

**Configuration**

| | |
|---|---|
| Initialized from | Stage 1 checkpoint |
| Batch size | 8 |
| Negative pool | 32 passages (8 × 4 queued batches) |
| Learning rate | 1e-5 → 1e-6 |
| Warmup | 5% of total steps |

---

### Stage 3: Refine — Hard-negative fine-tuning

The sharpest break in the pipeline, aimed at top-of-ranking discrimination and at making the 512-dimension truncation a first-class output. Cumulative batching and in-batch negatives are dropped entirely; the learning rate drops an order of magnitude below where Stage 2 ended, warmup is omitted since the model arrives converged, validation runs twice as often, and the released weights come from the best checkpoint rather than the last. Each query is scored against its own positive and its own four mined hard negatives — a five-way softmax with no easy negatives — so every step is spent on distinctions the model is likely to get wrong, producing this model's profile: strong Accuracy@1 at some cost to recall further down the ranking. The loss is computed on the full 1024 dimensions and on the first 512, averaged with equal weight; this covers two widths only, and narrower truncations were never trained and should not be assumed to work.

Negatives were mined with `intfloat/multilingual-e5-large` against a relative threshold — the positive's own score sets the reference, candidates are admitted only below 99% of it, and the top 4 become that query's hard negatives. Anchoring to the positive keeps difficulty consistent where raw cosine scores vary widely across queries, while the 1% margin drops false negatives, which are usually relevant passages themselves.

**Configuration**

| | |
|---|---|
| Initialized from | Stage 2 checkpoint |
| Batch size | 8 |
| Negatives per query | 4 mined hard negatives, no in-batch negatives |
| Learning rate | 1e-6 → 1e-7 |
| Warmup | None |

---

### Data and augmentation

Roughly 500,000 query–passage pairs from multiple sources, including AI Hub.

Because a growing share of retrieval corpora is LLM-generated and Markdown-formatted, part of the training data was converted into Markdown-style passages. Three augmentations were applied, each targeting a different failure mode:

| Augmentation | Targets |
|---|---|
| Pair concatenation | Multi-part queries and multi-passage contexts |
| Language transfer (ko ↔ en) | Cross-lingual retrieval |
| Style transfer (plain → Markdown) | Structured, LLM-generated passages |

Augmentation was performed with **Gemma-3-12B**.

---

## Evaluation

### Setup

Five dataset groups:

- **3 groups** — subsets extracted from AI Hub datasets
- **1 group** — synthetic queries paired with **Markdown-style passages**, generated by GPT-4o-mini from a sports regulation PDF
- **1 group** — a concatenation of the four groups above, as a mixed-domain set

**Train/eval separation.** Evaluation sets were split off from their source groups before training and were never seen during any of the three stages. Although AI Hub appears in both the training corpus and the evaluation groups, the specific query–passage pairs used for evaluation were held out and excluded from training.

Each query has a single correct passage, so Accuracy@k here is equivalent to Hit Rate@k. Reported numbers are the average across all five groups.

> The mixed group is a concatenation of the other four, so it is not statistically independent of them. The five-group average consequently weights the first four groups twice. Read the average as an aggregate summary rather than as five independent measurements.

### Results

| Architecture | Open/Closed | Acc@1 | Acc@3 | Acc@5 | Acc@10 |
|---|---|---|---|---|---|
| **FronyAI/frony-embed-arctic-ko-0.6B-v2.5** | Open | **0.6942** | 0.8361 | 0.8807 | 0.9197 |
| **FronyAI/frony-embed-arctic-ko-0.6B-v2.5 (half dim)** | Open | **0.6778** | 0.8277 | 0.8726 | 0.9129 |
| dragonkue/snowflake-arctic-embed-l-v2.0-ko | Open | 0.6612 | 0.8396 | 0.8931 | 0.9390 |
| nlpai-lab/KURE-v1 | Open | 0.6434 | 0.8240 | 0.8788 | 0.9285 |
| upstage-large | Closed | 0.6323 | 0.8522 | 0.9068 | 0.9459 |
| BAAI/bge-m3 | Open | 0.5849 | 0.7763 | 0.8420 | 0.8985 |
| intfloat/multilingual-e5-large | Open | 0.5764 | 0.7630 | 0.8267 | 0.8891 |
| Snowflake/snowflake-arctic-embed-l-v2.0 | Open | 0.5726 | 0.7591 | 0.8232 | 0.8917 |
| jinaai/jina-embeddings-v3 | Open | 0.5270 | 0.7242 | 0.7953 | 0.8644 |
| openai-text-embedding-3-large | Closed | 0.4903 | 0.6621 | 0.7316 | 0.8149 |

### On public benchmarks

No public benchmark scores are reported here, and this is a deliberate choice rather than an omission.

The training corpus was assembled from a broad mix of Korean sources, and we cannot currently rule out overlap with the evaluation splits of common public benchmarks. Reporting numbers under those conditions would produce scores that look strong for the wrong reason. We would rather publish an internal evaluation we can vouch for than a public one we can't.

Auditing the training corpus for benchmark contamination is planned. Public results will be added once the training set can be certified clean against the specific benchmarks reported — not before.

In the meantime, treat the table above as a comparison conducted under consistent conditions across all listed models, and validate on your own data before committing to any of them.

---

## References

The three-stage pipeline was assembled from ideas in the following work. Each
entry notes what was taken from it.

**Multi-stage pipeline structure**

- LG AI Research (2025). *EXAONE 4.0: Unified Large Language Models Integrating
  Non-reasoning and Reasoning Modes.* arXiv:2507.11407 — the shape of a
  sequential pipeline where each stage initializes from the previous checkpoint
  with a different objective.

**Token-level similarity (Stages 1 and 2)**

- Khattab, O., Zaharia, M. (2020). *ColBERT: Efficient and Effective Passage
  Search via Contextualized Late Interaction over BERT.* SIGIR 2020.
  arXiv:2004.12832 — the MaxSim late-interaction score.

**Self-distillation (Stage 2)**

- Chen, J., Xiao, S., Zhang, P., Luo, K., Lian, D., Liu, Z. (2024).
  *BGE M3-Embedding: Multi-Lingual, Multi-Functionality, Multi-Granularity Text
  Embeddings Through Self-Knowledge Distillation.* arXiv:2402.03216 — the idea
  of using one retrieval functionality's relevance scores as the teacher signal
  for another, within a single model. Stage 2 applies this between the token and
  dense representations.

**Hard-negative mining and training parameters (Stage 3)**

- Yu, P., Merrick, L., Nuti, G., Campos, D. (2024). *Arctic-Embed 2.0:
  Multilingual Retrieval Without Compromise.* arXiv:2412.04506 — hard-negative
  mining with a tuned false-positive cutoff, and much of the training
  configuration. This is also the base model for this work.

**Matryoshka objective (Stage 3)**

- Kusupati, A., et al. (2022). *Matryoshka Representation Learning.* NeurIPS 2022. arXiv:2205.13147 — the nested-dimension training objective.

**Contrastive objective (all stages)**

- van den Oord, A., Li, Y., Vinyals, O. (2018). *Representation Learning with
  Contrastive Predictive Coding.* arXiv:1807.03748 — the InfoNCE loss.

---

### Models and tools used

- `Snowflake/snowflake-arctic-embed-l-v2.0` — base model (cited above).
- `intfloat/multilingual-e5-large` — teacher model for hard-negative mining in
  Stage 3. Wang, L., Yang, N., Huang, X., Yang, L., Majumder, R., Wei, F.
  (2024). *Multilingual E5 Text Embeddings: A Technical Report.* arXiv:2402.05672
- `google/gemma-3-12b-it` — data augmentation (pair concatenation, ko↔en language
  transfer, plain→Markdown style transfer). Subject to the Gemma Terms of Use.
- `gpt-4o-mini` — synthetic evaluation queries for one of the five evaluation
  groups. Not used to generate training data.
- `bitsandbytes` — 8-bit Adam. Dettmers, T., Lewis, M., Shleifer, S.,
  Zettlemoyer, L. (2022). *8-bit Optimizers via Block-wise Quantization.*
  ICLR 2022. arXiv:2110.02861
- `sentence-transformers` — packaging and inference. Reimers, N., Gurevych, I.
  (2019). *Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks.*
  EMNLP 2019. arXiv:1908.10084
- `PyTorch Lightning` — training framework.

## License and attribution

**Model weights** are released under **Apache-2.0**.

**Training data.** The training corpus includes datasets from AI Hub, operated by the National Information Society Agency (한국지능정보사회진흥원, NIA) under the Ministry of Science and ICT. Per AI Hub's usage policy, this work is acknowledged as follows:

> 본 모델의 학습에는 과학기술정보통신부와 한국지능정보사회진흥원의 「지능정보산업 인프라 조성」 사업의 일환으로 구축된 AI 허브 데이터가 활용되었습니다.
>
> This model was trained in part on AI Hub datasets constructed under the Intelligent Information Industry Infrastructure Development project of the Ministry of Science and ICT and the National Information Society Agency (NIA), Republic of Korea.

Note the following, which concern the **underlying data** rather than these weights:

- AI Hub data may be used for research and development, commercial and non-commercial alike. However, **selling the datasets or other direct commercial use of the data requires separate agreement with the constructing institution.**
- **No AI Hub data is redistributed in this repository.** Only trained model weights are published.
- Rights to AI Hub data remain with the constructing and participating institutions and NIA. The Apache-2.0 license on these weights does not grant any rights to that data.
- **Organizations and individuals located outside Korea** require separate agreement with the constructing institution and NIA to use AI Hub data, and **transferring the data abroad** requires separate agreement as well. These conditions apply to the data itself; if your use case involves obtaining or handling AI Hub data, review them directly.

This summary is provided for convenience and is not legal advice. Verify current terms at the [AI Hub usage policy](https://aihub.or.kr/intrcn/guid/usagepolicy.do), and consult your own counsel for deployments where the answer matters.

<!-- TODO (optional): if any training source carries terms stricter than AI Hub's open-data
     policy — KETI, competition datasets, or other research-only releases are non-commercial —
     list it here. Enterprise users check this section before anything else. -->

## Contact

Open an issue or pull request with questions or suggestions, or email **flash659@gmail.com**.