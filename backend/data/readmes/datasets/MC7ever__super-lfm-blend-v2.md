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
pretty_name: super-lfm blend v2
tags:
  - lfm2.5
  - heretic
  - roleplay
  - sft
  - decontaminated
---

# super-lfm blend v2

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
| train | 41,057 |
| validation | 2,159 |
| total | 43,216 |

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

- rows in: 43472
- rows out: 43216
- dropped: 256
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
| code | 12,095 |
| general | 24,961 |
| humanlike | 5,023 |
| persona | 10,472 |

### Per source

| source | train | val | license |
|---|---:|---:|---|
| Anthropic/hh-rlhf | 947 | 50 | unknown |
| DarkArtsForge/Poe_v1 | 94 | 5 | unknown |
| HuggingFaceH4/no_robots | 4,648 | 245 | unknown |
| HuggingFaceH4/ultrafeedback_binarized | 882 | 46 | unknown |
| HumanLLMs/Human-Like-DPO-Dataset | 1,425 | 75 | unknown |
| Muennighoff/natural-instructions | 1,871 | 98 | unknown |
| Open-Orca/SlimOrca | 899 | 47 | unknown |
| PygmalionAI/PIPPA | 293 | 15 | unknown |
| TIGER-Lab/MathInstruct | 1,876 | 99 | unknown |
| TouchNight/HumanlikeRP | 1,374 | 72 | apache-2.0 |
| UCL-DARK/sequential-instructions | 506 | 27 | unknown |
| WizardLM/WizardLM_evol_instruct_70k | 900 | 47 | unknown |
| allenai/ai2_arc | 375 | 20 | unknown |
| allenai/openbookqa | 474 | 25 | unknown |
| allenai/ropes | 469 | 25 | unknown |
| allenai/winogrande | 475 | 25 | unknown |
| argilla/distilabel-intel-orca-dpo-pairs | 725 | 38 | unknown |
| b-mc2/sql-create-context | 950 | 50 | unknown |
| camel-ai/biology | 475 | 25 | unknown |
| camel-ai/math | 910 | 48 | unknown |
| codeparrot/apps | 474 | 25 | unknown |
| dair-ai/emotion | 950 | 50 | unknown |
| glaiveai/glaive-function-calling-v2 | 747 | 39 | unknown |
| google/boolq | 787 | 41 | unknown |
| hotpotqa/hotpot_qa | 949 | 50 | unknown |
| iamtarun/python_code_instructions_18k_alpaca | 936 | 49 | unknown |
| jerrimu/4o-emotional | 903 | 48 | unknown |
| jondurbin/airoboros-3.1 | 1,282 | 67 | unknown |
| jondurbin/cinematika-v0.1 | 73 | 4 | unknown |
| jondurbin/contextual-dpo-v0.1 | 418 | 22 | unknown |
| jondurbin/gutenberg-dpo-v0.1 | 8 | 0 | unknown |
| jondurbin/py-dpo-v0.1 | 423 | 22 | unknown |
| jondurbin/rosettacode-raw | 348 | 18 | unknown |
| jondurbin/truthy-dpo-v0.1 | 475 | 25 | unknown |
| lmsys/lmsys-chat-1m | 979 | 52 | unknown |
| migtissera/Synthia-v1.3 | 439 | 23 | unknown |
| nvidia/HelpSteer | 730 | 38 | unknown |
| open-thoughts/OpenThoughts-114k | 5 | 0 | unknown |
| persona_payload | 4,017 | 211 | unknown |
| rajpurkar/squad_v2 | 636 | 34 | unknown |
| reallycarlaost/emobank-single-binary | 473 | 25 | unknown |
| roneneldan/TinyStories | 1,424 | 75 | unknown |
| stanfordnlp/imdb | 2 | 0 | unknown |
| teknium/openhermes | 1,846 | 97 | unknown |
| unalignment/comedy-snippets-v0.1 | 7 | 0 | unknown |
| unalignment/spicy-3.1 | 433 | 23 | unknown |
| unalignment/toxic-dpo-v0.2 | 506 | 27 | unknown |
| ybisk/piqa | 219 | 12 | unknown |

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
python3 tools/build_studio_blend_dataset.py --out data/super_lfm/blend_v2.parquet
python3 tools/decontaminate_studio_blend.py \
  --in data/super_lfm/blend_v2.parquet \
  --out data/super_lfm/blend_v2_clean.parquet
python3 tools/publish_blend_to_hf.py
```

## Checksums

| file | sha256 |
|---|---|
| blend_v2_train.parquet | `e20b14b02e484ff70739f14506494c4e3fc9325e3390a098676d0be8203d7163` |
| blend_v2_val.parquet | `22ad0b9839ad511464eac97bcdd0522fb15a30ffe78f2eba069442740b86e568` |
| blend_v2_clean.parquet | `d1994b69cc232b7d575ba3790e0cc16ba550a701dfe0039effe8721e512d25af` |
