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

# Armiger Ultra `v3.2.1` (Model Bundle `v3.0.0` / `v3.0-gold-r5`) — Full Multi-Task Neural & Plugin Suite

**Release:** [`v3.2.1`](https://github.com/spencernorton/armiger/releases/tag/v3.2.1) · **Model Version:** `3.0.0` (`v3.0-gold-r5`) · **Weights:** `32.5 MB` FP32 ONNX / PyTorch + `15.7 MB` INT8 ONNX · **Parameters:** `8,295,882` · **License:** Apache-2.0

**Armiger Ultra** is a 9-head byte-level RoPE Transformer (`d=256`, `6` layers, `8` heads) with a 6-plugin pipeline for raw BitTorrent/DHT metadata (`name`, file-tree `paths` + `sizes`, optional tracker/DHT counters). Batched GPU latency is **0.21 ms/item** (`0.29 ms` on M4 Pro MPS). Library and container release **`3.2.1`** uses model bundle **`3.0.0`** (`NorviTech/armiger-ultra` pinned in [`src/armiger/model_manifest.json`](https://github.com/spencernorton/armiger/blob/main/src/armiger/model_manifest.json)). All 6 plugins ship in this repo via `ArmigerUltraPipeline`.

## Architecture & Bundled Capabilities

- **9 simultaneous heads (`armiger_ultra.fp32.onnx` & `armiger.int8.onnx`):** `category` (11-class), `adult`, `junk`/malware, `anime`, `english_subs`, spoken `lang` (3-class + 8-class audio guard), `title_language` (`english_title` vs `non_english_title`), `owner_scope` policy gate, and per-byte `span_bio` (`O`, `B-TITLE`, `I-TITLE`, `B-YEAR`, `I-YEAR`, `B-EP`, `I-EP`) via a constrained 7-tag Viterbi mask (`0` illegal transitions).
- **Bundled 6-plugin suite (`ArmigerUltraPipeline`):**
  1. **SwarmSurvivalNet (`swarm_survival.py` + `swarm_adapter.pt`):** 60-feature log1p-normalized residual MLP for swarm liveliness (`92.42%` AUROC on Public Tracker `N=757`; `96.83%` AUROC on Multi-Source `N=10,278`).
  2. **SwarmPriors (`swarm_priors.py`):** 4-pathway Empirical Bayes tracker/DHT peer-seeder priors; 50% modality dropout for zero-seed resilience.
  3. **ZeroCueCatalog (`zero_cue_plugin.py` + `validated_zero_cue_catalog.json`):** 929,400-title BLAKE2b-64 offline catalog (`26.0 MB`) for zero-cue disambiguation (`+23.86 pp` on `N=345` zero-cue titles).
  4. **AudioLanguageGuard (`audio_language_guard.py`):** Audio/subtitle-trap guard (`VOSTFR`/`VOSE`/`Eng.Sub` foreign audio vs. true English dubs).
  5. **CalibrationAndDHT (`calibration_and_dht.py` + `calibration.json`):** Per-head temperature scaling (`ECE = 1.93%` title language, `1.09%` owner scope); Mondrian conformal gates (`adult >= 0.5451`, `junk >= 0.1010`, `owner_scope >= 0.4770`).
  6. **ArmigerDHTDBSync (`armiger_dht_db_sync.py` + `csam_guard.py`):** Opt-in BEP-44/46 DHT sync and pre-ingestion CSAM filter (`opt_in_sharing=False` by default).

## Benchmark Verification (`Suite B LOTO`, `W5A-Test`, & `R5-Test`)

- **`Suite B LOTO N=1,025` — Non-Circular Leave-One-Teacher-Out:** Scored against held-out 2-of-3 teacher consensus (each LLM vs. the *other* teachers). Armiger Ultra v3: **`96.86%`** 6-dimension composite (`95% CI [96.35%, 97.38%]`; INT8 `96.85%`), ahead of Gemini Flash (`94.56%`), OpenAI GPT Fast Tier (`93.49%`, 5-dim; Junk N/A (Unprompted)), Claude Haiku 4.5 (`92.88%`), and Local 8B Instruct (`84.79%`). Junk/Malware (`N=977`, `65` positives): **`99.23%`** Balanced Accuracy (`64/65` caught).
- **`W5A-Test N=703` — Rule-3 Gold holdout:** **`97.01%`** 11-class accuracy (`95% Wilson CI [95.47%, 98.04%]`, `93.06%` Balanced Accuracy); **`96.87%`** 6-core-head exact match (`681/703`).
- **`R5-Test N=996` — 7-key zero-leakage holdout (`snap_wave13_r5_20261021`):** No cross-split leakage on `infohash`, `norm_name`, `work_id`, `imdb_id`, `CleanTitle+Year`, `FileTreeSig`, `BytePrefix64`. FP32 **`91.27%`** / INT8 **`91.16%`** 9-class accuracy (`86.27%` BalAcc), **`99.22%`** Title Language (`n=511`), **`99.09%`** English Subtitles (`n=110`), **`98.90%`** Owner Scope (`n=996`, `99.13%` BalAcc), **`95.82%`** Anime (`n=239`, `86.84%` BalAcc), **`84.49%`** 8-class Audio (`n=303`), **`90.34%`** BIO Balanced Byte Accuracy (`n=882`, `59.18%` exact span, `0` illegal transitions).

![Suite B LOTO Overall & 6-Dimension Comparison](assets/fig_v3_vs_llms_1_overall_and_6dims_loto.png)

![Armiger Ultra vs. Regular Armiger Performance Differences](assets/fig_v3_ultra_vs_base_armiger_diff.png)

## Quickstart (Docker Compose or Python SDK `v3.2.1`)

### Option A — Ready-made Docker Compose stacks (`v3.2.1`, no build or Python install needed)

Save as `compose.yaml` and run `docker compose up -d` (Docker Compose 2.34+):

- **[Bitmagnet + Armiger Ultra](https://github.com/spencernorton/armiger/blob/main/examples/bitmagnet/README.md):**
  ```yaml
  include:
    - oci://ghcr.io/spencernorton/armiger-bitmagnet-stack:3.2.1
  ```
- **[Rats Search + Armiger Ultra](https://github.com/spencernorton/armiger/blob/main/examples/rats-search/README.md):**
  ```yaml
  include:
    - oci://ghcr.io/spencernorton/armiger-rats-search-stack:3.2.1
  ```
- **[Standalone Armiger Ultra HTTP service (`ghcr.io/spencernorton/armiger:3.2.1`)](https://github.com/spencernorton/armiger/blob/main/docs/quickstart.md)**

### Option B — Python package (`v3.2.1`) with verified model download

```bash
python -m pip install "armiger[ultra] @ git+https://github.com/spencernorton/armiger.git@v3.2.1"
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

*(If running directly inside a checkout of this Hugging Face repository, `from armiger_ultra_pipeline import ArmigerUltraPipeline` is also supported as a flat-import alias.)*

## Connectors & Integrations

- **Lightweight CPU model (`15.7 MB` INT8 only):** [`NorviTech/armiger`](https://huggingface.co/NorviTech/armiger)
- **Core package, containers & evaluation harness (`v3.2.1`):** [`spencernorton/armiger`](https://github.com/spencernorton/armiger) · **License:** Apache-2.0
  - [Bitmagnet + Armiger Ultra Setup](https://github.com/spencernorton/armiger/blob/main/examples/bitmagnet/README.md) · [Bitmagnet Environment-Variable Reference](https://github.com/spencernorton/armiger/blob/main/docs/bitmagnet-configuration.md)
  - [Rats Search + Armiger Ultra Setup](https://github.com/spencernorton/armiger/blob/main/examples/rats-search/README.md)
  - [Standalone Container Quickstart](https://github.com/spencernorton/armiger/blob/main/docs/quickstart.md) · [Python API & Component Reference](https://github.com/spencernorton/armiger/blob/main/docs/reference.md) · [Evaluation & Limitations](https://github.com/spencernorton/armiger/blob/main/docs/evaluation.md)
- **Standalone sidecars for unmodified indexers (`v1.1.1`):** [`spencernorton/Armiger-Connectors`](https://github.com/spencernorton/Armiger-Connectors)
  - **Stock Bitmagnet (`bitmagnet-io/bitmagnet`):** [`bitmagnet/bitmagnet_connector.py`](https://github.com/spencernorton/Armiger-Connectors/blob/main/bitmagnet/bitmagnet_connector.py) — polls untagged torrents via GraphQL, runs vectorized Armiger inference, prunes `.exe`/`.scr`/`.lnk` malware and honeypot traps, writes `armiger-*` tags.
  - **Stock Rats Search (`librats/rats-search`):** [`rats-search/rats_search_connector.py`](https://github.com/spencernorton/Armiger-Connectors/blob/main/rats-search/rats_search_connector.py) — drop-in REST/SQLite sidecar classifier and safety filter.
  - **DH-Waypoint `processorapi/v1` plugin** ([`spencernorton/DH-Waypoint`](https://github.com/spencernorton/DH-Waypoint)): [`dh-waypoint/`](https://github.com/spencernorton/Armiger-Connectors/tree/main/dh-waypoint) — admission (`/v1/admit`), batch (`/v1/classify`), 4-tier feedback (`/v1/feedback`).
  - **Torznab pre-grab proxy (`Prowlarr`/`Sonarr`/`Radarr`/`Lidarr`/`Readarr`):** [`arr-stack/armiger_torznab_proxy.py`](https://github.com/spencernorton/Armiger-Connectors/blob/main/arr-stack/armiger_torznab_proxy.py) — filters malware lures, dead swarms, and unrequested foreign-audio releases from Torznab XML before grab.
  - **Post-import `*Arr`/qBittorrent webhook:** [`arr-stack/armiger_arr_webhook_receiver.py`](https://github.com/spencernorton/Armiger-Connectors/blob/main/arr-stack/armiger_arr_webhook_receiver.py) — `ffprobe` ground truth for local conformal calibration and opt-in anonymous BEP-44/46 updates.
