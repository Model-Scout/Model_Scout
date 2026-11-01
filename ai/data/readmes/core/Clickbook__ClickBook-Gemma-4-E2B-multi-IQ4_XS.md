---
license: apache-2.0
license_link: https://ai.google.dev/gemma/docs/gemma_4_license
base_model: google/gemma-4-E2B-it
library_name: gguf
pipeline_tag: text-generation
tags:
  - gguf
  - llama.cpp
  - on-device
  - mobile
  - vocabulary-pruned
  - quantized
language:
  - en
  - de
  - ar
  - fr
  - es
  - it
  - pt
  - nl
  - pl
  - tr
  - ru
  - zh
  - ja
  - ko
  - hi
  - ta
  - th
  - he
---

# ClickBook Gemma 4 E2B — multilingual, vocabulary-pruned, IQ4_XS

An on-device reading assistant model. A reader taps a word in a book; the model
explains it in the sense that sentence gives it, writes fresh examples, translates
the word, and translates the passage.

**1.844 GB**, built to fit a 1.85 GB application budget on iOS and Android.

## What was changed from the base model

1. **Vocabulary pruned from 262,144 to 231,955 tokens.** Scripts not served by the
   product were removed: Bengali, Gurmukhi, Gujarati, Oriya, Telugu, Kannada,
   Malayalam, Sinhala, Lao, Tibetan, Myanmar, Georgian, Ethiopic, Cherokee and
   others. Latin, Cyrillic, Arabic, CJK, Hangul, Devanagari, Tamil, Thai, Greek
   and Hebrew are retained.

   This matters more than it would in most architectures: Gemma 4 carries
   per-layer embeddings, so a vocabulary token costs **10,496 parameters** — about
   3.49 KB in this quantisation. Vocabulary is roughly a third of the file.

2. **Quantised to IQ4_XS** with **Q2_K token embeddings**, guided by an importance
   matrix computed over 1,538 calibration chunks.

   Embedding tensors are deliberately left out of imatrix guidance because they
   cannot benefit from it — embedding lookups are gather operations, not matrix
   multiplications, so `llama-imatrix` never observes them.

## Files

| file | purpose |
|---|---|
| `ClickBook-Gemma-4-E2B-multi-IQ4_XS.gguf` | the model |
| `prompts.json` | every prompt, per language, with placeholders and token caps |
| `MOBILE-INTEGRATION.md` | integration guide for client developers |

## Usage

```bash
llama-server -m ClickBook-Gemma-4-E2B-multi-IQ4_XS.gguf -c 2048 -ngl 99 --jinja
```

```jsonc
{
  "messages": [{ "role": "user", "content": "<prompt from prompts.json>" }],
  "temperature": 0.1, "top_k": 40, "top_p": 0.9, "repeat_penalty": 1.05,
  "max_tokens": 111,
  "chat_template_kwargs": { "enable_thinking": false }
}
```

### `enable_thinking: false` is required

Without it the model reasons before answering, spends the entire token budget in
`reasoning_content`, and returns **empty `content` with `finish_reason: "length"`**.
That is indistinguishable from a broken model or an unsupported language. If you
want reasoning, raise every cap to 1000 first.

## Language support

Support is uneven and the model card should be believed over the language tag list
above, which cannot express degrees.

| languages | reading | answering | evidence |
|---|:--:|:--:|---|
| English, German, Arabic | yes | yes | 90-item benchmark, two seeds |
| French, Portuguese, Spanish, Italian, Russian, Dutch, Polish, Turkish | yes | not yet | 183 items each on an earlier build, 69–86 |
| Chinese, Japanese, Korean, Hindi, Thai, Hebrew | yes | yes | smoke-tested, 4/4 tabs pass |
| Tamil | yes | **no** | passage translation into Tamil is corrupted |
| Greek | **no** | **no** | output mixes scripts and invents words |

**Greek is broken. Do not enable it.** Only 1,511 Greek tokens survived the prune,
which is not enough for coherent generation; output splices Cyrillic letters and
German words into Greek text.

**Tamil should be read but not written to.** Translating a passage into Tamil
produced Han, Kana and Hangul characters spliced into Tamil script.

The six smoke-tested languages passed every automated check and read two
deliberately hard idiomatic taps each correctly — 手が空いた, 발이 넓다, हाथ धोना,
ใจดี, יד חמה. That is a handful of sentences, not a benchmark. Treat them as beta.

## Evaluation

Measured on a 90-item held-out set of tapped words in English, German and Arabic,
graded 0–100 by an LLM judge against a rubric containing a reference sense. Same
prompts, sampler and seed throughout; the only variable is the model file.

| build | vocabulary | size | score | failures |
|---|---:|---:|---:|---:|
| same weights at **f16** | 231,955 | 8.676 GB | 80.5 | 12 |
| **this model** | 231,955 | **1.844 GB** | **79.2** | 15 |
| narrower prune, 11 languages | 180,850 | 1.666 GB | 79.0 | 15 |
| **unpruned vocabulary**, same quantisation | 262,144 | 1.950 GB | **63.6** | 23 |

Three things this shows.

**Quantisation is nearly free.** IQ4_XS with Q2_K embeddings costs **1.3 points**
against the same weights at f16, for a **4.7× smaller file** — 8.676 GB to 1.844 GB.

**Restoring seven scripts is free.** Going from 180,850 to 231,955 tokens — adding
CJK, Hangul, Devanagari, Tamil, Thai, Greek and Hebrew — moved the score by 0.2 and
the failure count not at all.

**Pruning is not only a size optimisation, it is a quality one.** The unpruned
262,144-token vocabulary, built with an identical recipe and imatrix, scores
**15.6 points lower** and fails 23 items instead of 15. The regression is worst on
the *easiest* third of the set (91.5 → 70.8). A plausible mechanism is that at
Q2_K precision the embedding table and output distribution spend capacity on tens
of thousands of tokens the model never needs, at the expense of the tokens it
does. The measurement is single-seed and reported as measured; the explanation is
a hypothesis.

### Packaging note for mobile

The file compresses by only 3% (ratio 0.970) — quantised weights are close to
incompressible, so download size is effectively file size. Google Play's asset
pack limit is 1.5 GB per pack, which this model exceeds, so Android delivery needs
**two asset packs** concatenated on device. Every smaller variant above exceeds it
too, so splitting is unavoidable regardless of which build is chosen.

## Limitations

- **Not a chat model.** It is tuned for four narrow tasks driven by the supplied
  prompts. General conversation is out of scope.
- The hardest word senses remain hard: polysemous common words (*bank*, *charge*,
  *Schloss*) are where the 15 failures concentrate.
- No on-device dictionary is bundled. An external sense resource was measured at
  +12.7 points on the same benchmark but is not included here.
- Quality in the newly-restored scripts is established by smoke tests only.

## License and provenance

**Apache License 2.0**, matching the licence declared by the base model,
[`google/gemma-4-E2B-it`](https://huggingface.co/google/gemma-4-E2B-it).

Google additionally publishes a
[Gemma 4 license page](https://ai.google.dev/gemma/docs/gemma_4_license), linked
from the upstream model card; consult it directly for anything the Apache 2.0
grant does not answer.

### Modifications from the base model

Apache 2.0 requires derivative works to state their changes. Two were made, both
described in full above:

1. **Vocabulary pruned** from 262,144 to 231,955 tokens, removing scripts the
   product does not serve.
2. **Quantised** to IQ4_XS with Q2_K token embeddings, guided by an importance
   matrix.

No weights were fine-tuned, distilled or otherwise retrained. Model architecture
and all non-vocabulary tensors are the base model's, requantised.

Gemma is a trademark of Google LLC. This is an independent derivative, not
endorsed by or affiliated with Google.
