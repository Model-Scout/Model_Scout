---
license: gemma
base_model: google/gemma-4-31b-it
tags:
  - depth-expansion
  - layer-insertion
  - gemma
  - gemma4
  - korean
  - legal
  - reasoning
  - qlora
language:
  - en
  - ko
pipeline_tag: text-generation
library_name: transformers
---

# extGemma4-40.5B

**extGemma4-40.5B** is a depth-expanded language model built by inserting new
transformer layers into a fine-tuned Gemma 4 31B-IT and then *healing* the model back
to health with lightweight training. It grows the network from 60 to 77 layers
(~40.5B parameters) **without** collapse or catastrophic forgetting — the central thing
this model is meant to demonstrate.

> **Why this model exists.** Conventional wisdom says that altering the architecture of
> an already fine-tuned model tends to break it. This model is a counter-example: with
> careful layer initialization and staged healing on a small dataset, the inserted
> capacity integrates cleanly and even begins to contribute to reasoning.

---

## What makes it different

Most layer-insertion methods initialize new layers as identity (pass-through) functions.
That's safe but starves the new layers of any learning signal — they contribute nothing,
so they receive almost no gradient and never learn. An earlier 88-layer attempt by the
authors failed exactly this way.

**extGemma4-40.5B instead initializes each new layer as an interpolation of its
neighbors**, so the layer is doing something meaningful from step one and can actually be
trained. Combined with careful insertion placement and a two-phase healing schedule
(freeze-then-anneal), the surgery heals rather than degrades.

## Results

### GPQA-Diamond (graduate-level science reasoning, 198 items, CoT)

| Model | GPQA-Diamond (flexible-extract) |
|---|---|
| Original fine-tune (60 layers) | 0.798 |
| Identity-init expansion, healed | 0.596 |
| **extGemma4-40.5B (interpolation-init, Phase 1)** | 0.641 ± 0.034 |
| **extGemma4-40.5B (interpolation-init, Phase 2 / final)** | **0.728 ± 0.034** |

The expanded model **recovers ~65% of the deficit** introduced by the surgery and reaches
**~91% of the original model's score**, using only selective freezing, QLoRA, and a small
(~45k example) STEM + Korean-legal dataset.

> Evaluation used a 4,000-token generation budget with greedy decoding. The baseline for
> comparison was fine-tuned on the *same* dataset, so the expanded model gets no unfair
> advantage from data familiarity.

### Self-healing of a structural defect

At initialization and after Phase 1, the expanded model had a structural generation flaw:
on certain low-probability, jargon-heavy paths it would derail into repeated non-Latin
characters and never terminate. This is **not** a training artifact — it appeared
identically before any healing, i.e. it was baked into the freshly-expanded structure.

During Phase 2 annealing the model **healed this defect on its own**:

| Stage | Behavior on the trigger prompt |
|---|---|
| Before healing | Injects non-Latin tokens, loops, never terminates |
| ~13% into Phase 2 | One malformed token, then self-corrects and finishes |
| ~50% and beyond | Fully fluent, terminates correctly |

Across a 10-domain English probe (physics, biology, history, philosophy, literature,
riddle, logic, math proof, economics, medicine), the healed model shows **0/10 collapse**
and **0/10 cross-script contamination**, and terminates cleanly on all 10.

### Emergent reasoning: it can out-reason its own parent

On a physics question — comparing the energy of a photon and an electron with equal
de Broglie wavelength — the **original** model answered incorrectly (it omitted the
electron's rest-mass energy). **extGemma4-40.5B answered correctly**, applying the
relativistic energy–momentum relation. The newly inserted capacity isn't decorative; on
this problem it does reasoning the base model could not.

## Intended use

- Research on depth expansion, layer insertion, and model "healing."
- English and Korean text generation and reasoning.
- Korean-legal-flavored assistance (the healing data included Korean legal chain-of-thought).

This is a **research artifact** demonstrating a method. It is close to, but does not beat,
its original parent on general benchmarks — and that was never the goal. The goal was to
show the surgery can be survived.

## Limitations & notes

- **Not a strict upgrade over the base model.** It recovers ~91% of the original GPQA
  score; on most tasks expect parity-or-slightly-below, with occasional pockets (like the
  physics case above) where the added depth helps.
- Minor rough edges remain in generation (e.g. an occasional clumsy self-correction on
  under-specified logic puzzles). No collapse, but not flawless polish.
- Inherits the base model's licensing, biases, and knowledge cutoff.
- The chat format and EOS handling follow the base Gemma 4 IT conventions; use the same
  chat template.

## How to use

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "your-org/extGemma4-40.5B"
tok = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.bfloat16, device_map="auto")

msgs = [{"role": "user", "content": "Explain in two sentences why the sky is blue."}]
ids = tok.apply_chat_template(msgs, add_generation_prompt=True, return_tensors="pt").to(model.device)
out = model.generate(ids, max_new_tokens=512, do_sample=False)
print(tok.decode(out[0][ids.shape[1]:], skip_special_tokens=False))
```

## Method summary (for the curious)

1. **Interpolation initialization.** Each inserted layer starts as a position-aligned
   blend of its neighboring layers — off-identity but coherent — so gradients flow from
   the first step.
2. **Careful placement.** Layers are inserted at stable positions within attention blocks,
   avoiding block boundaries and the block-terminal global-attention layers.
3. **Two-phase healing.** Phase 1 trains only the inserted layers (originals frozen);
   Phase 2 anneals the whole network. Both use QLoRA on a small STEM + Korean-legal
   dataset.

A fuller write-up (including why identity initialization silently fails on this
architecture, and why certain "obvious" fixes are no-ops) is available separately.

## Citation

```bibtex
@misc{extgemma4_2026,
  title  = {extGemma4-40.5B: Depth Expansion of a Fine-Tuned Gemma 4 via
            Interpolation-Based Layer Insertion},
  author = {Park, Sungjin and Park, Jungjoon},
  year   = {2026},
  note   = {Nextnine},
  howpublished = {\url{https://huggingface.co/your-org/extGemma4-40.5B}}
}
```

## Acknowledgements

Built on Google DeepMind's Gemma 4. Thanks to the r/LocalLLaMA community for feedback on
the earlier (failed) expansion attempt that motivated this work.