---
license: other
license_name: kodistill-vl-noncommercial-research-v1
license_link: LICENSE
language: [ko, en]
---

# KoDistill-VL research artifacts

This repository publishes original research code, configurations, dependency lock, scientific source manifests, and unmodified student-model prediction records under noncommercial research terms.

Training images/targets, teacher answers, benchmark questions/images/gold, authentication, workstation manifests, environments, vendor packages and checkpoints are not distributed. Obtain upstream data separately under the cited source conditions. Model-generated raw outputs are predictions, not redistributed annotation fields.

Package phase: complete five-role fresh-verified package.

| Role | Complete predictions | Protocol |
|---|---:|---|
| base | 8,798 | `9442b56b14f6e152a230aa2d5fa7796438158276b50fba1f8500da73c592a225` |
| sft | 8,798 | `9442b56b14f6e152a230aa2d5fa7796438158276b50fba1f8500da73c592a225` |
| grpo | 8,798 | `9442b56b14f6e152a230aa2d5fa7796438158276b50fba1f8500da73c592a225` |
| released | 8,798 | `9442b56b14f6e152a230aa2d5fa7796438158276b50fba1f8500da73c592a225` |
| fresh_download | 8,798 | `9442b56b14f6e152a230aa2d5fa7796438158276b50fba1f8500da73c592a225` |

[Actual Markdown results](reports/KoDistill-VL-results.md) · [Detailed results](reports/KoDistill-VL-results.json) · [Code lineage](manifests/code-lineage.json) · [Data provenance](manifests/data.json).

Source archives: [original SFT](code/sft.tar.gz), [current GRPO](code/grpo.tar.gz). Each contains source/configuration/scripts/tests/pyproject/uv.lock/README/PLAN and licensing. The archived training dependency hashes equal the corresponding actual training identities. Historical SFT documents describe the original protocol; the execution amendment records later user-approved execution changes. Document-only machine-path redactions are listed in code-lineage.json.

Reproduction: unpack the selected source archive, install Python 3.12, run `uv sync --frozen`, obtain the separately licensed source data at the recorded revisions, and use the archived data/materialization and benchmark acquisition modules. Ordered sample identity manifests provide source row IDs, teachers/translators, image-family hashes and private-row checksums; they do not grant permission to redistribute the underlying corpus. See the actual report for limitations and the distinction between local research permission and public release rights.

Fresh verified model Hub revision: `21c11de428eda737894822450e743796bca807fd`; full coverage: 8,798/8,798.

## Auxiliary choice-ranking diagnostic

[Registered protocol](diagnostics/choice-ranking-protocol.json) · [Actual results](diagnostics/choice-ranking-results.json) · [Gold-free log-probability records](diagnostics/choice-ranking-records.jsonl).

This posthoc analysis was registered after primary MCQ format/truncation failures were observed. It uses a forced answer prefix and allowed-choice next-token probabilities, rather than generated answers or an official MMStar metric. It contains 12,000 separate records: two complete 1,500-question benchmarks across Base/SFT/GRPO/merged roles. It changes neither the primary 43,990 prediction records nor the model selection.
