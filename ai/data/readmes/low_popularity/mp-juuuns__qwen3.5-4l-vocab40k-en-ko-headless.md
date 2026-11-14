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

**A four-layer, 120.6M-parameter text backbone cut from the 24-layer text model of Qwen3.5-0.8B, and measured as the
base of a document classifier on one English task, one GPU and one CPU.** Layers were removed in three distillation
stages (24 → 8 → 6 → 4), and the vocabulary was cut by a fixed rule from 248,320 rows to 39,866 English and Korean
entries. It has no head: you attach one and train it for your own labels. This card calls the headless backbone
*the root*.

This card records how the root was made and how it compares with the models we trained beside it. We are not arguing
that it is better than anything; where we have a guess about why a number moved, we say it is a guess.

*한국어: [`README_KO.md`](README_KO.md)*

What we measured:

- **Depth.** At the full 248k vocabulary, removing 20 of the 24 layers made the classifier 7.5x faster on one RTX
  5070 Ti (221 → 30 ms per document) and did not move macro F1 beyond the three-seed spread.
- **Quality.** On SemEval-2020 Task 11 (English news, 14 labels, three seeds), a classifier on the root scores
  0.5721 macro F1 on a 56-document split that its decision threshold was also picked on. A classifier that answers
  yes to every label scores 0.4756, and the highest of the 65 models trained the same way scores 0.5781; six of the
  65, this one among them, sit within one median seed SD of that highest mean, so they are not ordered. When four
  encoders were retrained with FP32 instead of BF16 weights they rose into the same range, so part of the root's place
  in that table may come from the training setup. In the one preregistered test evaluation, on a split the project
  had used before, the root did not separate from two RoBERTa models.
- **Compiling on a GPU.** In a separate end-to-end run, `torch.compile` made the same classifier 2.3x faster (32.0 →
  13.6 ms per document) and cut GPU energy by 39%. Four encoders timed beside it, backbone only, changed by 0.93x to
  1.06x and stay faster.
- **CPU and Korean (speed only).** On one CPU, on English documents, the root is 1.4x to 4.1x slower than four
  RoBERTa and DistilBERT classifiers retrained beside it with FP32 weights. On Korean news it finishes sooner than the
  RoBERTa models, whose English tokenizer splits Korean into about four times as many 256-token windows. DistilBERT
  stays faster, and so does a random-weight stand-in with XLM-R's shape and multilingual tokenizer.

| | |
|---|---|
| **Layers** | 4, alternating 2 [Gated DeltaNet](https://arxiv.org/abs/2412.06464) (linear attention) and 2 Gated Attention; hidden 1,024, FFN 3,584 |
| **Vocabulary** | 39,866 entries (`vocab40k` in the repository name): the first 32,768 upstream BPE entries, every token containing Hangul, the 256-byte alphabet, 33 added tokens |
| **Parameters** | 120,639,808 |
| **Weights** | BF16 safetensors 230.1 MiB (241,285,160 bytes). With a 14-label head, as the Q8_0 GGUF the containers run: 124 MiB ([`docker/bundle/model/`](docker/bundle/model/)) |
| **Head** | none — there is no `score.weight` |
| **Upstream** | [`Qwen/Qwen3.5-0.8B`](https://huggingface.co/Qwen/Qwen3.5-0.8B), 24 layers, 248,320 embedding rows |
| **Distillation data** | 4,096 unlabeled WikiText-103 rows, no task labels in the loss; which layers to keep was chosen with SemEval-2020 Task 11 labels ([step 3](#how-it-was-built)) |

---

## Why this model exists

The project began by asking a generative model to classify documents on a small edge board. Each step answered one
problem and exposed the next.

1. Prompting the generative model on the board gave every document the same class and ran out of memory at
   request 31. → We **attached a classification head** to the backbone instead.
2. The 24-layer classifier worked but took 221 ms per document on a desktop GPU. → We **distilled it to 8, then 6,
   then 4 layers**: 7.5x faster, quality within the seed-to-seed spread.
3. At four layers the embedding table was 76% of the parameters, mostly rows that English and Korean text never
   reach. → We **cut the vocabulary**, first to 128,000 entries and then, by a rule written down in advance, to a grid
   of four sizes.
4. A smaller vocabulary spends more tokens on the same text, so the file shrank but inference got slower: the smallest
   size built is 24% slower than the largest. → We **published the 39,866-entry size**, the last step where the latency
   cost stays near 1% ([step 6](#how-it-was-built)).
5. It was still slower than the encoder classifiers measured beside it. On the GPU, much of the time was the execution
   path: without optional kernels, the two linear-attention layers run on a slow fallback. → **`torch.compile`** cut
   the backbone's GPU time 2.8x when run two windows at a time, as the benchmark does (1.6x at 16 windows). How much of
   the remaining gap is the architecture itself was not measured.

![file size and quality from 24 layers / 248k to 4 layers / 39,866; the prompting step and compiling are not on this chart](benchmark/figures/06_stage_path.png)

*Quality in this figure is macro F1 of a fresh 14-label head trained on each backbone, on the calibration split
described under [Key results](#key-results).*

---

## Quick start

### Load it

Needs `transformers` 5.13.0, pinned in [`requirements.txt`](requirements.txt); the measurements used torch 2.11.0.

```python
from transformers import AutoModel, AutoTokenizer

model_id = "mp-juuuns/qwen3.5-4l-vocab40k-en-ko-headless"
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=False)
backbone = AutoModel.from_pretrained(model_id, trust_remote_code=False)
```

The outputs are hidden states. They carry no class meaning until you train a head. To attach an untrained head the
way the `finetune` command below does:

```python
from transformers import AutoModelForSequenceClassification
classifier = AutoModelForSequenceClassification.from_pretrained(
    model_id, num_labels=14, problem_type="multi_label_classification")
```

> **Renamed and replaced on 2026-09-20.** This repository was `qwen35-standalone4l-classification-base`. The old URL
> redirects, but `from_pretrained` on the old id is reported not to follow the redirect, so update pinned code; the old
> id now holds a weightless stub pointing here. Until then this repository held a 128,000-entry, 210.9M-parameter,
> 402.29 MiB root, still at the git revision before that change. Anything labelled "128k" here describes it, and
> [steps 5 and 6](#how-it-was-built) say why it changed.

### Check the tokenizer against your text

The vocabulary keeps English and Korean. Other scripts fall back to byte tokens and cost more. One short sentence
each ([figure](benchmark/figures/09_tokenizer_cost.png)):

| tokens for one sentence | upstream 248k | this root | ratio |
|---|---:|---:|---:|
| English | 9 | 12 | 1.33x |
| Korean | 16 | 16 | 1.00x |
| Chinese | 8 | 58 | **7.25x** |
| Japanese | 10 | 44 | **4.40x** |

Korean is unchanged because the rule keeps every Hangul-carrying token regardless of its id. Every Han
(Chinese-character) token in the upstream vocabulary sits above id 65,536 and none survives, so Chinese and Japanese
are spelled in bytes. Upstream was not counted on long documents; against the largest size built (72,455 entries, not
the upstream 248k), this root reads 1.06x the tokens on 56 English news documents (1,345 against 1,264). The model
reads text in 256-token windows and compute grows with the number of windows, so measure a representative document of
yours:

```python
len(tokenizer("a representative document from your data")["input_ids"])
```

### Train a head

Get the files with `hf download mp-juuuns/qwen3.5-4l-vocab40k-en-ko-headless --local-dir qwen3.5-4l`, or install
git-lfs before cloning; without it the weights arrive as small pointer files.

```bash
git clone https://huggingface.co/mp-juuuns/qwen3.5-4l-vocab40k-en-ko-headless
cd qwen3.5-4l-vocab40k-en-ko-headless/distillation
python -m pip install -e .
qwen35-distill finetune --checkpoint .. --train examples/multilabel_train.jsonl \
  --labels examples/labels.json --mode multilabel --output my-classifier-4l
```

`finetune` is a minimal recipe. It reads the first 256 tokens of each example (`--max-length`), trains for 3 epochs
with 8-step accumulation by default, and does not choose a decision threshold. The numbers in this card come from a
different runner, which is not in this repository: overlapping 256-token windows, a label counted present if any
window says so, 5 epochs, 32-step accumulation, and a threshold chosen per seed.

The packaged platform's commands — `validate-dataset`, `extract-text`, `materialize`, `materialize-classifier`,
`finalize-base`, `distill`, `finetune`, `distill-classifier` — do not cut a vocabulary. Running the ladder from the
upstream teacher reproduces the depth reduction and gives a four-layer model with the full 248,320-row embedding,
which is a different artifact from this root. If you want this vocabulary, start from this root.

Pick your own decision threshold on your own data. In the benchmark, the threshold chosen on the calibration data
moved 3x to 4x between seeds, and every run predicted more positives than the data held
([details](benchmark/README.md#if-you-train-a-head-the-threshold-is-yours-to-pick)).

### Make it fast on a GPU

```python
import torch
backbone = torch.compile(backbone.to("cuda", dtype=torch.bfloat16).eval(),
                         mode="max-autotune-no-cudagraphs", dynamic=False)
```

- The first call compiles and can take several minutes.
- With `dynamic=False`, pad inputs to a fixed length and pass the `attention_mask`.
- Compiled BF16 outputs are not bit-identical to eager; a few decisions near the threshold move
  ([Key results C](#c-the-same-model-eager-and-compiled)).
- Without compiling, the two linear-attention layers run on a slow pure-PyTorch fallback unless the optional
  `flash-linear-attention` and `causal-conv1d` kernels are installed. Compiling is the route measured here; the
  kernels were only partly tested ([notes](benchmark/README.md#is-it-the-architecture-that-costs-the-time)).

Measured on one RTX 5070 Ti; other GPUs were not measured.

### Run it on a CPU or in a container

On a CPU with native BF16 instructions, run it in BF16: of the paths measured, it was the fastest that left decisions
nearly unchanged. For a small CPU-only service there are two containers with a dedicated runtime: [`docker/`](docker/)
serves a worked example, and [`docker-train/`](docker-train/) trains, converts and serves your own classifier. See
[Deployment](#deployment).

---

## What changed from Qwen3.5-0.8B

```
Qwen3.5-0.8B text model, 24 layers, 248,320 rows
  └─ distil 24 → 8     keep layers (0, 4, 6, 11, 13, 16, 20, 23)
       └─ 8 → 6        keep (0, 1, 3, 4, 6, 7)
            └─ 6 → 4   keep (0, 2, 3, 5)
                 └─ vocabulary cut by rule, 248,320 → 39,866
                      └─ this root: 4 layers, headless, 120.6M parameters
```

Each stage's indices count the layers of the stage before it; the root keeps upstream layers 0, 11, 13 and 23
(`layer_maps` in [`root_manifest.json`](root_manifest.json)).

| | Qwen3.5-0.8B, text model | this root |
|---|---:|---:|
| Layers | 24 | **4** |
| Layer types | Gated DeltaNet and Gated Attention, 3 : 1 | the same two, 1 : 1 |
| Hidden / FFN | 1,024 / 3,584 | 1,024 / 3,584 |
| Vocabulary | 248,320 rows | **39,866** |
| Parameters | 752M | **120.6M** |
| Embedding share of parameters | 33.8% | 33.8% |
| Head | language-model head | none |

The order of the two cuts follows from where the parameters sit. Cutting 24 layers to 4 removes 84% of the layer
stack but leaves the embedding untouched, so at four layers the embedding is 76.1% of the model. Cutting the vocabulary
brings it back to 33.8%, the share the 24-layer model had.

![where the parameters live: the depth cut, then the vocabulary cut](benchmark/figures/20_where_the_parameters_live.png)

---

## Key results

**How to read the numbers.**

- **Score.** Macro F1 on [SemEval-2020 Task 11](https://aclanthology.org/2020.semeval-1.186/) (English news, 14
  propaganda-technique labels), mean ± SD over three seeds (41, 42, 43). A classifier that answers yes to every label
  scores 0.4756, *the all-positive floor*. Gaps inside the three-seed SD are not ranked.
- **The protocol.** Each run fine-tunes the backbone with a fresh 14-label head under one recipe, fixed (*frozen*)
  before the runs and never changed: 5 epochs, AdamW at 2e-5, BF16 weights, batch 1 with 32 accumulation steps. It
  reads each document in 256-token *windows* that overlap by 128, runs two windows per forward pass (*the protocol's
  batch of 2*), and counts a label as present if any window says so. A trained model is called an *arm* in the figures.
- **The calibration split.** One decision threshold per run is picked from an 18-point grid on the same 56 documents
  the scores are reported on. The project has looked at this split throughout, so it is not held out; E is the one run
  on a separate test split. A *decision* is one label on one document: 56 × 14 = 784 per seed.
- **Cost.** Latency (p50 is the median, p95 the 95th percentile) and energy are per document on one RTX 5070 Ti,
  eager PyTorch, unless a section says otherwise.
- **Why the root's score differs between sections.** Each separate run retrained it: 0.5721 is the benchmark's value,
  0.5701 the retrain in C, and 0.5769 the FP32-weight retrain in B.

### A. Removing layers

Same vocabulary (248k), same protocol, same seeds. Only depth changes. The 4-layer row is the model before its
vocabulary cut; the root is that model with 39,866 entries (B).

| depth | macro F1 | document p50 | BF16 file | GPU J / document |
|---:|---:|---:|---:|---:|
| 24 | 0.5487 ± 0.0228 | 221.3 ms | 1,435 MiB | 33.37 |
| 8 | 0.5686 ± 0.0212 | 73.8 ms | 802 MiB | 11.31 |
| 6 | 0.5627 ± 0.0241 | 52.0 ms | 720 MiB | 7.98 |
| 4 | 0.5602 ± 0.0391 | 29.7 ms | 637 MiB | 4.71 |

Quality spans 0.020 across the four depths; the seed SDs are 0.021 to 0.039, so no ordering is read. Latency falls
7.5x and energy 7.1x.

### B. Beside other models

65 models went through the protocol: 46 encoders from twelve families, 15 earlier Qwen models, and four vocabulary
sizes of this root. A few of them:

| model | macro F1 | document p50 | BF16 file | GPU J / document |
|---|---:|---:|---:|---:|
| **this root** (4 layers, 39,866) | 0.5721 ± 0.0087 | 30.4 ms | 230 MiB | 5.01 |
| this root's 23,551-entry sibling (highest mean of the 65) | 0.5781 ± 0.0032 | 33.8 ms | 198 MiB | 5.40 |
| Qwen3.5, 8 layers, 248k | 0.5686 ± 0.0212 | 73.8 ms | 802 MiB | 11.31 |
| Qwen3.5, 24 layers, 248k | 0.5487 ± 0.0228 | 221.3 ms | 1,435 MiB | 33.37 |
| `roberta-base` (12 layers) | 0.5524 ± 0.0143 | 11.1 ms | 238 MiB | 2.24 |
| `roberta-base-6l` | 0.5427 ± 0.0139 | 7.4 ms | 157 MiB | 1.29 |
| `distilbert-base-4l` | 0.5301 ± 0.0193 | 5.7 ms | 101 MiB | 0.91 |
| median of the 65 | 0.5121 | 11.2 ms | 238 MiB | 2.14 |
| a model that answers yes to every label | 0.4756 | — | — | — |

Six models, this root among them, sit within one median seed SD (0.0116) of the highest mean, so the top is not
ordered. The median is taken over the 62 models whose three seeds did not all score the all-positive floor. On latency
and energy the root is 52nd of 65 on the eager path; C shows the compiled path.

![quality against cost, all 65 models](benchmark/figures/14_field_quality_vs_cost.png)

*In the figure the "task-blind grid" is the four vocabulary sizes of this root, and "taskfree-base4l-v128k" is the
superseded 128k root. Latency and energy are the eager path.*

**Training precision may move the encoders.** The protocol trains with BF16 weights. A later run took `roberta-base`,
cut its own copies of three shallower encoders from `roberta-base` and `distilbert-base-uncased` by keeping their first
layers, and trained these four and the root with FP32 weights, following the protocol's other steps:

| model | benchmark (BF16 weights) | FP32-weight rerun |
|---|---:|---:|
| this root | 0.5721 ± 0.0087 | 0.5769 ± 0.0139 |
| `roberta-base` | 0.5524 ± 0.0143 | 0.5789 ± 0.0063 |
| RoBERTa, 8 layers | 0.5448 ± 0.0178 | 0.5761 ± 0.0221 |
| `roberta-base-6l` | 0.5427 ± 0.0139 | 0.5695 ± 0.0251 |
| `distilbert-base-4l` | 0.5301 ± 0.0193 | 0.5601 ± 0.0163 |

The four encoders scored 0.026 to 0.031 above the benchmark's values for encoders of the same names, and each one's
mean ± SD interval overlaps the root's. We do not rank the five reruns: the largest gap among them is 0.019 with
thresholds chosen on all 56 articles, and it widens to 0.048, with `distilbert-base-4l` 0.037 below the root, when
each article's threshold is chosen on the other 55.

Why the benchmark's encoders scored lower is not settled. In the same run, BF16 weights left `roberta-base-6l` at the
all-positive floor and `distilbert-base-4l` at 0.51 to 0.52; the other two encoders were not completed in BF16.
Neither precision reproduced the benchmark's encoder numbers, so the rise mixes precision with how the encoders were
built. Details: [`benchmark/cpu_vs_encoders/`](benchmark/cpu_vs_encoders/).

The full 65-model table is two files: [`benchmark/full/61_arm_bf16.csv`](benchmark/full/61_arm_bf16.csv) (61 models)
and [`benchmark/full/taskblind_grid.csv`](benchmark/full/taskblind_grid.csv) (the four vocabulary sizes, this root
among them), read together in [`benchmark/README.md`](benchmark/README.md#the-65-model-field-in-detail).

### C. The same model, eager and compiled

The root was retrained with seeds 41, 42 and 43 by the protocol's own code and run end to end — tokenize, window,
forward, aggregate — on the 56 calibration documents, one at a time, on one RTX 5070 Ti in BF16.

| | eager | compiled, `dynamic` at its default | compiled, padded to 256, `dynamic=False` |
|---|---:|---:|---:|
| document p50 | 32.0 ms | 13.6 ms (2.34x) | 13.8 ms (2.31x) |
| document p95 | 114.4 ms | 54.4 ms | 57.1 ms |
| GPU J / document | 5.09 | 3.10 | 3.09 |
| macro F1 | 0.5701 ± 0.0076 | 0.5671 ± 0.0105 | 0.5684 ± 0.0102 |
| decisions that differ from eager, of 784 per seed | — | 0 / 3 / 6 | 0 / 3 / 4 |

Both compiled columns use `mode="max-autotune-no-cudagraphs"`; the right one is the setting in
[Quick start](#make-it-fast-on-a-gpu). In FP32 the compiled and eager decisions are identical. In BF16 they are not:
the timed runs did not save the compiled probabilities, and in a rerun that did, each changed decision had one of its
two probabilities within 0.0044 of the threshold. The published quality numbers are for the eager path.

**Beside four encoders, backbone only.** On this GPU, compiling sped up the root's backbone 2.8x at the protocol's
batch of 2 (1.6x at batch 16), while the four encoders measured beside it — `roberta-base`, `roberta-base-6l`,
`distilbert-base` and `distilbert-base-4l`, not the four of B and D — changed by 0.93x to 1.06x. Why was not profiled;
our guess is in [What we learned](#what-we-learned). The other Qwen3.5 models, which share those layers, were not
measured. Even compiled, the root's backbone stays 1.28x slower per document than `roberta-base` and 3.75x slower
than `distilbert-base-4l` at batch 2 (1.54x and 4.86x at batch 16), each on its faster path.

![compiling helps the root and not the encoders; the gap narrows but stays](benchmark/figures/23_what_costs_the_time.png)

*Backbone only: the median time per 256-token window of random token ids (a batch of two, divided by two), multiplied
by each model's windows per document — computed, not timed on the documents. The end-to-end figure for the table above
is [figure 24](benchmark/figures/24_same_model_eager_vs_compiled.png).* Details:
[`benchmark/README.md`](benchmark/README.md#the-backbone-beside-four-encoders).

### D. On a CPU, in English and in Korean

Situation: an AMD Ryzen 5 7500F, six threads, BF16, PyTorch eager, one document at a time, end to end. The root and
four encoders are the FP32-weight reruns from B, one checkpoint each (seed 41). The Korean text is 56 Naver economy and
IT/science news articles; the classifiers were trained on English, so only speed is measured on Korean. Two models of
XLM-R base's shape, with random weights and XLM-R's multilingual tokenizer, stand in for a multilingual encoder; they
time like trained RoBERTa models of the same depth (within 1% per window).

| model | English: 56 SemEval articles, ms | Korean: 56 Naver articles, ms | Korean windows per article |
|---|---:|---:|---:|
| **this root** | 442 | 151 | 3.3 |
| `roberta-base` | 336 | 497 | 14.1 |
| RoBERTa, 8 layers | 229 | 331 | 14.1 |
| `roberta-base-6l` | 173 | 251 | 14.1 |
| `distilbert-base-4l` | 113 | 114 | 9.3 |
| XLM-R shape, 12 layers | 353 | 114 | 3.4 |
| XLM-R shape, 6 layers | 183 | 60 | 3.4 |

Mean per article in one run with both languages; the root was timed again at the end (443 and 141 ms). The two columns
are not a language comparison: the Korean articles have about a sixth of the characters (899 against 5,577) and a
third of the root's windows.

- **English.** The root is slower than every encoder: 1.3x to 3.9x on these means, and 1.4x (`roberta-base`) to 4.1x
  (`distilbert-base-4l`) at p50 in a separate three-seed run.
- **Korean.** The RoBERTa tokenizer splits Korean into 4.3x as many windows as the root's, so the root finishes 1.7x
  to 3.3x sooner, even though each window costs it more. `distilbert-base-4l` stays ahead: it reads 2.8x as many
  windows, but each costs about a quarter of the root's. Its tokenizer also maps about a quarter of Hangul syllables to
  [UNK], one [UNK] per affected word, so its window count is lower than the text would otherwise need. The XLM-R shapes
  stay ahead because their tokenizer is as compact on Korean as the root's: the root is 1.3x and 2.5x slower, close to
  its 1.25x and 2.4x in English.

Two conditions of this run: a read-only process ran on the host during the end of the root's English timing and the
first root and `roberta-base` Korean timings, and the rules for reading the Korean results were refined after those
two had printed. The root's repeat timing at the end of the run, and every comparison above, come out the same either
way. Details: [`benchmark/korean_input/`](benchmark/korean_input/).

### E. The one test evaluation

On 2026-09-23, eleven arms — ten models, with this root also run in Q8_0 — were evaluated once on the 55 documents of
the SemEval-2020 Task 11 "v2" test re-split (a split this project drew, not the official leaderboard test), under a
preregistration frozen before any test byte was read: thresholds taken from calibration, no training, every result
published. The project had used this split before, so it is not a never-seen holdout.

| model | calibration | test |
|---|---:|---:|
| **this root**, BF16 | 0.5719 ± 0.0092 | 0.5988 ± 0.0103 |
| this root, Q8_0 (seed 41) | 0.5849 | 0.5862 |
| `roberta-base` | 0.5524 ± 0.0143 | 0.5883 ± 0.0109 |
| `roberta-base-6l` | 0.5427 ± 0.0139 | 0.5839 ± 0.0152 |
| a model that answers yes to every label | 0.4756 | 0.4866 |

The calibration column is as the test run recorded it; for this root it is 0.0002 below B's 0.5721 (SD 0.0092 against
0.0087). Nine of the eleven arms scored higher on test than on calibration, and the two RoBERTa models rose the most
(+0.036 and +0.041, against the root's +0.027), so we read the rise as mostly a property of the split. The root's mean
± SD overlaps both RoBERTa models, so the test does not separate it from them. It clears the intervals of five Qwen
arms not shown here, by 0.0006 to 0.026: its three vocabulary siblings and the 4- and 24-layer 248k models. The
RoBERTa models here were trained with BF16 weights, the setting under which B's rerun saw encoders score lower.

![calibration to test](benchmark/figures/11_final_test_calibration_to_test.png)

*"Task-blind 4L N=32,768" is this root; "historical" arms are earlier Qwen models; "sealed" means the test file stayed
sealed until this run, not that the split was never used.* All eleven arms, per-label results and what the
preregistration fixed in advance: [`benchmark/README.md`](benchmark/README.md#the-final-test).

---

## What we learned

These are our readings of the measurements above, and of one context-length measurement kept on the detail page.
Where the measurement cannot settle a reading, we say it is a guess.

- **Depth.** On this task, 20 of the 24 layers could be removed without a quality change that three seeds can see,
  and cost fell about 7x. We have measured one task, so we do not know how far that holds.
- **Vocabulary.** A smaller vocabulary spends more tokens on the same text. Across the four sizes built, BF16 latency,
  CPU Q8_0 latency and GPU energy rose with the number of 256-token windows per document (1.24x to 1.35x against
  1.31x more windows), while file size fell ([step 6](#how-it-was-built)).
- **Execution path.** We think what compiling removed on the GPU ([C](#c-the-same-model-eager-and-compiled)) is the
  fallback that runs the linear-attention layers without optional kernels; the encoders measured beside it, which have
  no such layers, changed by 0.93x to 1.06x. This was not profiled, and a gap to `roberta-base` remains. On a CPU
  compiling helps less ([Deployment](#cpu-pytorch)). We think the CPU gap is also the fallback, but a different cost:
  there it upcasts to FP32 inside BF16 and loops in Python per chunk. No optimized CPU kernel was tested, so this is a
  guess.
- **Context length.** The backbone accepts 262,144 positions, but reading documents in wider windows did not help
  quality here, and past 1,024 tokens it cost more time. On one seed, an encoder limited to 8,192 positions lost as
  much from wider windows as this model did; a three-seed run trained at 4,096 is confounded with fewer training
  windows ([details](benchmark/README.md#does-the-262k-context-help)).
- **Training precision.** Our guess is that much of the root's 0.020 to 0.042 margin over the encoders in B comes from
  the protocol's BF16-weight training, because with FP32 weights the four encoders' mean ± SD intervals overlapped the
  root's ([B](#b-beside-other-models)). The benchmark's own encoders were not reproduced in either precision, so this is not
  settled.
- **Tokenizer and language.** On Korean news the tokenizer changed which model was faster. RoBERTa's English tokenizer
  split Hangul into byte pieces and needed 4.3x the root's windows; DistilBERT's mapped a quarter of Hangul syllables
  to [UNK] ([D](#d-on-a-cpu-in-english-and-in-korean)). The one multilingual tokenizer tried, XLM-R's, was as compact
  as the root's. Per window, the root stayed the more expensive model.

---

## How it was built

Each step was measured in the situation it was built for, and the data changes with the situation: step 1 on an edge
board with 37 internal documents, steps 2 to 6 on a desktop GPU with SemEval-2020 Task 11. We were not building for a
particular task. Full tables for every step: [`benchmark/README.md`](benchmark/README.md#the-path-step-by-step).

**1. Prompting the original model.** Situation: an Arduino UNO Q edge board classifying short documents under a
2.441 GiB memory ceiling; 37 internally labelled documents, 3 classes. Prompting the generative model (Q4_0 weights)
returned the majority class for all 37 (macro F1 0.2556) and ran out of memory at request 31. A 24-layer backbone with
a 3-class head reached 94.59% accuracy. An 8-layer distilled one reached 97.30% with about half the cold-start time,
and the paired bootstrap interval on the difference between those two includes zero.

**2. A classifier: 24 layers, 248k vocabulary.** Situation: a desktop GPU assigning 14 labels to news articles, under
the protocol described in [Key results](#key-results). Result: 0.5487 ± 0.0228 at 221.3 ms per document.

**3. Removing layers.** Each stage (24 → 8, 8 → 6, 6 → 4) trained the smaller model to reproduce the larger one's
hidden states, at the output and at the boundaries between kept layers, on 4,096 unlabeled WikiText-103 rows. There
was no label and no logit matching. 192 scalar parameters of the linear-attention layers were kept frozen (the
"recurrent scalars" in [Architecture and layer maps](benchmark/README.md#architecture-and-layer-maps)). The layer maps —
which layers each stage keeps, the tree in [What changed](#what-changed-from-qwen35-08b) — were ranked by train macro F1
on labelled SemEval-2020 Task 11 data, so that task shaped the distillation targets and is in the weights; the
vocabulary cut does not remove it. It is disclosed, not repaired; the detail page also notes a config field that
records this wrongly. Results: [A](#a-removing-layers).

**4. Changing precision.** At 4 layers, Q8_0 GGUF through llama.cpp halves the file (637 → 349 MiB) and moves macro F1
by +0.0010, far inside the SD. INT8 inside PyTorch behaves differently; see [Deployment](#gpu-pytorch).

**5. Cutting the embedding to 128k.** Remapping the embedding to 128,000 entries cut the Q8_0 file from 349 to
218 MiB, with quality inside the seed spread (0.5602 → 0.5637). Those 128,000 entries were carried over from a
SemEval classifier's tokenizer, and the rule that chose them is not documented, so the task may have influenced them.
The cut also removed most Korean tokens: the same Korean text cost 92% more tokens. Both are why step 6 exists.

**6. Cutting the original embedding by rule.** The rule was written and frozen before anything was built: keep the
first *N* entries by upstream BPE id, every token containing Hangul (and byte fragments made only of Hangul bytes),
the 256-byte alphabet and the 33 added tokens. Four sizes were built, each by re-running the whole 24 → 8 → 6 → 4
ladder:

| N | entries | macro F1 | BF16 p50 | Q8_0 file | GPU J / document |
|---:|---:|---:|---:|---:|---:|
| 8,192 | 15,380 | 0.5699 ± 0.0160 | 37.2 ms | 98 MiB | 6.00 |
| 16,384 | 23,551 | 0.5781 ± 0.0032 | 33.8 ms | 106 MiB | 5.40 |
| **32,768** | **39,866** | **0.5721 ± 0.0087** | **30.4 ms** | **124 MiB** | **5.01** |
| 65,536 | 72,455 | 0.5778 ± 0.0079 | 30.0 ms | 159 MiB | 4.73 |

Quality spans 0.008 against SDs up to 0.016, so no size is read as better. On cost, 64k → 32k saves 22% of the Q8_0
file for 1.2% more latency and 6% more energy; 32k → 16k saves 14% for 11% more latency and 8% more energy; 16k → 8k
saves 8% for 10% more latency and 11% more energy. No size was selected on task results. This repository publishes
32,768 because it is the last step where the latency cost stays near 1% — a judgement about the trade, not a score; it
did not score best. The three unpublished sizes would be named `vocab15k`, `vocab24k` and `vocab72k`.
[`root_manifest.json`](root_manifest.json) keeps the wording of 2026-09-20 for this reason (`why_this_grid_point`,
`size_selection_basis`); the reason given here is the corrected one.

![smaller vocabulary, more tokens, more cost](benchmark/figures/18_vocabulary_cost_inversion.png)

---

## Deployment

### GPU (PyTorch)

Compile as in [Quick start](#make-it-fast-on-a-gpu). 8-bit quantization inside PyTorch was also measured on the same
GPU, in a separate run, with torchao (W8A8: 8-bit weights and 8-bit activations). The compiled rows below use
`dynamic` at its default (C's middle column); the Quick start setting, `dynamic=False`, was not run with INT8.

| path | document p50 | weights in memory | macro F1 | decisions that differ from eager BF16, of 784 |
|---|---:|---:|---:|---:|
| BF16, compiled, `dynamic` default (from C) | 13.6 ms | 230 MiB | 0.5671 | 0 / 3 / 6 |
| INT8 W8A8, compiled | 15.8 ms | 154 MiB | 0.5595 | 20 / 27 / 27 |
| INT8 W8A8 + INT8 embedding, compiled | 14.9 ms | 118 MiB | 0.5590 | 26 / 25 / 28 |

The INT8 run's own eager BF16 reference was 32.0 ms and 0.5701. On this GPU INT8 bought size, not speed. Compiled W8A8
scored below eager BF16 on every seed, by 0.009 to 0.012 (mean 0.0105), more than either arm's three-seed SD (0.0076 and
0.0074); against compiled BF16 (0.5671 ± 0.0105) the gap is 0.008, inside that SD. Eager W8A8 did not move (+0.0006).
Sizes are the PyTorch state dict in memory, not a file; the Q8_0 GGUF file is 124 MiB. Details:
[`benchmark/int8/`](benchmark/int8/).

### CPU (PyTorch)

Measured on an AMD Ryzen 5 7500F (six threads), per document, three seeds, on the root retrained with FP32 weights
(B):

| path | document p50 | weights in memory | decisions that differ from FP32, of 784 |
|---|---:|---:|---:|
| FP32 | 758 ms | 460 MiB | — |
| **BF16** | **352 ms** | 230 MiB | 1 / 1 / 1 |
| INT8 W8A8 + INT8 embedding | 441 ms | 118 MiB | 13 / 8 / 17 |

This CPU has native BF16 instructions (`avx512_bf16` in `lscpu`), and on it BF16 was the fastest path that left
decisions nearly unchanged. `torch.ao` `quantize_dynamic` INT8, timed in a separate run on the BF16-trained root, was
faster (about 300 ms) but changed 58 to 70 decisions and cost 0.013 macro F1.

No CPU without native BF16 was measured. Our guess for such a CPU is the gap this one showed on its FP32 and INT8
paths: the root 1.5x to 4.7x behind the encoders.

Compiling the backbone on this CPU gained 1.06x in BF16 at batch 2 (1.24x to 1.33x in FP32 or at batch 16); compiled
end to end on a CPU was not timed.

### CPU (dedicated runtime and containers)

Alongside the model there is a runtime built only to run it: a vendored, patched copy of
[llama.cpp](https://github.com/ggml-org/llama.cpp) that builds one binary for Q8_0 classifiers.

- **Needs:** an x86 CPU with AVX-512 VNNI, and a GGUF that includes a classification head. This root is headless, so
  train a head first.
- **Does:** reads each window once, so it allocates no KV cache; runs the head inside the graph; uses no CPU when idle.
- **Exact:** its specialised path gives bit-identical logits to its generic path.

Details: [`runtime/README.md`](runtime/README.md) and [`benchmark/README.md`](benchmark/README.md#the-dedicated-runtime).
Get the files with the Hub CLI or install git-lfs first ([Train a head](#train-a-head)); without it both containers
stop and say so.

**[`docker/`](docker/) — see it work.** This root's backbone with a 14-label SemEval head attached, as a worked
example rather than a model to judge real documents with. Measured there, on a 12-core x86 host with 4 runtime
threads: no KV allocation, 173 MiB native RSS, and 56.4 ms of compute for one 28-token window. That is one short
window, not a document, so it does not compare with the per-document times above.

```bash
tar -xzf bundle/runtime_source.tar.gz -C bundle/
docker compose up --build        # then http://127.0.0.1:8787
```

**[`docker-train/`](docker-train/) — your own labels.** Your data in, a Q8 classifier and a serving container out.

```bash
python make_base.py                      # assembles base/ from this repository's weights
tar -xzf vendor/runtime_source.tar.gz -C vendor/
docker compose run --rm validate
docker compose run --rm train-cpu
docker compose run --rm export
docker compose up model
```

On the four bundled examples this ends at `"Please refund this purchase and return the order."` → `refund` 0.999 and
`"배송 상태를 알려주세요."` → `shipping` 0.998. On Microsoft Windows, run the same commands in PowerShell with Docker
Desktop; a clone made before 2026-09-22 has CRLF line endings and must be cloned again
([details](benchmark/README.md#containers-details)).

---

## Evidence and reproducibility

| what | where |
|---|---|
| the 65-model benchmark: every arm's three-seed mean and SD, latency, memory, file size and energy | [`benchmark/full/`](benchmark/full/), [`benchmark/README.md`](benchmark/README.md) |
| the final test: what was fixed in advance, every result, per-label metrics | [`benchmark/README.md`](benchmark/README.md#the-final-test); the report, results and preregistration are in the project's own evidence log, which is not public |
| what costs the time: eager against compiled, the backbone beside encoders on a GPU and a CPU | [`benchmark/cost_isolation/`](benchmark/cost_isolation/) |
| tokenization and window cost | [`benchmark/cost_probe/`](benchmark/cost_probe/) |
| the root beside four encoders on a CPU, with FP32-weight training | [`benchmark/cpu_vs_encoders/`](benchmark/cpu_vs_encoders/) |
| 8-bit quantization in PyTorch | [`benchmark/int8/`](benchmark/int8/) |
| Korean text on the CPU | [`benchmark/korean_input/`](benchmark/korean_input/) |
| all 24 figures; the scripts for 06–24 and the annotation of 01 (01–05 were drawn by earlier sessions whose plotting scripts are not in this repository) | [`benchmark/figures/`](benchmark/figures/) |
| the root's vocabulary rule, layer maps and hashes | [`root_manifest.json`](root_manifest.json) |
| a SHA-256 for every file in this repository | [`SHA256SUMS`](SHA256SUMS) |

Each evidence folder is described in its own README or in
[`benchmark/README.md`](benchmark/README.md#evidence-in-this-folder). The scripts are published as run; most import the
frozen benchmark's modules from the project tree, which is not part of this repository. No `test.jsonl` is included.

## Measurement methods and references

Latency percentiles after untimed warm-up, several cost measures side by side, energy next to accuracy, three seeds
reported as a spread, paired bootstrap intervals, and counts of decisions that change under compression follow
published practice (MLPerf, Reddi et al. 2020; Dehghani et al. 2022; Henderson et al. 2020; Reimers and Gurevych 2017;
Koehn 2004; Hooker et al. 2019). The tokenizer comparisons draw on Rust et al. 2021 and Petrov et al. 2023. All 40
numbered references (57 sources), each checked against its primary source, with what it is used for and where it
applies only in part: [`benchmark/REFERENCES.md`](benchmark/REFERENCES.md).

---

## Limitations

- **One test evaluation, and not a holdout.** The 2026-09-23 test used a split this project had used before. Every
  other quality number is the calibration split, on which the thresholds were also chosen.
- **The evaluation is small.** 56 documents and 14 labels; the rarest label appears in 6 documents, so one fourteenth
  of macro F1 rides on six samples, which we think is the main source of the seed SDs (0.003 to 0.039 in this card's
  tables, 0.001 to 0.039 across the 62 models not at the floor). Three seeds are run-to-run variation, not a
  confidence interval, and gaps inside them are not ranked.
- **The 65-model ranking used BF16-weight training.** Retrained with FP32 weights, four encoders scored 0.026 to 0.031
  higher, and their mean ± SD intervals overlap the root's. How much of the root's position in B comes from the
  protocol is not known.
- **The situations are ours, and few.** Quality comes from one English propaganda-technique task; step 1 comes from one
  small internal set. The model was not built for either; they are the situations we set up to watch the compression.
- **Korean is measured for tokenization and speed only.** No Korean quality evaluation exists here.
- **The layer maps were chosen on labelled data**, and that choice is in the weights; it is disclosed, not repaired.
- **Quality numbers belong to classifiers trained on this backbone**, not to the headless root itself.
- **Hardware.** One RTX 5070 Ti and one Ryzen 5 7500F for PyTorch; the Arduino UNO Q edge board for step 1 only.
  Other GPUs, Apple silicon and other CPUs were not measured for this root.
- Long-context behaviour, probability calibration, robustness, fairness and production safety are not established. Do
  not use this model as a fact checker, a safety filter or an autonomous decision maker.

## Files

| path | what |
|---|---|
| `model.safetensors`, `config.json`, tokenizer files | the headless backbone |
| [`root_manifest.json`](root_manifest.json) | its vocabulary rule, layer maps and hashes; its `why_this_grid_point` keeps the wording of 2026-09-20 (corrected in step 6) |
| [`benchmark/`](benchmark/) | every measurement behind this card, with scripts and figures |
| [`distillation/`](distillation/) | the reusable 24 → 8 → 6 → 4 distillation platform; it does not cut vocabularies |
| [`runtime/`](runtime/) | the dedicated runtime's two C++ sources, patched to accept a cut vocabulary, and its README |
| [`docker/`](docker/), [`docker-train/`](docker-train/) | the two CPU containers |
| [`models/semeval-propaganda/`](models/semeval-propaganda/) | a separate lineage, not a child of this root |
| `v128k_remap_manifest.json` | the one surviving record of the superseded 128k root |
| [`SHA256SUMS`](SHA256SUMS) | a SHA-256 for every file |

## License and attribution

Apache-2.0 for the released code and model artifacts, subject to upstream model and data terms. Qwen3.5 is attributed
to Qwen. Transformers, PyTorch, Hugging Face Hub, WikiText and SemEval remain the work of their authors, and no WikiText
or SemEval source records are redistributed. The Korean speed measurement used articles from
`daekeun-ml/naver-news-summarization-ko`; only their row indices and links are included here, not the article text.
The WikiText dataset page carries a license wording discrepancy — its metadata lists CC BY-SA 3.0 and GFDL while its
prose says CC BY-SA 4.0 — so check [`Salesforce/wikitext`](https://huggingface.co/datasets/Salesforce/wikitext)
directly.
