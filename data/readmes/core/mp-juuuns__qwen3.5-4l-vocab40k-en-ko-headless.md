---
license: apache-2.0
base_model: Qwen/Qwen3.5-0.8B
base_model_relation: finetune
pipeline_tag: feature-extraction
library_name: transformers
datasets:
  - Salesforce/wikitext
language:
  - en
  - ko
tags:
  - qwen3.5
  - backbone
  - headless
  - classification-backbone
  - feature-extraction
  - knowledge-distillation
  - model-compression
  - vocabulary-pruning
  - korean
  - edge-ai
---

# Qwen3.5 4L Headless Backbone (40k EN/KO)

A **headless four-layer text backbone** distilled from Qwen3.5-0.8B, with a vocabulary cut to
English and Korean. It has no language-model head, no classification head, no labels and no
thresholds. You attach a head and train it.

*Korean translation of this page: [`README_KO.md`](README_KO.md).*

This card is the record of how it was made. It walks the whole path — prompting the original
model, turning it into a classifier, removing layers, changing precision, cutting the
vocabulary, and cutting it again by rule — and shows what each step measured. We are not
arguing that this model is better than anything. We built it, we measured it beside other
models, and where we have a guess about why a number moved we say it is a guess.

| | |
|---|---|
| **Root model** | 4 layers, hidden 1024, **39,866** vocabulary entries |
| **Parameters** | 120,639,808 |
| **BF16 weights** | 241,285,160 bytes (230.1 MiB) |
| **Q8_0 GGUF** | 124 MiB |
| **Head** | none — `score.weight` is absent |
| **Upstream** | [`Qwen/Qwen3.5-0.8B`](https://huggingface.co/Qwen/Qwen3.5-0.8B), 24 layers, 248,320 rows |
| **Distillation data** | 4,096 unlabeled WikiText-103 rows, no task labels |
| **Language scope** | English and Korean. Han characters fall back to byte tokens. |

> **The root changed on 2026-09-20.** It used to be a 128,000-entry, 210.9M-parameter,
> 402.29 MiB model. Everything in this card that is labelled "128k" describes that previous
> root, which remains available at the git revision before that commit. What you download today
> is the 39,866-entry model in the table above. Sections 5 and 6 explain why it changed.
>
> **The repository was also renamed on 2026-09-20**, from
> `qwen35-standalone4l-classification-base` to `qwen3.5-4l-vocab40k-en-ko-headless`. The old URL
> redirects, but `from_pretrained` on the old id is reported not to follow that redirect, so pinned
> code should be updated. The old id now holds a weightless stub pointing here. `vocab40k` rounds
> the 39,866 entries; the three unpublished grid siblings would be `vocab15k`, `vocab24k` and
> `vocab72k`.

---

## How it compares

Every arm below was trained, calibrated and profiled under one frozen protocol on one split, so
the columns are like-for-like. There are 65 of them: 46 encoder arms across ten families, 15
earlier Qwen arms, and the four task-blind vocabulary grid arms, of which this root is one.

![the root on every metric](benchmark/figures/10_root_on_every_metric.png)

| metric | this root | rank | best in the field | field median |
|---|---:|---:|---:|---:|
| macro F1 (3 seeds) | **0.5721 ± 0.0087** | **3 / 65** | 0.5781 | 0.5121 |
| document p50 | 30.4 ms | **52 / 65** | 5.7 ms | 11.2 ms |
| peak process-tree RSS | 1,937 MiB | 40 / 65 | 1,601 MiB | 1,880 MiB |
| BF16 weight file | 230 MiB | 31 / 65 | 22 MiB | 238 MiB |
| GPU joules per document | 5.01 | **52 / 65** | 0.81 | 2.14 |

Read together: it is at the top on quality and in the bottom third on time and energy. Nothing in
the measurement resolves the top of the quality column — six arms sit within one median seed SD
(0.0117) of the best, and this root is one of them, so its third place is a tie, not a win. The
cost columns are not a tie: the fastest arm in the field answers a document in 5.7 ms against this
root's 30.4 ms, and spends 0.81 J against 5.01 J.

Inside that six-arm tie the comparison is narrower and more favourable. `roberta-base` reaches
0.5524 at 11.1 ms and 238 MiB; the best encoder is cheaper on every cost axis and 0.020 lower on
quality, against SDs of 0.0143 and 0.0087. Among the tied arms, `qwen35-taskfree-base8l-v248k`
matches the quality at 73.8 ms, 802 MiB and 11.31 J — this root reaches the same band at 30.4 ms,
230 MiB and 5.01 J.

*Our reading:* this is a 262,144-position decoder stack being used to read 256-token windows, and
most of the arms it loses to on time are encoders built for exactly that shape. We think the
architecture is what costs the time, not the vocabulary cut or the depth — but we have not isolated
that, so it stays a guess. What the cut and the depth did move is the file and the energy, and
those are visible in the panels above.

---

## Run it in a container

Two stacks, both CPU-only, both with the dedicated no-KV runtime compiled inside the image and
nothing fetched at run time.

**[`docker/`](docker/) — see it work now.**

```bash
tar -xzf bundle/runtime_source.tar.gz -C bundle/
docker compose up --build        # then http://127.0.0.1:8787
```

Be clear about what is in it: **not this root**, but this root's backbone carrying a 14-label
SemEval-2020 Task 11 head — the same 39,866-entry tokenizer, byte-identical in vocabulary, merges
and added tokens. It is a worked example of what the root becomes once a head is attached, not a
model to judge real documents with. Measured there: attention KV allocation 0 MiB, native RSS
173 MiB, 56.4 ms of compute on a 28-token window, 4 threads.

**[`docker-train/`](docker-train/) — the same idea with your own labels.** Your data in, a Q8
classifier and a serving container out.

```bash
python make_base.py                      # assembles base/ from this repository's own weights
tar -xzf vendor/runtime_source.tar.gz -C vendor/
docker compose run --rm validate && docker compose run --rm train-cpu
docker compose run --rm export && docker compose up model
```

On the four bundled example documents that runs in a couple of minutes and ends at
`"Please refund this purchase and return the order."` → `refund` 0.999 and
`"배송 상태를 알려주세요."` → `shipping` 0.998, because the vocabulary keeps every Hangul-carrying
token. Every export checks its own specialised-versus-generic output parity; on that run it was
0.0 on logits, 0.0 on probabilities and zero label disagreements.

Neither container runs the published root as it stands — the root is headless, so both work with a
head attached on top of it.

---

## Usage

```python
from transformers import AutoModel, AutoTokenizer

model_id = "mp-juuuns/qwen3.5-4l-vocab40k-en-ko-headless"
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=False)
backbone  = AutoModel.from_pretrained(model_id, trust_remote_code=False)
```

The weight file contains no `score.weight`. Outputs are hidden states; they have no class
meaning until you train a head.

### Check the tokenizer against your text first

The vocabulary is cut, so token counts differ from the upstream model, and they differ unevenly
by language. Measured on one sentence each:

| | upstream 248k | this root | ratio |
|---|---:|---:|---:|
| English | 9 | 12 | 1.33x |
| Korean | 16 | 16 | **1.00x** |
| Chinese | 8 | 58 | **7.25x** |
| Japanese | 10 | 44 | **4.40x** |

Korean is unchanged because the cut rule keeps every Hangul-carrying token regardless of its id.
Every Han token in the upstream vocabulary sits above id 65,536 and none survives, so Chinese
and Japanese encode as bytes. Compute scales with token count, so if your text is CJK this is
not the right root for you.

![what the cut costs per language](benchmark/figures/09_tokenizer_cost.png)

```python
len(tokenizer("a representative document from your data")["input_ids"])
```

### Train a head

```bash
git clone https://huggingface.co/mp-juuuns/qwen3.5-4l-vocab40k-en-ko-headless
cd qwen3.5-4l-vocab40k-en-ko-headless/distillation
python -m pip install -e .

qwen35-distill finetune \
  --checkpoint .. \
  --train examples/multilabel_train.jsonl \
  --labels examples/labels.json \
  --mode multilabel \
  --output my-classifier-4l
```

The packaged platform has six commands — `validate-dataset`, `extract-text`, `materialize`,
`materialize-classifier`, `finalize-base`, `distill` — and **none of them cuts a vocabulary**.
Running the ladder from the upstream teacher reproduces the depth reduction and gives you a
four-layer model with the full 248,320-row embedding, which is a different artifact from this
root. If you want this vocabulary, start from this root.

---

## Architecture

```
Qwen3.5-0.8B, 24 layers                 upstream
  └─ 24→8  knowledge distillation       layers (0,4,6,11,13,16,20,23)
       └─ 8→6                           layers (0,1,3,4,6,7)
            └─ 6→4                      layers (0,2,3,5)
                 └─ vocabulary cut      248,320 → 39,866 rows
                      └─ this root      4L · hidden 1024 · headless
```

| | |
|---|---|
| Layer types | `linear_attention → full_attention → linear_attention → full_attention` |
| Hidden / FFN | 1,024 / 3,584 |
| Runtime class | `Qwen3_5TextModel`, Transformers 5.13.0 |
| Distillation objective | hidden-state and interface representation matching; no logit KD, no cross-entropy, no labels |
| Recurrent scalars | 192 frozen during KD; the remaining parameters trained |

**How the layer maps were chosen, stated plainly.** They were selected by ranking candidate maps
on labeled SemEval-2020 Task 11 data — the 6→4 map is rank 1 of all fifteen four-of-six
candidates by train macro F1. Older `config.json` files in this repository record
`selection_basis: "predeclared_architecture_only_default"`, which is wrong; the current root
records `semeval_ranked_inherited`. Because the distillation boundary targets are a function of
the map, that choice is in the weights. Cutting the vocabulary does not remove it.

---

## The path, step by step

Everything below is measured. Each section is a **situation we assumed**, and it names the data
and hardware we used to set that situation up. We were not building for a particular task, so we
did not hold one dataset fixed across the whole path: section 1 assumes an edge board answering
short documents and uses a 3-class internal set for it; sections 2 onward assume a desktop GPU
doing multi-label document work and use a 14-label SemEval-derived set. Read each section as its
own scenario — the arms inside it share data, protocol and host, which is what makes the
comparison inside it mean something.

![the whole path in one picture](benchmark/figures/06_stage_path.png)

### 1. Prompting the original model

**Situation assumed:** an edge board classifying short documents under a hard memory ceiling.
**The data we used for it:** legacy37, 3 classes, 37 documents, internal labels, not human gold.
**Hardware:** UNO Q edge board. **Measured 2026-07-15.**

| arm | accuracy | macro F1 | artifact | one document | memory |
|---|---:|---:|---:|---:|---|
| **P0** prompt, Q4_0 generation | 62.16% | **0.2556** | 507.2 MB | warm p50 8.57 s | ≥2.441 GiB, **OOM at request 31** |
| **C24** 24L backbone + 3-logit head, Q6_K | 94.59% | 0.9571 | 629.7 MB | cold 21.32 s | 1,454.7 MiB |
| **C8Q** 8L distilled + head, F16/Q6_K | 97.30% | 0.9781 | 395.3 MB | cold 11.60 s | 1,192.0 MiB |

P0 returned a valid label for all 37 documents and returned `scam_attempt` for all 37 of them.
That is a class collapse, not a low score spread over classes: the set is 23 `scam_attempt` /
11 `normal` / 3 `scam_news_edu`, so 62.16% is exactly the majority-class rate. P0 also hit the
2.441 GiB cgroup limit after 31 consecutive requests and took the production runner down with it.

C8Q against C24 on the same runtime: 37-row wall 421.24 s → 145.07 s, cold-one 21.32 s → 11.60 s.
The paired bootstrap interval on the quality difference includes zero, so we read it as quality
not collapsing under the compression rather than as an accuracy win.

*What the numbers are measured at:* P0's memory is a container cgroup including the router and
model server; the classifier numbers are a single foreground process peak. The classifier
per-row wall is an amortized batch including model load, not a persistent HTTP p50. Different
layers, so read the memory column as “what the board had to hold,” not as a like-for-like delta.

*Our reading:* generation costs a system prompt and a decode loop per request, and in this
situation that was the binding constraint before accuracy ever was. Everything after this
section is a classifier.

### 2. As a classifier: 24 layers, 248k vocabulary

**Situation assumed:** a desktop GPU assigning many labels to long documents. **The data we used
for it:** SemEval-2020 Task 11, 14 labels, 56-document opened calibration split.
**Hardware:** RTX 5070 Ti. **Protocol:** 5 epochs, window 256 stride 128, batch 1 with 32-step
accumulation, AdamW lr 2e-5, BF16, labelwise-max aggregation, 18-point threshold grid.
**Three seeds (41/42/43), SD is a three-sample SD.**

| | macro F1 | p50 | peak RSS | weight file | GPU J/doc |
|---|---:|---:|---:|---:|---:|
| 24L, 248k, BF16 | 0.5487 ± 0.0228 | 221.3 ms | 2,037 MiB | 1,435 MiB | 33.37 |

This is the starting point for everything below: the full-depth, full-vocabulary backbone with a
freshly initialised 14-label head.

### 3. Removing layers

Same vocabulary, same protocol, same seeds. Only depth changes.

| depth | macro F1 | p50 | weight file | GPU J/doc |
|---:|---:|---:|---:|---:|
| 24L | 0.5487 ± 0.0228 | 221.3 ms | 1,435 MiB | 33.37 |
| 8L | 0.5686 ± 0.0212 | 73.8 ms | 802 MiB | 11.31 |
| 6L | 0.5627 ± 0.0241 | 52.0 ms | 720 MiB | 7.98 |
| 4L | 0.5602 ± 0.0391 | **29.7 ms** | 637 MiB | **4.71** |

Quality across the four depths spans 0.0199. The SDs span 0.0212 to 0.0391. The spread is
inside the run-to-run variation, so we do not read an ordering here. Latency moves 7.5x and
energy per document moves 7.1x over the same range.

*Our reading:* on this task the depth we removed was not carrying quality that this measurement
can see. We do not know whether that holds on a harder task; we have only measured this one.

### 4. Changing precision

4 layers, 248k vocabulary, same heads. BF16 runs on CUDA; the two GGUF precisions run on CPU
with 4 threads — two different deployment situations. The latency column therefore reads
within a row's own host, not down the column; the file and quality columns read down the column.

| precision | macro F1 | p50 | peak RSS | weight file |
|---|---:|---:|---:|---:|
| BF16 (CUDA) | 0.5602 ± 0.0391 | 29.7 ms | 2,082 MiB | 637 MiB |
| F16 GGUF (CPU) | 0.5592 ± 0.0398 | 783.8 ms | 2,075 MiB | 648 MiB |
| Q8_0 GGUF (CPU) | 0.5612 ± 0.0356 | 696.6 ms | **1,781 MiB** | **349 MiB** |

Q8_0 halves the file against BF16 and moves quality by +0.0010, far inside the SD.

*Our reading:* 8-bit quantization of this backbone did not cost anything we could detect. We
later saw a hint that quantization costs a little more once the vocabulary is cut — 0.0015 to
0.0068 across three cut arms, against roughly zero for the two full-vocabulary arms — but at
three seeds that is not separable either, and we record it as an observation, not a finding.

### 5. Cutting the embedding to 128k

The embedding dominates a four-layer model: 254,279,680 of 334,096,704 parameters, **76.11%**.
Depth reduction only ever touched the other 24%.

| | macro F1 | p50 | Q8_0 file |
|---|---:|---:|---:|
| 4L, 248k | 0.5602 ± 0.0391 | 29.7 ms | 349 MiB |
| 4L, 128k | 0.5637 ± 0.0321 | 29.5 ms | **218 MiB** |

No layer weights changed; only embedding rows were remapped.

**Where those 128,000 entries came from.** `v128k_remap_manifest.json` records
`source_128k_classifier_tokenizer` pointing at `models/semeval-propaganda`. The vocabulary was
carried over from the SemEval propaganda classifier's tokenizer by token string, and the rule
that chose those 128,000 entries is not documented anywhere in this repository. A root described
as task-free therefore had a vocabulary selected with the task in view. That is why there is a
section 6.

It also cost Korean. Korean-capable tokens fell from 10,927 to 2,137, and the same Korean text
costs **+92.17%** more tokens under the 128k vocabulary.

### 6. Cutting the original embedding by rule: English and Korean

This is the current root. The rule was written down and frozen before anything was built, and no
vocabulary size was chosen on task results — four sizes were built, all four were measured, and
one is published on cost grounds.

**The rule.** Keep the top *N* entries by upstream BPE id, plus every token that carries Hangul
(by Unicode script property, plus byte fragments whose bytes lie entirely in the Hangul ranges),
plus the 256-byte alphabet, plus the 33 added tokens. At *N* = 32,768 that is 39,866 entries.

The whole 24→8→6→4 ladder was re-distilled from the upstream teacher once per grid point, so
these are trained at their vocabulary rather than cut afterwards.

| N | entries | macro F1 | BF16 p50 | Q8_0 file | GPU J/doc |
|---:|---:|---:|---:|---:|---:|
| 8,192 | 15,380 | 0.5699 ± 0.0160 | 37.2 ms | 98 MiB | 6.00 |
| 16,384 | 23,551 | 0.5781 ± 0.0032 | 33.8 ms | 106 MiB | 5.40 |
| **32,768** | **39,866** | **0.5721 ± 0.0087** | **30.4 ms** | **124 MiB** | **5.01** |
| 65,536 | 72,455 | 0.5778 ± 0.0079 | 30.0 ms | 159 MiB | 4.73 |

The four span 0.0081 in quality against a largest SD of 0.0160. We do not read an ordering. An
earlier build of the same grid, discarded for an unrelated defect, put them in a different
order, which is the clearest evidence we have that the order is noise.

Cost is monotone and has a corner. 64k→32k buys 22.0% of the file for 1.2% BF16 latency;
32k→16k buys 14.1% for 11.2%; 16k→8k buys 8.2% for 10.2% and 11.1% more energy. We published
32k because it is the last step where the file saving is larger than what it costs, not because
it scored best — it did not.

![the grid](benchmark/figures/05_taskblind_grid.png)

---

## Beside other models

61 arms, one frozen protocol, 183 trainings, 549 calibrations and 549 isolated inference
profiles, completed 2026-09-19. Families: Qwen3.5 (13), Qwen2.5 (2), and ten encoder families
(46) — BERT, RoBERTa, XLM-R, DeBERTa-v3, mDeBERTa-v3, ALBERT, ELECTRA, MPNet, ModernBERT,
DistilBERT, mBERT, multilingual MiniLM. The four vocabulary grid arms of section 6 were trained
later under the same protocol, split and seeds, which brings the field to 65.

Top twelve by BF16 three-seed mean:

| # | arm | macro F1 | SD | p50 ms | file MiB | J/doc |
|---|---|---:|---:|---:|---:|---:|
| 1 | `qwen35-taskblind-base4l-N16384` (23,551) | 0.5781 | ±0.0032 | 33.8 | 198 | 5.40 |
| 2 | `qwen35-taskblind-base4l-N65536` (72,455) | 0.5778 | ±0.0079 | 30.0 | 294 | 4.73 |
| 3 | **`qwen35-taskblind-base4l-N32768` (39,866) — this root** | **0.5721** | ±0.0087 | 30.4 | 230 | 5.01 |
| 4 | `qwen35-taskblind-base4l-N8192` (15,380) | 0.5699 | ±0.0160 | 37.2 | 182 | 6.00 |
| 5 | `qwen35-taskfree-base8l-v248k` | 0.5686 | ±0.0212 | 73.8 | 802 | 11.31 |
| 6 | `qwen35-specialized4l-v128k` | 0.5685 | ±0.0133 | 29.8 | 402 | 4.67 |
| 7 | `qwen35-taskfree-base4l-v128k` | 0.5637 | ±0.0321 | 29.5 | 402 | 4.61 |
| 8 | `qwen35-taskfree-base6l-v248k` | 0.5627 | ±0.0241 | 52.0 | 720 | 7.98 |
| 9 | `qwen35-taskfree-base8l-v128k` | 0.5611 | ±0.0050 | 74.3 | 567 | 11.21 |
| 10 | `qwen35-taskfree-base4l-v248k` | 0.5602 | ±0.0391 | 29.7 | 637 | 4.71 |
| 11 | `qwen35-taskfree-base6l-v128k` | 0.5568 | ±0.0245 | 51.7 | 485 | 8.16 |
| 12 | `roberta-base` | 0.5524 | ±0.0143 | **11.1** | **238** | **2.24** |

The first four rows are the vocabulary grid, and their spread of 0.0081 is smaller than the
largest SD among them. The median three-seed SD across all 65 arms is 0.0117 and six arms sit
within one such SD of the top, so this ordering is not resolved by the measurement. Across the
same field, macro F1 spans 0.093 while document p50 spans 40x (5.7 ms to 228.9 ms), the weight
file spans 64x (22 MiB to 1,435 MiB) and GPU energy spans 43x (0.81 J to 34.76 J).

![the root on every metric](benchmark/figures/10_root_on_every_metric.png)

Three arms — `mdeberta-v3-4l`, `deberta-v3-base-6l`, `deberta-v3-base-8l` — score exactly
0.475627, which is the macro F1 of an all-positive predictor on this split. They failed to train
under the shared protocol. We report them rather than dropping them.

On cost the encoders are ahead of us at this depth: `roberta-base-6l` runs at 7.4 ms and 157 MiB
against our 29.5 ms and 402 MiB at the time of that table, with a quality difference of 0.021
against SDs of 0.014 and 0.032.

Full table: [`benchmark/full/61_arm_bf16.csv`](benchmark/full/61_arm_bf16.csv).

![quality against latency](benchmark/figures/01_quality_vs_latency.png)
![the top arms overlap](benchmark/figures/02_top_arms_overlap.png)
![depth](benchmark/figures/03_depth_quality_and_cost.png)

---

## Two things we checked because they would have changed the reading

### Does the host matter?

Our first cut-versus-source latency ratios used the benchmark's frozen rows as the denominator
and made every cut look slower. Re-measuring the source arm on the same host in the same run
gave a host factor of 1.0525 (BF16), 1.0448 (F16), 1.1059 (Q8_0), with RSS ratios at 0.99. On
the corrected same-host basis the ratios inverted: a 64k cut runs at 0.966x to 0.991x of the
source p50 depending on precision, and at 0.977x its BF16 energy per document.

| cut | Q8_0 p50 vs source | Q8_0 RSS vs source |
|---|---:|---:|
| v64k | **0.966x** | 0.680x |
| v32k | 1.036x | 0.623x |
| v16k | 1.167x | 0.598x |

![vocabulary cuts](benchmark/figures/04_vocabulary_cut_curve.png)

### Does the 262k context help?

The protocol reads every document in 256-token windows, which caps a 262,144-position decoder at
the same window as a 512-position encoder. The median calibration document is 1,034 tokens and
96% fit inside 4,096, so we tested it twice.

Reading at a longer window, same trained heads, seed 41:

| window | this family (262k ctx) | ModernBERT (8,192) | RoBERTa (514) | DeBERTa-v3 (512) |
|---:|---:|---:|---:|---:|
| 256 | **0.5816** | 0.5126 | 0.5381 | 0.5330 |
| 512 | 0.5633 | 0.4904 | **0.5509** | **0.5376** |
| 1,024 | 0.5722 | 0.4855 | — | — |
| 2,048 | 0.5408 | 0.4795 | — | — |
| 4,096 | 0.5480 | 0.4788 | — | — |

An encoder with an 8,192 context loses 0.0338 over 256→4,096 and the 262k model loses 0.0336.

![the window sweep](benchmark/figures/08_long_context_window.png)

Training the head at window 4,096 instead of 256, three seeds:

| training window | macro F1 |
|---|---:|
| 256 / stride 128 | 0.5721 ± 0.0087 |
| 4,096 / stride 2,048 | 0.5446 ± 0.0062 |

*Confound we did not resolve:* a 4,096 window yields 280 training windows where 256 yields
thousands, so the 50%-overlap windowing was also acting as augmentation. This comparison changes
the context and the amount of training signal at the same time.

*Our reading:* we do not think context length is what is moving numbers on this task, mostly
because the 8,192 encoder tracks the 262k model so closely. We are not claiming long context is
useless in general.

---

## The dedicated runtime

Alongside the model there is a runtime built only to run it. It is not needed to use this root —
everything in this card was measured without it — but it is the other half of the work, so here
is what it is.

### What it is

The runtime is a **vendored copy of llama.cpp**
([ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)) with a pinned patch set applied at
prepare time by `prepare_runtime.py`. Every patch is anchored to an exact source string and the
preparer raises if an anchor has moved, so the build either reproduces exactly or fails loudly.
The tree is vendored by per-file SHA-256 in a 1,389-file bundle manifest rather than pinned to an
upstream commit, so it rebuilds byte-for-byte but does not name an upstream revision.

It builds exactly one binary, `qwen35-classifier`, with everything a generator needs switched off:
no server, no examples, no tools, no CUDA, BLAS, Metal, Vulkan or OpenMP, no backend loading.
The x86 target needs AVX2, FMA, F16C, BMI2, SSE4.2 and AVX-512 F/CD/VL/DQ/BW/**VNNI**; a CPU with
only AVX-VNNI is not supported.

**What of it you can actually get.** The full v3 tree lives in the research repository's
`deployment/` directory, which is not published anywhere, so treat any path starting
`deployment/` in this card as a label for where a thing was measured, not as a link. What is
published is the part you can use: the two relaxed sources in [`runtime/`](runtime/), and a
complete buildable copy of the patched tree inside
[`docker-train/vendor/`](docker-train/vendor/), which is what that stack compiles its native
binaries from.

### Why a separate runtime at all

A classifier is not a generator, and most of what a decoding runtime does is wasted on it. There
is no sampling loop, no second token, nothing to carry between calls, and only one row of the last
hidden state ever reaches the head. Four things follow, and they hold at every specialisation
level from 2 up:

- **No KV cache is allocated.** Attention KV allocation is **0 MiB**. The window is read once.
- **The 14-label head runs inside the graph.** Logits come out of the C++ side; there is no Python
  or torch round trip in the request path.
- **Weights are packed once, at first call**, into a signed-offset layout and then held:
  **99,696,640 bytes** persistent, with a maximum input scratch of **2,064,384 bytes**.
- **Idling is free.** The thread pool is created with `poll=0`, so a loaded, idle service
  registers **0 CPU ticks in half a second**.

### What each specialisation level turns on

`Q35_SPECIALIZE_LEVEL` stages the whole thing, 0 being the stock path and 12 the x86 default.
Every step is a real switch, so each can be measured against the one below it.

| level | what it adds |
|---:|---|
| 1 | `concat` partitioned by channel instead of by `ne2`, for the classifier's `[tokens+3, 6144]` input |
| 2 | **specialised tail**: `inp_out_ids` is never built, the last block carries only the final 4 token rows, and the head takes one row by view instead of `ggml_get_rows` |
| 3 | last-layer Q / gate / output projection computed for **4 query tokens only**; K and V keep the whole window, the causal mask is sliced to match, RoPE positions untouched |
| 4 | hand-written 4x4 Q8 GEMM |
| 5 | packed Q8 kernel |
| 6 | **the v2 reference path**: packed weights carried in signed-offset form |
| 7 | aarch64 NEON Q8 kernel (present in the source; not built or tested here) |
| 8 | Q8 tiles at arbitrary column counts, not only multiples of four |
| 9 | 8 + a persistent thread pool that sleeps between requests |
| 10 | 9 + recurrent state kept hot row by row through decay, delta, update and output |
| 11 | 10 + a 4x8 ZMM Q8 kernel. **Measured slower, so not adopted** |
| 12 | 10 + a dedicated AVX-512 routine for the 128-wide recurrent state |

### Why it stays exact

None of this is an approximation. The packed kernel folds the unsigned-to-signed shift into a
single per-matrix correction and then uses `_mm512_dpbusd_epi32`, which preserves the reference
path's eight int32 lanes and its float accumulation order. The tail narrowing drops rows the head
provably never reads. The recurrent rewrite keeps every vector reduction in its original order.

The check that matters: across **56 documents and 511 windows**, level 12 against the level 6
reference gave a maximum absolute logit difference of **0.0**, a maximum absolute probability
difference of **0.0**, and **zero** window-level and document-level label disagreements. Reload,
A/B/A, thread counts 1/3/4 and the live service path all matched as well.

### What the specialisation buys

On the 128k model, level 12 against level 6 — same binary, same weights, same input:

| tokens in window | level 6 | level 12 | change |
|---:|---:|---:|---:|
| 33 | 15.76 ms | 12.29 ms | −22.1% |
| 64 | 20.96 ms | 19.85 ms | −5.3% |
| 129 | 50.84 ms | 37.44 ms | −26.3% |
| 233 | 92.14 ms | 70.47 ms | −23.5% |
| 256 | 77.33 ms | 73.36 ms | −5.1% |

The two small rows are the ones whose token counts sit badly against the 4-wide tile; 256 tokens
coming out cheaper than 233 is the same effect read from the other side.

### Making it accept a cut vocabulary

As shipped it refused any vocabulary other than 128,000, at two places:

| where | check | effect |
|---|---|---|
| `qwen35-classifier.cpp:47` | `llama_vocab_n_tokens(...) != 128000` | throws "this runtime supports only Qwen3.5 4L / 128k / 14-label classification" |
| `src/models/qwen35.cpp` | `GGML_ASSERT(n_layer == 4 && n_embd == 1024 && tok_embd->ne[1] == 128000)` | aborts inside `sched_reserve()` at level >= 2 |

Both are model-identity guards, not computational dependencies. The specialised tail reads
`n_embd`, `n_cls_out`, `n_seqs` and `n_tokens` and never the embedding row count, and the
hand-written Q8 kernels operate on hidden 1024. So the port relaxed the vocabulary equality only
(`tok_embd->ne[1] == 128000` becomes `> 0`), in a **copy** of the source tree; architecture, depth
and width are still enforced, and all five binaries of the frozen v3 build still match their
recorded SHA-256. The two relaxed sources are in [`runtime/`](runtime/).

After the port, all three cuts load at full specialisation and produce **bit-identical** output to
the generic path:

| cut | tokens in probe | level 0 | level 12 | change |
|---|---:|---:|---:|---:|
| v16k | 33 | 14.94 ms | 10.68 ms | −28.5% |
| v32k | 25 | 11.47 ms | 7.36 ms | −35.8% |
| v64k | 23 | 10.32 ms | 7.26 ms | −29.7% |

![what the runtime buys](benchmark/figures/07_runtime_specialization.png)

### Running it

The container in [`docker/`](docker/) is the shortest path, and
[`docker-train/`](docker-train/) builds its native binaries from this same patched tree. Both are
described at the top of this card.

### Before you reach for it

- **It needs a GGUF with a classification head.** This root is headless, so train a head and
  convert that checkpoint first. The runtime cannot run the published root as it stands.
- **The port is a development port.** It has not been through the v3 validation scripts
  (`validate_runtime.py`, `validate_reload.py`, `validate_threads_service.py`); the bit-identity
  above is the port's own parity check, not that suite.
- **x86 AVX-512 VNNI only** in practice. The NEON path exists in the source but was not built or
  tested, and the aarch64 / A53 variants are unmeasured.
- **The timings here are single-sentence native-compute medians** on a host with a desktop session
  running, not the benchmark's isolated document-level protocol. Token counts differ per cut for
  the same sentence, so compare within a row, not across rows.
- **No number anywhere else in this card came from this runtime.** Those all came from the
  benchmark's own `profile_inference.py`.

---

## What this does not tell you

- **No held-out evaluation.** Every number here is the opened 56-document calibration split.
  There is no `test.jsonl` in this repository.
- **The evaluation is small.** 56 documents, 14 labels, and the rarest label appears in 6 of
  them, so one fourteenth of macro F1 rides on six samples. This is the most likely source of the
  0.005–0.039 seed SDs.
- **The scenarios are ours, and they are few.** The numbers in sections 2–6 come from one
  situation — English SemEval-derived propaganda technique detection on a desktop GPU — and
  section 1 comes from one other. This root is not built for either of them; they are the
  situations we happened to set up to watch the compression. Korean appears only as tokenization
  parity, with no Korean evaluation anywhere here.
- **Three seeds are run-to-run variation, not a confidence interval.**
- **The layer maps were chosen on labeled data.** Disclosed above, not repaired.
- **Quality figures belong to fresh-head transfer checkpoints**, not to this headless root. The
  root's downstream quality is NR until you train a head.
- Long-context, calibration, robustness, fairness and production safety are not established.
- Do not use this as a fact checker, a safety oracle, or an autonomous decision maker.

## Files

| path | what |
|---|---|
| root | the 39,866-entry headless backbone |
| [`root_manifest.json`](root_manifest.json) | its vocabulary rule, layer maps, hashes, why this grid point |
| [`benchmark/full/`](benchmark/full/) | the 61-arm table, the grid, the same-host cuts |
| [`benchmark/figures/`](benchmark/figures/) | the ten figures above |
| [`runtime/`](runtime/) | the two relaxed sources of the dedicated runtime, and its own README |
| [`docker/`](docker/) | a container that runs the backbone with a head on it, CPU only |
| [`docker-train/`](docker-train/) | train a classifier on your own data, convert, serve |
| [`models/semeval-propaganda/`](models/semeval-propaganda/) | a separate lineage, not a child of this root |
| [`distillation/`](distillation/) | the reusable ladder platform |
| `v128k_remap_manifest.json` | the one surviving record of the superseded 128k root |
| `SHA256SUMS` | sha256 of every file in this repository |

## License and attribution

Apache-2.0 for the released code and model artifacts, subject to upstream model and data terms.
Qwen3.5 is attributed to Qwen. Transformers, PyTorch, Hugging Face Hub, WikiText and SemEval
remain the work of their respective authors. No WikiText or SemEval source records are
redistributed.

The WikiText dataset page carries a license wording discrepancy — metadata lists CC BY-SA 3.0
and GFDL while the prose says CC BY-SA 4.0. Check
[`Salesforce/wikitext`](https://huggingface.co/datasets/Salesforce/wikitext) directly.
