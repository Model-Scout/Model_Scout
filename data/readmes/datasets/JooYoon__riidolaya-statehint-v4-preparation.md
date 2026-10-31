---
license: apache-2.0
language:
- ko
- en
task_categories:
- text-classification
size_categories:
- 1K<n<10K
tags:
- synthetic
- ai-authored
- ai-reviewed
- train-only
- preparation-preview
configs:
- config_name: preview001
  data_files:
  - split: train
    path: data/preview001/train.jsonl
- config_name: preview002
  data_files:
  - split: train
    path: data/preview002/train.jsonl
- config_name: preview003
  data_files:
  - split: train
    path: data/preview003/train.jsonl
- config_name: preview004
  data_files:
  - split: train
    path: data/preview004/train.jsonl
- config_name: preview005
  data_files:
  - split: train
    path: data/preview005/train.jsonl
---

# State-hint V4 preparation — preview005

**840 fictional scenario families / 1,680 Korean-English training rows / 708 declared related-case groups.**
Each of the eight intents has 105 families. These are AI-authored and label-visible,
model-blind AI-reviewed examples, not human gold or independent product observations.
Of 931 authored source families, 91 are held and their text is excluded. Six additional
reserve designs have no wording. This completes the planned training quota only.

**가상 개발 상황 840개 / 한영 학습 문장 1,680행**입니다. 8개 의도마다 105개이며,
선언 계보는 708개입니다. 별도 평가 자료 360개 상황·720행, 전체 1,200개 상황·2,400행과
새 V4 학습·평가는 아직 준비 중입니다. 실제 업무 원문은 포함하지 않습니다.

[한국어 사용법](docs/preview005/README.ko.md) · [English usage](docs/preview005/README.en.md)
· [Provenance](provenance/preview005.json) · [File hashes](manifest/preview005.sha256.json)
· [Changes](docs/preview005/CHANGES.md) · [Progress](https://github.com/teamswyg/laya-tools/issues/155#issuecomment-6020154513).

Earlier preview001–004 data, documents, manifests and tags are preserved. Preview004
is fixed at 593 families/1,186 rows in [its historical revision](https://huggingface.co/datasets/JooYoon/riidolaya-statehint-v4-preparation/tree/6fd2cd9a0e13890e758978837469d7ec4efb8cbe).
Only the root README is updated. Verify prior manifests at their historical revisions.
**Releases are cumulative. Select one; do not concatenate them.**

Apache-2.0 covers original fictional material. No upstream corpus, private content,
credentials, model weights or raw profiles are included. This is not a Laya derivative.
New V4 fit/predict and operational mutations remain **zero** at this checkpoint.
Publication does not establish useful model performance or verified task completion.
