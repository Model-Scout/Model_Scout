---
license: mit
language:
- ko
- en
pretty_name: NOLLI
size_categories:
- 1K<n<10K
task_categories:
- question-answering
tags:
- reasoning
- logic
- puzzles
- korean
configs:
- config_name: array_formula
  data_files:
  - split: test
    path: array_formula/test-*
- config_name: causal_dag
  data_files:
  - split: test
    path: causal_dag/test-*
- config_name: cipher
  data_files:
  - split: test
    path: cipher/test-*
- config_name: cryptarithmetic
  data_files:
  - split: test
    path: cryptarithmetic/test-*
- config_name: inequality
  data_files:
  - split: test
    path: inequality/test-*
- config_name: jamo
  data_files:
  - split: test
    path: jamo/test-*
- config_name: kinship
  data_files:
  - split: test
    path: kinship/test-*
- config_name: korean_units
  data_files:
  - split: test
    path: korean_units/test-*
- config_name: minesweeper
  data_files:
  - split: test
    path: minesweeper/test-*
- config_name: number_baseball
  data_files:
  - split: test
    path: number_baseball/test-*
- config_name: saju
  data_files:
  - split: test
    path: saju/test-*
- config_name: sat_puzzles
  data_files:
  - split: test
    path: sat_puzzles/test-*
- config_name: sudoku
  data_files:
  - split: test
    path: sudoku/test-*
- config_name: time
  data_files:
  - split: test
    path: time/test-*
- config_name: yacht_dice
  data_files:
  - split: test
    path: yacht_dice/test-*
dataset_info:
- config_name: array_formula
  features:
  - name: id
    dtype: string
  - name: task
    dtype: string
  - name: language
    dtype: string
  - name: difficulty
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: solution
    dtype: string
  splits:
  - name: test
    num_bytes: 13407331
    num_examples: 600
  download_size: 3956244
  dataset_size: 13407331
- config_name: causal_dag
  features:
  - name: id
    dtype: string
  - name: task
    dtype: string
  - name: language
    dtype: string
  - name: difficulty
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: solution
    dtype: string
  splits:
  - name: test
    num_bytes: 10991552
    num_examples: 600
  download_size: 2486519
  dataset_size: 10991552
- config_name: cipher
  features:
  - name: id
    dtype: string
  - name: task
    dtype: string
  - name: language
    dtype: string
  - name: difficulty
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: solution
    dtype: string
  splits:
  - name: test
    num_bytes: 2191175
    num_examples: 600
  download_size: 277124
  dataset_size: 2191175
- config_name: cryptarithmetic
  features:
  - name: id
    dtype: string
  - name: task
    dtype: string
  - name: language
    dtype: string
  - name: difficulty
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: solution
    dtype: string
  splits:
  - name: test
    num_bytes: 2697176
    num_examples: 600
  download_size: 545993
  dataset_size: 2697176
- config_name: inequality
  features:
  - name: id
    dtype: string
  - name: task
    dtype: string
  - name: language
    dtype: string
  - name: difficulty
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: solution
    dtype: string
  splits:
  - name: test
    num_bytes: 2259573
    num_examples: 600
  download_size: 436357
  dataset_size: 2259573
- config_name: jamo
  features:
  - name: id
    dtype: string
  - name: task
    dtype: string
  - name: language
    dtype: string
  - name: difficulty
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: solution
    dtype: string
  splits:
  - name: test
    num_bytes: 384368
    num_examples: 300
  download_size: 52641
  dataset_size: 384368
- config_name: kinship
  features:
  - name: id
    dtype: string
  - name: task
    dtype: string
  - name: language
    dtype: string
  - name: difficulty
    dtype: string
  - name: question
    dtype: string
  - name: choices
    dtype: string
  - name: answer
    dtype: string
  - name: solution
    dtype: string
  splits:
  - name: test
    num_bytes: 3188738
    num_examples: 300
  download_size: 496080
  dataset_size: 3188738
- config_name: korean_units
  features:
  - name: id
    dtype: string
  - name: task
    dtype: string
  - name: language
    dtype: string
  - name: difficulty
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: solution
    dtype: string
  splits:
  - name: test
    num_bytes: 1401654
    num_examples: 300
  download_size: 639655
  dataset_size: 1401654
- config_name: minesweeper
  features:
  - name: id
    dtype: string
  - name: task
    dtype: string
  - name: language
    dtype: string
  - name: difficulty
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: solution
    dtype: string
  splits:
  - name: test
    num_bytes: 2570080
    num_examples: 600
  download_size: 424457
  dataset_size: 2570080
- config_name: number_baseball
  features:
  - name: id
    dtype: string
  - name: task
    dtype: string
  - name: language
    dtype: string
  - name: difficulty
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: solution
    dtype: string
  splits:
  - name: test
    num_bytes: 1299609
    num_examples: 600
  download_size: 220324
  dataset_size: 1299609
- config_name: saju
  features:
  - name: id
    dtype: string
  - name: task
    dtype: string
  - name: language
    dtype: string
  - name: difficulty
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: solution
    dtype: string
  splits:
  - name: test
    num_bytes: 180478
    num_examples: 300
  download_size: 26018
  dataset_size: 180478
- config_name: sat_puzzles
  features:
  - name: id
    dtype: string
  - name: task
    dtype: string
  - name: language
    dtype: string
  - name: difficulty
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: solution
    dtype: string
  splits:
  - name: test
    num_bytes: 28051763
    num_examples: 600
  download_size: 4931284
  dataset_size: 28051763
- config_name: sudoku
  features:
  - name: id
    dtype: string
  - name: task
    dtype: string
  - name: language
    dtype: string
  - name: difficulty
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: solution
    dtype: string
  splits:
  - name: test
    num_bytes: 1446800
    num_examples: 600
  download_size: 291709
  dataset_size: 1446800
- config_name: time
  features:
  - name: id
    dtype: string
  - name: task
    dtype: string
  - name: language
    dtype: string
  - name: difficulty
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: solution
    dtype: string
  splits:
  - name: test
    num_bytes: 258002
    num_examples: 300
  download_size: 39819
  dataset_size: 258002
- config_name: yacht_dice
  features:
  - name: id
    dtype: string
  - name: task
    dtype: string
  - name: language
    dtype: string
  - name: difficulty
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: solution
    dtype: string
  splits:
  - name: test
    num_bytes: 2112133
    num_examples: 600
  download_size: 374101
  dataset_size: 2112133
---

# NOLLI

**NOLLI (논리)** is a benchmark of rule-based logical puzzles in **Korean and English**, designed with
difficulty calibration in mind. It covers **15 task types x 3 difficulty tiers (easy / medium / hard)
x 100 examples** each, for a total of **7,500 examples** (EN 3,000 + KO 4,500).

All examples are programmatically generated with solver-verified answers. If you need more data,
the generators in the GitHub repository can produce additional examples for any task, language,
and difficulty tier.

📄 Paper: [https://arxiv.org/abs/2608.04397](https://arxiv.org/abs/2608.04397)\
💻 Code: [https://github.com/HAE-RAE/NOLLI](https://github.com/HAE-RAE/NOLLI)

## Tasks

Tasks follow a three-level cross-lingual spectrum: **direct translations**, **script adaptations**,
and **Korean-only** tasks.

### 1. Direct Translations (8 tasks · EN + KO)

Same generators and parameters in both languages, so performance gaps isolate presentation language.

| task | description | en (easy/med/hard) | ko (easy/med/hard) | total |
|---|---|---|---|---|
| `array_formula` | Apply row/column aggregation formulas (SUM/MEAN/MAX/...) to a 2D array in sequence | 100 / 100 / 100 | 100 / 100 / 100 | 600 |
| `causal_dag` | Infer event-propagation time through a causal graph with per-edge delays | 100 / 100 / 100 | 100 / 100 / 100 | 600 |
| `inequality` | CSP: place numbers 1..N satisfying inequality constraints (unique solution) | 100 / 100 / 100 | 100 / 100 / 100 | 600 |
| `minesweeper` | Minesweeper with minimal hints preserving a unique solution | 100 / 100 / 100 | 100 / 100 / 100 | 600 |
| `number_baseball` | Infer a hidden N-digit number from Strike/Ball hints | 100 / 100 / 100 | 100 / 100 / 100 | 600 |
| `sat_puzzles` | Boolean satisfiability (CNF) framed as a natural-language scenario | 100 / 100 / 100 | 100 / 100 / 100 | 600 |
| `sudoku` | 9x9 Sudoku with guaranteed-unique solutions | 100 / 100 / 100 | 100 / 100 / 100 | 600 |
| `yacht_dice` | Assign 12 dice rolls to 12 scoring categories to maximize total score; report the partial sum over spot-checked rounds | 100 / 100 / 100 | 100 / 100 / 100 | 600 |

### 2. Script Adaptations (2 tasks · EN + KO)

Not translation-equivalent: English uses Roman letters; Korean uses Hangul *jamo*.
Calibrated independently per language.

| task | description | en (easy/med/hard) | ko (easy/med/hard) | total |
|---|---|---|---|---|
| `cipher` | Decode stacked ciphers (Substitution, Vigenere, Reverse, Playfair, Transposition) | 100 / 100 / 100 | 100 / 100 / 100 | 600 |
| `cryptarithmetic` | Letters-for-digits arithmetic (SEND+MORE=MONEY style); Korean maps *jamo* groups | 100 / 100 / 100 | 100 / 100 / 100 | 600 |

### 3. Korean-Only (5 tasks · KO)

No English counterpart — built on structures specific to the Korean language and culture
(kinship terminology, the sexagenary calendar, traditional units, Hangul orthography).

| task | description | ko (easy/med/hard) | total |
|---|---|---|---|
| `jamo` | Decompose a Hangul syllable into 초성/중성/종성, shift 초성, recompose | 100 / 100 / 100 | 300 |
| `kinship` | Infer a Korean kinship term from a chain of family relationships (26-way multiple choice) | 100 / 100 / 100 | 300 |
| `korean_units` | Convert traditional Korean units (평·마지기·되·자·냥, ...) with randomized rates | 100 / 100 / 100 | 300 |
| `saju` | Compute the four 사주(四柱) pillars from a birth date/time | 100 / 100 / 100 | 300 |
| `time` | Korean calendar reasoning: holiday anchor + relative-day expression → date / 60갑자 일진 | 100 / 100 / 100 | 300 |

## Usage

```python
from datasets import load_dataset

# one task
ds = load_dataset("HAERAE-HUB/NOLLI", "sudoku", split="test")

# filter by language / difficulty (both are columns)
ko_hard = ds.filter(lambda x: x["language"] == "ko" and x["difficulty"] == "hard")
```

## Structure

Each config corresponds to one task. All configs share a single `test` split and the same schema
(the `choices` column exists only in `kinship`):

| column | type | description |
|---|---|---|
| `id` | str | unique example id, e.g. `sudoku_ko_0000` |
| `task` | str | task name (same as config name) |
| `language` | str | `ko` or `en` |
| `difficulty` | str | `easy` / `medium` / `hard` |
| `question` | str | full prompt for the model |
| `choices` | str | JSON-encoded answer choices — only present in the `kinship` config |
| `answer` | str | gold answer |
| `solution` | str | step-by-step reference solution |

## Citation

```bibtex
@misc{choi2026nolli,
      title={NOLLI: A Difficulty-Calibrated Puzzle Benchmark for Diagnosing the English-Korean Performance Gap},
      author={Dasol Choi and Joonyong Park and Daegon Yu and Soo Yong Kim and Youngsook Song and Seunghyeok Hong},
      year={2026},
      eprint={2608.04397},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2608.04397},
}
```
