---
language:
- en
- ko
task_categories:
- robotics
---
# LIBERO binary compression labels (contact overrides)

266,693 labels, 1,693 episodes, 40 tasks. Derived from the existing
[LIBERO confidence release](https://huggingface.co/datasets/prehj/libero-ratio-labels-contact).
No new VLM inference or policy evaluation was performed.

- `conf` is the original stored score, unchanged: weighted expected-grade support
  minus risk, mapped to [0,1]. It is NOT a success probability.
- `compress_2p5 = int(conf > 0.50)`; `compress_3 = int(conf > 0.55)`.
- These are initial heuristic thresholds, NOT calibrated from naive success rates.
  They do not impose per-task quotas or task ceilings. 3x implies 2.5x by construction.
- Contact policy: legacy fixed: contact transition guard plus action-proxy fallback. If active, both outputs become zero.
- `compress_valid=1` on labeled rows. 1 means compress, 0 means keep original speed.
  The columns represent separate binary targets; they are not a multiclass speed selector.
- `source_ratio` and `source_fixed` are historical provenance, NOT new supervision.
  No-contact retains contact metadata for auditing but never uses it in the targets.
- A..E, eg_A..E, gp_A..E are preserved. Probabilities are conditional over grades 1..5.

## Match to the dataset

Use the unchanged `kimtaey/libero_gr00t_delta` base. Join exactly on
`(episode_index, frame_index)`, not task name or parquet row order alone.
Last four frames per episode are unlabeled; the apply script preserves all original
rows and sets their validity to zero. Never train these tails as negative examples.
The script validates all episode lengths/instructions, exact keys and label checksum.

```bash
pip install numpy pyarrow
python apply_to_dataset.py --dataset /data/libero_gr00t_delta --dry-run
python apply_to_dataset.py --dataset /data/libero_gr00t_delta --out /data/libero_binary_sidecar
# Alternatively copy original parquets, preserving existing columns:
python apply_to_dataset.py --dataset /data/libero_gr00t_delta --mode dataset --out /data/libero_binary
```

The default sidecar contains one parquet per original episode. Dataset mode copies
original embedded-image parquets. Two optional `[binary_class, valid]` float32
carriers are `compress_2p5_label` and `compress_3_label`. A model/data configuration
must explicitly consume the selected binary target and validity; columns alone do
not configure a training loss. Carrier fields are not robot action dimensions.
Full join: 273,465 frames, 266,693 valid labels, 6,772 masked tail frames.

## Change thresholds later without VLM inference

```python
import pandas as pd
d = pd.read_parquet("labels/libero_training.parquet")
d["compress_2p5"] = ((d.conf > 0.50) & (d.contact_override == 0)).astype("int8")
d["compress_3"] = ((d.conf > 0.55) & (d.contact_override == 0)).astype("int8")
```

For a new package, update thresholds and the parquet SHA256 in `label_policy.json`;
the apply script intentionally rejects a file changed without updating its manifest.
Current positive counts: {"compress_2p5": 95431, "compress_3": 76807}.
