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

# Armiger `v3.2.1` (Model Bundle `v3.0.0` / `v3.0-gold-r5`) — 15.7 MB INT8 ONNX CPU Classifier

**Release:** [`v3.2.1`](https://github.com/spencernorton/armiger/releases/tag/v3.2.1) · **Model Version:** `3.0.0` (`v3.0-gold-r5`) · **Artifact:** `15.7 MB` (`armiger.int8.onnx` / `armiger.onnx`, per-channel asymmetric INT8 with FP32 embeddings) · **CPU latency:** `2.44 ms/item` (`326 items/s` batch-64, M4 Pro CPU) · **License:** Apache-2.0

**Armiger (`NorviTech/armiger`)** is the CPU-only INT8 edition of the 9-head byte-level RoPE Transformer (`8,295,882` parameters). It needs only `numpy` + `onnxruntime` and keeps **`99.90%`** parity with the 32.5 MB FP32 model. Library and container release **`3.2.1`** uses model bundle **`3.0.0`**. For FP32 weights and all 6 plugins (`SwarmSurvivalNet`, `SwarmPriors`, `ZeroCueCatalog`, `AudioLanguageGuard`, `CalibrationAndDHT`, `ArmigerDHTDBSync`), use [`NorviTech/armiger-ultra`](https://huggingface.co/NorviTech/armiger-ultra).

## Neural Outputs & Benchmark Summary

- **9 outputs, one CPU pass:** `category` (11-class), `adult`, `junk`/malware, `anime`, `english_subs`, spoken `lang`, `title_language`, `owner_scope`, and per-byte `span_bio` title/year/episode tags via a 7-tag Viterbi mask (`0` illegal transitions).
- **INT8 accuracy (all 3 suites):**
  - **`Suite B LOTO N=1,025`:** **`96.85%`** 6-dimension composite (`95% CI [96.33%, 97.36%]` with plugins) vs. Gemini Flash (`94.56%`), OpenAI GPT Fast Tier (`93.49%`, 5-dim; Junk N/A (Unprompted)), Claude Haiku 4.5 (`92.88%`).
  - **`W5A-Test N=703` (Rule-3 Gold):** **`97.01%`** 11-class accuracy (`95% Wilson CI [95.47%, 98.04%]`); **`96.87%`** 6-core-head exact match.
  - **`R5-Test N=996` (7-key zero-leakage):** **`91.16%`** INT8 9-class accuracy (FP32 `91.27%`; `99.90%` parity), **`99.22%`** Title Language (`n=511`), **`99.09%`** English Subtitles (`n=110`), **`98.90%`** Owner Scope (`n=996`), **`90.32%`** BIO Balanced Byte Accuracy (`n=882`), **`85.84%`** all-heads exact match (`n=996`).

![Suite B LOTO Overall & 6-Dimension Comparison](https://huggingface.co/NorviTech/armiger-ultra/resolve/main/assets/fig_v3_vs_llms_1_overall_and_6dims_loto.png)

## Quickstart (Standalone CPU ONNX Runtime)

### Option A — Install the Python package (`v3.2.1`) with verified model download

```bash
python -m pip install "armiger @ git+https://github.com/spencernorton/armiger.git@v3.2.1"
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

### Option B — Run directly from a checkout of this Hugging Face repository

```python
from armiger_inference import ArmigerStandaloneONNX

model = ArmigerStandaloneONNX()  # auto-loads armiger.onnx, vocab.json, calibration.json
res = model.predict({
    "name": "Tears.of.Steel.2012.1080p.BluRay.x264-OPEN",
    "size": 8_500_000_000,
    "files": [{"path": "Tears.of.Steel.2012.mkv", "size": 8_500_000_000}],
})
print(res["heads"]["category"], res["matching_identity"], res["mondrian_gates"]["passed_all"])
```

## Ready-Made Docker Setups & Integrations (`v3.2.1`)

- **Full FP32 + 6-plugin suite:** [`NorviTech/armiger-ultra`](https://huggingface.co/NorviTech/armiger-ultra)
- **Core package, containers & evaluation harness (`v3.2.1`):** [`spencernorton/armiger`](https://github.com/spencernorton/armiger) · **License:** Apache-2.0
  - **[Bitmagnet + Armiger Ultra](https://github.com/spencernorton/armiger/blob/main/examples/bitmagnet/README.md):** Two-line Docker Compose setup (`include: [oci://ghcr.io/spencernorton/armiger-bitmagnet-stack:3.2.1]`) · [Environment-Variable Reference](https://github.com/spencernorton/armiger/blob/main/docs/bitmagnet-configuration.md)
  - **[Rats Search + Armiger Ultra](https://github.com/spencernorton/armiger/blob/main/examples/rats-search/README.md):** Two-line Docker Compose setup (`include: [oci://ghcr.io/spencernorton/armiger-rats-search-stack:3.2.1]`)
  - **[Standalone Armiger Ultra HTTP Container](https://github.com/spencernorton/armiger/blob/main/docs/quickstart.md):** Prebuilt multi-arch image `ghcr.io/spencernorton/armiger:3.2.1` with `/v1/classify` and `/healthz`
  - **[Python API & Component Reference](https://github.com/spencernorton/armiger/blob/main/docs/reference.md)** · **[Evaluation & Limitations](https://github.com/spencernorton/armiger/blob/main/docs/evaluation.md)**
- **Standalone sidecars & connectors (`v1.1.1`):** [`spencernorton/Armiger-Connectors`](https://github.com/spencernorton/Armiger-Connectors)
  - **Stock Bitmagnet (`bitmagnet-io/bitmagnet`):** [`bitmagnet/bitmagnet_connector.py`](https://github.com/spencernorton/Armiger-Connectors/blob/main/bitmagnet/bitmagnet_connector.py) — polls untagged torrents via GraphQL, runs vectorized Armiger inference, prunes `.exe`/`.scr`/`.lnk` malware and honeypot traps, writes `armiger-*` tags.
  - **Stock Rats Search (`librats/rats-search`):** [`rats-search/rats_search_connector.py`](https://github.com/spencernorton/Armiger-Connectors/blob/main/rats-search/rats_search_connector.py) — drop-in REST/SQLite sidecar classifier and safety filter.
  - **DH-Waypoint `processorapi/v1` plugin** ([`spencernorton/DH-Waypoint`](https://github.com/spencernorton/DH-Waypoint)): [`dh-waypoint/`](https://github.com/spencernorton/Armiger-Connectors/tree/main/dh-waypoint) — admission (`/v1/admit`), batch (`/v1/classify`), 4-tier feedback (`/v1/feedback`).
  - **Torznab pre-grab proxy (`Prowlarr`/`Sonarr`/`Radarr`/`Lidarr`/`Readarr`):** [`arr-stack/armiger_torznab_proxy.py`](https://github.com/spencernorton/Armiger-Connectors/blob/main/arr-stack/armiger_torznab_proxy.py) — filters malware lures, dead swarms, and unrequested foreign-audio releases before grab.
  - **Post-import `*Arr`/qBittorrent webhook:** [`arr-stack/armiger_arr_webhook_receiver.py`](https://github.com/spencernorton/Armiger-Connectors/blob/main/arr-stack/armiger_arr_webhook_receiver.py) — `ffprobe` ground truth for local conformal calibration and opt-in anonymous BEP-44/46 updates.
