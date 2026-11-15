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
  - armiger
  - bittorrent
  - dht
  - media-classification
  - norvitech
---

# Armiger — CPU ONNX classifier for BitTorrent and DHT metadata

**Model file:** `armiger.int8.onnx`, 17,606,362 bytes (17.6 MB on disk).
**Architecture:** approximately 8 million parameters, byte-level RoPE transformer.
**License:** Apache-2.0. [Model release](https://github.com/spencernorton/armiger/releases/tag/v3.12.0).

This repository provides the CPU INT8 model. The Python example below uses the
GitHub package's `ArmigerStandaloneONNX` interface. It omits the Ultra catalogue
and swarm components. NumPy, ONNX Runtime and the package's other declared
dependencies are required; a GPU is not required.

**Model bundle 3.12.0.** [Armiger Ultra](https://huggingface.co/NorviTech/armiger-ultra) adds optional catalogue matching and swarm estimates. See the [Armiger software and setup](https://github.com/spencernorton/armiger) or [NorviTech model overview](https://norvitech.com/ai-models/#armiger).

## Comparison charts

**Latest published figures — provenance under review.** These archived charts retain their original model labels and scores. Their displayed values and vector-based source records still need reconciliation; they do not establish verified current-release performance. These Ultra hybrid comparisons do not measure standalone INT8 accuracy or payload safety. [Evaluation scope and source records](https://github.com/spencernorton/armiger/blob/main/docs/evaluation.md).

![Latest published Armiger Ultra comparison with cloud teacher models; provenance under review](https://huggingface.co/NorviTech/armiger-ultra/resolve/main/assets/armiger_vs_llms_overall_and_6dims.png)

Cloud teacher comparisons use separate common-support and swarm cohorts; panel-specific sample counts and metrics must remain separate.

![Latest published Armiger Ultra comparison with open-source torrent classifiers and parsers; provenance under review](https://huggingface.co/NorviTech/armiger-ultra/resolve/main/assets/armiger_vs_torrent_classifiers_6dims.png)

Classifier and parser comparisons cover separate category, catalogue, language, metadata-screening and swarm tasks. Original PNGs and recorded results are unchanged.

## Resources

**17.6 MB is a file size, not a RAM requirement.** Current-release standalone
working RAM is not established by the public resource evidence. Ultra and the
complete released SDK are different execution paths and can use substantially
more memory. One complete-SDK CPU service with additional policy/reference data
was observed near 2.1 GiB; that is not a measurement of this standalone API or a
universal minimum. See [resources and measurement scope](https://github.com/spencernorton/armiger/blob/main/docs/resources.md).

## Python quickstart

The quickstart uses software 3.12.3 with model bundle 3.12.0.

```bash
python -m pip install "armiger @ git+https://github.com/spencernorton/armiger.git@v3.12.3"
python -m armiger download --directory ./models-cpu --variant cpu
```

```python
from armiger import ArmigerStandaloneONNX

model = ArmigerStandaloneONNX(
    onnx_path="./models-cpu/armiger.int8.onnx",
    vocab_path="./models-cpu/vocab.json",
    calibration_path="./models-cpu/calibration.json",
)
result = model.predict({
    "name": "Example.Movie.2001.1080p.WEB.x264",
    "files": [{"path": "Example.Movie.2001.mkv", "size": 1_000_000_000}],
})
print(result["heads"]["category"])
```

## Limits and evaluation status

Armiger classifies supplied metadata. Audio/subtitle, junk, adult-content and
honeypot outputs are predictions or policy flags. It does not listen to audio,
inspect media payloads, scan executable contents, certify lawful content, or
guarantee a safe or available download. Optional post-import `ffprobe` checks in
a connector are a separate operation.

Published comparison graphics are under provenance review: the displayed
3.12.0 / 2,484-item overview and its 3.0.0 / 2,835-item data receipt do not
describe the same results. The latest published comparison charts are restored
above as archival figures with that provenance limit. Detailed charts also
combine newer aggregate values with older vector-based statistical panels.
Their restored visibility does not establish current-release qualification.
Historical hybrid results
also do not establish the standalone neural path's accuracy. See
[evaluation status](https://github.com/spencernorton/armiger/blob/main/docs/evaluation.md).
No new balanced benchmark or universal accuracy, zero-leakage or safety rate is
claimed here.

Sharing is optional. Payload filtering, encryption and signatures do not by
themselves provide end-to-end anonymity or certify prediction accuracy. See the
[distributed-update and privacy limits](https://github.com/spencernorton/armiger/blob/main/docs/distributed-updates.md).

Immutable historical revisions may retain earlier descriptions. This default
model card and the linked evaluation/resource notes record the corrections;
model files and immutable revisions are unchanged.

## Links

- [FP32 weights and Ultra components](https://huggingface.co/NorviTech/armiger-ultra)
- [GitHub package and setup guides](https://github.com/spencernorton/armiger)
- [Indexer connectors](https://github.com/spencernorton/Armiger-Connectors)
- [DH-Waypoint](https://github.com/spencernorton/DH-Waypoint)
