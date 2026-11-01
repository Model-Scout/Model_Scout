---
license: other
license_name: mixed
pretty_name: Curation decision mix
task_categories: [text-classification, zero-shot-classification]
language: [en, zh, pt, ja, id, ar, ko, fr, el, es, pl, uk, cs, hi, tr, sv, it, de, da, nl, "no", fi]
tags: [data-curation, decision-model, decision-models, system-one, gliclass, provenance, hf-jobs]
size_categories: [100K<n<1M]
configs:
  - {config_name: all, data_files: "data/*/train.parquet", default: true}
  - {config_name: base, data_files: data/base/train.parquet}
  - {config_name: decisionbank, data_files: data/decisionbank/train.parquet}
  - {config_name: prompt, data_files: data/prompt/train.parquet}
  - {config_name: web, data_files: data/web/train.parquet}
  - {config_name: nls, data_files: data/nls/train.parquet}
  - {config_name: tool, data_files: data/tool/train.parquet}
  - {config_name: harvard, data_files: data/harvard/train.parquet}
  - {config_name: arxiv, data_files: data/arxiv/train.parquet}
  - {config_name: procpile, data_files: data/procpile/train.parquet}
---

# Curation decision mix

The training data of [davanstrien/ultrabert-380m-curation](https://huggingface.co/davanstrien/ultrabert-380m-curation), a small decision model that answers curation questions about web pages, prompts,
maths problems and library records ("what topic is this page?", "how educational is it?", "how hard is this
problem?"). Each row is a text, a question, a set of options and a probability for each option. Every row records
where it came from, who made its label and under which licence.

This card is also the data recipe: it says which sources were used, why, and which choices moved the scores (see
[How the mix was designed](#how-the-mix-was-designed)). The scripts are in
[github.com/davanstrien/curation-decision-recipe](https://github.com/davanstrien/curation-decision-recipe). If you
train decision models, please share how you made your data too so others can learn from your work and open models can keep improving! 

|                |                                                                                                                                                                                                                                                                                |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Rows           | 516,964 released, from a 535,730-row training mix; 18,766 base rows without a verified open licence are left out (see Licences)                                                                                                                                                |
| Sources        | 9: public task collections, DecisionBank, curation labels from web/prompt datasets, library catalogues, program-computed tasks                                                                                                                                                 |
| Row shapes     | decision rows `{state, question, target}` and GLiClass rows `{text, all_labels, true_labels, prompt}`                                                                                                                                                                          |
| Labels made by | dataset gold, library cataloguers, programs, and LLMs (named per source and per row)                                                                                                                                                                                           |
| Licence        | mixed, per row; web page text is **not** included (labels plus a pointer to the source row; rebuild snippet below)                                                                                                                                                             |
| Trains         | [davanstrien/ultrabert-380m-curation](https://huggingface.co/davanstrien/ultrabert-380m-curation) (UltraBERT-380M + GLiClass head; 12,000 steps over this mix)                                                                                                                 |
| Build          | mix builder on Hugging Face Jobs (CPU), then [`scripts/release_build.py`](scripts/release_build.py) for the release (a record of how this repo was made: it reads the mix from a private bucket); test sets fixed before the mix was built, and every row checked against them |

```python
import json
from datasets import load_dataset
ds = load_dataset("davanstrien/curation-decision-mix", "all", split="train")   # or one config per source, e.g. "decisionbank"
ok = ds.filter(lambda r: r["licence_class"] == "permissive")                 # filter by licence before reuse
decisions = ok.filter(lambda r: r["row_type"] == "decision")                 # decision rows; the rest are GLiClass rows
q = json.loads(decisions[0]["question"])                                     # nested fields are JSON strings
```

---

## Layout

One config per source, plus `all`. `web` rows have an empty `state` by design (see Web text). Splitting by source keeps licence terms together, so a user can take only the parts
whose terms suit them.

| Config         |                               Rows (training mix) | Shape    |
| -------------- | ------------------------------------------------: | -------- |
| `base`         |     173,859 (192,625 in training; licence filter) | GLiClass |
| `decisionbank` |                                           165,277 | decision |
| `prompt`       |                                            52,491 | decision |
| `web`          | 41,890 (labels only; `state` empty until rebuilt) | decision |
| `nls`          |                                            23,846 | GLiClass |
| `tool`         |                                            21,089 | GLiClass |
| `harvard`      |                                            13,918 | decision |
| `arxiv`        |                                            13,597 | GLiClass |
| `procpile`     |                                            10,997 | GLiClass |

`manifest/training_mix_manifest.parquet` lists all 535,730 rows of the training mix (including the 18,766 rows not
released here): row id, source, licence class, labeller and a SHA-256 hash of each row's text.

Columns (union of both shapes; unused fields are null):

| Column                                        | Meaning                                                                                                                                                                                   |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                          | stable row id; prefix names the source (`db/…`, `procpile-…`, `knowledgator/gliclass-v2.0:…`)                                                                                             |
| `config`, `src`                               | source group and the finer origin (e.g. `db_bitext_support`, a tasksource task)                                                                                                           |
| `row_type`                                    | `decision` or `gliclass`                                                                                                                                                                  |
| `teacher`                                     | who made the label (e.g. `Llama-3.1-405B`, `cataloguer`, `program`, `50% source label + 50% Qwen3.8-27B`)                                                                                 |
| `licence_class`, `licence`                    | `permissive` / `sa` (share-alike, e.g. CC BY-SA, CDLA-Sharing) / `other_open` (MPL-2.0, AFL-3.0) / `publisher` (text not redistributed), and the licence id                               |
| `state`                                       | the input (decision rows): a string, or a record as a JSON string                                                                                                                         |
| `state_is_record`                             | decision rows: true when `state` was a record (dict or list) in training; false when it was text (some text states look like JSON)                                                        |
| `question`                                    | JSON string: `{type, instructions, criteria}`, `type` is `noul` or `choice`; `noul` = yes/no; `choice` options are `{key: description}`; graded scales use `level_<k>` keys, lowest first |
| `target`                                      | JSON string: probability per option (soft targets allowed; sums to 1 for single-answer rows)                                                                                              |
| `text`, `all_labels`, `true_labels`, `prompt` | GLiClass rows: text, label list, `{label: score}` or a list (JSON string), optional prompt                                                                                                |
| `multi_label`                                 | true when several options can be correct (per-option yes/no loss in training)                                                                                                             |
| `source_dataset`, `source_row`                | `web` rows only: source dataset and row index in its `train` split                                                                                                                        |

Example decision row (DecisionBank, shortened):

```json
{"id": "db/decider/bitext_support/286978::q1", "src": "db_bitext_support", "row_type": "decision",
 "teacher": "50% decider label + 50% Qwen3.8-27B", "licence_class": "sa", "licence": "cdla-sharing-1.0",
 "state": "how do i remove several articles from order {{Order Number}}",
 "question": {"type": "choice", "instructions": "What is the specific intent of this request?",
              "criteria": {"change order": "change order", "get refund": "get refund", "...": "..."}},
 "target": {"change order": 1.0, "get refund": 0.0, "...": 0.0}}
```

Example GLiClass row (procedural pile, shortened):

```json
{"id": "procpile-game_forced_win-89307", "row_type": "gliclass", "teacher": "program",
 "text": "In this graph game, decide whether player can force a win. … The answer is Yes or No.",
 "all_labels": ["No", "Yes"], "true_labels": {"No": 0.0, "Yes": 1.0}, "prompt": ""}
```

**Web text.** The `web` config carries labels only. `source_dataset` and `source_row` point at the row in the
source dataset's `train` split; the training text was the first 3,000 characters. To rebuild it for your own use
(do not redistribute it):

```python
from datasets import load_dataset

src = {}
def rebuild(r):
    if r["source_dataset"] not in src:
        src[r["source_dataset"]] = load_dataset(r["source_dataset"], split="train")
    return {"state": src[r["source_dataset"]][r["source_row"]]["text"][:3000]}
web = load_dataset("davanstrien/curation-decision-mix", "web", split="train").map(rebuild)
```

Row indices assume the source datasets are unchanged since October 2026. The snippet loads each source dataset in full; it has not been tested end to end.

**Train on it.** [`data/release_to_jsonl.py`](https://github.com/davanstrien/curation-decision-recipe/blob/main/data/release_to_jsonl.py)
in the recipe repo converts this dataset to the trainer's JSONL input (`uv run data/release_to_jsonl.py --out
mix.jsonl`; filter with `--configs` and `--licence-class`). We checked it against the private training mix: all
475,074 released rows with text are identical on every field the trainer reads. The recipe README has a tested
command that converts and trains on one GPU Job.

---

## Sources

| Source                                                                                                                                                                                                                                                                              |                         Rows | What the rows ask                                                                                                                                                                                                                                                                                                                                                                                                                         | Labels made by                                                                                                                                                 | Licence                                                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| base ([tasksource](https://huggingface.co/datasets/tasksource/tasksource-jev-typed-decisions) + Knowledgator GLiClass data: [v2.0](https://huggingface.co/datasets/knowledgator/gliclass-v2.0), [v3-logic](https://huggingface.co/datasets/knowledgator/gliclass-v3-logic-dataset)) | 173,859 (192,625 trained on) | many public classification tasks                                                                                                                                                                                                                                                                                                                                                                                                          | dataset gold; knowledgator gliclass-v2.0 / v3-logic (LLM-generated)                                                                                            | per source repo, in `licence`; only rows with a verified permissive, share-alike or other open licence are released (see Licences)            |
| [DecisionBank-260k](https://huggingface.co/datasets/jgeuter/DecisionBank)                                                                                                                                                                                                           |                      165,277 | public tasks, written and programmatic decision questions                                                                                                                                                                                                                                                                                                                                                                                 | 50 % source label + 50 % Qwen3.8-27B; Qwen3.8-27B with thinking; 50 % Jeff 1.0 teachers (Qwen3.6-27B, Qwen3.5-122B-A10B) + 50 % Qwen3.8-27B (4,188 rows); code | per row: CC BY / CC BY-SA, Apache, MIT, CC0 (public domain), CDLA-Sharing-1.0; non-commercial, research-only, unknown and other terms dropped |
| prompt slice                                                                                                                                                                                                                                                                        |                       52,491 | [NuminaMath-1.5](https://huggingface.co/datasets/AI-MO/NuminaMath-1.5) question type / problem type / validity; [DeepMath-103K](https://huggingface.co/datasets/zwhe99/DeepMath-103K) difficulty / topic; [WebInstruct-verified](https://huggingface.co/datasets/TIGER-Lab/WebInstruct-verified) answer type / category / difficulty; [LMArena](https://huggingface.co/datasets/lmarena-ai/arena-human-preference-140k) criteria and tags | dataset columns (NuminaMath, WebInstruct: labeller not documented); GPT-4o (DeepMath); LMArena classifiers                                                     | Apache-2.0; MIT; Apache-2.0; CC-BY-4.0                                                                                                        |
| web slice (**ids and labels only**)                                                                                                                                                                                                                                                 |                       41,890 | WebOrganizer [topic](https://huggingface.co/datasets/WebOrganizer/TopicAnnotations-Llama-3.1-405B-FP8) and [format](https://huggingface.co/datasets/WebOrganizer/FormatAnnotations-Llama-3.1-405B-FP8); [FineWeb-Edu](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu-llama3-annotations) educational value                                                                                                                     | Llama-3.1-405B (WebOrganizer; the annotation datasets state no licence); Llama-3-70B (FineWeb-Edu)                                                             | labels: none stated; ODC-By. Page text: publisher copyright, not included (rebuild snippet above)                                             |
| [National Library of Scotland](https://data.nls.uk/) catalogue                                                                                                                                                                                                                      |                       23,846 | subject areas of library records                                                                                                                                                                                                                                                                                                                                                                                                          | National Library of Scotland cataloguers                                                                                                                       | CC0                                                                                                                                           |
| tool lane (code decisions)                                                                                                                                                                                                                                                          |                       21,089 | linter findings (classification and yes/no) and complexity comparisons on functions from Python packages                                                                                                                                                                                                                                                                                                                                  | program-computed (linter and complexity tools)                                                                                                                 | permissive package licences (MIT / BSD / Apache-2.0 / PSF); the package is not recorded per row                                               |
| [Harvard Library](https://library.harvard.edu/open-metadata) modern catalogue                                                                                                                                                                                                       |                       13,918 | Library of Congress subject class, literary form, government publication                                                                                                                                                                                                                                                                                                                                                                  | Harvard Library cataloguers (from their catalogue records)                                                                                                     | CC0                                                                                                                                           |
| arXiv                                                                                                                                                                                                                                                                               |                       13,597 | arXiv subject category                                                                                                                                                                                                                                                                                                                                                                                                                    | author-chosen categories                                                                                                                                       | arXiv metadata (CC0)                                                                                                                          |
| [procedural pile](https://huggingface.co/datasets/reasoning-core/procedural-pile)                                                                                                                                                                                                   |                       10,997 | program-checkable reasoning                                                                                                                                                                                                                                                                                                                                                                                                               | program-computed                                                                                                                                               | CC BY 4.0 (attribute)                                                                                                                         |

---

## How the mix was designed

The mix results from a series of screened experiments (2026-10-23 → 10-27). Each choice below states what it rests
on: earlier decision-model reports, published curation work, or our own measurements. "Curation score" is the
benchmark used for selection: the mean of 16 curation test units (see the model card for the grouping and all 16 scores).

**1. Start from a broad public base, cleaned by task identity.** The base follows the GLiClass v4 recipe
(knowledgator): tasksource classification tasks plus knowledgator's GLiClass training sets, so the model keeps general
zero-shot skill. Contamination was screened by task, not only by canary strings: tasksource re-hosts BIG-bench tasks
without the canary, and whole sources (math_qa, cosmos_qa, vitaminc, qasc, social_i_qa, …) were removed (2.7 % of
the pool).

**2. Prefer clean, audited, family-covering data to volume.** Earlier decision-model reports found bulk open decision
data neutral or harmful, gains staying inside the task families covered, and source audits worth more than extra rows.
Our own runs agreed: adding bulk without audits did not help; diverse, audited sources did (+4 points over the base
alone on a sample of a public decision benchmark suite). So every source was audited before training:
- **Text-blind baselines** on every source (majority label, longest option, options-only ranker), in the spirit of
  hypothesis-only baselines for NLI ([Poliak et al., 2018](https://arxiv.org/abs/1805.01042);
  [Gururangan et al., 2018](https://arxiv.org/abs/1803.02324)). A generated-schema
  source that looked like +4.5 turned out to be mostly a "longest option is right" shortcut (real gain ≈ +2.3), so
  sources with option-only leaks were fixed or dropped.
- **Distractors weighted by gold frequency.** With uniformly sampled wrong options, a real-label source (arXiv)
  leaked a label prior (+18 points over chance from the options alone). The Harvard rows needed the same fix
  (options-only 52 % before it).
- **Same writing style for every class.** A source where one class was human-written and the other LLM-written taught
  "LLM style means unsupported" and was dropped.

**3. Train on the labels real curation pipelines use.** The curation slices reuse public labels from curation work:
WebOrganizer topic and format ([Wettig et al., 2025](https://arxiv.org/abs/2502.10341), *Organize the Web*), FineWeb-Edu educational value
([Penedo et al., 2024](https://arxiv.org/abs/2406.17557)), and prompt tags from NuminaMath-1.5, DeepMath-103K, WebInstruct-verified and LMArena. Fixed-head
classifiers trained on the same labels were used as a ceiling check before any claim (they still win their own
labels: 0.87 / 0.83 vs 0.84 / 0.74 for WebOrganizer topic/format).

**4. Keep the third-party labels; document them.** We tested replacing every LLM-made label with labels from a panel
of open models (2 seeds). The panel matched the 405B topic labels well (0.815) but lost 5.1 curation-score points,
almost all on graded axes (maths difficulty, educational value). Rubric-anchored prompts helped the panel (+0.07
rank correlation against Omni-MATH human ratings) but did not close the gap. So the release keeps the original labels and
states each labeller, model and licence (Sources table and the `teacher` column).

**5. Add human-made labels where they exist.** Library catalogue records (National Library of Scotland, Harvard) carry
labels made by cataloguers. Harvard rows lifted an unseen library scheme by +4.6 accuracy (3 seeds, all 9 seed pairs
positive) without hurting the curation score; the cost to watch is the Aegis safety test set (−4.7).

**6. Add DecisionBank, licence-filtered.** DecisionBank rows added +0.70 curation-score points at equal steps and +0.77 at equal passes
over the other rows (3 seeds each, all 9 pairs positive), mostly on evals whose gold is independent of any training
labeller. We kept only rows with allowed licences; we dropped the HelpSteer families because they are held-out test sets.

**7. Program-computed lanes for reasoning and tools.** Procedural reasoning tasks, tool selection and arXiv
categories have labels that are computed or author-chosen, so no LLM labeller is involved (the task design still shapes them). They help general decision
tasks more than the curation score.

### How train and eval were split

- **Evals first.** The eval sets (v3: 40 sets, 72,533 rows) were frozen before any mix was built, and every mix was
  decontaminated against all of them (exact, normalised, prefix, number-stripped skeleton, containment, 13-gram).
- **Hold out whole sources and schemes, not random rows.** Dev sets drawn from the training pool overestimate held-out
  scores (earlier reports saw dev scores rise while scores on private test sets fell, and data shaped like a benchmark
  inflate that benchmark's public score). So held-out test sets
  are whole sources (HelpSteer2/3, Polaris, Aegis, WildGuard) and label schemes not seen in training (the item types of
  US company filings, SEC form 8-K; a library item-form scheme).
- **Separate same-labeller from independent gold.** Where an eval's gold comes from the same LLM that labelled
  training rows (WebOrganizer, FineWeb-Edu, DeepMath), it partly measures agreement with that labeller. The fair
  comparison uses independent gold (Omni-MATH human ratings, Essential-Web), reported apart in the model card.
- **Seeds and review.** Each data choice was screened with ≥ 2 training seeds and claimed with ≥ 3; every claimed result was checked by
  two independent automated reviews (separate AI models) before adoption.

## Decontamination

We checked every row against every text in the test sets (version v3). Removed: 1,562 base rows (478 overlaps +
1,084 rows from HelpSteer3 sources, a held-out test source), 1,035 DecisionBank rows (mostly HelpSteer3 / Aegis
prompts), 1 Harvard row; the HelpSteer families of DecisionBank were dropped before the build. A 12-gram
near-duplicate check found 15 of 1,038 HelpSteer2 and 15 of 1,832 HelpSteer3 eval items sharing text with a
DecisionBank row. The catalogue test sets were kept out by id and title when the Harvard and National Library of Scotland sources were built.

## Licences

Licence classes in this release: permissive 375,637 rows, share-alike 98,941, other open 496, publisher terms 41,890
(`web` labels only; page text trained on, never redistributed). DecisionBank's own parts are CC BY-SA 4.0;
share-alike rows keep their licence in this dataset. The model is released under Apache-2.0. These are the licences
stated by each source; this is not legal advice, so check the terms of the sources you reuse.

Base rows, by the licence on the source repo's card (or, for tasksource tasks, the origin dataset's card; not legal
advice): of 200,000 rows before decontamination, 178,084 verified permissive, 1,127 share-alike (CC BY-SA), 497 under
other open licences (Mozilla Public License, Academic Free License), 13,263 not traced to an origin, 5,971 with no
licence stated and 1,058 under the GPL. The model was trained on all of them. This dataset releases only the
permissive, share-alike and other-open rows (173,859 after decontamination); the per-row licence is in `licence`.

## Compute

Every step ran on [Hugging Face Jobs](https://huggingface.co/docs/huggingface_hub/guides/jobs), with sources, mixes
and test sets in Hugging Face storage buckets mounted into each job.
- **Building the data** (source conversion, licence filtering, decontamination, the mix itself) ran on CPU jobs; the
  final mix build takes about 16 minutes.
- **Labelling experiments** (open-model panels, rubric and pairwise checks; see design note 4) called LLMs through
  Hugging Face Inference Providers from Jobs. Those labels are not in the final mix.
- **Training and evaluation** of each data choice ran on single RTX PRO 6000 GPU jobs, about an hour per training run.
- The release build (`scripts/release_build.py`) is a CPU job that reads the mix from a bucket and writes this repo.

## Known issues

- Several label sources are LLM outputs (named above and per row in `teacher`). The WebOrganizer annotation datasets
  carry no licence statement. The Llama 3 and Llama 3.1 licences cover the Llama-made labels (WebOrganizer, FineWeb-Edu);
  read them before you reuse those rows.
- Use terms of the original sources apply to their rows; check `licence` / `src` per row before reuse.
- Multilingual rows (DecisionBank) are present; the model was evaluated in English only.
- Difficulty labels are subjective and depend on the labeller (LLM-made here; human ratings agree only moderately).

## Notes for agents

- Filter on `licence_class` / `licence` before redistributing any subset; never redistribute rebuilt `web` text.
- `target` is a distribution, not a class index; take `argmax` for hard labels. Graded questions (`level_<k>` keys)
  are ordered: use the expected level or a rank correlation (Spearman), not top-1 accuracy alone.
- This release is not the exact training mix: 18,766 base rows are left out and web text is removed.
- Evals are not in this dataset; they are listed by name in the model card. Do not train on Omni-MATH, Essential-Web,
  HelpSteer, Polaris, Aegis or WildGuard if you want to compare with the model card.
