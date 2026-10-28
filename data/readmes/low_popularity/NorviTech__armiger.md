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
  - onnx
  - int8
  - cpu-inference
---

# Armiger `v3.4.0` — INT8 ONNX CPU Classifier

**Release:** [`v3.4.0`](https://github.com/spencernorton/armiger/releases/tag/v3.4.0) · **Artifact:** `17.6 MB` INT8 ONNX (`armiger.int8.onnx` / `armiger.onnx`) · **Parameters:** `8.05M` · **License:** Apache-2.0

**Armiger (`NorviTech/armiger`)** is the standalone CPU INT8 edition of the byte-level RoPE Transformer (`numpy` + `onnxruntime` only). For FP32 weights, pre-built `armiger-ultra` containers, and the 6-plugin pipeline, see [`NorviTech/armiger-ultra`](https://huggingface.co/NorviTech/armiger-ultra).

![Armiger v3.4.0 Overview](assets/armiger_overview.png)

## Quickstart

```bash
python -m pip install "armiger @ git+https://github.com/spencernorton/armiger.git@v3.4.0"
python -m armiger download --directory ./models-cpu --variant cpu
```

```python
from armiger import ArmigerStandaloneONNX

model = ArmigerStandaloneONNX(
    onnx_path="./models-cpu/armiger.int8.onnx",
    vocab_path="./models-cpu/vocab.json",
    calibration_path="./models-cpu/calibration.json",
)
res = model.predict({
    "name": "Tears.of.Steel.2012.1080p.BluRay.x264-OPEN",
    "size": 8_500_000_000,
    "files": [{"path": "Tears.of.Steel.2012.mkv", "size": 8_500_000_000}],
})
print(res["heads"]["category"], res["matching_identity"], res["mondrian_gates"]["passed_all"])
```

## Links & Ecosystem

- **Full FP32 + 6-Plugin Suite:** [`NorviTech/armiger-ultra`](https://huggingface.co/NorviTech/armiger-ultra)
- **Core Package, Containers & Evaluation (`v3.4.0`):** [`spencernorton/armiger`](https://github.com/spencernorton/armiger) (`ghcr.io/spencernorton/armiger-ultra:3.4.0`)
- **Indexer Sidecars (Bitmagnet, Rats Search, `*Arr` Torznab):** [`spencernorton/Armiger-Connectors`](https://github.com/spencernorton/Armiger-Connectors)
- **DH-Waypoint DHT Crawler & Indexer:** [`spencernorton/DH-Waypoint`](https://github.com/spencernorton/DH-Waypoint)
