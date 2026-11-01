---
license: other
license_name: mixed
pretty_name: DecisionBank
language:
- en
- zh
- pt
- ja
- id
- ar
- ko
- fr
- el
- es
- pl
- uk
- cs
- hi
- tr
- sv
- it
- de
- da
- nl
- 'no'
- fi
task_categories:
- text-classification
- multiple-choice
size_categories:
- 100K<n<1M
tags:
- decision-models
- system-one
- calibration
configs:
- config_name: DecisionBank-625k
  default: true
  data_files:
  - split: train
    path: data/DecisionBank-625k/train-*.jsonl
- config_name: DecisionBank-260k
  data_files:
  - split: train
    path: data/DecisionBank-260k/train-*.jsonl
dataset_info:
- config_name: DecisionBank-625k
  features:
    - name: id
      dtype: string
    - name: group_id
      dtype: string
    - name: family
      dtype: string
    - name: part
      dtype: string
    - name: source_dataset
      dtype: string
    - name: source_license
      dtype: string
    - name: target_origin
      dtype: string
    - name: state
      dtype: string
    - name: state_is_json
      dtype: bool
    - name: question
      dtype: string
    - name: options
      list:
      - name: id
        dtype: string
      - name: description
        dtype: string
    - name: qtype
      dtype: string
    - name: label
      dtype: int64
    - name: target_distribution
      sequence: float64
    - name: tier
      dtype: string
    - name: language
      dtype: string
    - name: use_case
      dtype: string
    - name: source_ref
      dtype: string
    - name: in_jeff_1_1
      dtype: bool
  splits:
  - name: train
    num_examples: 624517
- config_name: DecisionBank-260k
  features:
    - name: id
      dtype: string
    - name: group_id
      dtype: string
    - name: family
      dtype: string
    - name: part
      dtype: string
    - name: source_dataset
      dtype: string
    - name: source_license
      dtype: string
    - name: target_origin
      dtype: string
    - name: state
      dtype: string
    - name: state_is_json
      dtype: bool
    - name: question
      dtype: string
    - name: options
      list:
      - name: id
        dtype: string
      - name: description
        dtype: string
    - name: qtype
      dtype: string
    - name: label
      dtype: int64
    - name: target_distribution
      sequence: float64
    - name: tier
      dtype: string
    - name: language
      dtype: string
    - name: use_case
      dtype: string
    - name: source_ref
      dtype: string
    - name: in_jeff_1_1
      dtype: bool
  splits:
  - name: train
    num_examples: 261561
---

# DecisionBank

Training dataset for decision models. Each row has a state (text or JSON), a question, its options, and a
target, i.e. a probability for each option. The data comes in two configs with the same rows and fields:

| Config | Rows | Tokens | What it is |
|---|---:|---:|---|
| `DecisionBank-625k` (default) | 624,517 | 279M | the complete dataset |
| `DecisionBank-260k` | 261,561 | 108M | a subset of `DecisionBank-625k`, used for training [Jeff-1.1 models](https://huggingface.co/collections/jgeuter/jeff-11-6ada6708f3ed49beaf0f97ae) |

Tokens are the prompt tokens the models see (chat template, options labeled A, B, C, ...), counted with the Gemma 4
tokenizer; the Qwen3.5 / Qwen3.6 tokenizer gives 277M and 107M.

## Usage

```python
from datasets import load_dataset
import json

data = load_dataset("jgeuter/DecisionBank", "DecisionBank-625k", split="train")   # all 624,517 rows
mix = load_dataset("jgeuter/DecisionBank", "DecisionBank-260k", split="train")    # the Jeff 1.1 training file
row = data[0]
state = json.loads(row["state"]) if row["state_is_json"] else row["state"]
```

## What is in it

| Part (`part`) | Rows in `DecisionBank-625k` | Rows in `DecisionBank-260k` | Questions written by | Target (`target_origin`) |
|---|---:|---:|---|---|
| `decider`: decider's public training mixture, 79 task families | 300,042 | 161,638 | public datasets (66 families), code (12 families), decider's teacher (3 families) | 50% decider's label + 50% Qwen3.8-27B |
| `human_soft`: Civil Comments, Measuring Hate Speech, STS-B, ChaosNLI | 67,646 | 9,168 | public datasets | 50% human annotation distribution + 50% Qwen3.8-27B |
| `jeff10_llm`: synthetic business documents and decider's custom questions (from Jeff 1.0) | 50,137 | 4,188 | Qwen3.6-27B (documents); decider | 50% Jeff 1.0 teachers + 50% Qwen3.8-27B |
| `j11_written`: new decision questions | 138,782 | 58,125 | Qwen3.8-27B, thinking off | Qwen3.8-27B with thinking (mean of 2 samples) |
| `j11_generator`: new programmatic questions | 67,910 | 28,442 | code | computed by code |
| **total** | **624,517** | **261,561** | | |

- **decider's mixture:** rebuilt with the code of [decider](https://github.com/Mapika/decider) (commit 5f91c01), from
  public datasets such as CLINC, banking77, MNLI, BoolQ, ARC and MMLU's auxiliary training split. Its families are
  listed under [Licences](#licences). Targets rebuilt with labels from Qwen3.8-27B.
- **Qwen3.8-27B labels:** `Qwen/Qwen3.8-27B` (revision 1d4bf0f2), with thinking (up to 6,144 thinking tokens), two
  samples with the choice options shuffled. Its answer distribution is the mean of the two samples' option probabilities.
- **Jeff 1.0 teachers:** Qwen3.6-27B and Qwen3.5-122B-A10B, two thinking samples each, averaged.
- **New written questions:** each one is written from a short specification (task family, use case, question type,
  difficulty, language). A question is kept only when Qwen3.8-27B's own answer, with thinking, matches the answer the
  writer intended (this holds for every written row in both configs). They cover 22 languages (`DecisionBank-625k`: 112,727 in
  English and 1,091-1,343 in each other language; `DecisionBank-260k`: 47,361 in English and about 500 in each other language)
  and many business use cases.
- **New programmatic questions:** made by the generators of [OpenDecisions](https://huggingface.co/datasets/jgeuter/OpenDecisions)
  with a new random seed. Their labels are computed;
  22,251 of them in `DecisionBank-625k` (9,309 in `DecisionBank-260k`) also have exact answer probabilities.

**Question types:** Questions span multiple-choice yes/no (`noul`), and score questions.

| Question type | `DecisionBank-625k` | `DecisionBank-260k` |
|---|---:|---:|
| choice | 318,777 | 155,652 |
| yes/no (`noul`) | 171,257 | 66,830 |
| score | 134,483 | 39,079 |

### How DecisionBank-260k was made from DecisionBank-625k

The first three parts (`decider`, `human_soft`, `jeff10_llm`) form 87 task families of very different sizes in `DecisionBank-625k`
(from a few hundred rows up to 30,641; median 4,090). For `DecisionBank-260k`, every family was cut to at most 2,094 random rows
(the 11 smaller families stay whole), which leaves 174,994 of their 417,825 rows (41.9%). The written and the
programmatic questions were then sampled at the same rate (41.9%), so the three sources keep the shares they have in
`DecisionBank-625k` (66.9%, 22.2% and 10.9% of the rows). Random seed 23. So `DecisionBank-260k` balances the task families; it does not
change the share of the new data. We observed a small improvement on validation data from switching from `DecisionBank-625k` to `DecisionBank-260k`, but the difference was not significant.

## Fields

| Field | Meaning |
|---|---|
| `id`, `group_id` | row id; rows from the same source item or pair share a group |
| `family` | task family |
| `part`, `source_dataset` | which part of the data, and where the row comes from |
| `source_license` | the licence the source states (see [Licences](#licences)) |
| `target_origin` | where the target comes from |
| `state` | the state, always a string |
| `state_is_json` | true when `state` is a JSON object written as a string (46,133 rows in `DecisionBank-625k`, 15,117 in `DecisionBank-260k`); parse it to get the object the models saw |
| `question` | the question |
| `options` | list of `{id, description}`, in the stored order |
| `qtype` | `choice`, `noul` (yes/no) or `score` (ordered levels) |
| `label` | index of the target's most likely option |
| `target_distribution` | the training target, one probability per option; null for the programmatic rows without exact probabilities (45,659 in `DecisionBank-625k`, 19,133 in `DecisionBank-260k`), which were trained on `label` |
| `tier`, `language`, `use_case` | difficulty tier, language and use case of the new questions (null otherwise) |
| `source_ref` | a JSON string that points back to the source item (for example the task and example index in decider, or the comment id) |
| `in_jeff_1_1` | true for the rows of the `DecisionBank-260k` config (always true in that config) |


## Jeff-1.1 models

The four Jeff 1.1 models
([Jeff-1.1-Large](https://huggingface.co/jgeuter/Jeff-1.1-Large),
[Jeff-1.1-Qwen-27B](https://huggingface.co/jgeuter/Jeff-1.1-Qwen-27B),
[Jeff-1.1-Medium](https://huggingface.co/jgeuter/Jeff-1.1-Medium),
[Jeff-1.1-Qwen-4B](https://huggingface.co/jgeuter/Jeff-1.1-Qwen-4B)) trained on `DecisionBank-260k`:

| Model | Training steps | Training tokens (per seed) |
|---|---:|---:|
| Jeff-1.1-Large (Gemma 4 31B) | 1,500 | 89.2M |
| Jeff-1.1-Qwen-27B (Qwen3.6-27B) | 1,500 | 89.2M |
| Jeff-1.1-Medium (Gemma 4 12B) | 1,500 | 89.2M |
| Jeff-1.1-Qwen-4B (Qwen3.5-4B) | 800 | 47.5M |

Each model soups three training runs in weight space (=averaging weights). A step holds up to 65,536 tokens including padding
(about 59,500 real tokens, or about 145 questions). So 1,500 steps see about 83% of `DecisionBank-260k` once, and 800
steps about 44%. For more details, please see our paper
[Releasing the Inner Jev: A Simple Recipe for Open Decision Models](https://arxiv.org/abs/2610.17205).


**Disclosure:**

- **No OpenDecisions items and no JevBench items** are in this dataset.
- **The programmatic questions are template siblings of OpenDecisions.** They come from the same generator code as the
  code-labeled families of OpenDecisions (counting traps, composite rules, negation pairs, calibration items), with a
  new seed. None is identical to an OpenDecisions item.
- **No output of Jev or other TypeSafe products** is in this data.
- Some public sources contain outputs of other language models (for example UltraFeedback and hh-rlhf in decider's
  mixture), and the new questions and part of the targets come from Qwen models.

## Licences

The rows keep the terms of their sources. We release our own parts (`j11_written`, `j11_generator`, and the documents
and labels we made for `jeff10_llm`) under **CC BY-SA 4.0**. `source_license` holds the licence that each source states
on its dataset card; "unknown" means we found no licence statement. This is not legal advice: check the terms of a
source before you use its rows.

Several sources restrict use. **Do not use this data commercially.** Terms overview:

| Terms | Sources (rows) |
|---|---|
| non-commercial (CC BY-NC 4.0) | ToxicChat, customer-support-tickets, ChaosNLI |
| research use only | RACE, MS MARCO, Microsoft WikiQA, dair-ai/emotion, Mind2Web, SuperGLUE (COPA, WiC, MultiRC) |
| copyleft | FEVER (GPL-3.0 and CC BY-SA 3.0); share-alike sources such as SNLI, BoolQ, ARC and DBpedia |
| no licence stated | AG News, Yahoo Answers topics, 20 Newsgroups, SST-2, SST-5, tweet_eval, SMS spam, Enron spam, insincere questions, OpenBookQA, HellaSwag, PIQA, AgentTraj-L, SHP, MASSIVE, and other SetFit mirrors |
| other terms | IMDB, Yelp, Amazon reviews, GLUE (QQP: Quora terms) |

To keep only rows whose source states a permissive licence, filter on `source_license`.

## Citation

If you find this dataset helpful, please consider citing our paper:

```bibtex
@misc{geuter2026releasinginnerjevsimple,
      title={Releasing the Inner Jev: A Simple Recipe for Open Decision Models},
      author={Jonathan Geuter and Andrew Cheng and David Alvarez-Melis},
      year={2026},
      eprint={2610.17205},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2610.17205},
}
```
