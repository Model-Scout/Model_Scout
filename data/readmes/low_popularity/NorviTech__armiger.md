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

# Armiger v3.0 (`v3.0-gold-r5`) — 8.3 MB INT8 ONNX CPU Classifier

**Version:** `v3.0-gold-r5` · **Artifact:** `8.3 MB` (`armiger.onnx` dynamic INT8) · **CPU latency:** `2.44 ms/item` (`326 items/s` batch-64, M4 Pro CPU) · **License:** Apache-2.0

**Armiger v3 (`NorviTech/armiger`)** is the CPU-only INT8 edition of the 9-head byte-level RoPE Transformer (`8,295,882` parameters). It needs only `numpy` + `onnxruntime` and keeps **`99.90%`** parity with the 32.7 MB FP32 model. For FP32 weights and all 6 plugins (`SwarmSurvivalNet`, `SwarmPriors`, `ZeroCueCatalog`, `AudioLanguageGuard`, `CalibrationAndDHT`, `ArmigerDHTDBSync`), use [`NorviTech/armiger-ultra`](https://huggingface.co/NorviTech/armiger-ultra).

## Neural Outputs & Benchmark Summary

- **9 outputs, one CPU pass:** `category` (11-class), `adult`, `junk`/malware, `anime`, `english_subs`, spoken `lang`, `title_language`, `owner_scope`, and per-byte `span_bio` title/year/episode tags via a 7-tag Viterbi mask (`0` illegal transitions).
- **INT8 accuracy (all 3 suites):**
  - **`Suite B LOTO N=1,025`:** **`96.85%`** 6-dimension composite (`95% CI [96.33%, 97.36%]` with plugins) vs. Gemini Flash (`94.56%`), OpenAI GPT Fast Tier (`93.49%`, 5-dim; Junk N/A (Unprompted)), Claude Haiku 4.5 (`92.88%`).
  - **`W5A-Test N=703` (Rule-3 Gold):** **`97.01%`** 11-class accuracy (`95% Wilson CI [95.47%, 98.04%]`); **`96.87%`** 6-core-head exact match.
  - **`R5-Test N=996` (7-key zero-leakage):** **`91.16%`** INT8 9-class accuracy (FP32 `91.27%`; `99.90%` parity), **`99.22%`** Title Language (`n=511`), **`99.09%`** English Subtitles (`n=110`), **`98.90%`** Owner Scope (`n=996`), **`90.32%`** BIO Balanced Byte Accuracy (`n=882`), **`85.84%`** all-heads exact match (`n=996`).

![Suite B LOTO Overall & 6-Dimension Comparison](https://huggingface.co/NorviTech/armiger-ultra/resolve/main/assets/fig_v3_vs_llms_1_overall_and_6dims_loto.png)

## Quickstart (Standalone CPU ONNX Runtime)

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

## Connectors & Integrations

- **Full FP32 + 6-plugin suite:** [`NorviTech/armiger-ultra`](https://huggingface.co/NorviTech/armiger-ultra)
- **Core source & evaluation harness:** [`spencernorton/armiger`](https://github.com/spencernorton/armiger) · **License:** Apache-2.0
- **Standalone sidecars for unmodified indexers** ([`spencernorton/Armiger-Connectors`](https://github.com/spencernorton/Armiger-Connectors)):
  - **Stock Bitmagnet (`bitmagnet-io/bitmagnet`):** [`bitmagnet/bitmagnet_connector.py`](https://github.com/spencernorton/Armiger-Connectors/blob/main/bitmagnet/bitmagnet_connector.py) — polls untagged torrents via GraphQL, runs vectorized Armiger inference, prunes `.exe`/`.scr`/`.lnk` malware and honeypot traps, writes `armiger-*` tags.
  - **Stock Rats Search (`librats/rats-search`):** [`rats-search/rats_search_connector.py`](https://github.com/spencernorton/Armiger-Connectors/blob/main/rats-search/rats_search_connector.py) — drop-in REST/SQLite sidecar classifier and safety filter.
- **Turnkey indexer, Torznab & `*Arr` stacks** ([`examples/` at `v2.1.3`](https://github.com/spencernorton/armiger/tree/v2.1.3/examples) · [Integration Guide](https://github.com/spencernorton/armiger/blob/v2.1.3/docs/INTEGRATION_GUIDE.md)):
  - **DH-Waypoint `processorapi/v1` plugin** ([`spencernorton/DH-Waypoint`](https://github.com/spencernorton/DH-Waypoint)): [`examples/dh-waypoint/`](https://github.com/spencernorton/armiger/tree/v2.1.3/examples/dh-waypoint) — admission (`/v1/admit`), batch (`/v1/classify`), 4-tier feedback (`/v1/feedback`).
  - **Bitmagnet pre-ingest & GraphQL bridge:** [`examples/bitmagnet/`](https://github.com/spencernorton/armiger/tree/v2.1.3/examples/bitmagnet) (`bitmagnet_armiger_bridge.py`).
  - **Torznab pre-grab proxy (`Prowlarr`/`Sonarr`/`Radarr`/`Lidarr`/`Readarr`):** [`armiger_torznab_proxy.py`](https://github.com/spencernorton/armiger/blob/v2.1.3/examples/arr-stack/armiger_torznab_proxy.py) — filters malware lures, dead swarms, and unrequested foreign-audio releases before grab.
  - **Post-import `*Arr`/qBittorrent webhook:** [`armiger_arr_webhook_receiver.py`](https://github.com/spencernorton/armiger/blob/v2.1.3/examples/arr-stack/armiger_arr_webhook_receiver.py) — `ffprobe` ground truth for local conformal calibration and opt-in anonymous BEP-44/46 updates.
