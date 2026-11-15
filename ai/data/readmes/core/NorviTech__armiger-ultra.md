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
  - armiger
  - bittorrent
  - dht
  - media-classification
  - norvitech
  - swarm-availability
---

# Armiger Ultra — BitTorrent metadata classification and swarm estimates

**ONNX files:** 33,260,312 bytes (33.3 MB) FP32 and 17,606,362 bytes (17.6 MB) INT8.
**Architecture:** approximately 8 million parameters, byte-level RoPE transformer.
**License:** Apache-2.0. [Model release](https://github.com/spencernorton/armiger/releases/tag/v3.12.0).

Armiger Ultra combines neural metadata predictions with optional title-catalogue
matching, metadata-language rules, calibration and swarm-availability estimates.
Its classifier reads names, file lists and supplied counters. It runs on a CPU;
no GPU or paid inference API is required.

**Model bundle 3.12.0.** [Armiger Standalone](https://huggingface.co/NorviTech/armiger) provides the focused INT8 ONNX classifier. See the [Armiger software and setup](https://github.com/spencernorton/armiger) or [NorviTech model overview](https://norvitech.com/ai-models/#armiger).

## Comparison charts

**Latest published figures — provenance under review.** These archived charts retain their original model labels and scores. Their displayed values and vector-based source records still need reconciliation; they do not establish verified current-release performance. These Ultra hybrid comparisons do not measure standalone INT8 accuracy or payload safety. [Evaluation scope and source records](https://github.com/spencernorton/armiger/blob/main/docs/evaluation.md).

![Latest published Armiger Ultra comparison with cloud teacher models; provenance under review](https://huggingface.co/NorviTech/armiger-ultra/resolve/main/assets/armiger_vs_llms_overall_and_6dims.png)

Cloud teacher comparisons use separate common-support and swarm cohorts; panel-specific sample counts and metrics must remain separate.

![Latest published Armiger Ultra comparison with open-source torrent classifiers and parsers; provenance under review](https://huggingface.co/NorviTech/armiger-ultra/resolve/main/assets/armiger_vs_torrent_classifiers_6dims.png)

Classifier and parser comparisons cover separate category, catalogue, language, metadata-screening and swarm tasks. Original PNGs and recorded results are unchanged.

## Resources and performance

**ONNX file sizes are not working RAM.** The standalone ONNX interface, GitHub
Ultra package and full SDK snapshot with extra authority/policy assets are
different runtime paths. The GitHub package's INT8 Ultra option retains the
Ultra components; it is not the standalone API.

One CPU service using the complete R13.13 SDK with request-cache cleanup was
observed near 2.1 GiB whole-container memory during a 628.8-second live workload,
under a configured 4 GiB limit. This is one deployment observation, not a minimum
requirement or a measurement of every public API. See
[resources and measurement scope](https://github.com/spencernorton/armiger/blob/main/docs/resources.md).

The former `0.21 ms/item` GPU headline is withdrawn: the card did not provide
enough hardware, batch, model-identity or timing-scope evidence to reproduce it.
No current-release end-to-end CPU/GPU throughput or latency guarantee is made.

## Docker and Python

The quickstart uses software 3.12.3 with model bundle 3.12.0.
Choose the model-update channel explicitly; `off` keeps the bundled model pinned.

```bash
docker run -d --name armiger-ultra -p 127.0.0.1:8096:8096 \
  -e ARMIGER_UPDATE_CHANNEL=off \
  ghcr.io/spencernorton/armiger-ultra:3.12.3
```

For Bitmagnet or Rats Search, use the
[setup guides](https://github.com/spencernorton/armiger#choose-your-setup).
For Python, follow the [installation guide](https://github.com/spencernorton/armiger/blob/main/docs/reference.md#python-installation),
including CPU-only PyTorch on Linux when using the Ultra extra:

```bash
python -m pip install "armiger[ultra] @ git+https://github.com/spencernorton/armiger.git@v3.12.3"
python -m armiger download --directory ./models
export ARMIGER_UPDATE_CHANNEL=off
```

```python
from armiger import ArmigerUltraPipeline

pipeline = ArmigerUltraPipeline.from_directory(
    "./models", variant="ultra", rsi_mode="pull_only", opt_in_sharing=False,
)
result = pipeline.classify({
    "name": "Example.Movie.2001.1080p.WEB.x264",
    "files": [{"path": "Example.Movie.2001.mkv", "size": 1_000_000_000}],
})
print(result["category"])
```

This quickstart uses installed GitHub package code and its pinned, checksummed
data manifest. Direct use of the fuller SDK files in this Hub repository is a
separate integration; use a complete compatible snapshot rather than mixing
individual helper/config files from different revisions. Matching neural weights
alone does not establish complete policy/output parity across those paths.

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

- [Standalone INT8 model](https://huggingface.co/NorviTech/armiger)
- [GitHub package and reference](https://github.com/spencernorton/armiger)
- [Indexer connectors](https://github.com/spencernorton/Armiger-Connectors)
- [DH-Waypoint](https://github.com/spencernorton/DH-Waypoint)
