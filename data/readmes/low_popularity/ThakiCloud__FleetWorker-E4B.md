---
library_name: transformers
license: other
license_name: openmdw-1.1
license_link: https://openmdw.ai/license/1-1/
base_model: nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16
base_model_relation: finetune
pipeline_tag: text-generation
language:
- en
- ko
tags:
- lora
- gemma4
- nemotron
- on-device
- task-triage
- classification
- agents
- thakicloud
---

# FleetWorker-E4B

Version 1.0.0. Fine-tune of [nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16) published as `ThakiCloud/FleetWorker-E4B`.

Korean card: [MODEL_CARD.ko.md](./MODEL_CARD.ko.md)

FleetWorker-E4B is a small on-device classifier for task-board items. Given the title of an item it names the work stream (project) the item belongs to, with a priority suggestion in the same JSON object. The project label is the useful output. The released model was trained on descriptive, generic work-stream names in place of the board's internal project names, so no internal names are in the weights; this costs about 3 points of project accuracy against the internal-name model. The priority field is not reliable: on items whose priority was never set it answers P0 for about 8 in 10. Use the project field only, and never show the priority as urgency or apply it automatically.

## What it does

The system prompt lists the allowed project labels and the allowed priorities; the user message is the item title (Korean or English). The model replies with exactly one JSON object `{"project":..., "priority":...}`. Project labels are 25 generic work-stream names (for example `synthetic-data-pipeline`, `legal-decision-models`, `point-of-sale-app`), listed in `inference_example.py`; the model can only emit labels from that taxonomy, so use it as a reference for fine-tuning your own board rather than as a drop-in for another taxonomy.

## Intended use

- Suggesting a project label for new task-board items, with a person confirming it.
- Pre-sorting an inbox of items into work streams before review.
- Starting point for your own fine-tune on a different board taxonomy.

## How to use

### Prompt format

The model uses the base checkpoint's chat template with thinking disabled (`enable_thinking=False`). The rendered prompt is exactly:

```text
<bos><|turn>system
You triage a task-board item. Output exactly one compact JSON object with keys "project" and "priority" and nothing else. "project" is one of: <the project labels the model was trained on, comma separated>, or "other"; "unknown" if the text gives no way to tell. "priority" is one of: P0, P1, P2, P3.<turn|>
<|turn>user
title: Add retry with backoff to the nightly export job<turn|>
<|turn>model
```

Output format: one compact JSON object: `{"project":<label from the prompt list, "other" or "unknown">,"priority":"P0"|"P1"|"P2"|"P3"}`.

Replace the angle-bracket project list with the label set you fine-tune for. The example prints the project only: the model still emits a priority field, but it answers P0 for 120 of 151 items whose priority was never set, so do not display it as urgency and do not write it back to the board. If you want a priority hint, show it to a person on explicitly prioritised items only.

### Transformers + PEFT adapter

```python
import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

BASE = "nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16"
tok = AutoTokenizer.from_pretrained(BASE)
model = AutoModelForCausalLM.from_pretrained(BASE, dtype=torch.bfloat16, device_map="auto")
model = PeftModel.from_pretrained(model, "ThakiCloud/FleetWorker-E4B", subfolder="adapter").eval()

import json

SYSTEM = "You triage a task-board item. Output exactly one compact JSON object with keys \"project\" and \"priority\" and nothing else. \"project\" is one of: <the project labels the model was trained on, comma separated>, or \"other\"; \"unknown\" if the text gives no way to tell. \"priority\" is one of: P0, P1, P2, P3."
USER = "title: Add retry with backoff to the nightly export job"
messages = [
    {"role": "system", "content": SYSTEM},
    {"role": "user", "content": USER},
]
inputs = tok.apply_chat_template(messages, add_generation_prompt=True, enable_thinking=False,
                               return_tensors="pt", return_dict=True).to(model.device)
out = model.generate(**inputs, max_new_tokens=64, do_sample=False)
pred = json.loads(tok.decode(out[0, inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
print(pred["project"])  # project only: the priority field is unreliable, see Limitations
```

### Merged BF16

The LoRA delta is merged into the base weights (BF16).

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

tok = AutoTokenizer.from_pretrained("ThakiCloud/FleetWorker-E4B")
model = AutoModelForCausalLM.from_pretrained("ThakiCloud/FleetWorker-E4B", dtype=torch.bfloat16, device_map="auto").eval()

import json

SYSTEM = "You triage a task-board item. Output exactly one compact JSON object with keys \"project\" and \"priority\" and nothing else. \"project\" is one of: <the project labels the model was trained on, comma separated>, or \"other\"; \"unknown\" if the text gives no way to tell. \"priority\" is one of: P0, P1, P2, P3."
USER = "title: Add retry with backoff to the nightly export job"
messages = [
    {"role": "system", "content": SYSTEM},
    {"role": "user", "content": USER},
]
inputs = tok.apply_chat_template(messages, add_generation_prompt=True, enable_thinking=False,
                               return_tensors="pt", return_dict=True).to(model.device)
out = model.generate(**inputs, max_new_tokens=64, do_sample=False)
pred = json.loads(tok.decode(out[0, inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
print(pred["project"])  # project only: the priority field is unreliable, see Limitations
```

### llama.cpp (GGUF)

| File | Quantization | Size |
|---|---|---|
| `FleetWorker-E4B-Q4_K_M.gguf` | Q4_K_M, imatrix from training rows (recommended) | 5.34 GB (5335295200 bytes) |
| `FleetWorker-E4B-Q4_K_M-NV.gguf` | Q4_K_M with NVIDIA's recipe (Q8_0 token embeddings, BF16 per-layer projection), imatrix | 6.18 GB (6180447456 bytes) |
| `FleetWorker-E4B-Q8_0.gguf` | Q8_0 | 8.03 GB (8031245280 bytes) |

```bash
llama-server -m FleetWorker-E4B-Q4_K_M.gguf -c 8192 -ngl 99 --port 8080
```

Chat completions apply the template embedded in the GGUF; disable thinking per request:

```bash
curl http://localhost:8080/v1/chat/completions -H 'content-type: application/json' -d '{"messages": [{"role": "system", "content": "You triage a task-board item. Output exactly one compact JSON object with keys \"project\" and \"priority\" and nothing else. \"project\" is one of: <the project labels the model was trained on, comma separated>, or \"other\"; \"unknown\" if the text gives no way to tell. \"priority\" is one of: P0, P1, P2, P3."}, {"role": "user", "content": "title: Add retry with backoff to the nightly export job"}], "temperature": 0, "chat_template_kwargs": {"enable_thinking": false}}'
```

The reported GGUF numbers were measured by sending token ids rendered with the Hugging Face chat template, so the prompt is byte-identical to the BF16 run. If you call `/completion` with a raw string, check that the server does not add a second `<bos>`.

## Evaluation

Greedy decoding on a held-out test split, same prompts for every arm.

Test split: two held-out sets scored with the gold item text: an independent set of 206 items taken after the training cut-off (held-out validation period plus later items), and a larger test set of 594 items. Project accuracy is over all items; priority is scored on explicitly prioritised items only. FleetWorker-E4B is scored on the alias versions of these files (sha256 prefixes ef19eeee independent, 220269b7 larger); the base and v1 rows on the internal-name versions.
Test file fingerprint (sha256 prefix, from the ledger): 5711ab1b436d5f49, d27e10421aa2dbb3.

| Arm (model) | n | Project acc., independent set | Project acc., larger test set |
|---|---|---|---|
| Bolt base, zero-shot (internal label set) (nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16) | 206 items (independent) / 594 items (larger) | 0.2961 | 0.3855 |
| Earlier version (v1 adapter) (internal label set) (nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16) | 206 items (independent) / 594 items (larger) | 0.4951 | 0.5875 |
| FleetWorker-E4B (nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16) | 206 items (independent) / 594 items (larger) | 0.5291 | 0.5892 |

Run conditions:
- Bolt base, zero-shot (internal label set): greedy decode, enable_thinking=False, transformers 5.19.0; 1x B200
- Earlier version (v1 adapter) (internal label set): greedy decode, enable_thinking=False, transformers 5.19.0; 1x B200
- FleetWorker-E4B: greedy decode, enable_thinking=False, transformers 5.19.0; 1x H100

Caveats recorded with these results:
- Bolt base, zero-shot (internal label set): zero-shot
- Earlier version (v1 adapter) (internal label set): priority on explicitly-set labels only: v1 predicts P2 for everything (recall P2 1.0, P0/P3 0), so its overall priority score equals the default-label share, not skill.
- FleetWorker-E4B: Same items as the real-name v4 sets, with project labels replaced by descriptive generic aliases. On items left at the board default it predicts P0 for 120/151.

### Priority accuracy on explicitly prioritised items

| Variant | n | Independent set (55 items) | Larger test set (243 items) |
|---|---|---|---|
| Bolt base, zero-shot (internal label set) | 55 items | 0.3273 | 0.2716 |
| Earlier version (v1 adapter) (internal label set) | 55 items | 0.3636 | 0.2922 |
| FleetWorker-E4B | 55 items | 0.6 | 0.5432 |
| Always predict the most common class | 55 items | 0.3636 | 0.5267 |

Measured with small_set = the 55 explicitly prioritised items of the independent set; large_set = the 243 explicitly prioritised items of the larger test set. Items left at the board default are excluded.
Caveats: Accuracy over explicitly prioritised items only. The 'always predict the most common class' row is the bar a priority suggestion has to beat; on the larger set FleetWorker-E4B clears it by 1.7 points. On items whose priority was never set it answers P0 for 120 of 151, so the priority field is not usable there.

### Priority by class (explicitly labelled items only)

| Variant | n | P0 recall | P1 recall | P2 recall | P3 recall |
|---|---|---|---|---|---|
| FleetWorker-E4B recall | 55 explicit items | 0.5 | 0.4667 | 0.9412 | 0.0 |
| Earlier version (v1 adapter, internal label set) recall | 55 explicit items | 0.0 | 0.2 | 1.0 | 0.0 |

Measured with the 55 explicitly prioritised items of the 206-item independent test set; recall per priority class.
Caveats: Priority is a suggestion only and is not usable on unprioritised items: on the 151 items left at the board default the model answers P0 for 120, P1 for 27 and P2 for 4. A decode-time prior correction was tried on an earlier version and failed its pre-registered check, so it is not shipped.

### Merged weights and GGUF on the independent set (206 items)

| Variant | n | Project | Priority (explicit items) |
|---|---|---|---|
| Merged BF16 | 206 items | 0.5291 | 0.6 |
| GGUF Q8_0 | 206 items | 0.5291 | 0.6 |
| GGUF Q4_K_M (imatrix) | 206 items | 0.5291 | 0.6 |
| GGUF Q4_K_M-NV | 206 items | 0.5291 | 0.6 |

Measured with hardware H100, 1 GPU; independent set; GGUF runs feed the Hugging Face chat-template token ids to llama-server (llama.cpp 344be0a), greedy.
Caveats: All variants give identical project and explicit-priority accuracy. Leak probe (130 prompts asking for internal identifiers, project-name pattern enforced): 0 hits on merged BF16, Q4_K_M and Q4_K_M-NV; 0 internal names in 1,077 test outputs.

## Training

Method: LoRA fine-tune of the base model, loss on assistant turns only. Values below are copied from the training record.

| Setting | Value |
|---|---|
| LoRA rank r | 16 (from training summary) |
| LoRA alpha | 32 (from training summary) |
| Learning rate | 0.0001 (from training summary) |
| Epochs | 2.0 (from training summary) |
| Target modules | attn+mlp (from training summary) |
| Gradient accumulation | 8 (from training summary) |
| Max sequence length | 4096 (from training summary) |
| Optimizer steps | 1406 (from training summary) |
| Peak GPU memory (GiB) | 17.53 (from training summary) |
| Wall time (s) | 5815.2 (from training summary) |

## Data

Task-board items (title and gold project and priority labels from the board's event log), plus rows built from the board's own rules, plus a smaller set of paraphrases and harder cases written by a larger language model and kept only when code validators confirmed the label was preserved. Internal project names were replaced by descriptive generic aliases (whole-token replacement, 0 residual names, checked by code) before training. Priority labels that were just the board default were masked out of the loss. Train, validation and test splits are disjoint by period and item family. This version was trained from the base weights for two epochs and the checkpoint at step 450 of 1406 was selected on validation loss.

The training data is internal and is not released. This repository contains no dataset files.

Split sizes (items): train 5621, val 145, test 665, test_indep 206.

## Limitations

- Priority is not usable on unprioritised items: on items left at the board default it answers P0 for 120 of 151 in the independent set. On explicitly prioritised items it beats the majority-class baseline (0.600 vs 0.364 on 55 items; 0.543 vs 0.527 on 243 items) and never predicts P3. Use the project field only; never show or apply the priority automatically.
- The base and v1 rows were measured with the internal project names in the prompt and labels; FleetWorker-E4B is scored on the same items with the generic aliases, so the comparison is on the same items but not on identical label strings. A model trained on the internal names reached 0.563 on the independent set; it is not released.
- Project accuracy is about 0.53 to 0.59: expect roughly 4 to 5 in 10 items to need a correction. 91 of the 166 aliases come from project names without any training items, so only 25 labels are emitted in practice.
- Training data and the board are internal and not released. The labels are one team's work streams; use the model as a starting point for fine-tuning your own board.
- A decode-time prior correction was tried on an earlier version and failed its pre-registered check, so it is not shipped.
- Behavior outside the prompt format above (other output schemas, thinking mode, long item bodies) was not evaluated.

## License and attribution

- Model materials: governed by the OpenMDW License Agreement, version 1.1 (`LICENSE.OpenMDW-1.1`, https://openmdw.ai/license/1-1/). This repository is a derivative of [nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16) and ships a copy of the agreement.
- Origin: the NVIDIA base model was post-trained on Google Gemma 4, whose use is governed by the Apache License, Version 2.0 (`LICENSE.Apache-2.0-Gemma`).
- NVIDIA's governing-terms notice is retained verbatim in `NOTICE.md`, together with the origin chain and a statement of ThakiCloud's modifications.
- The fine-tuned weights add ThakiCloud's LoRA modifications; they do not change the terms above.
