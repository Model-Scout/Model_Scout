---
license: other
task_categories:
  - text-generation
  - other
language:
  - en
  - zh
  - ja
  - ko
  - ru
pretty_name: super-lfm blend v1
tags:
  - lfm2.5
  - heretic
  - roleplay
  - sft
  - decontaminated
---

# super-lfm blend v1

> **Content warning.** This dataset contains explicit horror and NSFW
> creative writing supplied by the dataset author, plus material from public
> roleplay and "uncensored" community datasets. It is published for research
> and private experimentation. It is not filtered for work or educational use
> and may contain material that is disturbing, sexually explicit, or both.


A blended chat-SFT corpus built for a single local fine-tune of
`MC7ever/LFM2.5-24B-A2B-Heretic-JANG_2M` (a JANG mixed-precision quant of
`OS-Software/LFM2.5-24B-A2B-Uncensored-Heretic`, itself a Heretic
abliteration of `LiquidAI/LFM2.5-24B-A2B`).

## Shape

| | rows |
|---|---|
| train | 15,713 |
| validation | 827 |
| total | 16,540 |

Schema: `messages` (`list<struct<role, content>>`) and `source` (string).

## Why the assistant turns start with `<think></think>`

The model's chat template opens the think block **unconditionally**:

```jinja
{%- if add_generation_prompt -%}{{- "<|im_start|>assistant\n<think>" -}}{%- endif -%}
```

There is no `enable_thinking` toggle, and the serving stack runs a `qwen3`
reasoning parser that splits the completion at `</think>`: text before the
tag becomes `reasoning_content`, text after becomes `content`. A model
trained on targets that never close the think block therefore answers with
an **empty `content`** -- the text exists, but it is all classified as
reasoning. That is exactly what happened to the previous no_robots fine-tune.

Every assistant turn here is prefixed with `<think></think>`, so the model
learns to close the block itself. The inference prompt
(`...assistant\n<think>`) is then an exact prefix of the training render, and
the trained completion is `</think>{answer}<|im_end|>`.

Verified with the trainer's own token preview: `<think>` and `</think>` are
trained tokens, the answer is trained, and the prompt scaffolding
(`<|im_start|>`, `assistant`, newlines) is masked out.

## Decontamination

Cosine decontamination against the benchmark battery the training repo
evaluates on, using `unsloth/bge-small-en-v1.5` on CPU.

Drop rule: `cos >= 0.95`, **or** (`cos >= 0.85` **and** a shared 8-word
shingle), **or** a normalised exact match. The shingle guard exists because
MCQ train/test sets are stylistically identical -- a pure cosine threshold
would delete arc, winogrande, piqa and boolq wholesale.

- rows in: 16632
- rows out: 16540
- dropped: 92
- benchmark sets: 20

| benchmark set | items |
|---|---|
| aime24 | 30 |
| arc_challenge | 1172 |
| arc_easy | 2376 |
| bb_emojis_emotion_mc | 2000 |
| bbh | 2997 |
| boolq | 3000 |
| eq_bench | 171 |
| gpqa_diamond_zeroshot | 198 |
| hellaswag | 3000 |
| logiqa | 651 |
| mmlu | 2998 |
| mmlu_prox_ja | 2994 |
| mmlu_prox_ko | 2996 |
| mmlu_prox_ru | 2996 |
| mmlu_prox_zh | 2995 |
| piqa | 1838 |
| sciq | 1000 |
| squadv2 | 2998 |
| truthfulqa_mc1_mc2 | 817 |
| winogrande | 1267 |

## Composition

| group | rows |
|---|---|
| code | 3,890 |
| general | 5,842 |
| humanlike | 1,993 |
| persona | 6,468 |

### Per source

| source | train | val | license |
|---|---:|---:|---|
| Anthropic/hh-rlhf | 380 | 20 | unknown |
| DarkArtsForge/Poe_v1 | 94 | 5 | unknown |
| HuggingFaceH4/no_robots | 1,396 | 74 | unknown |
| HuggingFaceH4/ultrafeedback_binarized | 352 | 18 | unknown |
| HumanLLMs/Human-Like-DPO-Dataset | 475 | 25 | unknown |
| Muennighoff/natural-instructions | 376 | 20 | unknown |
| Open-Orca/SlimOrca | 177 | 9 | unknown |
| PygmalionAI/PIPPA | 85 | 4 | unknown |
| TIGER-Lab/MathInstruct | 378 | 20 | unknown |
| TouchNight/HumanlikeRP | 545 | 29 | apache-2.0 |
| UCL-DARK/sequential-instructions | 380 | 20 | unknown |
| WizardLM/WizardLM_evol_instruct_70k | 359 | 19 | unknown |
| allenai/ai2_arc | 375 | 20 | unknown |
| allenai/openbookqa | 189 | 10 | unknown |
| allenai/ropes | 188 | 10 | unknown |
| allenai/winogrande | 190 | 10 | unknown |
| argilla/distilabel-intel-orca-dpo-pairs | 273 | 14 | unknown |
| b-mc2/sql-create-context | 285 | 15 | unknown |
| camel-ai/biology | 142 | 8 | unknown |
| camel-ai/math | 224 | 12 | unknown |
| codeparrot/apps | 284 | 15 | unknown |
| dair-ai/emotion | 190 | 10 | unknown |
| glaiveai/glaive-function-calling-v2 | 235 | 12 | unknown |
| google/boolq | 233 | 12 | unknown |
| iamtarun/python_code_instructions_18k_alpaca | 376 | 20 | unknown |
| jerrimu/4o-emotional | 373 | 20 | unknown |
| jondurbin/airoboros-3.1 | 506 | 27 | unknown |
| jondurbin/cinematika-v0.1 | 19 | 1 | unknown |
| jondurbin/contextual-dpo-v0.1 | 172 | 9 | unknown |
| jondurbin/gutenberg-dpo-v0.1 | 1 | 0 | unknown |
| jondurbin/py-dpo-v0.1 | 175 | 9 | unknown |
| jondurbin/rosettacode-raw | 132 | 7 | unknown |
| jondurbin/truthy-dpo-v0.1 | 190 | 10 | unknown |
| lmsys/lmsys-chat-1m | 250 | 13 | unknown |
| migtissera/Synthia-v1.3 | 176 | 9 | unknown |
| nvidia/HelpSteer | 288 | 15 | unknown |
| persona_payload | 4,017 | 211 | unknown |
| rajpurkar/squad_v2 | 199 | 10 | unknown |
| reallycarlaost/emobank-single-binary | 95 | 5 | unknown |
| unalignment/comedy-snippets-v0.1 | 7 | 0 | unknown |
| unalignment/spicy-3.1 | 433 | 23 | unknown |
| unalignment/toxic-dpo-v0.2 | 375 | 20 | unknown |
| ybisk/piqa | 124 | 7 | unknown |

### Deliberately excluded

| source | why |
|---|---|
| UCL-DARK/ludwig | no train split (configs 0-shot/1-shot/10-shot expose validation+test only) -- the recipe says train splits only, so it cannot be used for SFT. Better used as an eval set. |
| facebook/belebele | test split only, 122 language configs -- no train split to learn from. |
| ParisNeo/LoLLMS-Open-Community-discussions | dead on the Hub: main branch carries only a README + a prompt list, the auto-converted parquet branch holds 20 rows. |
| migtissera/Synthia-13B | repo gone; the successor migtissera/Synthia-v1.3 is used instead. |
| WhiteRabbitNeo/WRN-Chapter-1 / Chapter-2 | gated (401 without an accepted licence); the WRN-Chapter-1 parquet branch is reachable but the source material is offensive-cyber red-team text, kept out of a general chat blend. |
| PygmalionAI/PIPPA (deduped subset) | included, but only 150 rows: the source is a consent-gated 16.8k-row conversation set with bot personas, not general instruction data. |

## Training recipe it was built for

```json
{
  "model_name": "MC7ever/LFM2.5-24B-A2B-Heretic-JANG_2M",
  "training_type": "LoRA/QLoRA",
  "format_type": "chatml",
  "train_split": "train",
  "eval_split": "validation",
  "eval_steps": 100,
  "num_epochs": 2,
  "learning_rate": "0.0001",
  "batch_size": 1,
  "gradient_accumulation_steps": 9,
  "max_seq_length": 1024,
  "load_in_4bit": true,
  "lora_r": 8,
  "lora_alpha": 16,
  "lora_dropout": 0.01,
  "optim": "lion",
  "lr_scheduler_type": "linear",
  "warmup_steps": 10,
  "weight_decay": 0.001,
  "random_seed": 3407,
  "packing": false,
  "train_on_completions": true
}
```

## Provenance and licensing

This is an **aggregation** of independently licensed datasets plus one
author-supplied corpus. The per-source licences are listed above; this repo
carries `license: other` because the aggregate is not uniformly licensed.
Check each source's terms before redistribution. The author-supplied
horror/NSFW persona corpus has no upstream licence and is published here
with the author's permission.

## Reproducing

```bash
python3 tools/build_studio_blend_dataset.py --out data/super_lfm/blend_v1.parquet
python3 tools/decontaminate_studio_blend.py \
  --in data/super_lfm/blend_v1.parquet \
  --out data/super_lfm/blend_v1_clean.parquet
python3 tools/publish_blend_to_hf.py
```

## Checksums

| file | sha256 |
|---|---|
| blend_v1_train.parquet | `2f81b1921fa1bcdc1524e1f61f6e19d879475af84f6057d24367a4dcf6f7da61` |
| blend_v1_val.parquet | `176bba1dafd5018189f3d1f66dfe2f3594b4a98faebb24fbd7fa56152b56b22f` |
| blend_v1_clean.parquet | `e37e8f493023459991dfe5822e551f1aa82d62e9a60de9ad24d911cfb6f380bb` |
