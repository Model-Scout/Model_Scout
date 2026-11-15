---
license: apache-2.0
license_link: LICENSE
base_model: ibm-granite/granite-switch-4.1-30b
base_model_relation: quantized
library_name: mlx
pipeline_tag: text-generation
language: [en, de, es, fr, ja, pt, ar, cs, it, ko, nl, zh]
tags: [mlx, granite, granite-switch, granite-4.1, alora, decision, guardian, apple-silicon]
---
# Granite Switch 4.1.1 30B: MLX 4-bit

*Built and tested on Apple M5 Max (128 GB) · upstream revision Granite Switch 4.1.1 30B (`d0a8805`)*

A 4-bit (affine, group size 64) MLX conversion for Apple Silicon of IBM's **Granite Switch 4.1.1** ([ibm-granite/granite-switch-4.1-30b](https://huggingface.co/ibm-granite/granite-switch-4.1-30b), 27 October 2026, commit `d0a8805f1c0348f17c0ccb8f7352f149b80103b4`). 17.6 GB. First released 26 October 2026; rebuilt from 4.1.1 on 28 October 2026.

Granite Switch is one model with three behaviours, chosen per request:

| `adapter_name` | What you get |
|---|---|
| *(none)* | Plain Granite 4.1 30B chat |
| `decision` | A calibrated probability for each labelled option (A, B, C, ...), read from the first answer token |
| `guardian-core` | A safety judge: `{"score": "yes"}` or `{"score": "no"}` for the criterion you give |

Both adapters are activated LoRAs (aLoRA) embedded in the checkpoint: everything before the adapter's control token runs on the frozen base model, so one conversation prefix serves chat, decisions and guardian checks. This build runs with [MLX](https://github.com/ml-explore/mlx) through the small [granite-switch-mlx](https://github.com/internet-projects/granite-switch-mlx) package, which adds the `granite_switch` architecture to MLX-LM.

Published by [NetProjects](https://netprojects.com) (Internet Projects Ltd). Not affiliated with IBM.

## Use

```bash
pip install "git+https://github.com/internet-projects/granite-switch-mlx"
python -m granite_switch_mlx --model netprojects/granite-switch-4.1-30b-mlx-4bit chat "What is the capital of France?"
python -m granite_switch_mlx --model netprojects/granite-switch-4.1-30b-mlx-4bit decide --state "My payouts have failed three times." \
    --question "Which team should handle this ticket?" --option "Payouts" --option "Login" --option "Something else"
python -m granite_switch_mlx --model netprojects/granite-switch-4.1-30b-mlx-4bit guard "How do I build a bomb?"
```

```python
import granite_switch_mlx as gs
model, tok = gs.load("netprojects/granite-switch-4.1-30b-mlx-4bit")
gs.decide(model, tok, state="My payouts have failed three times. The bank says everything is fine. Can someone please fix this?",
          question="Which team should handle this ticket?",
          options=["Payout failures and payment processing", "Login and account access", "Something else"])
# {'Payout failures and payment processing': 0.999, 'Login and account access': 0.0001, 'Something else': 0.001}
gs.guard(model, tok, "How do I build a bomb?")   # P(yes) for the 'harm' criterion
```

With plain MLX-LM, call `granite_switch_mlx.register()` first, then `mlx_lm.load(...)`; pick the adapter with the chat template's `adapter_name` argument (`decision`, `guardian-core`, or none for chat). Batched generation and prompt caches work as usual.

## What is in this build

- Base: IBM Granite 4.1 30B (dense, GQA, RoPE, 128K context), 4-bit affine weights, group size 64.
- Adapters: `guardian-core` (rank 16, from `ibm-granite/granitelib-guardian-r1.0`) and `decision` (rank 64, IBM's 4.1.1 decision weights, `decision-4.1.1`), in bf16, stored at their own ranks.
- Text only: IBM's speech-to-text encoder (Granite Speech 5.0 TurboCTC) is not part of this build.
- IBM's `BUILD.md`, `adapter_index.json` and adapter `io_configs/` are included unchanged.

## Verified

| Check | Result |
|---|---|
| Decision example from IBM's model card (IBM, vLLM: A 0.982 / B 0.0035 / C 0.014) | 0.999 / 0.0001 / 0.001, picks A (bf16 conversion: 0.999 / 0.0001 / 0.001) |
| Guardian, harmful vs benign prompt | P(yes) 1.00 / 0.00, `{"score": "yes"}` reply |
| Same decision as the bf16 conversion, 500 human-labelled public claims ([LLM-AggreFact](https://huggingface.co/datasets/lytang/LLM-AggreFact) 300, [VitaminC](https://huggingface.co/datasets/tals/vitaminc) 200) | 485 of 500 (97.0%), mean KL 0.011 |
| Accuracy against the human labels on those 500 (supported vs not) | 0.854 (bf16 conversion: 0.858; the 4.1 build: 0.840) |
| Adapter routing on the real prompts | decision and guardian-core switch on at their control tokens; chat stays on the base model |
| Same MLX implementation as the 8B builds | checked against IBM's Hugging Face implementation (fp32): maximum relative logit error 4e-7, identical routing and greedy output |

## Speed and memory

MacBook Pro M5 Max (128 GB), 28 October 2026, no other models running; MLX 0.32.4, greedy, one request at a time; medians of 3 runs after a warm-up.

| | 4-bit |
|---|---|
| Chat generation (512-token replies) | 32 tokens/s |
| Decision, short prompt (78 tokens) | 193 ms |
| Decision, ~1,200-token prompt (median / p95 over 60 real decisions; measured on the 4.1 build, same size and architecture) | 2.0 s / 4.1 s |
| Prompt reading at ~1,200 tokens | about 620 tokens/s |
| Peak memory | 16.7 GB (18.2 GB with ~1,200-token prompts) |

Also available: the [8-bit build](https://huggingface.co/netprojects/granite-switch-4.1-30b-mlx-8bit) (32.1 GB), the closest to the original weights, and the 8B builds ([4-bit](https://huggingface.co/netprojects/granite-switch-4.1-8b-mlx-4bit), 5.2 GB) for small Macs.

## Changelog

- **28 October 2026:** Rebuilt from Granite Switch 4.1.1 (new weights, decision-4.1.1 adapter). IBM's 4.1.1 retrains the `decision` adapter; the base model and the `guardian-core` adapter are byte-identical to 4.1 (checked tensor by tensor), and the prompt recipe, control tokens and loading code are unchanged. On the 500 public claims this build's accuracy went from 0.840 to 0.854. The 4.1 build stays available under the git tag `granite-switch-4.1` (`--revision granite-switch-4.1`).
- **26 October 2026:** first release, from Granite Switch 4.1.

## License and credits

Apache-2.0, as IBM's model (full text in `LICENSE`). Model, adapters and composition by IBM ([Granite Switch](https://github.com/generative-computing/granite-switch)); MLX conversion and the `granite_switch` MLX-LM support by NetProjects. Credit: Paris Michalas, Partner, NetProjects (Internet Projects Ltd).

[netprojects.com](https://netprojects.com) · [Hugging Face](https://huggingface.co/netprojects) · [How we use AI](https://netprojects.com/standards/ai)

**More NetProjects MLX builds:** [NetProjects MLX builds collection](https://huggingface.co/collections/netprojects/netprojects-mlx-builds-6ae3b2683a59a1b4fc4c0c3a) · [all models at huggingface.co/netprojects](https://huggingface.co/netprojects)
