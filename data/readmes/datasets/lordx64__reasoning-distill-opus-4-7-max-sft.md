---
license: apache-2.0
language:
- en
tags:
- reasoning
- chain-of-thought
- distillation
- claude
- opus-4-7
- sft
- qwen-chat-template
task_categories:
- text-generation
size_categories:
- 1K<n<10K
dataset_info:
  features:
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 29328233
    num_examples: 7823
  download_size: 15809651
  dataset_size: 29328233
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

# Reasoning traces from Claude Opus 4.7 — SFT-ready

7,823 single-turn reasoning conversations from **Claude Opus 4.7** reformatted for supervised fine-tuning with `trl.SFTTrainer` + `train_on_responses_only`. Each row is a single `text` field containing a full Qwen-style chat-template conversation.

## Provenance

Every conversation's assistant response (including the `<think>...</think>` block) is output from **`claude-opus-4-7`** with Anthropic's `extended-thinking` enabled. This is the SFT-reformatted version of the raw dataset:

- **Raw upstream**: [`lordx64/reasoning-distill-claude-opus-4-7-max`](https://huggingface.co/datasets/lordx64/reasoning-distill-claude-opus-4-7-max) — has `model`, `thinking`, `response`, and `source_dataset` columns. Check there for full attribution.

### Why this dataset has `4-7` in the name but sources mention 4.6

The *prompts* were reused from earlier distillation corpora (some of which have "4.6" in their names because they originally targeted Opus 4.6). The *responses* in this dataset are all regenerated from scratch against Opus 4.7 — which is what determines the dataset's name. See the [raw dataset card](https://huggingface.co/datasets/lordx64/reasoning-distill-claude-opus-4-7-max) for the full prompt→response pipeline.

## Format

Each `text` value is a complete chat conversation in Qwen chat template with thinking:

```
<|im_start|>system
{system_prompt}<|im_end|>
<|im_start|>user
{user_prompt}<|im_end|>
<|im_start|>assistant
<think>
{opus_4_7_extended_thinking}
</think>

{opus_4_7_final_answer}<|im_end|>
```

Ready to feed to `SFTTrainer` with `dataset_text_field="text"`. The model we trained uses `train_on_responses_only` to mask loss on the user/system side — gradients only flow through the assistant turn, including its thinking tokens.

## Size

- **Rows**: 7,823 (a few dropped from the raw 8,124 during formatting — rows where `stop_reason != end_turn` or where `thinking` / `response` was empty)
- **Avg tokens per row**: ~4k (Qwen3 tokenizer), with long-tail reasoning chains going up to 32k tokens

## Model trained on this dataset

[`lordx64/Qwen3.6-35B-A3B-Claude-4.7-Opus-Reasoning-Distilled`](https://huggingface.co/lordx64/Qwen3.6-35B-A3B-Claude-4.7-Opus-Reasoning-Distilled) — attention-only LoRA, r=16, 2 epochs, single H200. Preliminary evals: GSM8K 84.3%, MMLU-Pro 74.9%.

## Terms of use

Generated using Anthropic's Claude Opus 4.7 via the official API. Downstream users should confirm compliance with [Anthropic's usage policies](https://www.anthropic.com/legal/usage-policy) for their specific use case.

License: Apache 2.0 (for the dataset packaging; content itself is subject to the upstream terms above).
