---
task_categories:
  - object-detection
license: other
tags:
  - image
  - yolo
  - patrol
  - safety
  - fire-detection
  - smoke-detection
  - sf
pretty_name: "NXP SF Balanced Fire/Smoke Dataset"
language:
  - ko
latest_revision: v3
---

# NXP SF Balanced Fire/Smoke Dataset

이 repo는 stable dataset family repo이며 revision snapshot은 `revisions/<revision>/` 아래에 저장합니다.

- stable repo: `LK-ROBOTICS/nxp-sf-train-balanced`
- latest revision: `v3`
- current recommended path: `revisions/v3`

## Revisions

| revision | path | train | val | test | note |
|---|---|---:|---:|---:|---|
| v1 | `revisions/v1` | 8,177 | 1,361 | 1,035 | original balanced revision |
| v2 | `revisions/v2` | 9,277 | 1,493 | 1,166 | expanded source mix |
| v3 | `revisions/v3` | 9,277 | 1,493 | 1,166 | cleaned labels (dedup + polygon->bbox) |
