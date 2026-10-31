---
pretty_name: All-in-One LLM Corpus — SFT + DPO + RL + Persona
license: other
language:
- en
- zh
- ja
- ko
- ru
- de
- uk
- cs
- sk
task_categories:
- text-generation
- reinforcement-learning
- question-answering
- multiple-choice
- text-ranking
- summarization
- translation
- text-classification
size_categories: 100K<n<1M
tags:
- all-in-one
- sft
- dpo
- rlhf
- grpo
- reinforcement-learning
- persona
- benchmark
- preference
- chat
- fine-tuning
- combined
- lfm2.5
- multilingual
- human-written
- no-slop
- slop-filtered
- creative-writing
- roleplay
- reasoning
- math
- code
- open-data
dataset_info:
- config_name: ct
  features:
  - name: prompt
    dtype: string
  - name: system
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  - name: source
    dtype: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 132791762
    num_examples: 46813
  - name: validation
    num_bytes: 14868325
    num_examples: 5240
  - name: test
    num_bytes: 15012678
    num_examples: 5196
  - name: benchmark
    num_bytes: 14831407
    num_examples: 5229
  download_size: 100134395
  dataset_size: 177504172
- config_name: persona
  features:
  - name: system
    dtype: string
  - name: user
    dtype: string
  - name: assistant
    dtype: string
  - name: source
    dtype: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 3157258
    num_examples: 3171
  - name: validation
    num_bytes: 358749
    num_examples: 352
  - name: test
    num_bytes: 344770
    num_examples: 352
  - name: benchmark
    num_bytes: 356395
    num_examples: 353
  download_size: 2126392
  dataset_size: 4217172
- config_name: rl
  features:
  - name: task_id
    dtype: string
  - name: family
    dtype: string
  - name: prompt
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: answer
    dtype: string
  - name: verifier
    dtype: string
  - name: tools
    list: string
  - name: metadata
    struct:
    - name: expected
      dtype: string
    - name: paired_with
      dtype: string
    - name: rule
      dtype: string
    - name: rule_text
      dtype: string
    - name: source
      dtype: string
    - name: verifier
      dtype: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 23984943
    num_examples: 34241
  - name: validation
    num_bytes: 2681087
    num_examples: 3813
  - name: test
    num_bytes: 2708378
    num_examples: 3795
  - name: benchmark
    num_bytes: 2676775
    num_examples: 3813
  download_size: 15951238
  dataset_size: 32051183
- config_name: sft
  features:
  - name: messages
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: source
    dtype: string
  - name: subset
    dtype: string
  - name: language
    dtype: string
  splits:
  - name: train
    num_bytes: 311092522
    num_examples: 271491
  - name: validation
    num_bytes: 22872069
    num_examples: 20145
  - name: test
    num_bytes: 23032002
    num_examples: 20161
  - name: benchmark
    num_bytes: 39948863
    num_examples: 55867
  download_size: 212985060
  dataset_size: 396945456
configs:
- config_name: ct
  data_files:
  - split: train
    path: ct/train-*
  - split: validation
    path: ct/validation-*
  - split: test
    path: ct/test-*
  - split: benchmark
    path: ct/benchmark-*
- config_name: persona
  data_files:
  - split: train
    path: persona/train-*
  - split: validation
    path: persona/validation-*
  - split: test
    path: persona/test-*
  - split: benchmark
    path: persona/benchmark-*
- config_name: rl
  data_files:
  - split: train
    path: rl/train-*
  - split: validation
    path: rl/validation-*
  - split: test
    path: rl/test-*
  - split: benchmark
    path: rl/benchmark-*
- config_name: sft
  data_files:
  - split: train
    path: sft/train-*
  - split: validation
    path: sft/validation-*
  - split: test
    path: sft/test-*
  - split: benchmark
    path: sft/benchmark-*
- config_name: sft_clean
  features:
  - name: messages
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: source
    dtype: string
  - name: subset
    dtype: string
  splits:
  - name: train
    num_examples: 47500
  - name: validation
    num_examples: 2500
- config_name: ct_clean
  features:
  - name: prompt
    dtype: string
  - name: system
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  - name: source
    dtype: string
  splits:
  - name: train
    num_examples: 9500
  - name: validation
    num_examples: 500

---

# 🧬 All-in-One LLM Corpus

**One repo. Four training stages. Everything a chat model needs — and nothing that sounds like a bot.**

SFT → DPO → RL → persona polish → benchmark, with clean splits for each step, de-slopified in v2 so the model learns to talk, act, think and pass as a person.

| | |
|---|---|
| 🔢 Total rows | **480,032** across 4 subsets × 4 splits |
| 🎯 Subsets | `sft` · `ct` · `rl` · `persona` |
| ✂️ Splits | `train` · `validation` · `test` · `benchmark` (all four in every subset) |
| 📐 Split policy | ~75% train / 25% eval ⇒ **1 eval row per 3 train rows** |
| 🚫 Leakage control | 55,867 benchmark items never appear in train/validation/test |
| 🧹 Dedup | 525,109 raw blend rows → **321,785 unique** (203,324 cross-version dupes removed), then v2 de-bot pass −19,874 |
| 🤖 De-bot v2 | −10,665 bot/corporo targets · −2,334 purple-prose density · assistant-identity system lines stripped |
| 🌍 Languages | `language` column on every row: en, zh, ja, ko, ru, **de, uk, cs, sk** (+ long tail) |
| 🆕 v2 sources | OpenAssistant/oasst1 + CohereLabs/aya (human-written) · facebook/belebele (cs/sk/de/uk eval) |
| 🤖 Models | model-agnostic chat format (LFM2.5, Qwen, Llama, Gemma, Mistral, …) |

## 🆕 What's new in v2

- **De-botting pass** — every row's target text is screened against a combined bot/corporo phrase list (heretic [`noslop`](https://github.com/p-e-w/heretic/blob/master/config.noslop.toml) · [`nohumor`](https://github.com/p-e-w/heretic/blob/master/config.nohumor.toml) markers + curated assistant-identity & corpo-speak patterns + [DrRiceIO7/SlopReview](https://huggingface.co/datasets/DrRiceIO7/SlopReview)-mined phrases). Assistant-identity system lines (*"You are a helpful assistant."*) are stripped, and prompts that interrogate AI identity are dropped. See **Results → Filter quality** for measured scores.
- **Human-written language additions** — German, Czech, Slovak and Ukrainian rows from OASST1 (crowd-written conversations) and Aya (human-annotated), deduped against the existing corpus and slop-filtered with the same rules.
- **`language` column everywhere** — langdetect-tagged on every row of every subset/split; filter to any language in one line.
- **belebele benchmarks** — reading-comprehension MCQ in `deu_Latn`, `ces_Latn`, `slk_Latn`, `ukr_Cyrl` added to `sft.benchmark` (eval-only; Czech & Slovak training data remains a documented gap — quality human-written cs/sk chat is not publicly available in bulk).
- **Expanded card metadata** — task categories, tags, full language table, results & scores.

## Subsets

| subset | what it's for | schema | train / validation / test / benchmark |
|---|---|---|---|
| **`sft`** | Supervised fine-tuning & continued SFT on blended chat data | `messages`, `source`, `subset`, `language` | 271,491 / 20,145 / 20,161 / 55,867 |
| **`ct`** | Continued training with DPO/ORPO preference pairs | `prompt`, `system`, `chosen`, `rejected`, `source`, `language` | 46,813 / 5,240 / 5,196 / 5,229 |
| **`rl`** | GRPO / verifiable-reward RL tasks | `task_id`, `family`, `prompt`, `answer`, `verifier`, `tools`, `metadata`, `language` | 34,241 / 3,813 / 3,795 / 3,813 |
| **`persona`** | Persona & style transfer SFT (system-prompt heavy) | `system`, `user`, `assistant`, `source`, `language` | 3,171 / 352 / 352 / 353 |

### Splits

The same four splits exist inside **every** subset:

- **`train`** — 75% of the subset. The only split you update weights on.
- **`validation`** — held-out, in-distribution: early stopping, mid-training loss / reward.
- **`test`** — untouched, in-distribution holdout: your final in-distribution number.
- **`benchmark`** — scored against ground truth, never trained on.
  - `sft.benchmark` = the **55,867-item benchmark suite** (families below), formatted as chat with the gold answer in the final turn; `source` holds the benchmark name (belebele rows: `facebook/belebele/<lang>`).
  - `ct` / `rl` / `persona` `.benchmark` = held-out rows in each subset's own format (the benchmark suite has no chosen/rejected, verifier, or persona shape).

Validation + test + benchmark combined vs train: `sft` 35.4% · `ct` 33.5% · `rl` 33.4% · `persona` 33.3% — around the designed 1-per-3 ratio (v2's extra eval rows push `sft` slightly above; new training rows were split 75/12.5/12.5 to compensate).

## Quickstart

```python
from datasets import load_dataset

REPO = "MC7ever/all-in-one-llm-corpus"

sft      = load_dataset(REPO, "sft")       # chat SFT
dpo      = load_dataset(REPO, "ct")        # preference pairs
grpo     = load_dataset(REPO, "rl")        # RL tasks
persona  = load_dataset(REPO, "persona")   # persona SFT

# a single split of a single subset
train = load_dataset(REPO, "sft", split="train")

# language filtering (v2: every row carries a `language` column)
de = train.filter(lambda r: r["language"] == "de")
human_de = de  # all de rows are human-written (OASST1/Aya), slop-filtered
```

### Suggested recipe

1. **SFT** — fit `sft/train`, pick checkpoints on `sft/validation`, report `sft/test` (in-distribution) and `sft/benchmark` (external).
2. **DPO** — start from the SFT model, fit `ct/train`, early-stop on `ct/validation` preference accuracy, report `ct/benchmark`.
3. **GRPO** — fit `rl/train` with the provided verifiers, monitor reward on `rl/validation`, report `rl/benchmark`.
4. **Persona** — mix `persona/train` into SFT or train a style LoRA; check adherence on `persona/test`.

```python
# RL with verifiable rewards only (drop free-form tasks for strict scoring):
rl_v = load_dataset(REPO, "rl", split="train").filter(lambda x: x["verifier"] != "free")
```

## Column reference

- **`language`** *(v2, all subsets & splits)* — ISO code from langdetect (`en`, `de`, `uk`, …) or `unknown` for very short/numeric prompts.

### `sft.subset` tags (train split)

| value | rows | meaning |
|---|---:|---|
| `general` | 147,499 | general instruction/chat data (incl. human-written de/uk additions) |
| `bench` | 37,631 | benchmark-style training items (upstream-decontaminated) |
| `reasoning` | 27,993 | reasoning / math / CoT |
| `legacy` | 23,302 | recovered from blend v1–v2, predate the tagging scheme |
| `persona` | 18,276 | persona-flavoured chat |
| `code` | 16,790 | code |
| `benchmark` | 55,867 | *(benchmark split only)* external eval items |

### `rl.verifier` (full task set)

free 17,394 · persona 5,868 · number 2,194 · format 1,530 · span 1,217 · mcq 1,216 · python 1,130 · label 765 · sql 748 · yn 625 · json 432 · refusal_benign 378 · tool_outcome 378 · refusal_harmful 366

### Benchmark families (`sft.benchmark`)

hellaswag 5,000 · mmlu_prox_ja 5,000 · bbh 4,999 · mmlu_prox_ko 4,999 · mmlu_prox_ru 4,999 · mmlu_prox_zh 4,999 · mmlu 4,995 · boolq 3,270 · squadv2 2,498 · arc_easy 2,376 · bb_emojis_emotion_mc 2,000 · piqa 1,838 · winogrande 1,267 · arc_challenge 1,172 · sciq 1,000 · belebele_de 900 · belebele_cs 900 · belebele_sk 900 · belebele_uk 900 · truthfulqa_mc1_mc2 805 · logiqa 651 · gpqa_diamond_zeroshot 198 · eq_bench 171 · aime24 30

Item kinds: `mcq`, `free`, `yn`, `span`, `label`, `set`, `number`.

## 🌍 Languages

langdetect over every row's first user prompt (`language` column, full detail in repo):

| lang | rows | share |
|---|---:|---:|
| `en` | 429,424 | 89.5% |
| `ru` | 7,258 | 1.5% |
| `ko` | 6,474 | 1.3% |
| `zh` | 6,353 | 1.3% |
| `unknown` | 6,335 | 1.3% |
| `ja` | 6,252 | 1.3% |
| `de` | 3,623 | 0.8% |
| `uk` | 1,744 | 0.4% |
| `es` | 1,510 | 0.3% |
| `fr` | 1,139 | 0.2% |
| `cs` | 1,056 | 0.2% |
| `sk` | 974 | 0.2% |
| `ro` | 860 | 0.2% |
| `ca` | 758 | 0.2% |

Coverage intent: **en, ja, de, zh, sk, cs, ru, uk** (+ existing ko and a ~1% long tail, kept per policy — the `language` column makes any subset trivial to select).

## 🧹 Cleaning & provenance

Built from 10 source datasets by deterministic script (`build.py`), then the v2 pass (`build_v2.py`):

| family | sources | what happened |
|---|---|---|
| chat blends | `super-lfm-blend-v1`…`v4` (525,109 rows) | concatenated, SHA1-deduplicated on normalized message content — 203,324 cross-version duplicates removed, newest version wins; 321,785 unique remain |
| RL tasks | `super-lfm-rl-tasks-v1`, `v2` | identical task IDs in both → v2 kept (richer metadata) |
| preference pairs | `super-lfm-pref-v1`, `v2` | identical content in both → v2 kept |
| benchmarks | `super-lfm-eval-v1` | 9 exact duplicates removed → 52,268; reformatted to chat; lives only in `sft.benchmark` |
| persona | `super-lfm-persona-v1` | 161 exact duplicates removed → 4,228 |
| human languages *(v2)* | `OpenAssistant/oasst1` (de/cs/sk/uk), `CohereLabs/aya_dataset` (de/uk) | 2,276 + 760 = 3,036 rows accepted after dedup + the same slop filter, split 75/12.5/12.5 into train/validation/test |
| reading benchmarks *(v2)* | `facebook/belebele` (deu_Latn, ces_Latn, slk_Latn, ukr_Cyrl) | 3,600 rows appended to `sft.benchmark` only |

- Every assistant turn carries the `<think></think>` think-fix prefix (already present across all blend versions).
- Splits use a fixed seed (42) shuffle with exact-count slicing — rebuilds reproduce bit-for-bit.
- Upstream blends report decontamination against 20 common benchmarks; independently, this repo guarantees benchmark rows never enter a training split.

### v2 de-bot pass — rows removed

| rule | rows removed |
|---|---:|
| bot-identity / corpo-speak phrase in the target text | 10,665 |
| same rules hitting DPO `chosen` (rejected kept as-is) | 5,787 |
| purple-prose density (heretic `noslop` markers ≥3/100 words) | 2,334 |
| same rules hitting RL gold answers | 1,054 |
| malformed conversation shape | 23 |
| AI-identity probe prompts ("are you an AI?") | 11 |
| **total** | **19,874** |

Design notes:

- `ct.rejected` is **never** removed for slop — dispreferred bot-speak is exactly the negative signal DPO needs. Only `chosen` (and assistant/gold targets everywhere else) is filtered.
- `persona` content is untouched (measured 0% slop; it's deliberate creative voice).
- Purple-prose is removed by **density**, not single words — human horror/creative writing uses words like *velvet* and *crimson* too; AI slop clusters them (≥3 markers per 100 words, or ≥5 distinct in one target).
- Assistant-identity system lines (*"You are a helpful assistant."*) are stripped rather than dropping the row.

## 📊 Results & scores

### Filter quality (measured)

Scored against [DrRiceIO7/SlopReview](https://huggingface.co/datasets/DrRiceIO7/SlopReview) `v3` — 6,579 labeled AI-slop rows and 1,000 labeled human rows:

| metric | score |
|---|---|
| AI-slop rows caught by the v2 filter | **56.6%** |
| human rows wrongly removed (false-positive rate) | 8.2% |
| pre-v2 slop prevalence (phrase scan) | sft 3.2% · ct 19.8% · rl 2.1% · persona 0.0% |

Slop inside `ct.rejected` is counted as *detected* here but deliberately **kept** in the dataset (negative examples).

### Reference local run (fill-in)

Designed for a small model on a 16 GB machine — MLX (`mlx-lm`) or Unsloth, LION-style optimizer:

| model | stage | steps / epochs | tokens | `sft.test` | `sft.benchmark` | `ct.benchmark` pref-acc | `rl.benchmark` reward |
|---|---|---|---|---|---|---|---|
| LFM 2.5 2.6B | SFT→DPO→GRPO | — | — | — | — | — | — |
| Spark 2.6 4B | SFT→DPO→GRPO | — | — | — | — | — | — |

**Eval protocol** (same for any model you put in the table):

1. `sft.benchmark` — exact-match / letter accuracy per family (mcq, yn, span, number, set, label).
2. `ct.benchmark` — preference accuracy: share of pairs where the model ranks `chosen` > `rejected`.
3. `rl.benchmark` — mean verifier reward, macro-averaged over families (exclude `free` for strict scoring).
4. `persona.benchmark` — held-out persona adherence (style rubric / judge score).
5. Report the same metrics on `test` splits as the in-distribution counterpart.

## ⚠️ Content notice

Inherited from source datasets: the chat blends contain explicit horror and NSFW creative writing plus material from public roleplay and "uncensored" community datasets. Published for research and private experimentation; not filtered for workplace or educational use.

## License

`other` — mixed upstream licenses; see the source dataset cards.
