---
language: [zh, en, ja, ru, ko, ar, pl, fr]
license: other
license_name: mixed-source-licenses
task_categories: [audio-to-audio]
tags: [speech, singing, xeus, features, experimental]
---
# XEUS L14 speech/singing features and experimental content projections

## Status / 状态
Research artifact, not a validated production SVC model. Intended initial visibility: **private**.
约 101.665 小时已选取音频对应的 XEUS L14 特征（包含留出数据）。不包含原始音频。
Features include eight languages. The v3 projection was fitted before French was added;
**French features in batch v6 were NOT used to fit the supplied v3 matrix**.

## Contents
- `data/`: lossless byte-planed NPY files in zstd level-6 compressed TAR shards.
- `manifests/`: one JSONL per batch, mapping every feature to its source audio clip.
- `weights/run_v3/`: previous evaluated experimental shared projection, a Chinese singing canonical-form W1 baseline, reference PCA and metadata.
- `weights/run_v2/`: prior version, retained for comparison.
- `reports/`: same-phoneme EER and per-layer tests, plus available evaluation records.
- `scripts/`: experimental extraction/fitting code snapshots. Several use `/content` paths and require adaptation; not a turnkey supported package.
- `provenance/statistics.json`: measured duration, clip and identity-label counts by batch/source/domain/split.
- `shards.jsonl`: generated shard contents and checksums. `PACKING_COMPLETE.json` is created only when every batch is packaged.

## Feature format and exact restoration
Each restored `.npy` is `[frames, 1024]`, little-endian float16. The encoder is
`espnet/xeus`, checkpoint `model/xeus_checkpoint_new.pth`, encoder block **14** (1-based),
without the encoder's terminal `after_norm`. Inputs are mono, resampled to 16 kHz.
Extraction used FP16 autocast, one utterance at a time, eval mode. Audio longer than
10 seconds was split into 10-second chunks and the resulting features concatenated.
**There is no explicit per-frame timestamp or chunk-boundary array**. Reconstruct
chunk timing using the extraction implementation, not simply t*20ms across all chunks.

The original NPY header is preserved; the float16 payload is rearranged into two byte
planes before archiving. This is lossless (no quantization beyond the stored FP16).
Do not load `.npy.bp` directly with numpy. Restore with:

```bash
pip install numpy zstandard
python scripts/restore_features.py --input data --output restored
```

The restoration script verifies each original NPY SHA-256. This is distinct from
manifest `sha256`, which hashes **the original encoded audio bytes**.

## Source traceability
Each manifest row has `dataset`, `language`, `domain`, `speaker`, `source`,
`seconds`, `frames`, `feature`, `split`, `sha256`; some also have `text`.
`feature` is relative to the restoration directory; `original_feature_path` records
the historical VM path. `source` identifies a dataset clip or archive member, NOT
necessarily an offset in a complete original song. Some Common Voice paths are old
cache paths; the clip basename and corresponding dataset/version identify the clip.

Batch overview:
1. GTSinger Japanese/Russian; LibriTTS-R English; AISHELL-3 Mandarin; MLS Polish.
2. M4Singer processed third-party mirror, OpenCpop excluded.
3. OpenSinger subset from CrawlSinger-OS archive (original source license retained).
4. Common Voice 18 Arabic and Zeroth-Korean.
5. Common Voice 17 Japanese/Russian.
6. Common Voice 17 French subset.

Identity labels are dataset namespaces, **not globally deduplicated natural persons**.
OpenSinger mirror exposed 76 gender/ID combinations versus 66 singers reported in
its original paper; do not advertise 76 verified distinct people. `heldout` is split
by identity label before fitting, but cross-corpus real-person overlap has not been audited.

## Weights
`W_shared_experimental_L14_r256.npy` has shape `[1024,256]`, float32. Inference:
```python
import numpy as np
x = np.load('restored/features_v1/example.npy').astype(np.float32)
w = np.load('weights/run_v3/W_shared_experimental_L14_r256.npy')
z = x @ w
```
No reference PCA or reference mean is applied at inference. **This is NOT canonical
USCF W1**: it uses local whitened SCF, PCA-reference orthogonal alignment, and shared
regression. The extra reference arrays document the fitting procedure.
`W1_Chinese_singing_baseline_L14_r256.npy` follows the original-form W1 regression,
but is only a small Chinese-singing baseline (up to 16 fitting singers), not a
multilingual final W1. A matrix fitted on L14 must not be reused on other layers.

## Evaluation and limits
The same-phoneme test used 240 English speech/singing clips from three GTSinger
identity labels absent from fitting manifests. Official phoneme boundaries were used;
references/queries were separated by song, with a separate rotating speaker for
phoneme references. This is **not a TIMIT replication** and is a small-sample probe.
Speaker EER near 50% means difficulty for this particular verifier, not absence of
all recoverable identity. Phoneme EER must also be checked. Shared projections improved
phoneme cosine discrimination in this test, but did not demonstrate clear additional
speaker removal in singing. No downstream SVC listening evaluation has been conducted.
Per-layer tests used the same small English pool, not a multilingual benchmark.
See reports for exact scores and exclusions; French is not covered by those evaluations.

## Provenance and reproducibility
Encoder code: wanchichen/espnet `ssl`, commit
`5b52d57b4f872ff7babded35316a79642e9e6c12`.
USCF reference: HSTEHSTEHSTE/uscf, commit
`784a97aeb2c1446bb285e55a56dc7513d967aa4b`.
Checkpoint compatibility adjustments are recorded in scripts: ignore disabled
`normalize_output=false`; rename positional convolution checkpoint keys to older
branch names; strict parameter loading. Equivalence to newer training implementation
has not been separately established. Data source repositories were not all pinned
to immutable revisions; source audio hashes assist matching exact clips.

## Licensing
See LICENSE_NOTES.md. Do not treat this mixed collection or the experimental weights
as MIT/CC0 or automatically commercially usable. Verify redistribution rights before
making the repository public. A private upload does not itself resolve license questions.

## v4 update (French included)
`weights/run_v4/` adds French fit identities from batch v6; heldout identities remain excluded. v3 remains unchanged and excludes French. v4 is the same experimental shared-projection method, not canonical USCF. See run_v4/fit_metadata.json, quality_report.json and phoneme_report.json for measured results; completion is not a claim of production SVC quality.
