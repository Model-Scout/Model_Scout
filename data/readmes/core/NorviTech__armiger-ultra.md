---
license: apache-2.0
library_name: onnx
pipeline_tag: text-classification
language:
  - en
  - ja
  - fr
  - de
  - es
  - it
  - ru
  - ko
  - zh
tags:
  - torrent
  - metadata-classification
  - byte-transformer
  - rope
  - onnx
  - bitmagnet
  - rats-search
---

# Armiger Ultra `v3.4.0`

**Release:** [`v3.4.0`](https://github.com/spencernorton/armiger/releases/tag/v3.4.0) · **Weights:** `33.3 MB` FP32 ONNX + `17.6 MB` INT8 ONNX · **Parameters:** `8.05M` · **License:** Apache-2.0

**Armiger Ultra** is an 8.05M-parameter multi-head byte-level RoPE Transformer (`0.21 ms/item` batched GPU) and 6-plugin pipeline for BitTorrent and DHT metadata classification, canonical title/year extraction, audio/subtitle verification, malware filtering, and swarm liveliness scoring.

![Armiger Ultra v3.4.0 Overview](assets/armiger_overview.png)

## Quickstart

### Pre-Built Docker Container & Compose Stacks (`v3.4.1`)

Library and container 3.4.1 fix connector startup permissions and use the same 3.4.0 model bundle.

Run the pre-built `armiger-ultra`:

```bash
docker run -d --name armiger-ultra -p 127.0.0.1:8096:8096 \
  -e ARMIGER_DHT_AUTO_UPDATE=true \
  ghcr.io/spencernorton/armiger-ultra:3.4.1
```

Or include a ready-made stack in `compose.yaml` (`docker compose up -d`):

```yaml
include:
  - oci://ghcr.io/spencernorton/armiger-bitmagnet-stack:3.4.1
  # or: oci://ghcr.io/spencernorton/armiger-rats-search-stack:3.4.1
```

### Python SDK

```bash
python -m pip install "armiger[ultra] @ git+https://github.com/spencernorton/armiger.git@v3.4.1"
python -m armiger download --directory ./models
```

```python
from armiger import ArmigerUltraPipeline

pipeline = ArmigerUltraPipeline.from_directory("./models", variant="ultra")
res = pipeline.classify({
    "name": "Tears.of.Steel.2012.2160p.UHD.BluRay.REMUX.HEVC.TrueHD.7.1.Atmos-OPEN",
    "size": 68_400_000_000,
    "files": [{"path": "Tears.of.Steel.2012.mkv", "size": 68_400_000_000}],
    "swarm": {"tracker_known": True, "tracker_seeders": 142, "tracker_leechers": 19, "tracker_completed": 810},
})
print(res["category"], res["mondrian_gates"]["passed_all"], res["swarm_viability"]["viability_tier"])
```

## Links & Ecosystem

- **Core Package, Containers & Evaluation (`v3.4.1`):** [`spencernorton/armiger`](https://github.com/spencernorton/armiger) ([Quickstart](https://github.com/spencernorton/armiger/blob/main/docs/quickstart.md) · [DHT Auto-Update](https://github.com/spencernorton/armiger/blob/main/docs/distributed-updates.md) · [Evaluation](https://github.com/spencernorton/armiger/blob/main/docs/evaluation.md))
- **CPU INT8 Model (`17.6 MB`):** [`NorviTech/armiger`](https://huggingface.co/NorviTech/armiger)
- **Indexer Sidecars (Bitmagnet, Rats Search, `*Arr` Torznab):** [`spencernorton/Armiger-Connectors`](https://github.com/spencernorton/Armiger-Connectors)
- **DH-Waypoint DHT Crawler & Indexer:** [`spencernorton/DH-Waypoint`](https://github.com/spencernorton/DH-Waypoint)
