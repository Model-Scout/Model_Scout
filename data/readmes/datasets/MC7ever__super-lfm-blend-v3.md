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
| train | 163,048 |
| validation | 8,582 |
| total | 171,630 |

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

- rows in: 175412
- rows out: 171630
- dropped: 3782
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

### Per source

| source | train | val | license |
|---|---:|---:|---|
| 4o_emotional | 466 | 24 | unknown |
| ai2_arc_ARC-Challenge_test | 10 | 0 | unknown |
| ai2_arc_ARC-Challenge_train | 1,047 | 55 | unknown |
| ai2_arc_ARC-Challenge_validation | 280 | 15 | unknown |
| ai2_arc_ARC-Easy_test | 22 | 1 | unknown |
| ai2_arc_ARC-Easy_train | 2,094 | 110 | unknown |
| ai2_arc_ARC-Easy_validation | 536 | 28 | unknown |
| ai_llm_finetune_convos | 4,614 | 243 | unknown |
| airoboros_22 | 3,502 | 184 | unknown |
| airoboros_221 | 3,804 | 200 | unknown |
| arkhaios_dpo | 211 | 11 | unknown |
| authors_assistant | 1,742 | 92 | unknown |
| boolq | 2,802 | 148 | unknown |
| cogbeth_gpt | 258 | 14 | unknown |
| comedy_snippets | 4 | 0 | unknown |
| confident_writer | 2,027 | 107 | unknown |
| contextual_dpo | 759 | 40 | unknown |
| creative_writing_3k | 1,234 | 65 | unknown |
| denker_sft | 4,926 | 259 | unknown |
| emotion | 4,742 | 250 | unknown |
| evol_instruct | 7,662 | 403 | unknown |
| generalchat_gpt | 7,784 | 410 | unknown |
| great_firewall_dpo | 276 | 14 | unknown |
| gutenberg2_dpo | 4 | 0 | unknown |
| helpsteer | 2,010 | 106 | unknown |
| hh_rlhf | 9,422 | 496 | unknown |
| human_writing_dpo | 306 | 16 | unknown |
| humanlike_dpo | 1,861 | 98 | unknown |
| humanlike_rp | 456 | 24 | unknown |
| literally_literary | 1,662 | 88 | unknown |
| lmsys_24k | 395 | 21 | unknown |
| lmsys_openleecher_120k | 6,549 | 345 | unknown |
| multi_round_code | 26 | 1 | unknown |
| nmtrn_sft | 1,150 | 60 | unknown |
| nmtrn_sft_think | 781 | 41 | unknown |
| no_robots | 8,586 | 452 | unknown |
| openbookqa | 2,846 | 150 | unknown |
| persona_payload | 3,870 | 204 | unknown |
| personal_finance | 2,689 | 142 | unknown |
| poe_v1 | 94 | 5 | unknown |
| purpura_dpo | 205 | 11 | unknown |
| py_dpo | 1,315 | 69 | unknown |
| python_alpaca | 4,664 | 246 | unknown |
| re_wiz_20k | 2,965 | 156 | unknown |
| roleplaying | 2,124 | 112 | unknown |
| ropes | 2,805 | 148 | unknown |
| schule_dpo | 5 | 0 | unknown |
| selfhelp_sharegpt | 2,173 | 114 | unknown |
| sequential_instructions | 470 | 25 | unknown |
| slimorca | 8,442 | 444 | unknown |
| spicy_31 | 389 | 20 | unknown |
| sql_create_context | 4,750 | 250 | unknown |
| squad_v2 | 3,182 | 168 | unknown |
| stemmix | 3,996 | 210 | unknown |
| thinkmix_gpt | 375 | 20 | unknown |
| tom_dpo | 649 | 34 | unknown |
| toxic_dpo | 503 | 26 | unknown |
| truthy_dpo | 950 | 50 | unknown |
| ultrafeedback | 7,253 | 382 | unknown |
| vernunft_sft | 9,650 | 508 | unknown |
| verstand_sft | 7,800 | 411 | unknown |
| weasel_dpo | 124 | 6 | unknown |
| winogrande | 4,750 | 250 | unknown |

### Deliberately excluded

| source | why |
|---|---|
| natural_instructions (757 files, too slow) | (see notes) |
| apps (script dataset) | (see notes) |
| piqa (script dataset) | (see notes) |
| winogrande_xl (included) | (see notes) |
| WildChat (1.6GB, too big) | (see notes) |
| TinyStories (1GB) | (see notes) |
| Step-Flash-SFT (5.3GB) | (see notes) |
| hotpotqa (332MB, slow) | (see notes) |
| LMSYS (gated) | (see notes) |
| Nemotron-SFT-Agentic-v4 (no parquet) | (see notes) |

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
python3 tools/build_studio_blend_dataset.py --out data/super_lfm/blend_v3.parquet
python3 tools/decontaminate_studio_blend.py \
  --in data/super_lfm/blend_v3.parquet \
  --out data/super_lfm/blend_v3_clean.parquet
python3 tools/publish_blend_to_hf.py
```

## Checksums

| file | sha256 |
|---|---|
| blend_v3_train.parquet | `9d5fa161459901097c836014add62aebe1433f729b692f76c6b88f0f47971174` |
| blend_v3_val.parquet | `14002494b24c3f854fb7a4af61d5e021b9e932e6a996d70e51ba7a0b703dfddf` |
| blend_v3_clean.parquet | `6095f4be61b184feeb4829985ebd7b91831b80555f75bc27b0081c3861457abd` |
