---
license: cc-by-4.0
pretty_name: Synthetic Bedroom Layouts (ABO furniture)
task_categories:
  - other
language:
  - en
  - ko
size_categories:
  - 1K<n<10K
viewer: false
tags:
  - indoor-scene-synthesis
  - layout
  - 3d
  - synthetic
---

# Synthetic Bedroom Layouts

4,000 procedurally composed bedroom layouts with 27,025 furniture placements,
in the box format used by indoor scene-synthesis models (ATISS-style `boxes.npz`).
Furniture is drawn from **Amazon Berkeley Objects** (CC BY 4.0), so the whole
dataset is redistributable and usable commercially.

**Nothing here derives from 3D-FRONT, 3D-FUTURE, or any dataset that restricts
redistribution.** Where the numbers came from is written out, value by value, in
[`PROVENANCE.md`](PROVENANCE.md).

## What makes this different

Free indoor-layout data exists — ProcTHOR-10K (Apache-2.0) is the obvious
alternative and is larger. This dataset is narrower and differs in four ways:

- **Every layout is physically checked.** No overlapping boxes, nothing through
  the floor, nothing outside the room, nothing floating, every item reachable
  from the door, nothing blocking the door swing, no window blocked by tall
  furniture within 60 cm of its wall. Zero violations across all 4,000 rooms.
  Six of these checks have a regression test that feeds them input that should
  fail; one does not yet, and that gap is listed below.
- **Clearances are continuous, not snapped.** Gaps between furniture and walls
  are sampled from a distribution rather than set to a constant. A constant puts
  a point mass in the training distribution, which an autoregressive model learns
  as a delta — any jitter in its output then crosses the boundary. `check_sc1.py`
  fails the dataset if more than 5% of gaps land in one 0.1 mm bin.
- **Real product meshes, fetched not bundled.** 304 distinct ABO models appear across
  the 4,000 rooms, each baked to a single material. `asset_licences.csv` covers
  the full licensed pool of 523, including classes this release never emits.
  Models are admitted by shape **and** by what the ABO catalogue says they are:
  a bar stool is not a dining chair, a table lamp is not a ceiling fixture, and a
  wall-mounted shelf is not a free-standing one. Getting that wrong is invisible to
  every geometric check and obvious in a render.
- **Clean provenance.** Every constant that shapes the data is either traceable
  to a licence-compatible source or listed as an authored choice with its reason,
  including the ones that are merely conventional (`PROVENANCE.md` §4.5).

## What is in here

| Path | Contents |
| --- | --- |
| `layouts/` | 4,000 room folders, each `boxes.npz` + `shell.npz`, plus a copy of `dataset_stats.txt` (the loader reads the one inside this folder) |
| `layouts-config/` | `split.csv` (8:1:1) and two empty filter files the ATISS loader opens by name |
| `dataset_stats.txt` | Class vocabulary, per-class counts, the prior's source stamp, and the gap values the generator actually used |
| `asset_licences.csv` | Per-asset attribution for all 523 ABO models in the pool |
| `asset_library.json` | The per-model extents the generator used — needed to reproduce the rooms |
| `PROVENANCE.md` | Where every number came from |
| `PROCTHOR_ASSESSMENT.md` | Why ProcTHOR-10K was measured and not used |
| `build_licence_table.py` | Rebuilds or verifies `asset_licences.csv` (also in `code/`) |
| `code/` | The generator, the prior builder, and every check. `preview_room.py` renders a room and must be run as `blenderproc run preview_room.py …` |
| `code/train/` | What is needed to reproduce the downstream numbers — ATISS itself must be cloned separately (non-commercial licence) |

`shell.npz` fields: `floor_*`, `ceiling_*`, `wallinner_*` (`_vertices` / `_faces`
per part), `window_count`, `windows` (one row per window: wall index 0=−z, 1=+x,
2=+z, 3=−x; centre along that wall; width), `window_sill`, `window_height`.

`boxes.npz` fields: `class_labels` (one-hot, 23 columns — 21 furniture types plus
a start and an end token; 12 of the 21 are used), `translations`, `sizes`
(half-extents), `angles` (yaw about Y), `room_layout` (256² floor mask, rows ↔ +z,
cols ↔ +x), `floor_plan_vertices` / `_faces` / `_centroid`, `jids` (ABO model ids),
`uids`, `door_centre`, `door_width`, `ceiling_height`, and four loader-convention
strings: `scene_id`, `scene_uid`, `scene_type`, `json_path`. `json_path` names a
per-scene JSON the ATISS loader expects but never opens for cached datasets; no
such file exists here.

One filename in `layouts-config/` reads `invalid_threed_front_rooms.txt`. That is
the name the ATISS loader opens, not a dependency — the file is empty (0 bytes),
and nothing in this dataset derives from 3D-FRONT. Renaming it would break the
loader.

**Rotation convention:** positions rotate as `v.dot(R)` with `+θ` (row-vector).
Getting this mirrored passes every static check and silently breaks rotation
augmentation — it cost this project a full training run to find.

## Numbers

| | |
| --- | --- |
| Rooms | 4,000 |
| Furniture placements | 27,025 |
| Classes | 12 |
| Items per room | median 6 (5–95%: 4–10) |
| Floor area | median 15.3 m² (5–95%: 8.3–23.8) |
| Distinct meshes used | 304 |
| Licensed asset pool | 523 |
| Size | 0.32 GB |

## What this dataset does not claim

- **Realism is rule-checked, not benchmarked.** There is no score here for
  "does this look like a room a person designed" — measuring that needs a
  human-designed reference, which is exactly what this project refuses to use. What
  was done instead is adversarial: rooms were rendered and inspected, defects were
  turned into rules, and the whole set was regenerated, six times over. That loop
  removed chairs stranded away from their desk (70.5% of chairs), beds you could not
  get into (8.7%), wardrobes with no room to open (19.9% of rooms), table lamps hung
  from the ceiling (84.8%), wall shelves standing on the floor (18.2%) and windowless
  bedrooms (46.4%). Each figure is the rate before the fix; each is now zero or near
  it. What survives is listed below — the rules are a floor on realism, not a
  measurement of it.
- **Some labels are looser than they look.** Classes come from ABO product names,
  filtered by shape and by catalogue type. A residual remains: a few `cabinet`
  entries are chests of drawers, and one `ceiling_lamp` model is a flush-mount
  ceiling fan. Nothing in the pool is a different kind of object from its label, but
  the fit is not always exact.
- **The asset pool is small in places.** Five single-bed models, seven shelves,
  sixteen ceiling lamps. The commonest single bed appears in roughly one room in six,
  so browsing the set you meet the same furniture repeatedly. That is ABO's bedroom
  coverage, not a sampling choice.
- **Composition is authored, and rejection reshapes it.** The prior declares what a
  room should contain; a room that cannot be built is discarded whole rather than
  quietly shipped short. About half of all attempts are discarded, so what survives
  is thinner than what was declared — desks in particular are rare in small rooms.
  `check_sc1.py` prints the gap between declared and realised instead of hiding it.
- **Bed mix is a judgment call.** 42.5% of rooms have a double bed, 57.5% a single.
  Doubles appear only in rooms meeting the UK space standard for a double bedroom
  (11.5 m², 2.75 m wide), with probability rising with area.
- **Small rooms are tight.** Furniture covers about 31% of the floor at the median,
  and in the smallest rooms the walking space left over is genuinely cramped.
- **It teaches its own procedure.** The authored choices in `PROVENANCE.md` §4
  are the dataset's character.
- **Nine classes never appear:** armchair, stool, sofa, table, dressing chair,
  dressing table, coffee table, children's cabinet, kids bed. For most of them no
  public source gave a defensible bedroom rule. Dressing table is different: five of
  the seven ABO models under that name are desks and the other two are dressers, so
  the class could not be filled honestly and was dropped.
- **Window counts are skewed by furniture.** The generator asks for 1–2 windows,
  but drops any it cannot place clear of tall furniture, so the realised counts are
  12 / 2,236 / 1,752 rooms. Windows never share the door's wall, and never sit
  behind the head of a bed.
- **All rooms are rectangular**, 7.5–25 m², at most 1.6 times as long as wide;
  1.7% have one side of exactly 6.000 m, the preprocessing cap, which puts a small
  point mass in the floor masks the model conditions on.
- **One of the seven checks has no regression test:** the floating check. The
  other six are re-verified against purpose-built failing input by the tools'
  own `--self-check`; floating was verified by hand only.
- **The 6 cm nightstand gap is not fully independent** of the licensed dataset
  this pipeline was severed from; `PROVENANCE.md` §4.3 says how.
- **No model weights are shipped.** The model used for the downstream check
  (ATISS) is under a non-commercial licence; that restriction does not touch this
  data or this code.

## Downstream check

An ATISS model is being retrained on **this** version of the data; the table that
belongs here is not published yet, and the numbers from the previous version are
deliberately not carried over — the layouts, the asset pool and the composition
rules all changed, so those figures would not describe this release.

What the earlier run established still holds as a shape of result rather than as a
number: a model trained on physically valid layouts does not thereby produce them.
Its output violated the same conditions this dataset satisfies exhaustively, in most
rooms. The reason to measure it here is to give a baseline to beat, not to argue
that the data works.

`code/check_generated.py` reproduces the measurement once you have a trained model,
and `code/train/README.md` says how to train one. The dataset's own guarantee is the
other half of that comparison — zero violations across all 4,000 rooms — and it is
verified exhaustively rather than sampled.

## Licence

**CC BY 4.0.** Attribute Amazon Berkeley Objects for the furniture meshes;
`asset_licences.csv` carries the per-asset attribution. The layouts and the code
are ours and released under the same terms.

The count bounds come from [Infinigen](https://github.com/princeton-vl/infinigen)
(BSD 3-Clause); the room-area floor comes from the UK nationally described space
standard (Open Government Licence v3.0). Neither imposes conditions on this
dataset beyond attribution.

## Reproducing it

The furniture library has to be built first, from raw ABO downloads. The meshes
are not shipped here — ABO is the canonical source and is large.

The asset pool was not built in one command — lamp classes needed a second pass
because the first left too few. Expect to iterate rather than to reproduce 523
exactly.

```bash
python build_asset_manifest.py           # ABO's own index → asset_manifest.csv
python download_assets.py --per-class 60 --out out/assets/raw
blenderproc run bake_assets.py --index out/assets/assets_index.json \
    --raw out/assets/raw --out out/assets/baked
python build_asset_library.py --baked out/assets/baked --manifest asset_manifest.csv
python build_licence_table.py --public
```

`--manifest` is not optional in practice: without the catalogue names, bar stools
enter as dining chairs and table lamps as ceiling fixtures. Every shape check
still passes; only a render shows it.

`run_all_checks.sh` runs every check. Its defaults assume the layout of the
repository it was written in, so pass the package's paths:

```bash
cd code
bash run_all_checks.sh ../layouts ../bedroom_prior.json ../asset_licences.csv
```

Two checks need things this package does not carry: **G1** needs Blender on
`PATH` (or `BLENDER` set), and **G1** and **G3b** need the baked ABO meshes. Both
report "건너뜀" (skipped) rather than failing when those are absent, so the run
exits 0 on a fresh download.

**If you only want to reproduce the shipped rooms**, the asset rebuild is not
needed — `asset_library.json` carries the per-model extents the generator used.
Run these from `code/` (the scripts import each other as siblings):

```bash
python build_bedroom_prior.py --rooms 20000 \
    --library ../asset_library.json --out ../bedroom_prior_check.json
python generate_layouts.py --rooms 4000 --out /tmp/layouts --seed 0 \
    --assets ../asset_library.json --compositions ../bedroom_prior.json
python build_room_shells.py --rooms /tmp/layouts --seed 0
```

Both the prior and the rooms come out byte-identical to the shipped ones.

Then the full path, if you want to rebuild the asset pool as well:

```bash
python build_bedroom_prior.py --rooms 20000 \
    --library out/assets/asset_library.json \
    --out out/assets/bedroom_prior.json
python generate_layouts.py --rooms 4000 --out out/layouts --seed 0 \
    --assets out/assets/asset_library.json \
    --compositions out/assets/bedroom_prior.json
python build_room_shells.py --rooms out/layouts --seed 0
bash run_all_checks.sh
```

The generator refuses to run unless the prior file states its source and licence.

## Citing

```bibtex
@misc{synthetic_bedroom_layouts_2026,
  title  = {Synthetic Bedroom Layouts (ABO furniture)},
  year   = {2026},
  note   = {Version 1.0. Procedurally composed; see PROVENANCE.md},
  url    = {https://huggingface.co/datasets/Spatial1ntelligence/synthetic-bedroom-layouts}
}
```

Please also cite Amazon Berkeley Objects for the furniture meshes.

## Version

**1.0**. Asset library, prior, layouts and shells were all built in one pass on
2026-09-09 with seed 0, so the shipped code, the shipped prior and the shipped
rooms agree. `PROVENANCE.md` records every value the generator used; regenerating
with the same seed and prior reproduces the rooms bit for bit — verified by
regenerating and comparing every array.
