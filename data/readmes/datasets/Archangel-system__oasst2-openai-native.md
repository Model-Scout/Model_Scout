---
language:
- en
- es
- ru
- zh
- de
- fr
- pt
- ca
- it
- th
- uk
- ja
- eu
- pl
- vi
- hu
- ar
- da
- eo
- tr
- fi
- nl
- ko
- id
- he
- cs
language_bcp47:
- pt-BR
- uk-UA
license: apache-2.0
pretty_name: OASST2 OpenAI-Native (SFT + DPO, 26 languages)
task_categories:
- text-generation
- reinforcement-learning
size_categories:
- 10K<n<100K
tags:
- conversational
- openai
- chatml
- sft
- dpo
- preference
- multilingual
- oasst2
configs:
- config_name: sft
  data_files:
  - split: train
    path: data/final/sft/train.parquet
  - split: test
    path: data/final/sft/test.parquet
- config_name: dpo
  data_files:
  - split: train
    path: data/final/dpo/train.parquet
  - split: test
    path: data/final/dpo/test.parquet
---

# oasst2-openai-native

A deterministic, native OpenAI/TRL reconstruction of
[OpenAssistant/oasst2](https://huggingface.co/datasets/OpenAssistant/oasst2).
It turns the original flat `parent_id` message table into two directly usable
configs without LLM transformation: multilingual SFT conversations and ranked
DPO preference pairs.

## At a glance

| Config | Train | Test | Unit |
|---|---:|---:|---|
| `sft` | 12,717 | 671 | alternating conversation ending in assistant |
| `dpo` | 42,639 | 2,284 | prompt + chosen/rejected assistant pair |

The data is multilingual: SFT train contains 26 languages. English is 4,996 /
12,717 (39.29%), Spanish 3,975 (31.26%), Russian 1,136 (8.93%), Chinese 543
(4.27%), German 534 (4.20%), and French 340 (2.67%). The complete distribution
is in `reports/stats.json`.

## Why use this

**What it is for.** Two things you would otherwise have to build yourself from
the raw `parent_id` table:

- `sft` — supervised fine-tuning on human-written multilingual dialogue. Useful
  for teaching a base model to hold a conversation, or for restoring chat
  ability to a model that was heavily fine-tuned on a narrow task.
- `dpo` — preference optimisation (DPO, IPO, KTO, ORPO, reward modelling) on
  pairs that come from real human rankings, not from an LLM judge.

**What it improves over the upstream repo.** `OpenAssistant/oasst2` ships a flat
table of 135,174 messages linked by `parent_id`. Before training you must walk
the trees, pick a path per tree, decide what "best" means among ranked siblings,
filter on the label columns, and split without letting a tree straddle
train/test. That is the work done here, deterministically and with the numbers
measured: 13,388 SFT conversations and 44,923 DPO pairs, loadable with one
`load_dataset()` call and no parsing adapter.

**Where it is most useful.** Spanish is 31% of the SFT rows and Russian 9%,
which is unusually high for a human-written preference corpus — most open
alternatives are English-dominant. If you are training a non-English or
multilingual assistant, that distribution is the reason to pick this over an
English-only preference set.

**What it will not do.** It will not make a model factually correct: these are
human conversations from 2023, with human errors in them. It is dialogue
ability and preference signal, not a knowledge base.

## Format

JSONL is canonical. It retains native lists and objects:

```json
{"messages":[{"role":"user","content":"..."},{"role":"assistant","content":"..."}],"meta":{"lang":"fr","tree_id":"...","depth":2,"quality":0.81,"toxicity":0.02}}
```

`messages` roles are only `user` and `assistant` in this source-derived corpus;
they alternate strictly and each SFT row ends with `assistant`.

DPO rows use native lists too:

```json
{"prompt":[{"role":"user","content":"..."}],"chosen":[{"role":"assistant","content":"..."}],"rejected":[{"role":"assistant","content":"..."}],"meta":{"lang":"en","tree_id":"...","rank_chosen":0,"rank_rejected":2,"margin":2}}
```

Parquet is supplied for the Dataset Viewer. Its `sft.messages`, `dpo.prompt`,
`dpo.chosen`, and `dpo.rejected` columns are typed Arrow lists of `{role,
content}` structs. `meta` is a JSON string **only in Parquet**, because SFT and
DPO have heterogeneous metadata fields; it remains an object in canonical
JSONL. `load_dataset("json", ...)` and `load_dataset("parquet", ...)` both
load successfully with no parsing adapter.

## Curation and reproducibility

- Source: `OpenAssistant/oasst2`, revision
  `179dd21fc55192153d94adb0e0ce8f69e222bf75`, Apache-2.0.
- Raw content includes both upstream files; their upstream split was discarded
  and rebuilt deterministically by `message_tree_id` using seed 42.
- No tree crosses train/test (measured tree-id intersection: 0).
- SFT keeps one deepest best-rank path per tree. DPO caps each ranked sibling
  group at two deterministic best-vs-lower alternatives, avoiding the
  combinatorial overweighting of large sibling groups.
- Filters use source labels and deterministic rules: assistant quality >= 0.25,
  `review_result != False`, spam/lang-mismatch <= 0.5, and Detoxify toxicity
  <= 0.9. DPO rejected alternatives are not quality-filtered because they are
  the intended negative signal.
- Near deduplication: MinHash LSH, Jaccard >= 0.85, 128 permutations, 5-word
  shingles; character tokens are used for predominantly non-segmented scripts.
- Decontamination: train rows sharing any 13-gram with test are removed only
  from train. It removed 98 SFT and 460 DPO train rows; final 13-gram overlap is
  exactly zero.
- Root-prompt leak removal: the tree split guarantees no message tree straddles
  train and test, but two *different* trees can share a prompt shorter than 13
  words verbatim (1.45% duplicate prompts in the source), which yields no
  13-gram and slips past the pass above. Rows whose first user message also
  opens a test conversation are removed from train only: 16 SFT and 82 DPO.
  Measured leakage after this pass is 0/671 SFT and 0/2284 DPO.
- Build command: `python src/build.py`.
  Two complete builds produced byte-identical final SHA-256 values.

See `reports/validation.md` for decisions, measured rejection motives,
acceptance output, and known environment limitation; see `reports/stats.json`
for the full provenance, distributions, parameters, and hashes.

## Measured characteristics

SFT train conversations have a median of 2 turns (p95 4; maximum 6). Assistant
content length is median 770 characters and p95 2,473 characters. DPO train
chosen responses have median 738 characters (p95 2,443); rejected responses
have median 425 (p95 2,198).

From 13,851 SFT candidate paths, 13,388 are published (3.343% removed). From
46,248 DPO candidate pairs, 44,923 are published (2.865% removed). Rejection
counts by reason are measured and listed in the validation report.

## Limitations and intended use

- This is a reconstruction of human-authored OASST2 conversation trees, not a
  factual-correctness guarantee. Source labels are imperfect and not all rows
  have equivalent reviewer coverage.
- The source contains potentially sensitive, offensive, sexual, biased, or
  unsafe material. Basic label/toxicity filtering reduces but does not eliminate
  it. Review the source's risk documentation before deployment.
- Short answers are intentionally retained when correct (e.g. arithmetic
  answers); there is no arbitrary minimum-length filter.
- The DPO `rejected` response can be low quality by design; it must not be used
  as standalone SFT target text.
- The included `test` split is a reproducible held-out sample of the same
  source, not an external benchmark.

## Attribution and license

This derivative preserves attribution to **OpenAssistant/oasst2**,
revision `179dd21fc55192153d94adb0e0ce8f69e222bf75`, licensed under
[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0). The original project
and its contributors are credited for the human-authored source data. This
repackaging is released under Apache-2.0.

Attribution: source data collected by the OpenAssistant project and its
volunteer contributors. Normalisation and deterministic pipeline by
archangel-system.

## File integrity (SHA-256)

| File | SHA-256 |
|---|---|
| `data/final/sft/train.jsonl` | `86a79188344a924ca67e271dce1f2064605fc8382a225d53d4e431380876c411` |
| `data/final/sft/test.jsonl` | `cadc2a8cea7e2b15852bc0c51cb01f9b37ee8fd01a8cb2dcca20c23cb731c2be` |
| `data/final/sft/train.parquet` | `014a4eafeb72996d1d6b20c01daa2fdeda2f472b82b61558f7de8822ee8acdee` |
| `data/final/sft/test.parquet` | `34ec632fdb6f5dfc87c74464a30ebaf19bf9489c6d6d3dfa83cb5e76584b58b8` |
| `data/final/dpo/train.jsonl` | `39e678da3edce1350017bb28476f8a9a69047d4f9ee5a6a4b66717b70b09bbba` |
| `data/final/dpo/test.jsonl` | `fa015a8be6b332676d204166f79db67d6c979a44c86d0fa62da6867d59b08c98` |
| `data/final/dpo/train.parquet` | `bdacc8109f490d82ca440a78dc190643425bec0ac79295be237a2b207cb73bc5` |
| `data/final/dpo/test.parquet` | `dff358e34af23eb35e893f065c1ce586a4eb3ec573a6f112ffe2c2f74358de7b` |
