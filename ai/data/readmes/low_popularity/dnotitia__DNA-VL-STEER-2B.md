---
license: apache-2.0
library_name: sentence-transformers
pipeline_tag: sentence-similarity
base_model:
- Qwen/Qwen3-VL-Embedding-2B
tags:
- sentence-transformers
- transformers
- multimodal-embedding
- multilingual
- qwen
- embedding
language:
- en
- fr
- de
- es
- zh
- ko
- bn
- fil
- hi
- sw
- te
- ja
- ru
- ar
- vi
- tr
- th
- el
- fa
- fi
- id
- he
- pl
- uk
- nl
- it
- pt
- cs
- sv
- hu
- ro
- hr
- da
- "no"
- mi
- quz
---

# DNA-VL-STEER-2B

**STEER** — **S**teering **T**rajectories onto the **E**stablished **R**esidual-stream.

`DNA-VL-STEER-2B` is a language-bias–calibrated variant of
[**Qwen/Qwen3-VL-Embedding-2B**](https://huggingface.co/Qwen/Qwen3-VL-Embedding-2B).
It keeps everything that makes the base model good — the same architecture, the same
2048-dim shared image/text/video embedding space, the same instruction-aware interface —
and closes most of the **cross-lingual retrieval gap**: low-resource languages that lagged
far behind English in the frozen model are pulled up sharply, while English, the other
high-resource languages, and the vision side are preserved.

> **What's new in this release.** This version is calibrated on **all 36 XM3600 languages**
> (previous releases used 11). Broadening the calibration set does two things: it lifts the
> low-resource languages *further*, and — crucially — it **extends the gains to the languages a
> language-limited calibration left behind**. On the full 36-language XM3600 pool, mean
> image→text R@1 goes **59.8 → 70.3** and text→image **48.7 → 59.5**. The 25 languages that were
> *outside* the earlier 11-language calibration (and actually regressed under it) now **improve
> from 61.4 → 72.2 (i2t)**.

It is a **drop-in replacement**: load it exactly like the base model and the API is
identical. Under the hood only the early residual-stream layers are adjusted; every other
weight (including the entire vision tower) is bit-identical to the base.

- **Base model:** Qwen/Qwen3-VL-Embedding-2B (28 layers, 2048-dim, 32K context, MRL 64–2048)
- **Modalities:** text · image · screenshot · video · arbitrary interleaved combinations
- **Calibrated languages (36):** en, fr, de, es, zh, ko, bn, fil, hi, sw, te, ja, ru, ar, vi,
  tr, th, el, fa, fi, id, he, pl, uk, nl, it, pt, cs, sv, hu, ro, hr, da, no, mi, quz
  — i.e. the full XM3600 language set, spanning high-resource, low-resource, and
  previously-unseen languages.
- **Korean** improves across every retrieval benchmark (**+4 to +7 R@1**), image and video
  alike — see the dedicated section below.

---

## Usage

Because the release copies the base model's Sentence-Transformers configuration verbatim,
usage is **identical to `Qwen/Qwen3-VL-Embedding-2B`** — only the model id changes.

> ### Requires `transformers >= 5.0`
> ```bash
> pip install "transformers>=5.0" sentence-transformers qwen-vl-utils
> ```
> **Enforced automatically.** This repo declares a `requirements` field in
> `config_sentence_transformers.json`, so recent `sentence-transformers` versions raise a clear
> error *before any weights load* when `transformers` is too old — nothing to check by hand.

<details>
<summary><b>Why the floor exists</b> — older <code>transformers</code> loads RANDOM weights <b>silently</b></summary>

On `transformers 4.57.x` and earlier, `Qwen3VLModel.base_model_prefix` is `""` while the
checkpoint stores its 625 tensors under a `model.` prefix, so **zero keys match** and the model
is randomly initialized. There is no error — only a `newly initialized` warning that is easy to
miss, and embeddings that look plausible but are meaningless. This affects the **base
`Qwen/Qwen3-VL-Embedding-2B` identically**; it is not specific to STEER.

The `requirements` check runs inside `SentenceTransformer.__init__`. If you are on an older
`sentence-transformers` that predates that field, or you load the weights without Sentence
Transformers, the check does not run — verify manually:

```python
from sentence_transformers import SentenceTransformer
m = SentenceTransformer("dnotitia/DNA-VL-STEER-2B")
a, b, c = m.encode(["a photo of a cat", "a picture of a cat", "quarterly earnings fell"])
print(float(a @ b) > float(a @ c) + 0.1)   # must be True
```
</details>

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("dnotitia/DNA-VL-STEER-2B")
```

### 1. Text alone

```python
sentences = [
    "고양이가 창턱에서 자고 있다.",           # Korean: "A cat is sleeping on the windowsill."
    "Un chat dort sur le rebord de la fenêtre.",  # French, same meaning
    "The stock market fell sharply today.",
]
emb = model.encode(sentences)          # (3, 2048), L2-normalized
print(model.similarity(emb, emb))      # the KO/FR pair scores high; the finance line low
```

### 2. Image alone

```python
images = [
    "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-VL/assets/demo.jpeg",
    "/path/to/local/photo.jpg",        # local paths work too
]
img_emb = model.encode(images)         # (2, 2048)
```

### 3. Interleaved (text + image in one input)

Pass a dict with `text` and/or `image`. This is how you embed a captioned image, a
screenshot with a question, a document page with a title, etc.

```python
documents = [
    {"text": "A golden retriever offering its paw on a beach at sunset.",
     "image": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-VL/assets/demo.jpeg"},
    {"text": "City skyline at night."},                       # text-only entry
    {"image": "/path/to/local/photo.jpg"},                    # image-only entry
]
doc_emb = model.encode(documents)      # (3, 2048)
```

### 4. Cross-lingual, cross-modal retrieval

All modalities and languages share one space, so a query in any language retrieves
matching images/text directly:

```python
queries = [
    "해변에서 강아지와 노는 여자",          # Korean query
    "mujer jugando con su perro en la playa",  # Spanish query
]
gallery = [
    "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-VL/assets/demo.jpeg",
    {"text": "A woman plays with her golden retriever on a sunlit beach."},
    {"text": "A city skyline viewed from a rooftop at night."},
]
q = model.encode(queries)
g = model.encode(gallery)
print(model.similarity(q, g))          # both queries rank the beach image/caption first
```

### 5. Video

Pass a `video` key. **An `.mp4` path works and a list of frame paths works — a directory does
not.** The two working routes are not the same protocol, so pick deliberately:

| you pass | sampling | matches our reported numbers? |
|---|---|---|
| `"/path/to/clip.mp4"` | `fps=1`, capped at 64 frames | no — close, but not identical |
| `["f0.jpg", "f1.jpg", ...]` | uniform 64 + pixel budget | **yes** — this is what we benchmarked |
| `"/path/to/frames_dir"` | — | **no — fails silently, see warning** |

```python
# convenient: let the loader decode the file (fps=1, capped at 64 frames)
vid_emb = model.encode([{"video": "/path/to/clip.mp4"}])

# reproducible: uniform 64 frames, the protocol behind every video number in this card
import decord, numpy as np
vr  = decord.VideoReader("/path/to/clip.mp4")
idx = np.linspace(0, len(vr) - 1, 64).astype(int)
frames = [...]                                   # save/collect those 64 frames as paths or PIL
vid_emb = model.encode([{"video": frames}])

# text -> video retrieval: same instruction on both sides
q = model.encode(["a person kneading dough on a floured counter"])
print(model.similarity(q, vid_emb))
```

> ### Never pass a directory path as `video`
> The video backends cannot open a directory, the error is swallowed, and you get an embedding
> that does not depend on the input at all — we
> measured cosine **1.0000** between three different clips passed this way (the same clips as
> frame lists: 0.57–0.67). Nothing raises, so this corrupts a retrieval index silently. Expand
> the directory to a sorted list of frame paths yourself:
> `{"video": sorted(glob.glob(f"{d}/*.jpg"))}`.

Uniform **64 frames** is the protocol behind the reported video numbers; fewer will cost you
accuracy on anything temporal. Note the `.mp4` route samples at 1 fps, so a clip shorter than
64 s yields fewer than 64 frames — for short clips the two routes diverge most.

### 6. Zero-shot classification

Put the **task instruction on the media side** and leave the class names on the neutral
default. Do **not** wrap labels in a template, and **do not lowercase them** — see the measured
effects below.

```python
labels = ["ApplyEyeMakeup", "Knitting", "PlayingGuitar"]   # keep original casing
lab_emb = model.encode(labels)                             # neutral default prompt

vid_emb = model.encode(
    [{"video": "/path/to/clip.mp4"}],
    prompt="Recognize the category of the video content.",  # task instruction here
)
pred = labels[int(model.similarity(vid_emb, lab_emb).argmax())]
```

### 7. Task instructions & custom dimensions (inherited from the base)

The model is instruction-aware and supports Matryoshka (MRL) output dimensions (64–2048).
Per Qwen's guidance, **write instructions in English even for non-English inputs**.

```python
# custom instruction — see the measured effect below
q = model.encode(queries, prompt="Retrieve the image that matches this description.")

# shorter embeddings via MRL — truncate + renormalize, no second model load
import numpy as np
emb512 = emb[:, :512]
emb512 /= np.linalg.norm(emb512, axis=1, keepdims=True)

# (SentenceTransformer(..., truncate_dim=512) also works, but loads the model a second time —
#  slicing an existing embedding is identical and free.)
```

**How much does the instruction matter?** Measured on video classification, swapping the
neutral default for a task instruction (`"Recognize the category of the video content."`):

| task | labels | gain |
|---|---|---|
| Kinetics-700 | 519 fine-grained | **+3.8** |
| SomethingSomethingV2 | 175, fragments like `holding pen` | **+3.7** |
| Breakfast | 10 bare nouns | **+1.8** |
| UCF101 | 101 distinctive compounds | +0.1 |
| HMDB51 | 51 | 0.0 |

The gain scales with how **ambiguous** the label set is — large or fragmentary label sets
benefit, already-distinctive labels do not. A CLIP-style template (`"a video of {}"`) does
**not** help and slightly hurts once a proper instruction is set.

**Keep label capitalization.** On UCF101, lowercasing class names costs **−5.4** and splitting
CamelCase costs a further −1.5; `ApplyEyeMakeup` (94.3) beats `apply eye makeup` (91.4) beats
`applyeyemakeup` (88.9). Capitalization does word-segmentation work the tokenizer relies on.

> ### Pro tip — sharp reproduction
> STEER inherits the base model's exact preprocessing protocol, and the reported numbers
> depend on it. To reproduce cleanly:
> - **Load in `bfloat16`** and **L2-normalize** outputs (Sentence-Transformers does this by default).
> - **Keep the official image pixel budget** — `min_pixels = 4·32²`, `max_pixels = 1800·32²`,
>   patch size 16, and **do not let your image loader pre-downscale**; feeding smaller
>   images than the protocol is the most common cause of "my numbers are lower than the card".
> - **Pooling is last non-pad token** of the post-final-RMSNorm hidden state — don't substitute
>   mean-pooling.
> - **Check your `max_length` against your actual documents.** Harnesses commonly default to
>   8192 (the official MMEB value) while this model has a **32K** context. On a long-document
>   benchmark that silently truncates: we measured 13.5 against a published 94.4 purely because
>   documents ran to ~24.5k words and the answer sat past the cut.
> - **Fix the batch size when two runs must match exactly.** Right padding plus last-token
>   pooling makes embeddings mildly batch-composition dependent (~5e-3), which is ±0.2–0.7 on a
>   small benchmark. Same batch size ⇒ bit-identical results.
> - **Instructions in English**, even for non-English queries, and reuse the *same* instruction
>   across the query/document sides you intend to compare.
> - The calibration boost covers the **36 languages listed above** — expect the largest lifts on
>   low-resource languages and preservation on English and the vision side (see below).

---

## Performance

All numbers are **frozen base → STEER** on the official post-norm protocol. STEER's design goal
is to lift low-resource languages *without* paying for it on English or vision, so read the
tables as: **big LRL gains, high-resource preserved, small honest costs where they exist.**

### Korean capability

Korean is one of the calibrated languages, and it gains sharply in **both** directions on
**every** retrieval benchmark — image and video — while nothing about the English side is
sacrificed. If your workload is Korean-centric, STEER is a clear upgrade over the base model.

**Korean image↔text retrieval (R@1, frozen → STEER):**

| Benchmark | image→text | text→image |
|---|---|---|
| XM3600 (full pool) | 70.2 → **75.0** (+4.8) | 57.9 → **64.2** (+6.3) |
| Flickr30k-1k | 71.3 → **78.7** (+7.4) | 68.4 → **79.5** (+11.1) |
| XTD-1k | 58.8 → **64.9** (+6.1) | 53.6 → **63.8** (+10.2) |

**Korean zero-shot video retrieval (R@1, frozen → STEER)** — trained only on image–text, transfers to video:

| Dataset | text→video | video→text |
|---|---|---|
| MSR-VTT | 39.7 → **43.6** | 39.7 → **42.4** |
| DiDeMo | 38.4 → **43.1** | 34.9 → **43.0** |
| MSVD | 47.4 → **53.7** | 73.6 → **78.2** |
| VATEX | 31.5 → **38.3** | 47.7 → **55.4** |

### Multilingual image↔text retrieval — XM3600 (R@1, full 3,600-image pool)

Calibrated on all 36 languages, the gains now cover the **entire** XM3600 language set — the
low-resource tier jumps, and the languages that were previously *outside* the calibration
(and lost ground under a language-limited calibration) now improve too.

| Tier | image→text | text→image |
|---|---|---|
| **HRL-6** (high-resource) | 75.3 → **77.8** | 64.7 → **67.4** |
| **LRL-5** (low-resource) | 32.8 → **51.8** (+19.0) | 21.2 → **41.0** (+19.8) |
| **+25 additional languages** | 61.4 → **72.2** (+10.8) | 50.4 → **61.2** (+10.8) |
| **Overall-36** | 59.8 → **70.3** (+10.5) | 48.7 → **59.5** (+10.8) |

<sub>Protocol: every caption is used as a query (~7,200 per language) against the full
3,600-image pool. A first-caption-only protocol gives lower i→t absolutes because there is
then one relevant caption per image instead of ~2; the frozen→calibrated deltas are the same
either way. These figures are computed by the same harness as the benchmark report attached
to this repo, so the two agree cell for cell.</sub>

The high-resource↔low-resource R@1 gap (i→t) narrows from **42.6 → 25.9**.

### Cross-benchmark multilingual retrieval (R@1)

| Benchmark | HRL i→t | LRL i→t | HRL−LRL gap |
|---|---|---|---|
| **Flickr30k-1k** | 79.1 → 82.9 | 48.7 → **74.5** (+25.8) | 30.4 → **8.4** |
| **XTD-1k** | 67.5 → 71.4 | 42.5 → **63.3** (+20.8) | 25.1 → **8.1** |

### Zero-shot cross-modal transfer — video retrieval (Text→Video R@1)

Trained only on image–text, yet low-resource **video** retrieval improves and English is preserved.

| Dataset | en | ko | zh |
|---|---|---|---|
| MSR-VTT | 53.1 → 50.7 | 39.7 → **43.6** | 47.6 → 49.6 |
| DiDeMo | 54.8 → 53.9 | 38.4 → **43.1** | 48.5 → 49.4 |
| MSVD | 61.1 → 60.8 | 47.4 → **53.7** | 53.6 → 56.8 |
| VATEX | 47.8 → 47.5 | 31.5 → **38.3** | 44.2 → 44.6 |

### MIEB (Multilingual) — 130-task battery, Overall = mean of 10 category means

| | Overall | Multilingual retrieval | (other 9 categories) |
|---|---|---|---|
| frozen | 66.71 | 64.80 | preserved |
| **STEER** | **67.86** | **71.98** | preserved |

The multilingual-retrieval category rises **+7.18** while the nine non-target categories move
within noise: 9 of 10 categories improve and the only decline is document understanding at
−0.33. Recomputed on the identical 130 tasks for every model with full coverage.

<sub>Overall is the mean of the 10 task-type means, per the MIEB(Multilingual) definition — not
a flat mean over the 130 tasks (a flat mean gives 60.06 → 60.53 and understates the effect,
because the 3-task multilingual-retrieval category is swamped by the 45-task general-retrieval
one). English visual STS is 79.88 → 80.24; an earlier version of this card reported
77.2 → 80.2 for that row, which came from a mis-slice of the VisualSTS aggregate tasks.</sub>

### Document retrieval (preservation check)

| Benchmark | frozen → STEER |
|---|---|
| ViDoRe (v3) (nDCG) | 52.9 → 53.2 |

Multilingual visual-document retrieval is unchanged — calibration does not disturb the
document-understanding capability of the base model.

### Honest limitations

- **Calibration targets the multilingual visual-caption domain.** The gains are largest on
  multilingual image/text/video retrieval across the 36 calibrated languages. Languages entirely
  outside this set, and abstract text-only domains far from visual captions, should be expected
  to see little change rather than a large lift.
- **Breadth trades against per-language peak.** Spreading calibration across all 36 languages
  gives each low-resource language a slightly smaller individual boost than a calibration
  narrowly focused on a handful of them would, but coverage is uniform across the language set.
- **Some tasks regress — pick the variant per workload.** An earlier version of this card said
  nothing regresses relative to the frozen base. That is not correct, and broader evaluation
  since has measured where it does:

  | workload | STEER vs frozen |
  |---|---|
  | Multilingual retrieval (XM3600, ko/zh video) | **+5 to +11** |
  | Abstract text retrieval (Wikipedia multilingual) | **−7.9 R@1** (2B), −4.1 (8B) |
  | Video action classification | **−4 to −9** |
  | Fine-grained visual (logo retrieval) | **−3.1 mAP** |

  The calibration is *visual-vocabulary specific*: it helps caption-like multilingual retrieval
  and costs abstract text and fine-grained visual discrimination. If your workload is English,
  text-only, or fine-grained classification, **use the frozen base model.** The effect also
  attenuates with size — at 8B the gains shrink and several tasks turn net-negative.
- **Composed queries are not supported.** "This video, but with X changed" does not work: on
  Dense-WebVid-CoVR both an instruction-conditioned composition and a vector-sum composition
  scored *below* using the edit target's caption alone. The model was trained for symmetric
  similarity, not edit-application; no inference-time prompt recovers it.
- **Matryoshka truncation is task-dependent.** Degradation is smooth and monotonic at every
  width, but how much you can cut varies enormously: text retrieval keeps **99.6%** of its
  score at 64 dims, while fine-grained logo retrieval keeps only **49.5%**. At 512 dims the
  median cost across 15 benchmarks is **1.6%**. Measure on your own task before truncating hard.

---

*Derived from `Qwen/Qwen3-VL-Embedding-2B`. Vision tower and all layers outside the early
residual-stream are unchanged from the base model. Calibrated on the full 36-language XM3600
set.*
