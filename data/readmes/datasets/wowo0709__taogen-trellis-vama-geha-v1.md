---
pretty_name: TRELLIS VAMA GEHA ablation data
language:
- en
- ko
tags:
- trellis
- 3d-reconstruction
- ablation
---
# Native TRELLIS VAMA / GEHA ablation data

Public, frozen native TRELLIS SS data, TAO reframing, pretrained assets, CUDA dependency wheels and canonical evaluation targets. Source datasets and pretrained models retain their original licenses.

- Training: 26,033 objects, one view/object/epoch, 5 epochs / global batch24 /5,425 steps.
- Quick100: 60 validation +40 held-out, frozen case IDs and seeds.
- Full3473: 1,407 validation +bench2066.
- Contents: 1,014,605 files /37.1GB; 50 tar shards with per-file and archive SHA256.
- Bench conditioning: native_trellis_tao_518_margin01_v1. This is not a claim of pixel parity with the SAM3D fixed crops.
- Verified: anonymous download of pinned release.json and a143.5MB shard, archive SHA256 and all50 shard metadata hashes.
- No new fine-tuned checkpoints or experiment results are stored here. Results/checkpoints use a separate private repository.

Code: [0d8642eaf3e3445af07e80aad1d246d18d0f7242](https://github.com/churyone/tao-generation/commit/0d8642eaf3e3445af07e80aad1d246d18d0f7242), tag `taogen-ablation-20261024-v2`.

[H200 setup / commands / result sync](https://github.com/churyone/tao-generation/blob/0d8642eaf3e3445af07e80aad1d246d18d0f7242/docs/taogen_h200.md).

Pinned immutable data revision: `f7fa3582b8afcb21e1c9d0deea0c694a97af879f`. Visibility change leaves these files and hashes unchanged.
