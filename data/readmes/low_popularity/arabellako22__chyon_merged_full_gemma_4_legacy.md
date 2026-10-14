---
license: gemma
base_model: unsloth/gemma-4-E2B-it
pipeline_tag: text-generation
language:
- ko
- en
tags:
- gemma
- gemma4
- full-weights
- legacy
- not-recommended
- conversational
- korean
---

# Chyon Gemma 4 — Legacy Merge

> **Status: not recommended.** This is the earlier full-weight Chyon merge. Artifact testing found repeated prompt-template tokens in generated output. Use the [verified Unsloth re-merge](https://huggingface.co/arabellako22/chyon_unsloth_remerged_full_gemma_4) instead.

## Key facts

| Field | Value |
|---|---|
| Developer | [arabellako22](https://huggingface.co/arabellako22) |
| Original base | [unsloth/gemma-4-E2B-it](https://huggingface.co/unsloth/gemma-4-E2B-it) |
| LoRA adapter | [arabellako22/chyon_lora_model](https://huggingface.co/arabellako22/chyon_lora_model) |
| Merge method | Standard PEFT `merge_and_unload()` path |
| Format | Full-weight Safetensors, approximately 10.3 GB |
| Architecture | `Gemma4ForConditionalGeneration` |
| Precision | FP16 |
| Task | Conversational text generation |
| Languages | Korean; English was not separately evaluated |
| License | Gemma license |

## Why this repository is retained

The files remain available for reproducibility and comparison. They should not be used as the source for GGUF conversion or deployment because the post-merge smoke test failed.

The replacement model was saved through Unsloth's 16-bit merge path, reloaded, and verified before GGUF conversion:

- [Verified full model](https://huggingface.co/arabellako22/chyon_unsloth_remerged_full_gemma_4)
- [Verified GGUF builds](https://huggingface.co/arabellako22/chyon_gemma_4_gguf_v2)

## Recorded issue

| Check | Result |
|---|---|
| Model reload | Completed |
| Persona prompt generation | Repeated prompt-template tokens |
| Release decision | Rejected in favor of the verified Unsloth re-merge |

## Limitations

- This artifact failed its recorded generation smoke test.
- The source adapter used a small, creator-curated, partly template-augmented dataset.
- No standardized factuality, safety, bias, robustness, or Korean benchmark is published.
- English and multimodal behavior were not separately validated.

Use the verified replacement for inference and downstream conversion.
