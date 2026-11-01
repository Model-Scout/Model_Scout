---
pretty_name: KR-Housing-LongRAG-Bench
language:
  - ko
license: cc-by-4.0
task_categories:
  - question-answering
  - text-retrieval
tags:
  - korean
  - long-context
  - rag
  - table-question-answering
  - housing
  - benchmark
configs:
  - config_name: qa
    data_files:
      - split: dev
        path: data/dev.jsonl
      - split: test_public
        path: data/test_public.jsonl
  - config_name: prompts
    data_files:
      - split: prompts
        path: data/prompts.jsonl
  - config_name: metadata
    data_files:
      - split: source_manifest
        path: data/source_manifest.jsonl
  - config_name: gold_fixes
    data_files:
      - split: gold_fixes
        path: data/gold_fixes_v0.9.2.jsonl
  - config_name: errata
    data_files:
      - split: errata
        path: data/errata_v0.9.3.jsonl
  - config_name: errata_v0.9.2
    data_files:
      - split: errata
        path: data/errata_v0.9.2.jsonl
  - config_name: errata_v0.9.1
    data_files:
      - split: errata
        path: data/errata_v0.9.1.jsonl
---


# KR-Housing-LongRAG-Bench v0.9.9

> Superseded by KHAT (https://doi.org/10.5281/zenodo.23429293, https://github.com/comsa33/khat).

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.23312498-blue.svg)](https://doi.org/10.5281/zenodo.23312498)

KR-Housing-LongRAG-Bench is a Korean public-housing benchmark for evaluating long-context LLMs, RAG systems, and table/tool pipelines on official housing announcements, public tabular data, and housing-law evidence. This Hugging Face package publishes the public-safe split files only: no raw PDF/HWP/HWPX documents, extracted document text, bundle text, or API keys. Code, scripts, per-item judge verdicts and human labels are in the [GitHub repository](https://github.com/comsa33/kr-housing-longrag-bench).

## Evaluation scope in v0.9.9 (read before scoring)

1. **Exclude the `cross_document_legal_reasoning` family** (109 items, 42 in test_public), as in v0.9.1. Its gold answers follow the statute versions in the corpus (2015/2018), not the current statutes.
2. **Exclude 5 ill-posed test_public items** (unchanged from v0.9.2): `krhlrb_v05_0994`, `0995`, `1125`, `1132` (table header misparsed) and `1369` (the answer depends on a supply type the question does not name).
3. **Exclude 7 dev items with confirmed errors** (new in v0.9.3): `krhlrb_v05_0596`, `0788`, `0800`, `0875`, `0884`, `1056`, `1142`. Two non-author annotators reviewed 100 random dev items and agreed on these 7 errors, which the author confirmed.
4. **Use the corrected gold for 24 test_public items** (config `gold_fixes`, unchanged from v0.9.2). 23 items accept any of several answers that the source supports; one item (`krhlrb_v05_0568`) has a new answer.
5. **Bundle-based settings only (BM25, dense, full context): also exclude 122 dev items** whose 512k bundle lacks at least one of their gold pages (`data/bundle_exclusions.txt`). Keep them in closed-book. Since v0.9.9, also exclude 20 answerability items (7 test_public, 13 dev) whose bundle holds pages of the announcement the question asks about; the combined list of 142 items is `data/v0.9.9/bundle_exclusions.txt` in the GitHub repository and on Zenodo.
6. **Closed-book prompts: drop the leaking locator fields.** The `prompts` config is unchanged and still carries the locator fields. For 64 count items the number of `row_ids` equals the answer, and for 4 items a document identifier contains the answer date. `data/cb_locator_fix.jsonl` lists the 68 items and the fields to remove; the v0.9.3 `build_prompt` in the GitHub repository removes them.

7. **Dev full review (new in v0.9.7): exclude 11 more dev items and use the corrected gold for 79 dev items.** The 11 items are listed in `data/v0.9.7/eval_exclusions.txt` and the corrections (74 accept-any, 5 replaced; corrected evidence locators of 30 items in the `new_locator` column since v0.9.8) in `data/errata_v0.9.7.csv`; both files are in the GitHub repository and on Zenodo, not in this Hugging Face package.

Items 2 and 3 are listed in `data/eval_exclusions.txt`.

| Scope | Total | dev | test_public |
|---|---:|---:|---:|
| Items in the files (unchanged since v0.9) | 1,997 | 1,608 | 389 |
| v0.9.2 evaluation scope | 1,883 | 1,541 | 342 |
| v0.9.3 evaluation scope | 1,876 | 1,534 | 342 |
| v0.9.3 bundle-based settings (items with a bundle, minus the 122) | 1,303 | 964 | 339 |
| **v0.9.7 evaluation scope** | **1,865** | **1,523** | **342** |
| v0.9.7 bundle-based settings | 1,293 | 954 | 339 |
| v0.9.9 bundle-based settings | 1,273 | 941 | 332 |

```python
from datasets import load_dataset

qa = load_dataset("comsa33/kr-housing-longrag-bench", "qa")
fixes = load_dataset("comsa33/kr-housing-longrag-bench", "gold_fixes")["gold_fixes"]
dev_errors = {"krhlrb_v05_0596", "krhlrb_v05_0788", "krhlrb_v05_0800", "krhlrb_v05_0875",
              "krhlrb_v05_0884", "krhlrb_v05_1056", "krhlrb_v05_1142"}
excluded = {r["qa_id"] for r in fixes if r["action"] == "exclude_from_evaluation"} | dev_errors
accepted = {r["qa_id"]: r["accepted_answers"] for r in fixes if r["action"] != "exclude_from_evaluation"}

keep = lambda r: r["task_type"] != "cross_document_legal_reasoning" and r["qa_id"] not in excluded
test, dev = qa["test_public"].filter(keep), qa["dev"].filter(keep)
print(len(test), len(dev))  # 342 1534
# For qa_id in `accepted`, a prediction is correct if it matches any of accepted[qa_id].
```

The `data/*.jsonl` QA files are byte-identical to v0.9.1; the gold changes are published only in `gold_fixes`. With an LLM judge, show accept-any gold as `다음 중 어느 하나와 일치하면 정답: (1) … / (2) …` (the format used for the reported results).

## What changed from v0.9.8

The data files and every config are unchanged. v0.9.9 adds a bundle exclusion list in the GitHub repository and on Zenodo: 20 answerability items whose bundle also holds the asked-about announcement are dropped from the bundle-based settings (closed-book keeps them).

## What changed from v0.9.7

The data files and every config are unchanged, and so is every reported number. v0.9.8 adds a machine-readable `new_locator` column (30 items, 31 page mappings) to `data/errata_v0.9.7.csv` in the GitHub repository and on Zenodo, updates the recall script to read it, and corrects three statements in the v0.9.7 release notes.

## What changed from v0.9.6

The data files and every config are unchanged; v0.9.7 adds review files, errata, an exclusion list and re-judged verdicts in the GitHub repository and on Zenodo (not in this Hugging Face package).

- **Full human review of dev.** Two of four non-author annotators labeled each of the 1,534 evaluated dev items independently; the author confirmed 120 errors (7.8%, Wilson 95% [6.6, 9.3]). 79 gold answers were corrected, 30 evidence locators fixed and 11 items excluded (scope item 7). The dev predictions on the 79 corrected items were re-judged under both judges; pooled accuracy changes by at most 1.1 points.
- **Second judge-validation sample.** Two annotators labeled 216 predictions; the primary judge agrees with all 200 adjudicated labels of the main sample (Wilson 95% lower bound 98.1%).

## What changed from v0.9.5

The data files and every config are unchanged; v0.9.6 adds one pre-specified run in the GitHub repository and on Zenodo (not in this Hugging Face package).

- **k=50 plus the announcement page.** On the 18 aggregation items whose dense k=50 passages lack the announcement page (two announcement-table pairs), adding the whole page as one passage raises gpt-5.5, minimax-m3, glm-5.2 and claude-sonnet-5-5 from 0 to 15-18 of 18 (`results/judge_verdicts_v0.9.6/` and `results/predictions_v0.9.6/` on GitHub; pre-specification document `results/judge_verdicts_v0.9.6/PRESPECIFICATION.md`). The effect of the page cannot be separated from these two announcements.

## What changed from v0.9.4

The data files and every config are unchanged; v0.9.5 adds model answers in the GitHub repository and on Zenodo (not in this Hugging Face package).

- **Model answers.** The final answer text of every judged prediction behind the reported results (24,074 model answers, `results/predictions_v0.9.5/` on GitHub), so the evaluation can be re-judged. Reasoning traces, the model input prompts (which contain bundle text), bundle text and the unreported qwen3.5 runs are excluded; 1 source-text span and 6 unverified phone numbers are masked.
- **Terms.** The model answers are not covered by CC BY 4.0, remain subject to each model provider's terms of use, are released for reproducing and re-judging the evaluation, and must not be used to train competing models.

## What changed from v0.9.3

The data files and every config are unchanged; v0.9.4 adds results and scripts in the GitHub repository.

- **Dense retrieval at k=50 on the 81 aggregation items.** Six models read 50 bge-m3 passages under a comparison rule fixed before any generation call. The 50 passages hold the announcement page and every matched row for 63 items, and no model answers any of the other 18 correctly. Verdicts: `results/judge_verdicts_v0.9.4/` on GitHub.
- **Recall rule.** Gold-page recall now assigns each retrieved passage to the one page that holds most of its characters. BM25 recall@5: dev 74.9%, pooled 78.7%, test_public 89.7% (unchanged).
- **Disclosures.** The minimax-m3 reasoning flag no longer reproduced its reported behaviour, and four July 2026 full-context answers of minimax-m3 were re-called once; see CHANGELOG 0.9.4 on GitHub.

## What changed from v0.9.2

- **Closed-book locator fix.** Count items exposed their answer through the number of `row_ids` (17 test_public, 47 dev), and 4 items exposed an answer date inside a document identifier. The closed-book runs on these 68 items were redone without those fields. See item 6 above.
- **Second human review round.** The two non-author annotators reviewed 100 random dev items: 7 errors, 7.0% (Wilson 95% [3.4, 13.7]), κ 1.0 between them. The 7 items are excluded (item 3). Of the 54 detector flags on dev, 6 fell in the sample and all 6 were confirmed; the other 48 remain unverified flags and stay in evaluation. The annotators also labeled the 80 judge-validation predictions independently and agreed with the primary judge on all 78 that both labeled.
- **Third human review round.** On the 74 predictions of the two Anthropic models where six LLM judges disagreed, the two annotators labeled the answers blind to the model; the author settled their disagreements under a rule fixed in advance.
- **Bundle evidence.** 122 dev items have a 512k bundle that lacks at least one of their gold pages (item 5): 60 lack every gold page, 62 lack one of two.
- **Page-marker fix (code).** The passage splitter did not read Hangul page identifiers (18 SH announcements), so dev and pooled BM25 recall were under-counted. Retrieved text and accuracy were unaffected. The GitHub code is fixed; `KRH_LEGACY_PAGE_MARKERS=1` reproduces the old runs.
- **Errata.** Config `errata` (`data/errata_v0.9.3.jsonl`, same rows as `data/errata_v0.9.3.csv`) has 206 rows: the 29 confirmed test errors from v0.9.2, the 7 confirmed dev errors, the 48 unverified dev flags, and the 122 dev items whose bundle lacks a gold page. The v0.9.2 errata (83 rows) are kept as config `errata_v0.9.2`, and the v0.9.1 errata (111 rows) as `errata_v0.9.1`.
- **Human naturalness labels.** The v0.9.2 test review also asked whether each question reads naturally (not an error criterion). Two or more of the three annotators marked 52 of the 347 reviewed items as not natural, 51 of them script-generated. The labels are in the GitHub repository.

## Status and known issues

This is a **public-ready seed benchmark**. It is **not** a sealed-hidden leaderboard benchmark and **not** a final model ranking. The evaluated test_public items were reviewed by three annotators; every evaluated dev item was reviewed by two of four annotators (v0.9.7).

- Public splits: dev 1,608 / test_public 389. There is no hidden split, and all answers are included.
- `split_tags` mark generalization subsets within test_public: `ood_region` (116), `ood_year` (50).
- Near-duplicate clusters: 282. The evaluators report **cluster-weighted** accuracy so repetition cannot inflate scores.
- **Known issue.** The `mix_multiprovider_256k` bundle is about 710k tokens, longer than its tier name (37 items in scope: dev 28, test_public 9). Report the 256k tier with and without these items.
- Long-context bundle text is not redistributed. Rebuild local bundles from the official source URLs with the scripts in the GitHub repository.

## Files

| File | Config / split | Description |
|---|---|---|
| `data/dev.jsonl` | qa / dev | 1,608 items, answers included |
| `data/test_public.jsonl` | qa / test_public | 389 items, answers included (v0.9.1 gold) |
| `data/prompts.jsonl` | prompts | locator-only public-safe prompt inputs (1,997); see item 6 for closed-book use |
| `data/source_manifest.jsonl` | metadata | source registry, license posture, checksums |
| `data/gold_fixes_v0.9.2.jsonl` | gold_fixes | 29 rows: 23 accept-any, 1 replace, 5 excluded |
| `data/gold_fixes.json` | — | the same fixes in the GitHub repository format |
| `data/eval_exclusions.txt` | — | 12 items excluded in every setting (5 test_public, 7 dev) |
| `data/bundle_exclusions.txt` | — | 122 dev items excluded from the bundle-based settings |
| `data/cb_locator_fix.jsonl` | — | 68 items and the locator fields to drop in closed-book prompts |
| `data/errata_v0.9.3.csv`, `data/errata_v0.9.3.jsonl` | errata | 206 rows (see above) |
| `data/errata_v0.9.2.csv`, `data/errata_v0.9.2.jsonl` | errata_v0.9.2 | 83 rows, unchanged |
| `data/errata_v0.9.1.csv`, `data/errata_v0.9.1.jsonl` | errata_v0.9.1 | 111 rows, unchanged |
| `data/task_schema.json` | — | QA schema |

## Scoring

Use the evaluators in the GitHub repository. Prediction JSONL format: `{"qa_id": "krhlrb_v05_0001", "prediction": "your model answer"}`. `results/README.md` on GitHub shows how to recompute the paper tables from the released per-item judge verdicts, for example:

```bash
git clone https://github.com/comsa33/kr-housing-longrag-bench && cd kr-housing-longrag-bench
python3 scripts/score_judge.py --exclude-family cross_document_legal_reasoning \
    --exclude-ids data/v0.9.3/eval_exclusions.txt \
    --exclude-bundle-ids data/v0.9.3/bundle_exclusions.txt \
    --verdicts-dir results/judge_verdicts_v0.9.3/claude-sonnet-5-5
```

## License

Benchmark annotations are released under CC BY 4.0. Underlying source materials remain governed by their original public-data, public-work, statutory, or provider-specific terms. Do not redistribute raw third-party documents unless their source license permits it.

## Citation

Cite the **v0.9.9 release** by its Zenodo versioned DOI, or use the concept DOI to always cite the latest version:

```bibtex
@dataset{lee_kr_housing_longrag_bench_2026,
  author    = {Lee, Ruo},
  title     = {KR-Housing-LongRAG-Bench},
  year      = {2026},
  version   = {v0.9.9 (1,997 QA; full dev review, bundle exclusions)},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.23312498},
  url       = {https://doi.org/10.5281/zenodo.23312498}
}
```

DOIs: v0.9.9 `10.5281/zenodo.23312498`; v0.9.8 `10.5281/zenodo.23311591`; v0.9.7 `10.5281/zenodo.23311037`; v0.9.6 `10.5281/zenodo.23307114`; v0.9.5 `10.5281/zenodo.23306443`; v0.9.4 `10.5281/zenodo.23300582`; v0.9.3 `10.5281/zenodo.23298455`; v0.9.2 `10.5281/zenodo.23291297`; v0.9.1 `10.5281/zenodo.23282680` (2026-10-10); concept DOI `10.5281/zenodo.20559127` (resolves to the latest version); v0.9 `10.5281/zenodo.20640480`; v0.8 `10.5281/zenodo.20571211`; v0.7 `10.5281/zenodo.20570856`; v0.6.3 data build `10.5281/zenodo.20563604`.

Machine-readable citation metadata is in `CITATION.cff`.
