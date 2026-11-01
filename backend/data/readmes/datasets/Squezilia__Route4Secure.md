---
license: cc-by-4.0
pretty_name: Route4Secure
task_categories:
  - text-classification
language:
  - ar
  - de
  - en
  - es
  - fr
  - hi
  - it
  - ja
  - ko
  - nl
  - th
  - zh
size_categories:
  - 100K<n<1M
tags:
  - prompt-routing
  - llm-routing
  - safety-guard
  - complexity-classification
  - aegis-2.0
  - multilingual
  - nemotron
  - oasst1
  - oasst2
  - openthoughts
configs:
  - config_name: default
    default: true
    data_files:
      - split: train
        path: Route4Secure.parquet
  - config_name: oasst1
    data_files:
      - split: train
        path: OASST1.parquet
  - config_name: oasst2
    data_files:
      - split: train
        path: OASST2.parquet
  - config_name: nemotron
    data_files:
      - split: train
        path: nemotron.parquet
  - config_name: open_thoughts
    data_files:
      - split: train
        path: open_thoughts.parquet
---

![Route4Secure Banner](./Route4Secure%20Banner.png)

# Route4Secure: Multilingual Prompt Complexity, Intent & Safety Routing Dataset

**Route4Secure** is a large-scale, multilingual dataset designed for training **unified LLM prompt routers and safety guardrails**. It combines human-curated conversational prompts from **OpenAssistant (`OASST1` & `OASST2`)**, adversarial, synthetic, and real-world safety examples from **NVIDIA Nemotron Safety Guard Dataset v3**, and high-complexity (`level 5–7`) code, math, and science prompts from **OpenThoughts3-1.2M** (machine-translated into 11 languages with **`Hy-MT2-7B`**), annotated under a unified 12-column schema using **`Qwen3.5-9B`**.

Unlike single-objective routing datasets that only score prompt difficulty or binary toxicity in isolation, **Route4Secure** provides joint supervision across five routing dimensions for every prompt:
1. **Prompt Complexity (`level`: `0`–`7`)**: Inherent technical, mathematical, logical, or linguistic difficulty of the underlying task (explicitly stripping away decorative vocabulary inflation).
2. **Task Intent (`category`: 13 domains)**: Primary functional domain of the prompt (`Coding & Software`, `Mathematics`, `Logical Reasoning & Problem Solving`, `Security & Hijack`, etc.).
3. **Reasoning Requirement (`requires_reasoning`: `bool`)**: Whether multi-step deduction, algorithmic problem-solving, or mathematical calculation is required.
4. **Binary Safety (`safe`: `bool`)**: **57.62% Safe / 42.38% Unsafe** distribution in the primary `default` configuration (see [§4](#4-dataset-construction-safety-12-language--complexity-level--3-balancing) and [§7](#7-limitations--ethical-considerations)).
5. **Fine-Grained Aegis 2.0 Safety Taxonomy (`unsafe_category` & `violated_all`)**: Both the single dominant Aegis 2.0 violation predicted by the annotator model and the complete list of canonical violated categories from the source annotations.

---

## 1. Repository Configurations & Files

All Parquet files in this repository share the **exact same 12-column PyArrow schema** (with dictionary-encoded categorical columns and `zstd` compression). You can load the main dataset (`default`) or inspect any individual source shard:

| Config Name | File | Rows | Size | Languages | Safe / Unsafe Split | Description |
| :--- | :--- | ---: | ---: | :--- | :--- | :--- |
| **`default`** | `Route4Secure.parquet` | **130,050** | 58.7 MB | 12 languages | **57.62% Safe** (`74,938`) / **42.38% Unsafe** (`55,112`) | **Main training dataset.** Combines language- and complexity-balanced `OASST1` + `OASST2` with `nemotron` and a `level 5–7` subset of `open_thoughts`. |
| **`oasst1`** | `OASST1.parquet` | **33,170** | 5.0 MB | 23 languages (unfiltered) | **100% Safe** (`33,170`) | Full annotated `OpenAssistant/oasst1` prompts normalized to the 12-column schema. |
| **`oasst2`** | `OASST2.parquet` | **48,051** | 7.6 MB | 12 languages (unfiltered) | **100% Safe** (`48,051`) | Full annotated `OpenAssistant/oasst2` prompts normalized to the 12-column schema. |
| **`nemotron`** | `nemotron.parquet` | **97,369** | 40.2 MB | 12 balanced languages | **40.68% Safe** (`39,610`) / **59.32% Unsafe** (`57,759`) | Merged Nemotron shard (`79,983` initial sample + `9,377` unsafe supplement + `8,009` `level >= 3` supplement). |
| **`open_thoughts`** | `open_thoughts.parquet` | **39,732** | 26.6 MB | 12 perfectly balanced languages (`3,311` each) | **100% Safe** (`39,732`) | Cleaned `level 3–7` OpenThoughts3-1.2M prompts: `3,311` unique English source prompts × 12 languages (English original + 11 `Hy-MT2-7B` translations). |

---

## 2. Unified 12-Column Schema & Dictionary Encodings

Every configuration conforms to the following 12-column Arrow schema:

| Column | Arrow Type | Nullable | Description |
| :--- | :--- | :---: | :--- |
| `id` | `int32` | No | Sequential integer identifier (`0 .. N-1`). |
| `prompt` | `string` | No | Raw user prompt text to be classified/routed. |
| `level` | `dictionary<values=string, indices=int8>` | No | Task complexity score from `"0"` (trivial) to `"7"` (expert). |
| `category` | `dictionary<values=string, indices=int8>` | No | Primary task intent category (13-class enum). |
| `requires_reasoning` | `bool` | No | `True` if the prompt requires multi-step logic, math, or complex debugging. |
| `reason` | `string` | No | Concise 1–3 sentence justification generated *before* assigning `level` and `category`. |
| `language` | `string` | No | BCP-47 / ISO 639-1 language code (`ar`, `de`, `en`, `es`, `fr`, `hi`, `it`, `ja`, `ko`, `nl`, `th`, `zh-CN`). |
| `source` | `string` | No | Upstream dataset identifier (`OpenAssistant/oasst1`, `OpenAssistant/oasst2`, `nvidia/Nemotron-Safety-Guard-Dataset-v3`, or `open-thoughts/OpenThoughts3-1.2M`). |
| `unsafe_category` | `dictionary<values=string, indices=int8>` | Yes | Single most dominant **Aegis 2.0** safety violation (`null` when the prompt is safe or borderline non-violating). |
| `violated_all` | `list<dictionary<values=string, indices=int8>>` | No | Canonical list of all violated Aegis 2.0 categories from source annotations (`[]` for safe prompts). |
| `safe` | `bool` | No | Ground-truth binary safety flag (`True` = safe, `False` = unsafe). |
| `synthetic` | `bool` | No | `True` if the source safety label was synthetically annotated (`llm_jury`) **or** the prompt text is a machine translation (`Hy-MT2-7B` rows of `open_thoughts`); `False` for human-curated annotations (`OASST1`, `OASST2`, human-labeled Nemotron rows) and original English OpenThoughts prompts. |

---

## 3. Annotation Protocol (`Qwen3.5-9B`)

All prompts across `OASST1`, `OASST2`, and `Nemotron` were annotated using **`Qwen3.5-9B`** (`unsloth/Qwen3.5-9B-GGUF:Q4_K_M`) served via `llama.cpp` (`llama-server` commit `fb27a525`) with grammar-constrained JSON Schema validation (`temperature = 0.1`, `max_tokens = 768`, `context_per_slot = 8192`, thinking disabled). The English source prompts of `open_thoughts` were annotated with the same model, system prompt, and rubric (see [§3.1](#31-openthoughts-pipeline-classification--translation--cleaning)).

### Key Design Principles of the Annotation Pipeline
- **Anti-Inflation Complexity Scoring (`reason`-first)**: A common failure mode in LLM complexity routers is scoring ornate or academic-sounding phrasing as "hard" even when the underlying task is trivial (e.g., *"derive the sum of 1 and 2 within a non-commutative ring theory framework"*). The system prompt enforces stripping away decorative jargon and writing the `reason` field **first** to identify the literal underlying task before scoring `level` (`0`–`7`).
- **Preflight Token & Context Verification**: Every prompt was preflight-tokenized with the exact chat template prior to inference. Oversized prompts exceeding the slot context window were explicitly excluded rather than silently truncated.
- **Refusal & Schema Filtering**: Prompts where the annotator model triggered an explicit refusal, truncated output, invalid JSON schema, or English refusal heuristic (`I cannot assist`, `I must decline`, etc.) were excluded from training exports.
- **Dominant Aegis 2.0 Resolution**: For multi-label unsafe prompts in Nemotron, the annotator received the normalized ground-truth `hint_violated_categories` and independently selected the **single most severe/dominant** Aegis 2.0 category for `unsafe_category`, while `violated_all` preserves the full multi-label set.
- **Safe Polyfill for OpenAssistant & OpenThoughts**: Because `OpenAssistant/oasst1`, `OpenAssistant/oasst2`, and `open-thoughts/OpenThoughts3-1.2M` do not contain unsafe violation flags, their safety columns are polyfilled as `safe = True`, `unsafe_category = None`, and `violated_all = []` (`synthetic = False` for OpenAssistant; see the `synthetic` column definition for OpenThoughts).

### 3.1. OpenThoughts Pipeline (Classification → Translation → Cleaning)
1. **Candidate Pool & Level Filtering**: A `60,000`-prompt candidate pool was drawn from the code, math, and science shards of `open-thoughts/OpenThoughts3-1.2M` and interleaved round-robin (`Code → Math → Science`). Each candidate was classified with the `Qwen3.5-9B` rubric above, and only prompts scored `level >= 3` were accepted until per-level quotas were met (`4,247` accepted English prompts).
2. **Translation into 11 Languages**: Each accepted English prompt was translated into `ar, de, es, fr, hi, it, ja, ko, nl, th, zh-CN` with **`tencent/Hy-MT2-7B-GGUF`** (`Q4_K_M`, `temperature = 0.7`, `top_p = 0.6`, `top_k = 20`, `repetition_penalty = 1.05`, `max_tokens = 4096`, `context_per_slot = 8192`).
3. **Label Propagation**: Translations inherit the English source prompt's `level`, `category`, `requires_reasoning`, and (English) `reason`. Every source prompt therefore forms a **12-row translation group** with identical labels.
4. **Group-Level Cleaning** (`4,247` → **`3,311`** groups, `50,964` → **`39,732`** rows): Entire 12-row groups were removed when the English source prompt was an exact duplicate of another source prompt (including duplicates with conflicting `level` labels), contained `<image>` placeholders (references to images unavailable in text-only prompts), or had any broken / truncated translation.

---

## 4. Dataset Construction: Safety, 12-Language & Complexity (`level >= 3`) Balancing

Raw `OASST1` (`33,170` rows) and `OASST2` (`48,051` rows) contain `81,221` safe prompts across 23 languages, but are heavily skewed toward English (`39,172` rows) and Spanish (`17,047` rows). Meanwhile, `nvidia/Nemotron-Safety-Guard-Dataset-v3` supports **12 balanced languages** (`ar, de, en, es, fr, hi, it, ja, ko, nl, th, zh-CN`). Furthermore, natural prompt distributions follow a steep Zipfian curve dominated by `level = 1` queries.

To construct the balanced **`default` (`Route4Secure.parquet`)** split across all three axes (12 languages, safety, and enriched `level >= 3` complexity):
1. **12-Language Alignment**: `OASST1` and `OASST2` language codes were normalized (`zh` $\rightarrow$ `zh-CN`) and filtered to the 12 languages supported by Nemotron (excluding `12,024` rows in non-Nemotron languages).
2. **100% Preservation of `level >= 3` in OpenAssistant (`10,052` rows)**: Rather than losing rare high-complexity prompts during language capping, **100% of all `level >= 3` prompts (`10,052` rows)** across all 12 in-scope languages in `OASST1 + OASST2` were retained. In English (`6,409` `level >= 3` rows), only `level >= 3` prompts were taken from OASST and the `1,409` excess above the `5,000` language cap was swapped 1-for-1 by removing `1,409` `level = 1` English rows from Nemotron. In Spanish (`2,277` `level >= 3` rows), the remaining `2,723` slots to reach `5,000` were sampled proportionally from `level = 0` and `level = 2` (`0` rows from `level = 1`).
3. **50/50 Safe / Unsafe Supplement (`9,377` rows)**: To balance the safe OASST prompts against the initial `79,983`-row stratified Nemotron pass (`33,184` safe + `46,799` unsafe), a deterministic zero-overlap supplement of **`9,377` valid `unsafe` Nemotron rows** was collected.
4. **High-Complexity (`level >= 3`) Nemotron Mining & 1-for-1 Swap (`8,009` rows)**: From the remaining `362,030` unprocessed Nemotron rows, candidates were scored per language using structural complexity signals (language-normalized length, multi-line structure, code/math/step-by-step/technical markers) and evaluated in round-robin order with `Qwen3.5-9B`, retaining only prompts verified as `level >= 3`. This yielded **`8,009` additional `level >= 3` Nemotron rows** (`3,533` L3, `3,350` L4, `1,040` L5, `61` L6, `25` L7), which were swapped 1-for-1 per `(language, safe)` against `level = 1` rows in Nemotron. This reduced `level = 1` share from `48.56%` down to **`36.63%`** and more than doubled `level >= 3` coverage from `10.15%` (`11,400` rows) to **`23.69%` (`26,611` rows)** while keeping total dataset size (`112,338` rows), 12-language balance, and near-50/50 safety (**50.94% Safe / 49.06% Unsafe**) intact.
5. **Expert-Tier (`level 5–7`) OpenThoughts Expansion (`17,712` rows)**: After step 4, the top three complexity classes were still severely under-represented (`L5` `2.00%`, `L6` `0.35%`, `L7` `0.17%`; a `214×` ratio between the largest and smallest class). From the cleaned `open_thoughts` shard, **whole 12-language translation groups** were sampled (seed `42`): **`500` groups (`6,000` rows) each for `L5` and `L6`, and all `476` available `L7` groups (`5,712` rows)**. Three groups whose prompts are pure chemical formulas / LaTeX (identical text across all 12 languages) were excluded. These rows are **appended** (no swap), with zero overlap against the existing rows.
   - `L5` / `L6` / `L7` grew from `2,247` / `397` / `192` to **`8,247` / `6,397` / `5,904`** rows (**`6.34%` / `4.92%` / `4.54%`**).
   - The largest-to-smallest class ratio dropped from `214×` to **`7.0×`**, and `level` entropy rose from `2.29` to **`2.68`** bits (max `3.00`).
   - Because all appended rows are safe, the global safety split moved from `50.94% / 49.06%` to **`57.62% / 42.38%`**.
   - OpenThoughts rows occupy `id` `112,338`–`130,049`, ordered group by group (languages in alphabetical order within each group). **The translation group key is `(id - 112338) // 12`** (in the `open_thoughts` config: `id // 12`). Use it for group-aware train/validation/test splits to avoid cross-lingual leakage.

---

## 5. Dataset Statistics (`default` — 130,050 Rows)

### 5.1. Breakdown by Source & Safety
| Source Dataset | `safe` | `synthetic` | Rows | Share (%) |
| :--- | :---: | :---: | ---: | ---: |
| `nvidia/Nemotron-Safety-Guard-Dataset-v3` | `False` | `False` | 40,541 | 31.17% |
| `nvidia/Nemotron-Safety-Guard-Dataset-v3` | `True` | `False` | 25,391 | 19.52% |
| `open-thoughts/OpenThoughts3-1.2M` | `True` | `True` | 16,236 | 12.48% |
| `OpenAssistant/oasst2` | `True` | `False` | 14,885 | 11.45% |
| `nvidia/Nemotron-Safety-Guard-Dataset-v3` | `False` | `True` | 14,571 | 11.20% |
| `OpenAssistant/oasst1` | `True` | `False` | 9,502 | 7.31% |
| `nvidia/Nemotron-Safety-Guard-Dataset-v3` | `True` | `True` | 7,448 | 5.73% |
| `open-thoughts/OpenThoughts3-1.2M` | `True` | `False` | 1,476 | 1.13% |
| **Total** | **74,938 Safe / 55,112 Unsafe** | **91,795 Non-synthetic / 38,255 Synthetic** | **130,050** | **100.00%** |

### 5.2. Language Distribution (12 Languages)
| Language | Code | Safe (`True`) | Unsafe (`False`) | Total Rows | Share (%) |
| :--- | :---: | ---: | ---: | ---: | ---: |
| English | `en` | 10,386 | 3,790 | 14,176 | 10.90% |
| Spanish | `es` | 9,228 | 4,399 | 13,627 | 10.48% |
| Chinese (Simplified) | `zh-CN` | 8,568 | 4,420 | 12,988 | 9.99% |
| German | `de` | 7,993 | 4,805 | 12,798 | 9.84% |
| French | `fr` | 6,802 | 4,691 | 11,493 | 8.84% |
| Thai | `th` | 5,522 | 5,018 | 10,540 | 8.10% |
| Dutch | `nl` | 4,122 | 5,353 | 9,475 | 7.29% |
| Arabic | `ar` | 4,312 | 5,024 | 9,336 | 7.18% |
| Japanese | `ja` | 4,762 | 4,387 | 9,149 | 7.03% |
| Italian | `it` | 4,785 | 4,359 | 9,144 | 7.03% |
| Hindi | `hi` | 4,293 | 4,382 | 8,675 | 6.67% |
| Korean | `ko` | 4,165 | 4,484 | 8,649 | 6.65% |

### 5.3. Complexity Level Distribution (`level` `0`–`7`)
| Level | Tier | Safe (`True`) | Unsafe (`False`) | Total Rows | Share (%) |
| :---: | :--- | ---: | ---: | ---: | ---: |
| `"0"` | Trivial | 10,744 | 6,594 | 17,338 | 13.33% |
| `"1"` | Trivial | 9,725 | 31,429 | 41,154 | 31.64% |
| `"2"` | Moderate | 15,289 | 11,946 | 27,235 | 20.94% |
| `"3"` | Moderate | 9,027 | 1,961 | 10,988 | 8.45% |
| `"4"` | Complex | 10,140 | 2,647 | 12,787 | 9.83% |
| `"5"` | Complex | 7,896 | 351 | 8,247 | 6.34% |
| `"6"` | Expert / Advanced | 6,330 | 67 | 6,397 | 4.92% |
| `"7"` | Expert / Advanced | 5,787 | 117 | 5,904 | 4.54% |

- **`level >= 3`**: `44,323` (34.08%) · **`level >= 5`**: `20,548` (15.80%)
- **`requires_reasoning = False`**: `96,747` (74.39%)
- **`requires_reasoning = True`**: `33,303` (25.61%)

### 5.4. Task Intent Category Distribution (`category`)
| Category | Rows | Share (%) |
| :--- | ---: | ---: |
| `Other` | 32,441 | 24.95% |
| `Information & Science` | 24,492 | 18.83% |
| `Writing & Content Creation` | 20,950 | 16.11% |
| `Security & Hijack` | 14,399 | 11.07% |
| `Coding & Software` | 11,292 | 8.68% |
| `Roleplaying` | 8,340 | 6.41% |
| `Mathematics` | 6,982 | 5.37% |
| `Logical Reasoning & Problem Solving` | 4,657 | 3.58% |
| `Text Processing & Summarization` | 2,252 | 1.73% |
| `Arts & Culture` | 1,955 | 1.50% |
| `Data Manipulation` | 1,222 | 0.94% |
| `Language Translation` | 682 | 0.52% |
| `Media Generation` | 386 | 0.30% |

### 5.5. Dominant Aegis 2.0 Safety Category Distribution (`unsafe_category`)
| Aegis 2.0 Category | Rows | Share (%) |
| :--- | ---: | ---: |
| `null` (Safe / Non-violating) | 74,837 | 57.54% |
| `Criminal Planning/Confessions` | 16,449 | 12.65% |
| `Hate/Identity Hate` | 7,712 | 5.93% |
| `Harassment` | 4,119 | 3.17% |
| `PII/Privacy` | 3,641 | 2.80% |
| `Controlled/Regulated Substances` | 3,308 | 2.54% |
| `Sexual` | 3,090 | 2.38% |
| `Violence` | 2,790 | 2.15% |
| `Suicide and Self Harm` | 2,297 | 1.77% |
| `Profanity` | 1,821 | 1.40% |
| `Guns/Illegal Weapons` | 1,723 | 1.32% |
| `Unauthorized Advice` | 1,510 | 1.16% |
| `Illegal Activity` | 1,455 | 1.12% |
| `Immoral/Unethical` | 1,286 | 0.99% |
| `Sexual Minor` | 805 | 0.62% |
| `Fraud/Deception` | 791 | 0.61% |
| `Political/Misinformation/Conspiracy` | 720 | 0.55% |
| `Malware` | 537 | 0.41% |
| `Manipulation` | 517 | 0.40% |
| `Threat` | 314 | 0.24% |
| `High Risk Gov. Decision Making` | 180 | 0.14% |
| `Copyright/Trademark/Plagiarism` | 148 | 0.11% |

---

## 6. Usage

### Loading with Hugging Face `datasets`

```python
from datasets import load_dataset

# 1. Load the main Route4Secure dataset (130,050 rows)
ds = load_dataset("Squezilia/Route4Secure", split="train")
print(ds)

# 2. Load individual normalized source shards if needed
oasst1_ds = load_dataset("Squezilia/Route4Secure", "oasst1", split="train")              # 33,170 rows
oasst2_ds = load_dataset("Squezilia/Route4Secure", "oasst2", split="train")              # 48,051 rows
nemotron_ds = load_dataset("Squezilia/Route4Secure", "nemotron", split="train")          # 97,369 rows
open_thoughts_ds = load_dataset("Squezilia/Route4Secure", "open_thoughts", split="train")  # 39,732 rows
```

### Reading Dictionary-Encoded Parquet Directly with `pyarrow` / `pandas`

```python
import pyarrow.parquet as pq

table = pq.read_table("hf://datasets/Squezilia/Route4Secure/Route4Secure.parquet")
df = table.to_pandas()
print(df[["prompt", "level", "category", "requires_reasoning", "safe", "unsafe_category", "language"]].head())
```


---

## 7. Limitations & Ethical Considerations

- **Adversarial & Sensitive Content Warning**: Because roughly 42% of `Route4Secure` consists of unsafe and jailbreak prompts sourced from `nvidia/Nemotron-Safety-Guard-Dataset-v3`, the dataset contains explicit examples of hate speech, criminal planning, self-harm, violence, malware requests, and other harmful categories. It is intended **strictly for training and evaluating safety guardrails, moderation classifiers, and LLM routers**.
- **LLM Annotation Disagreements**: Complexity (`level`), domain (`category`), `requires_reasoning`, and dominant `unsafe_category` annotations are generated by `Qwen3.5-9B` (`Q4_K_M`). While `safe` and `violated_all` preserve upstream ground-truth labels, `unsafe_category` reflects the annotator model's prediction and can occasionally disagree with the binary `safe` flag on borderline prompts (~6% disagreement rate in raw Nemotron). Users training strict binary safety classifiers should rely on `safe` (or `len(violated_all) > 0`) as the ground-truth safety target.
- **High-Complexity Safety & Domain Skew**: `97.4%` of `level 5–7` rows are safe, and `~86%` of them come from OpenThoughts (code, math, and science only). A naive classifier may learn shortcuts such as *"expert-level ⇒ math/code ⇒ safe"* or *"long prompt ⇒ high level"* (OpenThoughts `L6`/`L7` prompts are much longer than other `L6`/`L7` rows). High-complexity unsafe prompts (e.g., sophisticated multi-step jailbreaks) remain scarce; consider class- or source-aware reweighting and evaluate on held-out complex unsafe prompts.
- **Machine-Translated Content**: 11/12 of every OpenThoughts group is a `Hy-MT2-7B` translation (`synthetic = True`) that inherits the English labels and English `reason`. Despite group-level cleaning, translations may contain residual errors, and math/code-heavy prompts naturally keep a large share of Latin script, LaTeX, and code in non-Latin-script languages.
- **Long Prompts**: OpenThoughts prompts are long (median `~370` XLM-R tokens; `~37%` exceed `512` tokens). Encoder models with a `512`-token limit will truncate them; head+tail truncation is recommended so that the final question is preserved.
- **Residual Language Ratio Skew**: The 12 languages each represent 6.6%–10.9% of the dataset, but languages with heavy OpenAssistant coverage (`en`, `es`, `zh-CN`, `de`) have a higher internal proportion of `safe` prompts (~62%–73% safe) compared to languages sourced primarily from Nemotron (`nl`, `ar`, `ko`, `hi`, ~44%–50% safe).

---

## 8. License & Attribution

This dataset is released under the **Creative Commons Attribution 4.0 International (`CC-BY-4.0`)** license, consistent with upstream attribution requirements:
- **[nvidia/Nemotron-Safety-Guard-Dataset-v3](https://huggingface.co/datasets/nvidia/Nemotron-Safety-Guard-Dataset-v3)** — Licensed under `CC-BY-4.0`.
- **[OpenAssistant/oasst1](https://huggingface.co/datasets/OpenAssistant/oasst1)** & **[OpenAssistant/oasst2](https://huggingface.co/datasets/OpenAssistant/oasst2)** — Licensed under `Apache-2.0`.
- **[open-thoughts/OpenThoughts3-1.2M](https://huggingface.co/datasets/open-thoughts/OpenThoughts3-1.2M)** — Licensed under `Apache-2.0`. Translations produced with **[tencent/Hy-MT2-7B](https://huggingface.co/tencent/Hy-MT2-7B-GGUF)**.

### Citation

```bibtex
@dataset{squezilia_route4secure_2026,
  author       = {Squezilia},
  title        = {Route4Secure: Multilingual Prompt Complexity, Intent and Safety Routing Dataset},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/datasets/Squezilia/Route4Secure}}
}
```
