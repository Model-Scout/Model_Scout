---
pretty_name: "Subjects, Not Authors — Evidence Package"
license: cc-by-4.0
language:
- en
- ko
tags:
- dataspaces
- odrl
- usage-control
- llm-agents
- access-control
- model-context-protocol
- reproducibility
size_categories:
- n<1K
viewer: false
---

# Subjects, Not Authors — Evidence Package

Evidence package for:

> Seungho Lee and Changbin Lee. **Subjects, Not Authors: The Authorship Hazard in Agentic Dataspaces.**
> arXiv:2609.30614, 2026. Korea Trade Network (KTNET).

This repository holds the preregistrations, corpora, raw trial records and analysis scripts behind Section 8 of
the paper, and the preregistered clean-environment corrective replication of its live-model runs (CASE-B-CR-1,
`case_b_cr1/`): 585 files, 51.5 MB. The public arXiv listing is version 1; this release supports the forthcoming
arXiv version 2 and the CSI submission (see *Paper versions*). `python -B reproduce/check_all.py` recomputes their
Section 8 figures from the raw records here and takes the model-dependent ones from the corrective replication (see
*Reproducing the figures*). Claim maps written against earlier manuscript versions are kept in
`correction_history/` as a record of corrections; they are not a source for the current figures.

- **Dataset:** https://huggingface.co/datasets/ktnet-research/subjects-not-authors-evidence (its DOI is listed on
  that page once assigned)
- **Paper:** https://arxiv.org/abs/2609.30614 (public listing: version 1; this release supports the forthcoming
  version 2 and the CSI submission; see *Paper versions*)
- **Licenses:** data and documents CC BY 4.0; code written by the authors MIT; files derived from Eclipse
  Tractus-X EDC or Eclipse Dataspace Components code, and the new Java file of the profile extension, Apache-2.0,
  listed in `third_party/README.md`. See `LICENSE`.

## Paper versions

The arXiv listing currently shows version 1. This release supports the forthcoming arXiv version 2 and the CSI
submission, which differ from version 1 in two ways:

- They correct figures of version 1. The corrections are listed in Appendix B of the forthcoming version and in
  `correction_history/README.md` (see also *Corrections relative to arXiv v1*).
- Their model-dependent figures - Table 7, the Section 8.2 text numbers and Section 8.6 - come from the corrective
  replication CASE-B-CR-1 (`case_b_cr1/`). The original live-model runs under `v5.3/` were not hermetic (see
  *Data*). Their figures, for example 49/220 and 57/220 adversarial leaks under prompt-only and discovery filtering
  in Table 7 and 39 of 900 in Section 8.6, are kept as the historical record; the forthcoming version reports
  56/219, 54/219 and 52 of 895 from the corrective replication.

Figures that do not depend on a model's output - the hashes of the Case B extension, Case D5 and Case D2
preregistrations and of the profile-extension diff, Table 6 and Section 8.1, Section 8.3 and Appendix A, Tables 8–11
and Sections 8.4–8.5 - are not affected by the corrective replication. The fifth hash the forthcoming version cites,
`d5b5760b…`, is that of the corrective replication's own preregistration (*Preregistrations and hashes*).

## Data

All corpora and raw records use constructed values. The asset is a constructed certificate of origin with fields
in sensitivity classes F0 (public trade facts), F1 (commercial quantities) and F2 (identities). Party names and
record values are written out in the corpus code (`v5.3/case_b_original/experiment_b1/tools/query_certificate.py`,
`v5.3/case_b_extension/corpus/`, `v5.3/case_d/draft_corpus.py`, `v5.4/case_d2/src/design.py`). No real customer or
transaction data is included.

Raw outputs of the evaluated models are included. In Section 8.2: claude-opus-5, claude-sonnet-5, claude-fable-5-1
and claude-haiku-4-5-20251001 through claude-code 2.1.278; gpt-5.6-luna, gpt-5.6-sol, gpt-5.6-terra and
gpt-6-astra through codex-cli 0.155.1; qwen3:8b (Q4_K_M) served locally by ollama 0.24.0. In Section 8.6: four
Claude models through claude-code 2.1.278; gpt-5.6-sol through codex-cli 0.145.0; and gpt-5.6-sol, gpt-5.6-luna,
gpt-5.6-terra and gpt-6-astra through codex-cli 0.155.1. No model weights, vendor binaries or container images
are included. Two Section 8.2 claude-fable-5-1 records (task A14, prompt-only and compiled) were answered by a
fallback model after the provider's safeguard declined the request. They are included as recorded and counted under
claude-fable-5-1 in the original-run figures; excluding them changes none of the qualitative claims. For the
codex-cli runs the served model is not recorded.

Properties of the raw model outputs that should be known before using them:

- A post-run audit of runtime session records found that the original live-model runs were not hermetic. The
  claude-code runs disabled tools, settings files and MCP servers (`--tools ""`, `--setting-sources ""`,
  `--strict-mcp-config`), but every Claude trial still received runtime-level context that was not part of the
  experimental prompts: in Section 8.2 the project's auto-memory, the account's e-mail address and the
  working-folder path; in Section 8.6 the account's e-mail address and the working-folder path. The original
  runtime session logs are retained privately for audit and are not part of this repository. Some raw outputs show
  traces of that context and are kept as recorded: outside task A11, which asks for a Korean translation, 138
  Section 8.2 Claude responses are in Korean (claude-opus-5 110, claude-fable-5-1 22, claude-sonnet-5 6) although no
  prompt or system policy contains Korean; one claude-opus-5 response offers to format its answer for an internal
  wiki; five claude-opus-5 responses name "KTNET"; and four Section 8.6 claude-opus-5 responses refer to a
  "scratchpad" working folder. We therefore preserve the original outputs as correction history and report a
  preregistered clean-environment corrective replication for the model-dependent results (`case_b_cr1/`, next
  paragraph). Metrics measured at the gateway before model invocation are unaffected.
- In the codex-cli records of Section 8.2 (`v5.3/case_b_extension/experiment_b_extension_raw/gpt_b1b_*_raw.jsonl`),
  the field `runtime_banner_head` held a runtime warning that named the experiment machine's temporary folder. This
  release replaces that path with `<TEMP>`; `RELEASE_FILEMAP.json` (`sanitized`) lists the original and released
  SHA-256 of the four files. No other field changed.

**Original runs and the corrective replication.** The original runs under `v5.3/` are the pre-corrective
live-model records; they are kept unchanged as correction history. The corrective replication under
`case_b_cr1/` is a separate, preregistered experiment that ran the same design again in a hermetic harness: one
rootless container per trial, an empty home and working folder, an allow-listed environment, no tools for the
Claude runtime, an egress proxy that allows only the runtime's model and feature-flag hosts, and a per-trial audit
of what reached the model.
Its preregistration fixed, before the first trial, the claims to be re-tested and the rule that classifies the
outcome; four timestamped amendments record what changed during the run. Result: all ten preregistered claims hold
in both runs (classification A, CLAIM_STABLE, over all nine Section 8.6 cells). Every one of the 2,709 recorded trials
passed the audit; eight claude-fable-5-1 trials answered by a fallback model were counted as routing mismatches, and
39 trials whose container never started were run once more.
The model-dependent figures of the forthcoming version (Table 7, the Section 8.2 text numbers and Section 8.6) come
from the corrective replication; `case_b_cr1/README.md` sets the two runs side by side. Runtime session logs of neither run are published; the
corrective replication publishes per-trial audit fields and an audit summary instead.

**Privacy.** The repository contains no account e-mail addresses, credentials, API keys or runtime session logs.
Raw model outputs are published as recorded. The corrective-replication harness is published with local folder
defaults replaced by paths relative to this tree and two literal identifying strings in its audit patterns replaced
by placeholders. Runtime session identifiers that the corrective replication's audit recorded (session-log file
names and the codex `session id` line of the preflight records) are replaced by `<session-id>` in its run records;
the SHA-256 of each privately retained session log is kept. `RELEASE_FILEMAP.json` lists these sanitized copies
with their original and released SHA-256.

"KTNET" otherwise appears in the authors' affiliation, in the dataset's Hugging Face organization name
(`ktnet-research`), in two scenario namespaces (`w3id.org/ktnet/dpp/policy/`, `ktnet.example`) and in the corrective
replication's audit patterns, which check model outputs for that name. The provenance audit names the internal code
bases that were searched for reused components by role (`v5.3/COMPONENT_PROVENANCE.md`, `v5.3/provenance/`).

**Language.** Of the 91 Markdown documents from the two deliveries, 77 are written mainly in Korean and 6 mix
Korean and English (`RELEASE_MANIFEST.md` gives the rule); code comments and some JSON fields are also in Korean. This README, `reproduce/README.md`, `third_party/README.md`,
`correction_history/README.md`, the preregistration hash files and the raw records are the entry points for
English-speaking readers.

## Preregistrations and hashes

The paper cites five hashes. Each matches this package.

| Paper | Object | File | Full SHA-256 |
|---|---|---|---|
| `3484d360…` | Case B extension preregistration (combined hash, 8 files; frozen 2026-09-21 20:26:51 KST) | `v5.3/case_b_extension/experiment_b_extension_planned/PREREGISTRATION.sha256` | `3484d3603ab241b3b3c0574fe41b977c24d12162f5e03fc447b8195b59821203` |
| `d5b5760b…` | CASE-B-CR-1 clean-environment corrective replication preregistration (combined hash, 2 files; frozen 2026-10-02 08:13:21 KST) | `case_b_cr1/planned/FREEZE.json` | `d5b5760b8b09ab273f7f58442f5007d20b6a670020d07e3f5f338def5aea7921` |
| `94b52959…` | Case D5 preregistration (combined hash, 3 files; frozen 2026-09-24 17:25:59 KST) | `v5.3/case_d5_federated/experiment_d5_planned/PREREGISTRATION.sha256` | `94b52959027e4076e2bff61ee5089994cb52970e6d33651d54c9e90848dda89d` |
| `20d86cf9…` | Case D2 preregistration (combined hash, 39 files; frozen 2026-09-28 16:36:34 KST) | `v5.4/case_d2/experiment_d2_planned/PREREGISTRATION.sha256` | `20d86cf908fb65d5230c1b3f0ea9001721dac63978b1913fe680ce37b939a14d` |
| `d5bad0bb…` | Profile-extension diff, 82 lines (App. A) | `v5.3/case_b_original/experiment_b1/agreement/real_primary/run4_level4/profile_patch/profile_patch.diff` | `d5bad0bb3474bb590fb15179a69ee362316df78283499b2052009e3770e5fe5b` |

Combined hashes are recomputed from the frozen files with the rule of the experiments' freeze scripts
(`freeze_prereg.py`; for CASE-B-CR-1, `case_b_cr1/harness/freeze.py`): SHA-256 over the sorted lines
`<file SHA-256>  <path>`. `reproduce/check_all.py` recomputes the four combined hashes and compares each in full with
the value recorded in the file listed above (for CASE-B-CR-1 also with the full value in this table), computes the
SHA-256 of the profile-extension diff, and checks all five against the eight-digit prefix the paper prints.

The CASE-B-CR-1 preregistration froze two files: the preregistration document
`case_b_cr1/planned/PREREGISTRATION.md` and the execution manifest `case_b_cr1/planned/EXECUTION_MANIFEST.json`. The
manifest published here is a sanitized release copy (two identifying strings in its recorded audit patterns replaced
by placeholders), so combining its current bytes does not reproduce the frozen hash, and
`case_b_cr1/harness/freeze.py --check` reports a mismatch on this tree. The manifest's SHA-256 at the freeze is
recorded in `case_b_cr1/planned/FREEZE.json` and kept as `original_sha256` in `RELEASE_FILEMAP.json`.
`reproduce/check_all.py` (rows `H5.*`) checks that the released manifest is the copy listed there (`release_sha256`),
takes the frozen SHA-256 from that entry, hashes the preregistration document, which is published unchanged, and
recomputes `d5b5760b…` in full; a missing entry or any mismatch fails the check. Changes made after the freeze are
timestamped amendments in `case_b_cr1/planned/amendments/`, outside the frozen set.

The Case B extension preregistration was frozen before any extension run. The live-model design of Section 8.2
(nine configurations; one repetition for the eight hosted configurations, three for the local one) was set by four
amendments, AMENDMENT-001 to -004 in `v5.3/case_b_extension/experiment_b_extension_planned/`, each registered with
its hash in `AMENDMENTS.sha256` before the live-model runs it governs. They postdate the deterministic runs of
Section 8.1, which they leave unchanged, and AMENDMENT-004 also postdates the local-model runs, which it leaves
unchanged. AMENDMENT-005 was recorded after all runs: it changes no design element and corrects the
preregistration's statement that a freeze check gated every batch. The runners did not call that check; the
frozen files were verified afterwards. Case D5 and Case D2 have no amendments.

## Layout and mapping to the paper

`v5.3/` and `v5.4/` are the two evidence deliveries (v5.3 of 2026-09-24, cumulative; v5.4 of 2026-09-28, Case D2).

| Paper | Experiment | Folder | Raw records |
|---|---|---|---|
| §8.1, Table 6 | Case B, deterministic boundary measurement: 105-case risk set, 16-case stress group, separate 22-case risk set | `v5.3/case_b_extension/`, `v5.3/case_b_original/experiment_b1/b1a/` | `v5.3/case_b_extension/experiment_b_extension_raw/b1a_expanded_raw.jsonl` (450 trials); `v5.3/case_b_original/experiment_b1/b1a/raw_results.jsonl` (22-case set, provenance, retention, fail-closed) |
| §8.2, Table 7 (original runs, historical record) | Case B with nine model configurations, 1,320 calls | `v5.3/case_b_extension/` | `v5.3/case_b_extension/experiment_b_extension_raw/claude_b1b_*_raw.jsonl`, `gpt_b1b_*_raw.jsonl`, `qwen_b1b_raw.jsonl` |
| §8.3, App. A | Case E, Tractus-X EDC 0.13.0 negotiation; profile extension; condition (iv) | `v5.3/case_b_original/experiment_b1/agreement/`, `v5.3/case_e_condition_iv/` | `v5.3/case_b_original/experiment_b1/agreement/real_primary/`; replay `v5.3/case_b_extension/experiment_b_extension_raw/b1c_expanded_raw.jsonl`; condition (iv) `v5.3/case_e_condition_iv/raw*/` |
| §8.4, Tables 8–9 | Case D2, 90 preregistered edits over 344,512 requests; 25 literal insertions | `v5.4/case_d2/` | `v5.4/case_d2/results/raw/raw_results.jsonl` |
| §8.4, Table 10 | Earlier constructed validation (380 drafts) and centralized queue simulation | `v5.3/case_d/`, `v5.3/case_d_queue/` | `v5.3/case_d/raw_results.jsonl`; `v5.3/case_d_queue/raw_v2/` (the run with V2 = 0.7105 used in the paper; `raw/` is the superseded run with 0.842) |
| §8.4 | Case D5, federated topology | `v5.3/case_d5_federated/` | `v5.3/case_d5_federated/raw/` |
| §8.5, Table 11 | Case A, per-action evaluation cost and revocation timing | `v5.3/case_a/` | `v5.3/case_a/raw/a1_pdp_roundtrip.jsonl` to `a5_failure.jsonl` |
| §8.6 (original runs, historical record) | Prompt-only output behavior, 1,350 trials | `v5.3/case_b_original/experiment_b0/` | `v5.3/case_b_original/experiment_b0/raw.jsonl` (the files in `extensions/` are per-cell copies of rows already in `raw.jsonl`) |
| — | Experiment methods for the §8.6 study, the 22-case set and Case E | `v5.3/case_b_original/handoff/EXPERIMENT_METHODS.md` | its B1-B section describes an earlier 240-call run, not the 1,320-call study of §8.2 |
| §8.2, Table 7, §8.6 (current values: corrective replication) | CASE-B-CR-1, the eighteen live-model configurations of §8.2 and §8.6 re-run in a hermetic harness | `case_b_cr1/` | `case_b_cr1/runs/raw/main_*.jsonl` (2,670 planned trials; 2,709 records including 39 re-runs) |
| — | Claim maps from earlier manuscript versions (correction history) | `correction_history/` | — |
| — | Third-party notices | `third_party/` | — |

Documents written during the project refer to paths in the authors' working repository (for example
`13-연구/case_d2/...`). Those paths are not part of this release; where a named file was delivered, it is under
`v5.3/` or `v5.4/`.

## Reproducing the figures

From the repository root, with Python 3.11 or later and nothing else installed:

```
python -B reproduce/check_all.py
```

It recomputes the five hashes the paper cites and checks them as described under *Preregistrations and hashes*,
re-runs the Case D2 invalidation checks for this layout, checks every file of the two deliveries against their own
`SHA256SUMS.txt` and `RELEASE_FILEMAP.json`, and recomputes the Section 8 figures from the raw records. Expected and
recomputed values are printed side by side; the run ends with `OVERALL: PASS` (203 checks). It writes nothing into
the repository. It can be run in a git clone or an `hf download --local-dir` copy: the root `.gitattributes`, `.git/`
and `.cache/huggingface/` are not counted as unlisted files, while any other file that `MANIFEST.sha256` does not
list fails the check. The rows fall into three groups:

| Rows | Figures | Recomputed from | Expected value |
|---|---|---|---|
| `CR1.*` | model-dependent figures of the forthcoming version: Table 7, the Section 8.2 text numbers, Section 8.6 | the corrective replication's records `case_b_cr1/runs/raw/`, through its frozen analysis `case_b_cr1/harness/analyze.py compare` | the forthcoming version's values, for example 56/219 and 54/219 adversarial leaks in Table 7 and 52 of 895 in Section 8.6; the recomputed analysis must also equal `case_b_cr1/runs/analysis/compare_9cell.json` |
| `T7.*`, `S82.*`, `S86.*` | the same figures for the original, pre-corrective runs | `v5.3/case_b_extension/experiment_b_extension_raw/`, `v5.3/case_b_original/experiment_b0/raw.jsonl` | what those records give, for example 49/220 and 57/220 and 39 of 900; historical record, not the forthcoming version's values |
| all other rows | figures that do not depend on a model's output: hashes and package integrity, Table 6 and Section 8.1, Section 8.3 and Appendix A, Tables 8–11, Sections 8.4–8.5 | the delivered records under `v5.3/` and `v5.4/` | the forthcoming version's values |

`python -B case_b_cr1/harness/analyze.py compare <output.json>` runs the corrective replication's analysis on its own
and writes the full claim comparison of both runs; `case_b_cr1/README.md` describes it. One column is checked rather
than recomputed: the transform overhead of Table 6 comes from an in-process microbenchmark that stored only its
aggregates (`v5.3/case_b_original/experiment_b1/b1a/latency.json`), not per-iteration samples.

Live-model trials (§8.2, §8.6) ran through vendor command-line runtimes at each runtime's default sampling settings
and cannot be re-run deterministically; the raw records are the ground truth. The experiment scripts inside `v5.3/`
and `v5.4/` (runners, adapters, scoring and recompute scripts, preregistration tools) are kept as delivered; some of
them expect the original working-folder layout (`reproduce/README.md`).

## Corrections relative to arXiv v1

Appendix B of the forthcoming version lists them. For example, the revocation counts in Table 11 are 99 (five-second
cache), 591 (thirty-second cache) and 439 (agreement-only path), not 101, 593 and 440, because v1 also counted the
admission decision and, where present, the final denial. `correction_history/README.md` lists the figures in older
claim maps and experiment write-ups that the forthcoming version replaces, for example the earlier 84.2% escalation figure, which
the paper splits into 71.1% human review and 13.2% automatic rejection.

## What was removed from the deliveries

Internal coordination notes, a superseded working draft of the paper, messages between the authors, the authors'
pre-execution design notes for Case A and the earlier Case D validation, and seven compiled upstream classes were
not carried over; three claim maps were moved to `correction_history/`. Eight files were replaced by sanitized
copies: one note without a coauthor's local folder path, the four Section 8.2 codex-cli raw files with the
temporary-folder path replaced in `runtime_banner_head`, and three provenance files with internal repository names,
registry host names and a policy id replaced by role labels. Twenty-two scripts that only packaged, delivered,
validated or supervised the deliveries, or checked their wording, were not carried over; one of them is the internal
provenance scanner, whose output file was removed with it. The experiment runners, adapters, scoring and recompute
scripts and the preregistration tools are kept.
`RELEASE_FILEMAP.json` lists each of these files with the SHA-256 the delivery recorded for it and, for sanitized
copies, the released SHA-256 and what changed. Some documents inside `v5.3/` and `v5.4/` still refer to removed files.

## Limitations

The edit space of Case D is constructed, not sampled, and its policy evaluator reimplements the paper's rules
rather than running inside the EDC decision point. Case C was not run, and there is no external baseline. See
Section 10 of the paper.

## Citation

```bibtex
@misc{lee2026subjects,
  title         = {Subjects, Not Authors: The Authorship Hazard in Agentic Dataspaces},
  author        = {Lee, Seungho and Lee, Changbin},
  year          = {2026},
  eprint        = {2609.30614},
  archivePrefix = {arXiv}
}

@misc{lee2026subjects_evidence,
  title     = {Subjects, Not Authors --- Evidence Package},
  author    = {Lee, Seungho and Lee, Changbin},
  year      = {2026},
  publisher = {Hugging Face},
  url       = {https://huggingface.co/datasets/ktnet-research/subjects-not-authors-evidence}
}
```
