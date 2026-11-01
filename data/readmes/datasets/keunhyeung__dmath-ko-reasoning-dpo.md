---
license: mit
language:
- ko
task_categories:
- text-generation
- question-answering
tags:
- math
- korean
- reasoning
- dpo
- education
size_categories:
- 1K<n<10K
configs:
- config_name: reasoning
  data_files:
  - split: train
    path: data/reasoning/train.jsonl
  - split: validation
    path: data/reasoning/validation.jsonl
- config_name: reasoning-sft
  data_files:
  - split: train
    path: data/reasoning/train_sft_eligible.jsonl
  - split: validation
    path: data/reasoning/validation_sft_eligible.jsonl
- config_name: dpo
  data_files:
  - split: train
    path: data/dpo/train.jsonl
  - split: validation
    path: data/dpo/validation.jsonl
---

# dmath-ko-reasoning-dpo

Korean elementary math word problems from **DMath** (MIT, EMNLP 2023), extended with
**execution-verified natural-language reasoning** and an **execution-verified DPO pair
set**. The full SFT pipeline — from the original problems to verified reasoning to
preference pairs — is visible in this one repository.

## Pipeline (how each column came to be)

```
DMath train (7,943, human-written, MIT)
  │  ① whitelisted postfix executor re-runs every solution tree;
  │     rows whose execution disagrees with the gold answer are dropped
  │  ② numeric-masked template dedup → 80/20 split, seed 42 (no shared templates)
  ▼
source rows 3,619  (train 2,895 / validation 724)          → config `reasoning`
  │  ③ gpt-5 (gpt-5-2025-08-07) writes short Korean explanation clauses ONLY;
  │     equations and the final answer are assembled by code from the gold trace,
  │     so every equation in `reasoning` is true by construction
  │  ④ validators: schema, banned patterns, arithmetic re-check, 512-token length,
  │     exact-trace fidelity; 100-sample human audit (natural 95.9%, major errors 0
  │     after blacklisting 2 upstream gold defects)
  ▼
sft_eligible 3,390  (train 2,708 / validation 682)          → config `reasoning-sft`
  │  ⑤ deterministic plan mutations (operator swap, operand substitution,
  │     subtree swap, non-commutative order) → executed → wrong answer confirmed
  │  ⑥ rejected = same gpt-5 clause leads, equations/answer re-assembled from the
  │     mutated trace (style-parity by construction; no length/style shortcut)
  ▼
DPO pairs 2,576  (pref_train 2,322 / pref_dev 254)          → config `dpo`
```

## Configs

| config | rows | what it is |
|---|---|---|
| `reasoning` | 2,895 / 724 | all source rows: 9 original DMath columns + generated `reasoning`, `response`, `text`, validation results, `sft_eligible` flag |
| `reasoning-sft` | 2,708 / 682 | rows passing all automatic checks and the post-audit blacklist — ready for SFT |
| `dpo` | 2,322 / 254 | `prompt` / `chosen` / `rejected` plus full mutation provenance (`gold_plan`, `mutated_plan`, `mutation_family`, ...) |

## Known issues (upstream gold defects)

Two records are excluded from `reasoning-sft` and the DPO pool
(`sft_eligible=false` in `reasoning`), traced to the **original DMath annotations**:

- `dmath:train:928`: gold plan answers "max remainder when dividing 12" as `12 − 1 = 11`,
  logically fragile in the original annotation.
- `dmath:train:6477`: source text says 밀리리터 while the gold trace subtracts 리터.

## Provenance & licensing

- Source: [DMath](https://github.com/JiwooKimAR/dmath) @ `149a740`, MIT (see `LICENSE`,
  `NOTICE`). Original 9 columns are preserved unchanged.
- Generated clauses: OpenAI `gpt-5-2025-08-07` (Batch API, temperature 0, reasoning
  effort minimal). Per OpenAI's Terms of Use, outputs are owned by the requesting user;
  the generated columns are released here under **MIT**, same as the source.
- Equations, answers, tags, splits: deterministic code, no model involvement.
- The dataset's raw generation/audit trail (API attempts, request ids) is kept private
  and is not part of this repository.

## Citation

Please cite the DMath paper for the underlying problems:

```bibtex
@inproceedings{kim2023dmath,
  title={It Ain't Over: A Multi-aspect Diverse Math Word Problem Dataset},
  author={Kim, Jiwoo and Kim, Youngbin and Baek, Ilwoong and Bak, JinYeong and Lee, Jongwuk},
  booktitle={EMNLP},
  year={2023}
}
```
