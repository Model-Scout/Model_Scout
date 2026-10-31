---
language:
  - ko
license: other
task_categories:
  - image-to-text
  - sentence-similarity
pretty_name: Korean Visual Document Retrieval (VDR) Hard Negatives
size_categories:
  - 100K<n<1M
tags:
  - multimodal
  - retrieval
  - visual-document-retrieval
  - korean
  - hard-negative-mining
  - qwen3-vl
extra_gated_prompt: >-
  By requesting access you agree to use this dataset strictly for research
  purposes and to respect the licenses of the constituent image sources
  (ko-vdr-train-public-v2.0 / ko-vdr-train-private-v0.1). Redistribution of the
  underlying images is not permitted without contacting the original authors.
extra_gated_fields:
  Name: text
  Affiliation: text
  Intended use case: text
  I will use this dataset for research only: checkbox
configs:
  - config_name: corpus
    data_files:
      - split: train
        path: corpus/train-*
  - config_name: naive
    data_files:
      - split: train
        path: naive/train-*
  - config_name: shifted_by_n
    data_files:
      - split: train
        path: shifted_by_n/train-*
  - config_name: marginpos
    data_files:
      - split: train
        path: marginpos/train-*
  - config_name: percpos
    data_files:
      - split: train
        path: percpos/train-*
  - config_name: ko-vdr-train-public-v2.0_reranked_stratified
    data_files:
      - split: train
        path: ko-vdr-train-public-v2.0_reranked_stratified/train-*
  - config_name: ko-vdr-train-public-v2.0_reranked_hardest
    data_files:
      - split: train
        path: ko-vdr-train-public-v2.0_reranked_hardest/train-*
  - config_name: distill_stratified
    data_files:
      - split: train
        path: distill_stratified/train-*
  - config_name: distill_hardest
    data_files:
      - split: train
        path: distill_hardest/train-*
  - config_name: ensembledistill_stratified
    data_files:
      - split: train
        path: ensembledistill_stratified/train-*
  - config_name: ensembledistill_hardest
    data_files:
      - split: train
        path: ensembledistill_hardest/train-*
---

# Korean Visual Document Retrieval (VDR) Hard Negatives

Multimodal retrieval training set used to fine-tune visual-document retrieval
embedding models on Korean document pages: the query is text, the document is a
page image, and each mining row ships 1 positive + mined hard negatives.

Hard negatives were mined with `Qwen/Qwen3-VL-Embedding-8B`. Mining was performed
within each source dataset, and positives sharing the same query within the same
source dataset were excluded from the negative candidates.

## Structure

The repo groups its configs into an image store, the embedding-mined hard
negatives, and reranker-scored sets used for knowledge distillation.

**Image store**

| config   | rows   | description                                             |
|----------|--------|---------------------------------------------------------|
| `corpus` | 35,815 | deduplicated image store, one row per unique page image |

**Embedding-mined hard negatives** — 1 positive + 7 negatives, mined within each source dataset

| config         | rows    | description                                                        |
|----------------|---------|--------------------------------------------------------------------|
| `naive`        | 411,423 | Top-K hard negatives                                               |
| `shifted_by_n` | 411,423 | Top-K shifted by N hard negatives, with N=5                        |
| `marginpos`    | 397,534 | Top-K MarginPos hard negatives, with margin=0.05                   |
| `percpos`      | 406,945 | Top-K PercPos hard negatives, with threshold=95% of positive score |

**Reranker-scored (teacher distillation)** — 1 positive + 8 negatives, plus a per-candidate `label` score

| config                                         | rows    | corpus         | `label`                                    |
|------------------------------------------------|---------|----------------|--------------------------------------------|
| `ko-vdr-train-public-v2.0_reranked_stratified` | 146,687 | public         | reranker score (existing; public-only)     |
| `ko-vdr-train-public-v2.0_reranked_hardest`    | 146,687 | public         | reranker score (existing; public-only)     |
| `distill_stratified`                           | 265,311 | public+private | raw reranker log-odds                      |
| `distill_hardest`                              | 265,311 | public+private | raw reranker log-odds                      |
| `ensembledistill_stratified`                   | 265,311 | public+private | reranker × embedding ensemble, in [0, 1]   |
| `ensembledistill_hardest`                      | 265,311 | public+private | reranker × embedding ensemble, in [0, 1]   |

Splitting `corpus` from the mining/distillation configs keeps the image pool
stored once on Hub instead of being re-embedded on every training row.

### `corpus` schema

| column   | type    | example                                                   |
|----------|---------|-----------------------------------------------------------|
| image_id | string  | `ko-vdr-public/3818.png`                                  |
| source   | string  | `ko-vdr-train-public-v2.0` \| `ko-vdr-train-private-v0.1` |
| image    | Image() | PIL image (lazy-decoded on access)                        |

### Mining config schema (`naive`, `shifted_by_n`, `marginpos`, `percpos`)

| column        | type   | example                                    |
|---------------|--------|--------------------------------------------|
| anchor        | string | `30인 이상 상용근로자를 보유한 기업의 ...` |
| positive_id   | string | `ko-vdr-public/3818.png`                   |
| negative_1_id | string | `ko-vdr-public/7753.png`                   |
| ... up to     |        |                                            |
| negative_7_id | string | `ko-vdr-public/2185.png`                   |

### Distillation config schema (`distill_*`, `ensembledistill_*`)

| column        | type          | example                                         |
|---------------|---------------|-------------------------------------------------|
| anchor        | string        | `100년 재현빈도 설계기준 강화와 ...`            |
| positive_id   | string        | `ko-vdr-public/7130.png`                        |
| negative_1_id | string        | `ko-vdr-public/791.png`                         |
| ... up to     |               |                                                 |
| negative_8_id | string        | `ko-vdr-private/b9113c366a.png`                 |
| label         | list[float]   | `[positive, neg_1, ..., neg_8]` (length 9)      |

## Access

This is a **gated dataset**. Request access via the dataset page and briefly
describe your intended use case.

Once approved:

```bash
huggingface-cli login
```

## Usage

### Mining method options

Choose one mining config as `method`:

| method         | use when you want...                                       |
|----------------|------------------------------------------------------------|
| `naive`        | the top seven valid retrieved negatives                    |
| `shifted_by_n` | slightly easier negatives by skipping the top N candidates |
| `marginpos`    | negatives filtered by an absolute positive-score margin    |
| `percpos`      | negatives filtered by a percentage of the positive score   |

```python
method = "naive"  # one of: naive, shifted_by_n, marginpos, percpos
```

### Option A - Rehydrate to a local image directory (recommended for training)

Download the corpus once, unpack every image to disk using its `image_id` as the
relative path. This gives back the same directory structure used during mining,
so existing pipelines that expect path strings work unchanged.

```python
from pathlib import Path
from datasets import load_dataset

repo_id = "whybe-choi/ko-vdr-hn"
OUT_IMG_DIR = Path("./ko_vdr_images")

corpus = load_dataset(repo_id, name="corpus", split="train")
for row in corpus:
    dst = OUT_IMG_DIR / row["image_id"]
    if dst.exists():
        continue
    dst.parent.mkdir(parents=True, exist_ok=True)
    row["image"].save(dst)
```

Then fold the IDs back into absolute paths for your trainer / collator:

```python
from datasets import load_dataset

repo_id = "whybe-choi/ko-vdr-hn"
method = "naive"  # one of: naive, shifted_by_n, marginpos, percpos

train = load_dataset(repo_id, name=method, split="train")

def resolve(row):
    row["positive"] = str(OUT_IMG_DIR / row.pop("positive_id"))
    for i in range(1, 8):
        neg_id = row.pop(f"negative_{i}_id")
        row[f"negative_{i}"] = str(OUT_IMG_DIR / neg_id) if neg_id is not None else None
    return row

train = train.map(resolve)
# schema now matches the original local layout:
#   anchor, positive, negative_1, ..., negative_7  (all strings; image cols are paths)
```

### Option B - Lazy lookup at dataloader time (no image extraction)

Keep images inside the HF `corpus` dataset and resolve IDs -> PIL images on
demand. Good when you train from a single machine and don't want to manage a
separate image dir, but slower than path-based loading because every access
decodes the bytes stream.

```python
from datasets import load_dataset

repo_id = "whybe-choi/ko-vdr-hn"
method = "naive"  # one of: naive, shifted_by_n, marginpos, percpos

corpus = load_dataset(repo_id, name="corpus", split="train")
id2idx = {cid: i for i, cid in enumerate(corpus["image_id"])}

train = load_dataset(repo_id, name=method, split="train")

def resolve(batch):
    batch["positive"] = [corpus[id2idx[i]]["image"] for i in batch["positive_id"]]
    for k in range(1, 8):
        key = f"negative_{k}_id"
        batch[f"negative_{k}"] = [
            corpus[id2idx[i]]["image"] if i is not None else None
            for i in batch[key]
        ]
    return batch

train.set_transform(resolve)  # lazy; decodes only the rows a dataloader pulls
```

### Training with `sentence-transformers` (contrastive learning)

After rehydrating via **Option A**, each mining config can be used with a
multi-negative ranking setup:

```python
from sentence_transformers import SentenceTransformer, losses

model = SentenceTransformer("Qwen/Qwen3-VL-Embedding-2B")

loss = losses.CachedMultipleNegativesRankingLoss(
    model=model,
    scale=20.0,
    mini_batch_size=4,
)
```

The column order matters: the first column (`anchor`) is treated as the query,
the second (`positive`) as the paired positive, and the rest
(`negative_1`...`negative_7`) as hard negatives for in-batch + triplet loss.

### Training with `sentence-transformers` (knowledge distillation)

The `distill_*` and `ensembledistill_*` configs additionally carry a `label`
column so they can be trained with a knowledge-distillation objective
instead of, or alongside, a contrastive loss. This matches the expected format of
`sentence-transformers`' distillation losses exactly:
`(anchor, positive, negative_1..8)` texts + a `label` list of teacher scores.

```python
from sentence_transformers import SentenceTransformer, losses

model = SentenceTransformer("Qwen/Qwen3-VL-Embedding-2B")

# KL divergence between the student and teacher score distributions (recommended)
loss = losses.DistillKLDivLoss(model, temperature=1.0)

# alternative: pairwise margin MSE against the teacher margins
# loss = losses.MarginMSELoss(model)
```

Rehydrate images via **Option A**, but keep the `label` column and extend the
negative loop to `negative_1..8`:

```python
def resolve(row):
    row["positive"] = str(OUT_IMG_DIR / row.pop("positive_id"))
    for i in range(1, 9):                       # 8 negatives
        row[f"negative_{i}"] = str(OUT_IMG_DIR / row.pop(f"negative_{i}_id"))
    return row                                  # `label` is left untouched

train = load_dataset(repo_id, name="distill_stratified", split="train").map(resolve)
# columns: anchor, positive, negative_1..8, label
```

`DistillKLDivLoss` applies a softmax over the teacher scores internally, so both
the raw log-odds (`distill_*`) and the normalized ensemble scores
(`ensembledistill_*`) work directly; raise `temperature` to soften the target
distribution.

## Mining details

For each query-positive pair, hard negatives were selected by embedding the query
and candidate document images, then retrieving visually and semantically similar
images within the same source dataset.

For each query, all known positives in the same source dataset were excluded from
the candidate negatives.

- `naive`: uses the top seven remaining retrieved documents as `negative_1_id` through `negative_7_id`.
- `shifted_by_n`: skips the top N remaining candidates, then uses the next seven retrieved documents. The current configuration uses N=5.
- `marginpos`: keeps candidates with `negative_score < positive_score - margin`, then uses the top seven. The current margin is 0.05.
- `percpos`: keeps candidates with `negative_score <= positive_score * threshold`, then uses the top seven. The current threshold is 0.95.

All mining-method configs are derived from the same retrieved candidate lists for
each query-positive pair. Rows are kept only when all seven hard negatives are
available for the corresponding method.

Following the Positive Refinement step described in the
`Qwen/Qwen3-VL-Embedding` paper, each query is retained only if at least one of
its positive documents achieves a score above the positive-score threshold. This
dataset uses `positive_score > 0.3` as the retention criterion; queries whose
positive documents all score `<= 0.3` are discarded. The threshold was set to
`0.3` after inspecting the positive score distribution below and manually
reviewing randomly sampled examples for false negatives.

![ko_positive_score_distribution](https://cdn-uploads.huggingface.co/production/uploads/655eeb5532537bcc8d7460ab/AK6BdyAyvCUybzfjQGWez.png)

Positive Refinement removed the following queries and rows:

| config         | rows before | removed queries | removed rows | rows after |
|----------------|------------:|----------------:|-------------:|-----------:|
| `naive`        | 428,850     | 15,194          | 17,427       | 411,423    |
| `shifted_by_n` | 428,850     | 15,194          | 17,427       | 411,423    |
| `marginpos`    | 403,362     | 4,734           | 5,828        | 397,534    |
| `percpos`      | 416,304     | 7,667           | 9,359        | 406,945    |

Diagnostic columns such as `positive_score` are produced during mining and used
for Positive Refinement, but are not included in the uploaded mining-method
configs.

## Reranker-distillation configs (`distill_*`, `ensembledistill_*`)

These four configs add **teacher scores for knowledge distillation**. Unlike the
embedding-mined configs above (mined within each source), their hard negatives
are mined over the **combined public + private corpus**, so negatives are
cross-source (a public query can receive private negatives and vice versa).

### How the scores were produced

1. **Candidate mining.** For each query, a 32-candidate pool is built from the
   combined corpus with `Qwen/Qwen3-VL-Embedding-8B` (bf16, FlashAttention-2,
   `min_pixels=4096`, `max_pixels=1310720`): the **top-16** most similar images
   (embedding-hard) plus **16 uniformly random** images from the rest of the
   corpus. Positives of the same query are excluded from the candidates.
2. **Teacher scoring.** `Qwen/Qwen3-VL-Reranker-8B` (bf16, FlashAttention-2, same
   pixel budget) scores the positive and all 32 negatives. The score is the
   **raw log-odds** `logit("yes") - logit("no")` taken with an identity activation
   (no sigmoid), so values are unnormalized and negatives are common.
3. **Embedding score (`ensembledistill_*` only).** Cosine similarity
   `cos(query, doc)` from `Qwen/Qwen3-VL-Embedding-8B` for the positive and all 32
   negatives.
4. **Ensemble (`ensembledistill_*` only).** Per query, min-max scale the reranker
   log-odds and the embedding cosines **separately over all 33 items** (positive +
   32 negatives) to `[0, 1]`, then average:
   `score = ( minmax(reranker) + minmax(embedding) ) / 2`.
5. **Selection (K = 8).** From the 32 negatives, keep 8, ordered hardest -> easiest:
   - `*_stratified` — using the per-query min-max score, take 8 quantile anchors at
     evenly-spaced cumulative probabilities `p_j = (j-1)/(K-1)` for `j = 1..8`, and
     pick the distinct negative closest to each anchor. This spreads the kept
     negatives across the full difficulty range, following
     [arXiv:2604.04734](https://arxiv.org/abs/2604.04734).
   - `*_hardest` — simply the top-8 negatives by score.

The `distill_*` configs stop after step 2 (reranker only); the `ensembledistill_*`
configs use the step-4 ensemble score for both selection and the stored `label`.

**`label` semantics**

- `distill_stratified`, `distill_hardest` — **raw reranker log-odds**
  (unnormalized; negative values are expected; positive is the highest). Values
  reflect the bf16 teacher forward.
- `ensembledistill_stratified`, `ensembledistill_hardest` — **normalized ensemble
  score in [0, 1]** (the score used for selection).

`label` is a length-9 list aligned to `[positive_id, negative_1_id, ...,
negative_8_id]`. These configs reuse the same `corpus` image store, so Option A /
Option B above work unchanged (extend the negative range to `1..9`).

## Sources and licensing

Images come from two Korean VDR training sources with different provenances:

| source                      | files  | notes                            |
|-----------------------------|--------|----------------------------------|
| [ko-vdr-train-public-v2.0](https://huggingface.co/datasets/NomaDamas/ko-vdr-train-public)  | 7,548  | Korean VDR public training data  |
| [ko-vdr-train-private-v0.1](https://huggingface.co/datasets/whybe-choi/ko-vdr-train-private-v0.1) | 28,267 | Korean VDR private training data |

Because of the mixed licensing, this repo is gated and must not be re-uploaded
or redistributed. Cite the upstream Korean VDR sources if you use this dataset
in published work.

## Citation

If this dataset is useful for your work, please cite the upstream Korean VDR
sources, and mention this repo as the hard-negative mining pipeline source.

```bibtex
@article{choi2026kovre,
  title={KoVRE: Training an Efficient Embedding Model for Korean Visual Document Retrieval},
  author={Choi, Yongbin and Shim, Gyuho and Jang, Youngjoon},
  journal={arXiv preprint arXiv:2608.01389},
  year={2026}
}
```
