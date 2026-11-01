---
pretty_name: LLM Speed Prompt Mix
license:
- mit
- apache-2.0
- cc-by-4.0
- cc-by-sa-4.0
language:
- ar
- bn
- de
- en
- es
- fr
- hi
- ja
- ko
- ru
- sw
- te
- th
- vi
- zh
multilinguality:
- multilingual
task_categories:
- text-generation
- question-answering
size_categories:
- n<1K
tags:
- benchmark
- inference-speed
- llama.cpp
- mixture-of-experts
- long-context
- multilingual
- korean
- code
dataset_info:
- config_name: all
  features:
  - name: id
    dtype: string
  - name: config
    dtype: string
  - name: tier
    dtype: string
  - name: language
    dtype: string
  - name: domain
    dtype: string
  - name: task
    dtype: string
  - name: license
    dtype: string
  - name: license_url
    dtype: string
  - name: attribution
    dtype: string
  - name: source_name
    dtype: string
  - name: source_url
    dtype: string
  - name: source_revision
    dtype: string
  - name: source_config
    dtype: string
  - name: source_split
    dtype: string
  - name: source_id
    dtype: string
  - name: source_articles
    list:
    - name: title
      dtype: string
    - name: url
      dtype: string
    - name: id
      dtype: string
  - name: source_files
    sequence: string
  - name: messages
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: follow_up
    sequence: string
  - name: reference
    dtype: string
  - name: target_tokens
    dtype: int64
  - name: tokens_deepseek_v4_1
    dtype: int64
  - name: needle_depth
    dtype: float64
  - name: chars
    dtype: int64
- config_name: mmlu_en
  features:
  - name: id
    dtype: string
  - name: config
    dtype: string
  - name: tier
    dtype: string
  - name: language
    dtype: string
  - name: domain
    dtype: string
  - name: task
    dtype: string
  - name: license
    dtype: string
  - name: license_url
    dtype: string
  - name: attribution
    dtype: string
  - name: source_name
    dtype: string
  - name: source_url
    dtype: string
  - name: source_revision
    dtype: string
  - name: source_config
    dtype: string
  - name: source_split
    dtype: string
  - name: source_id
    dtype: string
  - name: source_articles
    list:
    - name: title
      dtype: string
    - name: url
      dtype: string
    - name: id
      dtype: string
  - name: source_files
    sequence: string
  - name: messages
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: follow_up
    sequence: string
  - name: reference
    dtype: string
  - name: target_tokens
    dtype: int64
  - name: tokens_deepseek_v4_1
    dtype: int64
  - name: needle_depth
    dtype: float64
  - name: chars
    dtype: int64
- config_name: mmmlu
  features:
  - name: id
    dtype: string
  - name: config
    dtype: string
  - name: tier
    dtype: string
  - name: language
    dtype: string
  - name: domain
    dtype: string
  - name: task
    dtype: string
  - name: license
    dtype: string
  - name: license_url
    dtype: string
  - name: attribution
    dtype: string
  - name: source_name
    dtype: string
  - name: source_url
    dtype: string
  - name: source_revision
    dtype: string
  - name: source_config
    dtype: string
  - name: source_split
    dtype: string
  - name: source_id
    dtype: string
  - name: source_articles
    list:
    - name: title
      dtype: string
    - name: url
      dtype: string
    - name: id
      dtype: string
  - name: source_files
    sequence: string
  - name: messages
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: follow_up
    sequence: string
  - name: reference
    dtype: string
  - name: target_tokens
    dtype: int64
  - name: tokens_deepseek_v4_1
    dtype: int64
  - name: needle_depth
    dtype: float64
  - name: chars
    dtype: int64
- config_name: gsm8k_en
  features:
  - name: id
    dtype: string
  - name: config
    dtype: string
  - name: tier
    dtype: string
  - name: language
    dtype: string
  - name: domain
    dtype: string
  - name: task
    dtype: string
  - name: license
    dtype: string
  - name: license_url
    dtype: string
  - name: attribution
    dtype: string
  - name: source_name
    dtype: string
  - name: source_url
    dtype: string
  - name: source_revision
    dtype: string
  - name: source_config
    dtype: string
  - name: source_split
    dtype: string
  - name: source_id
    dtype: string
  - name: source_articles
    list:
    - name: title
      dtype: string
    - name: url
      dtype: string
    - name: id
      dtype: string
  - name: source_files
    sequence: string
  - name: messages
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: follow_up
    sequence: string
  - name: reference
    dtype: string
  - name: target_tokens
    dtype: int64
  - name: tokens_deepseek_v4_1
    dtype: int64
  - name: needle_depth
    dtype: float64
  - name: chars
    dtype: int64
- config_name: hrm8k_ko
  features:
  - name: id
    dtype: string
  - name: config
    dtype: string
  - name: tier
    dtype: string
  - name: language
    dtype: string
  - name: domain
    dtype: string
  - name: task
    dtype: string
  - name: license
    dtype: string
  - name: license_url
    dtype: string
  - name: attribution
    dtype: string
  - name: source_name
    dtype: string
  - name: source_url
    dtype: string
  - name: source_revision
    dtype: string
  - name: source_config
    dtype: string
  - name: source_split
    dtype: string
  - name: source_id
    dtype: string
  - name: source_articles
    list:
    - name: title
      dtype: string
    - name: url
      dtype: string
    - name: id
      dtype: string
  - name: source_files
    sequence: string
  - name: messages
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: follow_up
    sequence: string
  - name: reference
    dtype: string
  - name: target_tokens
    dtype: int64
  - name: tokens_deepseek_v4_1
    dtype: int64
  - name: needle_depth
    dtype: float64
  - name: chars
    dtype: int64
- config_name: mgsm
  features:
  - name: id
    dtype: string
  - name: config
    dtype: string
  - name: tier
    dtype: string
  - name: language
    dtype: string
  - name: domain
    dtype: string
  - name: task
    dtype: string
  - name: license
    dtype: string
  - name: license_url
    dtype: string
  - name: attribution
    dtype: string
  - name: source_name
    dtype: string
  - name: source_url
    dtype: string
  - name: source_revision
    dtype: string
  - name: source_config
    dtype: string
  - name: source_split
    dtype: string
  - name: source_id
    dtype: string
  - name: source_articles
    list:
    - name: title
      dtype: string
    - name: url
      dtype: string
    - name: id
      dtype: string
  - name: source_files
    sequence: string
  - name: messages
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: follow_up
    sequence: string
  - name: reference
    dtype: string
  - name: target_tokens
    dtype: int64
  - name: tokens_deepseek_v4_1
    dtype: int64
  - name: needle_depth
    dtype: float64
  - name: chars
    dtype: int64
- config_name: humaneval
  features:
  - name: id
    dtype: string
  - name: config
    dtype: string
  - name: tier
    dtype: string
  - name: language
    dtype: string
  - name: domain
    dtype: string
  - name: task
    dtype: string
  - name: license
    dtype: string
  - name: license_url
    dtype: string
  - name: attribution
    dtype: string
  - name: source_name
    dtype: string
  - name: source_url
    dtype: string
  - name: source_revision
    dtype: string
  - name: source_config
    dtype: string
  - name: source_split
    dtype: string
  - name: source_id
    dtype: string
  - name: source_articles
    list:
    - name: title
      dtype: string
    - name: url
      dtype: string
    - name: id
      dtype: string
  - name: source_files
    sequence: string
  - name: messages
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: follow_up
    sequence: string
  - name: reference
    dtype: string
  - name: target_tokens
    dtype: int64
  - name: tokens_deepseek_v4_1
    dtype: int64
  - name: needle_depth
    dtype: float64
  - name: chars
    dtype: int64
- config_name: mbpp
  features:
  - name: id
    dtype: string
  - name: config
    dtype: string
  - name: tier
    dtype: string
  - name: language
    dtype: string
  - name: domain
    dtype: string
  - name: task
    dtype: string
  - name: license
    dtype: string
  - name: license_url
    dtype: string
  - name: attribution
    dtype: string
  - name: source_name
    dtype: string
  - name: source_url
    dtype: string
  - name: source_revision
    dtype: string
  - name: source_config
    dtype: string
  - name: source_split
    dtype: string
  - name: source_id
    dtype: string
  - name: source_articles
    list:
    - name: title
      dtype: string
    - name: url
      dtype: string
    - name: id
      dtype: string
  - name: source_files
    sequence: string
  - name: messages
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: follow_up
    sequence: string
  - name: reference
    dtype: string
  - name: target_tokens
    dtype: int64
  - name: tokens_deepseek_v4_1
    dtype: int64
  - name: needle_depth
    dtype: float64
  - name: chars
    dtype: int64
- config_name: humaneval_x
  features:
  - name: id
    dtype: string
  - name: config
    dtype: string
  - name: tier
    dtype: string
  - name: language
    dtype: string
  - name: domain
    dtype: string
  - name: task
    dtype: string
  - name: license
    dtype: string
  - name: license_url
    dtype: string
  - name: attribution
    dtype: string
  - name: source_name
    dtype: string
  - name: source_url
    dtype: string
  - name: source_revision
    dtype: string
  - name: source_config
    dtype: string
  - name: source_split
    dtype: string
  - name: source_id
    dtype: string
  - name: source_articles
    list:
    - name: title
      dtype: string
    - name: url
      dtype: string
    - name: id
      dtype: string
  - name: source_files
    sequence: string
  - name: messages
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: follow_up
    sequence: string
  - name: reference
    dtype: string
  - name: target_tokens
    dtype: int64
  - name: tokens_deepseek_v4_1
    dtype: int64
  - name: needle_depth
    dtype: float64
  - name: chars
    dtype: int64
- config_name: belebele
  features:
  - name: id
    dtype: string
  - name: config
    dtype: string
  - name: tier
    dtype: string
  - name: language
    dtype: string
  - name: domain
    dtype: string
  - name: task
    dtype: string
  - name: license
    dtype: string
  - name: license_url
    dtype: string
  - name: attribution
    dtype: string
  - name: source_name
    dtype: string
  - name: source_url
    dtype: string
  - name: source_revision
    dtype: string
  - name: source_config
    dtype: string
  - name: source_split
    dtype: string
  - name: source_id
    dtype: string
  - name: source_articles
    list:
    - name: title
      dtype: string
    - name: url
      dtype: string
    - name: id
      dtype: string
  - name: source_files
    sequence: string
  - name: messages
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: follow_up
    sequence: string
  - name: reference
    dtype: string
  - name: target_tokens
    dtype: int64
  - name: tokens_deepseek_v4_1
    dtype: int64
  - name: needle_depth
    dtype: float64
  - name: chars
    dtype: int64
- config_name: mt_bench
  features:
  - name: id
    dtype: string
  - name: config
    dtype: string
  - name: tier
    dtype: string
  - name: language
    dtype: string
  - name: domain
    dtype: string
  - name: task
    dtype: string
  - name: license
    dtype: string
  - name: license_url
    dtype: string
  - name: attribution
    dtype: string
  - name: source_name
    dtype: string
  - name: source_url
    dtype: string
  - name: source_revision
    dtype: string
  - name: source_config
    dtype: string
  - name: source_split
    dtype: string
  - name: source_id
    dtype: string
  - name: source_articles
    list:
    - name: title
      dtype: string
    - name: url
      dtype: string
    - name: id
      dtype: string
  - name: source_files
    sequence: string
  - name: messages
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: follow_up
    sequence: string
  - name: reference
    dtype: string
  - name: target_tokens
    dtype: int64
  - name: tokens_deepseek_v4_1
    dtype: int64
  - name: needle_depth
    dtype: float64
  - name: chars
    dtype: int64
- config_name: long_wiki_ko
  features:
  - name: id
    dtype: string
  - name: config
    dtype: string
  - name: tier
    dtype: string
  - name: language
    dtype: string
  - name: domain
    dtype: string
  - name: task
    dtype: string
  - name: license
    dtype: string
  - name: license_url
    dtype: string
  - name: attribution
    dtype: string
  - name: source_name
    dtype: string
  - name: source_url
    dtype: string
  - name: source_revision
    dtype: string
  - name: source_config
    dtype: string
  - name: source_split
    dtype: string
  - name: source_id
    dtype: string
  - name: source_articles
    list:
    - name: title
      dtype: string
    - name: url
      dtype: string
    - name: id
      dtype: string
  - name: source_files
    sequence: string
  - name: messages
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: follow_up
    sequence: string
  - name: reference
    dtype: string
  - name: target_tokens
    dtype: int64
  - name: tokens_deepseek_v4_1
    dtype: int64
  - name: needle_depth
    dtype: float64
  - name: chars
    dtype: int64
- config_name: long_wiki_en
  features:
  - name: id
    dtype: string
  - name: config
    dtype: string
  - name: tier
    dtype: string
  - name: language
    dtype: string
  - name: domain
    dtype: string
  - name: task
    dtype: string
  - name: license
    dtype: string
  - name: license_url
    dtype: string
  - name: attribution
    dtype: string
  - name: source_name
    dtype: string
  - name: source_url
    dtype: string
  - name: source_revision
    dtype: string
  - name: source_config
    dtype: string
  - name: source_split
    dtype: string
  - name: source_id
    dtype: string
  - name: source_articles
    list:
    - name: title
      dtype: string
    - name: url
      dtype: string
    - name: id
      dtype: string
  - name: source_files
    sequence: string
  - name: messages
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: follow_up
    sequence: string
  - name: reference
    dtype: string
  - name: target_tokens
    dtype: int64
  - name: tokens_deepseek_v4_1
    dtype: int64
  - name: needle_depth
    dtype: float64
  - name: chars
    dtype: int64
- config_name: long_code
  features:
  - name: id
    dtype: string
  - name: config
    dtype: string
  - name: tier
    dtype: string
  - name: language
    dtype: string
  - name: domain
    dtype: string
  - name: task
    dtype: string
  - name: license
    dtype: string
  - name: license_url
    dtype: string
  - name: attribution
    dtype: string
  - name: source_name
    dtype: string
  - name: source_url
    dtype: string
  - name: source_revision
    dtype: string
  - name: source_config
    dtype: string
  - name: source_split
    dtype: string
  - name: source_id
    dtype: string
  - name: source_articles
    list:
    - name: title
      dtype: string
    - name: url
      dtype: string
    - name: id
      dtype: string
  - name: source_files
    sequence: string
  - name: messages
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: follow_up
    sequence: string
  - name: reference
    dtype: string
  - name: target_tokens
    dtype: int64
  - name: tokens_deepseek_v4_1
    dtype: int64
  - name: needle_depth
    dtype: float64
  - name: chars
    dtype: int64
configs:
- config_name: all
  default: true
  data_files:
  - split: test
    path: data/*.jsonl
- config_name: mmlu_en
  data_files:
  - split: test
    path: data/mmlu_en.jsonl
- config_name: mmmlu
  data_files:
  - split: test
    path: data/mmmlu.jsonl
- config_name: gsm8k_en
  data_files:
  - split: test
    path: data/gsm8k_en.jsonl
- config_name: hrm8k_ko
  data_files:
  - split: test
    path: data/hrm8k_ko.jsonl
- config_name: mgsm
  data_files:
  - split: test
    path: data/mgsm.jsonl
- config_name: humaneval
  data_files:
  - split: test
    path: data/humaneval.jsonl
- config_name: mbpp
  data_files:
  - split: test
    path: data/mbpp.jsonl
- config_name: humaneval_x
  data_files:
  - split: test
    path: data/humaneval_x.jsonl
- config_name: belebele
  data_files:
  - split: test
    path: data/belebele.jsonl
- config_name: mt_bench
  data_files:
  - split: test
    path: data/mt_bench.jsonl
- config_name: long_wiki_ko
  data_files:
  - split: test
    path: data/long_wiki_ko.jsonl
- config_name: long_wiki_en
  data_files:
  - split: test
    path: data/long_wiki_en.jsonl
- config_name: long_code
  data_files:
  - split: test
    path: data/long_code.jsonl
---

# LLM Speed Prompt Mix

A fixed set of 460 real prompts for measuring LLM inference speed: 15 languages and code, from short questions
to 64K-token documents, with the license and source of every row in its own columns.

Use it to measure prefill and decode speed, to compare two builds of the same model on the same inputs, and to check
that a faster build still gives the same answers. It is not an accuracy benchmark: most categories have only a few items.

## Why this set exists

We built it while speeding up DeepSeek-V4.1-Flash, a mixture-of-experts (MoE) model, in llama.cpp. Synthetic inputs kept
giving us numbers that did not hold on real text, and we found no public prompt set that covered the languages, domains and
lengths we needed under a license that let us share it.

- **MoE speed depends on the text, not only on its length.** `llama-bench` fills its prompts with random token ids
  (`std::rand() % n_vocab`). For a dense model that is fine, since every token does the same work. In an MoE model the
  router sends each token to a few experts, and how a batch's tokens spread over the experts sets the size of every expert
  matrix multiplication. Random ids spread almost evenly; real text does not. In DeepSeek-V4.1-Flash we measured the busiest
  expert of a layer receiving 61–80% of a batch's tokens. A kernel change that looked faster under uniform routing in our
  unit tests turned out 9–35% slower at 8–16 tokens per batch on real text, and we dropped it.
- **Language changes the token count and the routing.** With the DeepSeek-V4.1 tokenizer, Korean text averages about 1.4
  characters per token, English about 4.6 and source code about 2.9, so a Korean document has more than three times as many
  tokens as an English document with the same number of characters. Different scripts and subjects also activate different
  experts, so a speedup measured on English prose alone may not carry over.
- **Korean long-context prompts with a reusable license are hard to find.** Large Korean benchmarks such as KMMLU and
  KorQuAD 2.0 do not allow derivatives, and the long-context suites we found that include Korean embed third-party texts or
  do not say where their texts come from. So we built Korean and English long documents from Wikipedia, and long code
  documents from llama.cpp itself.
- **Length decides which code paths run.** A 100-token prompt and a 64K-token prompt go through different matrix
  multiplication kernels and spend very different shares of their time in attention, and decoding slows down as the context
  grows. Fixed length buckets from about 100 to 64K tokens cover each regime.
- **A faster build must give the same answers.** Every row keeps the reference answer of its source, and every long
  document hides one synthetic sentence with a 7-digit code and ends with a question about it. A build that breaks
  long-context attention then returns a wrong number instead of only a different speed.
- **Results should be reproducible and shareable.** Every row comes from a source whose license allows redistribution and
  modification, and carries its license, attribution and exact source revision in its own columns. The build scripts are
  included and pin every source revision, so the set can be rebuilt.

## Contents

| config | rows | standard | languages | content | source | license |
|---|---:|---:|---|---|---|---|
| `mmlu_en` | 57 | 2 | en | 1 question for each of the 57 subjects | [MMLU](https://huggingface.co/datasets/cais/mmlu) | MIT |
| `mmmlu` | 113 | 16 | ar 8, de 8, es 8, fr 8, hi 8, ja 8, ko 57, zh 8 | Korean: 1 question per subject; 7 other languages: 8 subjects | [MMMLU](https://huggingface.co/datasets/openai/MMMLU) | MIT |
| `gsm8k_en` | 20 | 2 | en | grade-school math word problems | [GSM8K](https://huggingface.co/datasets/openai/gsm8k) | MIT |
| `hrm8k_ko` | 20 | 2 | ko | Korean translations of GSM8K problems | [HRM8K (GSM8K part)](https://huggingface.co/datasets/HAERAE-HUB/HRM8K) | MIT |
| `mgsm` | 40 | 20 | bn 4, de 4, es 4, fr 4, ja 4, ru 4, sw 4, te 4, th 4, zh 4 | GSM8K problems translated into 10 languages | [MGSM](https://github.com/google-research/url-nlp/tree/main/mgsm) | CC BY 4.0 |
| `humaneval` | 15 | 2 | en | Python function completion | [HumanEval](https://huggingface.co/datasets/openai/openai_humaneval) | MIT |
| `mbpp` | 15 | 2 | en | Python programs from a description and tests | [MBPP (sanitized)](https://huggingface.co/datasets/google-research-datasets/mbpp) | CC BY 4.0 |
| `humaneval_x` | 20 | 4 | en | C++, Java, JavaScript and Go function completion | [HumanEval-X](https://huggingface.co/datasets/zai-org/humaneval-x) | Apache-2.0 |
| `belebele` | 50 | 20 | ar 5, de 5, en 5, es 5, fr 5, hi 5, ja 5, ko 5, vi 5, zh 5 | passage, question and 4 options | [Belebele](https://huggingface.co/datasets/facebook/belebele) | CC BY-SA 4.0 |
| `mt_bench` | 80 | 8 | en | open-ended chat in 8 categories, 2 turns | [MT-Bench prompts](https://huggingface.co/datasets/HuggingFaceH4/mt_bench_prompts) | Apache-2.0 |
| `long_wiki_ko` | 12 | 4 | ko | Korean articles, about 2K/8K/32K/64K tokens, with a needle | [Korean Wikipedia](https://huggingface.co/datasets/wikimedia/wikipedia) | CC BY-SA 4.0 |
| `long_wiki_en` | 12 | 4 | en | English articles, about 2K/8K/32K/64K tokens, with a needle | [English Wikipedia](https://huggingface.co/datasets/wikimedia/wikipedia) | CC BY-SA 4.0 |
| `long_code` | 6 | 3 | code | CUDA and C++ source, about 8K/32K/64K tokens, with a needle | [llama.cpp](https://github.com/ggml-org/llama.cpp) | MIT |

Languages: Arabic, Bengali, Chinese, English, French, German, Hindi, Japanese, Korean, Russian, Spanish, Swahili, Telugu, Thai, Vietnamese, plus source code (Python, C++, Java, JavaScript, Go, CUDA). Subjects include
the 57 MMLU subjects (law, medicine, sociology, economics, philosophy, computer security and more), math word problems,
reading comprehension, programming, open-ended chat and long documents.

The long-document rows, with their measured length in DeepSeek-V4.1 tokens (prompt text only, without the chat template):

| config | tokens per bucket |
|---|---|
| `long_wiki_ko` | 2K: 2,017, 1,945, 2,018 · 8K: 8,200, 7,309, 8,021 · 32K: 32,465, 32,898, 31,787 · 64K: 65,712, 65,083, 63,226 |
| `long_wiki_en` | 2K: 2,192, 2,261, 2,131 · 8K: 8,845, 9,566, 8,344 · 32K: 30,256, 33,623, 31,605 · 64K: 67,260, 69,186, 69,431 |
| `long_code` | 8K: 6,850, 8,067 · 32K: 34,500, 34,086 · 64K: 63,490, 65,597 |

Each long document has one inserted sentence (the needle) at 25/50/75% depth (code: 30/70%) and ends with a question about it;
`reference` holds the answer.

### Standard tier

`tier == "standard"` marks 89 rows that still cover every subset, language and length bucket: two prompts per language
in each short subset, one prompt per category in `mt_bench`, one per programming language in `humaneval_x`, and one
document per length bucket in the long subsets. We run the standard tier for every A/B comparison and the full set when a
change needs a closer look.

## Usage

Load everything (the `all` config) or one subset:

```python
from datasets import load_dataset

ds = load_dataset("developer0hye/llm-speed-prompt-mix", split="test")  # all 460 rows
standard = ds.filter(lambda r: r["tier"] == "standard")  # 89 rows
korean = load_dataset("developer0hye/llm-speed-prompt-mix", "long_wiki_ko", split="test")  # one subset
print(ds.to_pandas().groupby(["license", "config"]).size())
```

`messages` holds one user turn; apply the chat template of the model under test. With llama.cpp, start a server and run the
included script, which sends every prompt through the OpenAI-compatible chat endpoint (the server applies the template),
turns prompt caching off so each prompt is processed from scratch, decodes a fixed number of tokens and records the
server's timings and whether the needle answer came back:

```bash
llama-server -m model.gguf -c 81920 -np 1 --jinja
python scripts/speedrun.py http://127.0.0.1:8080 developer0hye/llm-speed-prompt-mix run_0_base.jsonl --tier standard
# ...run each build in turn (for example A B B A), naming the files run_<i>_<build>.jsonl, then:
python scripts/summarize.py . base new
```

`-c 81920` leaves room for the longest prompts with DeepSeek-V4.1; models with a longer tokenization may need more.

## Example: DeepSeek-V4.1-Flash on 8× RTX A6000

We ran every prompt once through llama.cpp's `llama-server` (master at `aa588a3`, 2026-10-30) with DeepSeek-V4.1-Flash in Q8_0 on
8× RTX A6000 (`-sm layer`, flash attention, `-b 2048 -ub 1024`, one slot, non-thinking chat template), 32 generated tokens per
prompt, using `scripts/speedrun.py`.

- All 460 prompts ran; with the chat template they are 16 to 69,435 tokens long.
- The model gave the right code for 30 of 30 needle questions.
- The whole set took 55.1 minutes and the standard tier 18.4 minutes.

Long documents (median of the rows in each bucket; Korean / English / code):

| length | prompt tokens | prefill tok/s | decode tok/s |
|---|---|---|---|
| 2K | 2,021 / 2,196 / – | 345 / 350 / – | 31.5 / 32.4 / – |
| 8K | 8,025 / 8,849 / 7,463 | 340 / 341 / 346 | 31.8 / 31.8 / 31.7 |
| 32K | 32,469 / 31,609 / 34,297 | 341 / 338 / 351 | 31.6 / 31.7 / 31.6 |
| 64K | 65,087 / 69,190 / 64,548 | 337 / 312 / 334 | 31.4 / 31.5 / 31.5 |

In this setup prefill throughput barely depends on length: 334–351 tok/s from 2K to 64K tokens, with the English 64K
documents (the longest rows, about 69K tokens) at 312 tok/s. Decode slows by about 5%, from 33 tok/s on short prompts to
31.4 tok/s at 64K context, so the time per token is set by the layer weights rather than by attention over the context.
At similar lengths, Korean, English and code ran within 4% of each other with this build.

Short prompts (median per subset):

| subset | prompt tokens | prefill tok/s | decode tok/s |
|---|---:|---:|---:|
| `belebele` | 213 | 252 | 33.0 |
| `gsm8k_en` | 70 | 161 | 33.1 |
| `hrm8k_ko` | 104 | 199 | 33.0 |
| `humaneval` | 144 | 226 | 33.3 |
| `humaneval_x` | 151 | 215 | 33.1 |
| `mbpp` | 104 | 184 | 33.2 |
| `mgsm` | 92 | 192 | 33.1 |
| `mmlu_en` | 73 | 164 | 33.1 |
| `mmmlu` | 108 | 199 | 33.1 |
| `mt_bench` | 40 | 137 | 33.1 |

Prefill speed on short prompts is low because a few hundred tokens do not fill the GPUs; it shows the fixed cost per request
more than the model's throughput.

## Fields

All subsets share one schema, so the license and source of each row can be read and filtered directly.

| column | meaning |
|---|---|
| `id`, `config` | row id and subset name |
| `tier` | `standard` (the fixed 89-row subset) or `extended` |
| `language`, `domain`, `task` | ISO 639-1 language code (`code` for source code), subject or category, task type |
| `license` | SPDX identifier of the license that applies to the row |
| `license_url` | link to the license; the full texts are in `LICENSES/` |
| `attribution` | authors or citation of the source, and of the work it translates where there is one |
| `source_name`, `source_url`, `source_revision` | source dataset, its location and the exact revision used |
| `source_config`, `source_split`, `source_id` | where the row is in the source (original index or id) |
| `source_articles` | Wikipedia articles used (title, URL, id), or for Belebele the original page of the passage |
| `source_files` | files used: llama.cpp paths for `long_code`, the data file for `mgsm` and `humaneval_x` |
| `messages` | chat messages, a single user turn |
| `follow_up` | later user turns (`mt_bench` only) |
| `reference` | the answer from the source dataset, or the needle value; empty where the source has none |
| `target_tokens`, `tokens_deepseek_v4_1` | long documents: length bucket and measured length with the DeepSeek-V4.1 tokenizer |
| `needle_depth`, `chars` | long documents: position of the needle (0–1) and length in characters |

## How it was built

Rows were picked at random with a fixed seed (0) from pinned revisions of each source, then formatted as chat prompts. The
scripts in `scripts/` rebuild the set: `build_benchset.py` (selection), `addtok.py` (token counts), `restructure.py`
(schema, licenses, tiers) and `make_card.py` (this card).

| config | source revision | what was changed |
|---|---|---|
| `mmlu_en` | `c30699e8356d` | one test question per subject, formatted as a multiple-choice prompt |
| `mmmlu` | `325a01dc3e17` | Korean: one test question per subject; other languages: 8 fixed subjects; multiple-choice prompts |
| `gsm8k_en` | `740312add88f` | 20 test problems with a step-by-step instruction; reference is the final answer |
| `hrm8k_ko` | `c360cabf8d73` | 20 problems from the GSM8K part of HRM8K (Korean translations of GSM8K) with a step-by-step instruction |
| `mgsm` | `3622039cf51f` | 4 test problems for each of 10 languages, unchanged question text; reference is the answer number |
| `humaneval` | `7dce6050a7d6` | 15 problems; the prompt wraps the original function stub |
| `mbpp` | `4bb6404fdc6c` | 15 sanitized test problems with their asserts appended to the prompt |
| `humaneval_x` | `62c78627f307` | 5 problems for each of C++, Java, JavaScript and Go; the prompt wraps the original function stub |
| `belebele` | `7899cdfa4e1e` | 5 questions for each of 10 languages, passage + question + 4 options |
| `mt_bench` | `e3a795c5e9a8` | all 80 prompts; first turn as the message, later turns in follow_up |
| `long_wiki_ko` | `b04c8d1ceb2f` | consecutive Wikipedia articles (>= 2000 chars) concatenated to about 2K/8K/32K/64K tokens, cut to length, with one synthetic sentence (the needle) inserted at 25/50/75% depth and a question about it |
| `long_wiki_en` | `b04c8d1ceb2f` | consecutive Wikipedia articles (>= 2000 chars) concatenated to about 2K/8K/32K/64K tokens, cut to length, with one synthetic sentence (the needle) inserted at 25/50/75% depth and a question about it |
| `long_code` | `8ca4060b7e30` | llama.cpp source files (CUDA backend and core) concatenated to about 8K/32K/64K tokens with one inserted comment line and a question about it |

Multiple-choice prompts list the options as A–D and end with "Answer with the letter of the correct option." Long documents
concatenate consecutive articles (Wikipedia articles of at least 2,000 characters) or source files, cut the text to length
and insert the needle on a line of its own. For `long_code`, files are read from the pinned public commit; generated files
and files that carry a third-party notice (code adapted from other projects) are left out.

## What is not included, and why

We only took sources whose license allows redistribution and modification, and checked each license against the original
release (the license file or statement of the original repository, or the Wikimedia Terms of Use), not only against Hub
metadata or re-uploads:

| source | why it is not included |
|---|---|
| KMMLU, KorQuAD 2.0 | CC BY-ND: no derivatives |
| KoMT-Bench | released under LGPL-3.0, a software license whose terms for text are unclear |
| LongBench v2 | its card says Apache-2.0, but its long documents are third-party texts (books, papers, reports and more) collected from elsewhere |
| OneRuler | covers Korean long context, but its documents come from books whose sources and licenses are not stated |
| MultiPL-E | its card says MIT, but its repository license adds a ban on use as training data; HumanEval-X covers the other programming languages instead |
| HRM8K, MATH and KSM parts | they reproduce competition and exam problems (MATH: American math competitions; KSM: Korean olympiads, the CSAT and teacher certification exams); the original MATH dataset was disabled on the Hub after a DMCA notice. Only the GSM8K part of HRM8K is used |
| `juletxara/mgsm` | a re-upload of MGSM labeled CC BY-SA 4.0; we take MGSM from Google's original release, which is CC BY 4.0 (the text is identical) |

## Licenses

Each subset keeps the license of its source, and each row states it in `license`:

| license | subsets | rows |
|---|---|---:|
| MIT | `mmlu_en`, `mmmlu`, `gsm8k_en`, `hrm8k_ko`, `humaneval`, `long_code` | 231 |
| Apache-2.0 | `humaneval_x`, `mt_bench` | 100 |
| CC-BY-SA-4.0 | `belebele`, `long_wiki_ko`, `long_wiki_en` | 74 |
| CC-BY-4.0 | `mgsm`, `mbpp` | 55 |

- The MIT copyright notices of all MIT sources are in `LICENSES/MIT.txt`; the Apache-2.0, CC BY 4.0 and CC BY-SA 4.0 texts
  are in `LICENSES/`. `LICENSE.md` maps subsets to licenses and copyright holders.
- Translated subsets name the work they translate in `attribution`: MMMLU translates MMLU, HRM8K and MGSM translate GSM8K,
  HumanEval-X translates HumanEval (all MIT; their notices are in `LICENSES/MIT.txt`).
- Wikipedia text has been licensed under CC BY-SA 4.0 since the Wikimedia Terms of Use of June 2023, and modified text must
  stay under CC BY-SA 4.0 or later. The `long_wiki_*` subsets are distributed under CC BY-SA 4.0 and each row lists the URLs
  of the articles it uses, the form of attribution the Terms of Use describe.
- If you redistribute modified versions of `belebele` or `long_wiki_*` rows, release them under CC BY-SA 4.0 as well.
- The instructions, needle sentences and questions we added are released under the license of the subset they appear in.
- MMLU and MMMLU are used as released under MIT by their authors; the MMLU questions were collected by its authors from
  public sources.

## Limitations

- Not an accuracy benchmark: a few randomly chosen items per category.
- Lengths are measured with the DeepSeek-V4.1 tokenizer; other tokenizers give different counts, so a "64K" Korean document
  can be much longer or shorter for another model.
- The needles are synthetic sentences in unrelated text and easy to find for a working model; they check that long context
  works, not long-context reasoning.
- Multiple-choice instructions are in English for every language.
- The Wikipedia text is the 2023-11-01 dump; the articles may have changed since.

## Citation

Please cite the sources of the subsets you use:

- **MMLU**: Hendrycks et al., Measuring Massive Multitask Language Understanding, ICLR 2021. <https://arxiv.org/abs/2009.03300>
- **MMMLU**: OpenAI, Multilingual Massive Multitask Language Understanding. <https://huggingface.co/datasets/openai/MMMLU>
- **GSM8K**: Cobbe et al., Training Verifiers to Solve Math Word Problems, 2021. <https://arxiv.org/abs/2110.14168>
- **HRM8K**: Ko et al., Understand, Solve and Translate: Bridging the Multilingual Mathematical Reasoning Gap, 2025. <https://arxiv.org/abs/2501.02448>
- **MGSM**: Shi et al., Language Models are Multilingual Chain-of-Thought Reasoners, ICLR 2023. <https://arxiv.org/abs/2210.03057>
- **HumanEval**: Chen et al., Evaluating Large Language Models Trained on Code, 2021. <https://arxiv.org/abs/2107.03374>
- **MBPP**: Austin et al., Program Synthesis with Large Language Models, 2021. <https://arxiv.org/abs/2108.07732>
- **HumanEval-X**: Zheng et al., CodeGeeX: A Pre-Trained Model for Code Generation with Multilingual Benchmarking on HumanEval-X, KDD 2023. <https://arxiv.org/abs/2303.17568>
- **Belebele**: Bandarkar et al., The Belebele Benchmark: a Parallel Reading Comprehension Dataset in 122 Language Variants, ACL 2024. <https://arxiv.org/abs/2308.16884>
- **FLORES-200**: NLLB Team, No Language Left Behind: Scaling Human-Centered Machine Translation, 2022. <https://arxiv.org/abs/2207.04672>
- **MT-Bench**: Zheng et al., Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena, NeurIPS 2023 Datasets and Benchmarks. <https://arxiv.org/abs/2306.05685>
- **Wikipedia**: Wikipedia contributors, Korean and English Wikipedia (2023-11-01 dump via wikimedia/wikipedia). <https://huggingface.co/datasets/wikimedia/wikipedia>
- **llama.cpp**: The ggml authors, llama.cpp. <https://github.com/ggml-org/llama.cpp>

## 한국어 요약

LLM 추론 속도를 잴 때 쓰는 고정 프롬프트 460개입니다. llama.cpp에서 MoE 모델인 DeepSeek-V4.1-Flash를 고속화하다가 만들었습니다.

- **왜 만들었나:** `llama-bench`는 무작위 토큰으로 속도를 잽니다. MoE 모델은 토큰마다 다른 전문가(expert)로 라우팅되는데,
  실제 텍스트에서는 한 레이어 토큰의 61–80%가 한 전문가에 몰립니다. 그래서 무작위 토큰에서 빨라진 커널이 실제 텍스트에서는
  9–35% 느려지기도 했습니다. 언어마다 토큰 수와 라우팅이 달라서 한국어·영어·다국어·코드를 모두 넣었습니다. 재배포할 수 있는
  한국어 장문 벤치마크가 드물어, 위키백과로 2K–64K 토큰 문서도 만들었습니다.
- **구성:** 15개 언어와 코드, MMLU 57개 분야(법·의학·사회학 등), 수학, 코드, 독해, 대화, 장문(2K/8K/32K/64K). 장문
  중간에 7자리 확인 코드 문장(needle)을 넣고 마지막에 물어보므로, 빨라진 빌드가 답을 제대로 내는지도 함께 확인할 수 있습니다.
- **라이선스:** 행마다 `license`, `license_url`, `attribution`, 원본 위치와 리비전이 컬럼으로 들어 있습니다. 재배포와 수정이
  허용된 출처(MIT, Apache-2.0, CC BY 4.0, CC BY-SA 4.0)만 썼고, Hub 카드뿐 아니라 원 저장소의 라이선스 파일까지 확인했습니다.
- **사용법:** `tier == "standard"`인 89개 행이 빠른 A/B 비교용입니다. `scripts/speedrun.py`로 llama-server에 바로 넣을 수
  있습니다.
