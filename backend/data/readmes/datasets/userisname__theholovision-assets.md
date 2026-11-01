---
license: mit
task_categories:
- other
language:
- en
- ko
tags:
- unreal-engine
- 3d-assets
- holovision
---

# TheHolovision External Assets

Large binaries for [theholovision](https://github.com/lilyth-y/theholovision) — not stored in Git.

## Bundles

| Folder | Local path |
|--------|------------|
| `ue5-external-assets/` | `ue5-content/HumanSpirit/Assets/ExternalAssets/` |
| `metahuman-yui/` | `ue5-content/HumanSpirit/MetaHumans/MH_Yui/` (mesh imports only) |

ML models (Gemma GGUF, Piper ONNX) are downloaded from upstream Hugging Face model repos via `scripts/download-models.ps1`.

## Download

```powershell
git clone https://github.com/lilyth-y/theholovision.git
cd theholovision
.\scripts\download-assets.ps1
```
