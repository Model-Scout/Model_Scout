---
license: other
license_name: fourier-actionnet-terms
license_link: https://huggingface.co/datasets/FourierIntelligence/ActionNet
task_categories:
- robotics
tags:
- robotics
- humanoid
- gr1
- video-generation
- data-filtering
- ground-truth-depth
language:
- ko
- en
size_categories:
- n<1K
configs:
- config_name: manifest
  data_files: manifest.csv
---

# synth100 — 100 generated clips for validating Pre-Contact Level Filtering

100 episodes drawn (seed 20260824) from the 952-episode multi-object generation set, packaged so
Stage-5 filtering can be run on them without re-deriving anything. Every input the filter needs
travels with the package, in the space it is consumed in.

**Read section 1 before using this.** The single most important fact about this data is not in the
file layout, and getting it wrong invalidates any score computed from it.

---

## 0. Attribution and license

**Part of this package is a third-party dataset.** Read this before using it.

| | |
|---|---|
| Upstream capture | [FourierIntelligence/ActionNet](https://huggingface.co/datasets/FourierIntelligence/ActionNet) (Fourier Intelligence). Robot: Fourier GR1-T1, 6-DoF Fourier DexHands, one head-mounted camera |
| ActionNet-derived, redistributed here | `conditioning/`, `conditioning_undist/`, `real_video/` (real frames and episodes), `gtdepth/` (the release's own sensor depth, undistorted and downsampled), `s0.npz`, and the `prompt_actionnet_real` / `task_actionnet` columns |
| Upstream terms govern that payload | Whatever the upstream repository states. **If they disallow redistribution, tell us and this comes down.** |
| Ours (CC-BY-4.0) | `generated/` (our I2V generators' output), `actions/` (IDM read-out), `instruction_generated/`, all four mask resolutions, `pre_*/`, `pre2_*/`, `occ_*/`, `sphere/`, `gallery2/`, `manifest.csv`, `camera.json`, and this document |

A fuller treatment of the capture itself -- what the depth is, the two-clock alignment bug, the
fisheye-vs-pinhole mask warning -- is in the companion card,
[`glory-hyeok/actionnet-subset100-gtdepth`](https://huggingface.co/datasets/glory-hyeok/actionnet-subset100-gtdepth).
That card is the reference for the capture; this one is about what we generated from it.

---

## 1. The instruction is counterfactual — this is not a reproduction task

The generator was **not** asked to reproduce the source episode. It was given the episode's real
first frame and told to fetch a **different object**:

| | |
|---|---|
| what the real video shows | *"Pick up the donut and put it on the third shelf"* |
| what the generator was told | *"…pick up the target **plastic cup** and put it in the plastic basket"* |

**91 of the 100** name a target the real episode never touches. Three consequences, all of which
change how a number computed here should be read:

1. **Judge against `instruction_generated/`, never against `prompt_actionnet_real`.** The latter is
   provenance only — it says which episode the conditioning frame came from.
2. **`real_video/` is not ground truth.** Its arm goes to a different object. It is not an upper
   bound on anything.
3. **`real_video/` is therefore a negative control**, and a good one: same scene, same conditioning
   frame, an arm that genuinely moves and grasps — just not the instructed object. Harder than the
   idle-hand control used on the real set, which never moves at all.

---

## 2. Layout

```
manifest.csv                 ulid · instruction_generated · target_object · destination ·
                             prompt_actionnet_real · task_actionnet · s0_source · n_action
s0.npz                       ulids (100) + s0 (100, 44)          the robot at the conditioning frame
camera.json                  K_pinhole · K_fisheye · D · space definition

conditioning/<U>.png         real conditioning frame, 1280x800, FISHEYE, lossless
conditioning_undist/<U>.png  the same frame, 1280x800, UNDISTORTED PINHOLE   <- estimate depth here
real_video/<U>.mp4           the full real episode, 1280x800 fisheye, 30 fps  (negative control)

mask/<U>_{target,source}.png       1280x800 FISHEYE      as delivered
mask_undist/<U>_{target,source}.png 1280x800 PINHOLE     for the 3-D lift
mask_768/<U>_{target,source}.png    768x432              for occlusion on the generated clip

generated/{mot,diffonly,block18}/<U>.mp4   768x432, 16 fps, 93 frames
actions/{mot,diffonly,block18}/<U>.npz     action (93,44) + timestamp, from the IDM

gtdepth/depth_<U>.npz        GROUND-TRUTH depth at the conditioning frame, from the sensor:
                             depth (1,400,640) float32 metres, ds=2, K_ds, frame_indices
instruction_generated/<U>.txt  the counterfactual instruction, verbatim, one per clip

pre_{mot,diffonly,block18}/pre_<U>.json    Pre-Contact result: entry frame, sphere centre and
                                           radius, per-frame tip_{L,R}_cm
occ_{mot,diffonly,block18}/occ_<method>_0.json   Occlusion result: peak over the +-1 s window
sphere/<method>_<U>_web.mp4      Pre-Contact video   (10 sampled clips)
gallery2/<method>_<U>_web.mp4    Occlusion video     (the same 10)
```

`gtdepth/` is the sensor's own depth, extracted from the public ActionNet release with
`synth_gtdepth_npz.py` through the SAME undistort maps as the masks. It is here so a depth
model can be scored against it -- at inference the filter is meant to run on a predicted map
from `conditioning_undist/` alone. All 100 verified: object-region validity median 100 %,
minimum 61.5 %; object distance 0.46-0.94 m.

`target` is the object to fetch, `source` is the acting arm. Both are frame-0 masks.

---

## 3. Three spaces, and which one each thing lives in

| space | what is in it | K |
|---|---|---|
| fisheye 1280x800 | `conditioning/`, `real_video/`, `mask/` | 127° equidistant, f 577.47 |
| **pinhole 1280x800** | `conditioning_undist/`, `mask_undist/`, **depth belongs here** | `[[640,0,639.5],[0,640,399.5]]` |
| 768x432 | `generated/`, `mask_768/` | fx 384, **fy 345.6** — see below |

**Depth must be estimated on `conditioning_undist/`, not on the fisheye frame.** `P = D·K⁻¹p` with a
pinhole K over fisheye pixels bends a flat table into a bowl.

**768x432 is an anisotropic resize of the fisheye frame, not a crop.** Solved by matching the same
frame in both resolutions (correlation 0.997) and confirmed against the generator's own dataloader:
`F.resize(frame, (432,768), antialias=True)`. Horizontal scale 0.600, vertical 0.540 — pixels are
not square, so **do no geometry at 768x432**. Occlusion is a ratio of two masks that both went
through the same resize, so it is unaffected. `mask_768` is produced the way the generator produces
it: `TF.interpolate(mask/255, (432,768), mode="area") > 0.5`, not nearest-neighbour.

---

## 4. The IDM actions: units and sign

`actions/` holds what an inverse-dynamics model read out of the generated pixels. Same 44-channel
layout as our states (left_arm 0-7, left_hand 7-13, left_leg 13-19, neck 19-22, right_arm 22-29,
right_hand 29-35, right_leg 35-41, waist 41-44), and the **body** channels are radians on both
sides. The **hand** channels are not:

| | our 44-D state (`s0.npz`) | IDM action |
|---|---|---|
| units | Fourier raw, 0–10.3 | **radians** |
| closing | negative in this URDF | **positive** |
| the exception | thumb pitch, whose range is reversed | thumb pitch, same sign |

Feeding IDM hand values through the Fourier conversion puts the fingers at nonsense angles, and
mixing the two in a rollout (`q + α(a − q)`) is arithmetic across unit systems. Use
`fk.rollout_from_idm_actions`, which brings both into radians first. Confirmed physically: the
values start near 0, rise to 0.8–1.7 mid-clip and return — a hand opening, closing on the object,
and letting go.

The clip is **16 fps**, so a ±1 s window is **±16 frames**, not ±30. The rollout coefficient needs
no adjustment for that: the same episode rolled at 15 and 16 Hz differs by 0.03°, against the
rollout's own 0.46° error.

The acting arm is named in the instruction (*"the source **right** robot arm"*) — 74 right, 26 left
— so it need not be inferred.

---

## 5. Where s₀ came from, and why row 0 is safe

`observation.state[0]` of the matching LeRobot episode. The ActionNet→LeRobot conversion pairs a
60 Hz robot sample with a 30 fps camera frame, so indexing states by frame number is wrong by up to
9 cm at the moving arm — but **not at frame 0**, where both conventions coincide. Checked against
our own hdf5-resampled states on the 6 episodes present in both sets: **body joints agree to 1e-4
rad**; only a thumb channel differs, by 2.7 % of its raw range.

5 of the 952 have no recoverable s₀ and were excluded before sampling.

---

## 6. What this data is harder than the real set at

| | real 100 (croissants) | here |
|---|---|---|
| distinct prompts | 3 | 91 |
| target mask, median | 11 844 px | **2 414 px** |
| boundary sphere | 8.2 cm | **6.23 cm measured** (≈3.7 cm expected — see §7) |
| clip | ~400 frames @ 30 fps | 93 @ 16 |

The targets are blocks, cubes and cups — 0.45x the croissants in linear size. Any tolerance measured
on the real set (depth scale error, rollout offsets) is **looser than what is needed here** and has
to be re-derived. The rollout offsets' largest arm term is 4.29°, about 6 cm at the fingertip, which
now exceeds the sphere itself.

---

## 7. Known limitation: the boundary sphere is inflated, and why the real set never showed it

Measured on all 100 with GT depth, the sphere's median radius is **6.23 cm** against the ~3.7 cm the
objects' size predicts, and **16 of 100 exceed 10 cm** -- larger than the croissant sphere on the
real set, for objects less than half the size.

Splitting the clips by how far the depth spreads over the target mask shows what is moving:

| depth spread (1-99 pct) | clips | x | y | z | sphere |
|---|---|---|---|---|---|
| <= 5 cm | 14 | 5.8 | 5.0 | **3.2** | **4.02 cm** |
| 5-10 cm | 43 | 6.5 | 6.2 | 5.8 | 5.64 cm |
| 10-15 cm | 22 | 7.5 | 7.2 | 8.6 | 7.21 cm |
| > 15 cm | 21 | 9.3 | 6.6 | **15.2** | 11.46 cm |

Width and height barely move; depth runs 3.2 -> 15.2 cm, a factor of 4.75. One class of object
cannot keep its width and quintuple its thickness, so what varies is the measurement, not the
object. The clean group's 4.02 cm also lands on the ~3.7 cm predicted independently from object
size -- that is the real number.

**Why the real set never showed this.** The same border leak is present there. Two things hid it:

1. *The croissant is large and anisotropic.* Its AABB is 13.1 x 7.0 x 7.1 cm -- a genuine 13 cm
   object, whose longest axis is real and dominates the half-diagonal (depth is 43 % of it). The
   block is 5.8 x 5.0 x 3.2 -- nearly isotropic, and **depth is its shortest true axis**, so it has
   the most room to be corrupted and takes over the diagonal the moment it is. Adding 5 cm of leak
   to z grows the croissant sphere 24 % and the block sphere 42 %.
2. *The scene.* Every real episode has `n_obj = 1`, and the mask is ours -- SAM 3 text prompt,
   largest component, area band. A leak has only the tablecloth to land on, at nearly the
   croissant's own depth. Here the scene is multi-object, the masks ship with the clips, and
   **91 of 100 have two or more connected components**. A leak lands on a neighbouring object at a
   different distance, which is exactly a large jump in z.

**The direction is permissive.** A bigger sphere is entered earlier, so an entry that should not
have counted does. Entry counts from this package are an upper bound on the affected clips.

Fitting the depth band around the median instead of by percentile suppresses the tail
(same 100 clips, sphere radius):

| z selection | median | > 10 cm | max |
|---|---|---|---|
| 5-95 percentile *(what produced the numbers here)* | 6.09 cm | 15 | 26.1 cm |
| median +- 3 MAD | 5.30 cm | 10 | 17.2 cm |
| **median +- 6 cm (fixed band)** | 5.77 cm | **3** | **13.2 cm** |
| mask eroded 2 px, percentile trim | 5.30 cm | 11 | 24.4 cm |

The fixed band is a prior on object depth extent rather than a measurement, so it is recorded here
and not yet applied -- changing it moves the gate, and the gate is being settled against human
labels.

One thing this table already rules out: **the stray mask components are not the cause.** 91 of the
100 target masks carry more than one connected component (up to 30), which looks like the obvious
culprit -- but the extra components are specks, the largest holds 99.8 % of the area at the median,
and tracing the far-depth pixels puts **0 % of them in the specks against 73 % on the main blob's
rim**. Keeping only the largest component moves the median 6.09 -> 5.90 cm and the tail 15 -> 13
clips: worth doing as hygiene, since the real set's masks are built that way, but it is not the fix.
The leak is a border-bleed on the object's own blob, and only the depth selection reaches it.

---

## 8. How to apply Pre-Contact filtering to these clips

The criterion is the one applied to real episodes in
[`glory-hyeok/actionnet-subset100-gtdepth`](https://huggingface.co/datasets/glory-hyeok/actionnet-subset100-gtdepth),
whose card carries the full recipe. **Read that first**; this section is only the four places the
generated set differs, and each of them is a place to get it wrong.

### 8.1 The action stream is predicted, and its hand channels are not the real set's units

There, the rollout integrates the dataset's recorded actions. Here it integrates what an inverse
dynamics model read out of the generated pixels -- which is the whole point: the actions are the
only thing the generation can influence, so this half of the filter looks at the generation through
them and never at the rendering.

The rollout model is identical (`beta = 0`, `alpha = 0.45` body / `0.60` hand), and so are both
offset layers. What is **not** identical is the hand:

| | real set | here |
|---|---|---|
| hand channels | DexHand raw, `[0, 10.3]` | **radians**, with their own sign |
| sign | as recorded | `[-1, -1, -1, -1, +1, -1]` over the 6 slots -- thumb pitch is the one slot that agrees |

So the hand cannot go through the same conversion. Feeding the raw mixture subtracts radians from
DexHand units, and any clamp written for `[0, 10.3]` then flattens **every closing finger to zero** --
silently, with a trajectory that still looks plausible. If you reuse a rollout routine from the real
path, check its hand clamp is unit-aware before trusting a single number.

A convention check that needs no unit knowledge: the fingertips should **converge** at the entry
frame. They do, by 2.57 cm in 19 of 20 clips -- the geometric event and the grasp coincide, from two
signals that share no code.

### 8.2 The clock is 16 fps, so +-1 s is +-16 frames

Not 30. `actions/<method>/<U>.npz` holds 93 actions per clip, the clip holds 93 frames, and
`rollout[t]` corresponds to **video frame `t`** (`rollout[0]` is s0, the conditioning frame). The
rollout is one sample longer than the video; that last sample has no pixel and should be ignored.

### 8.3 Two spaces, and only an integer crosses between them

| | space | why |
|---|---|---|
| **Pre-Contact** | 1280x800 pinhole (`conditioning_undist/`, `mask_undist/`, `gtdepth/`) | K and the extrinsic are calibrated there, and it is where the object is lifted. No fisheye model, no anisotropic resize. |
| **Occlusion** | 768x432 (`generated/`, `mask_768/`) | the arm mask has to come out of the generated frames, and that is their resolution |

The only thing that crosses is **the entry frame number**. Nothing is unprojected on the Occlusion
side, so the anisotropic resize costs nothing there -- the score is a ratio of two masks that both
went through it.

**Do not score Pre-Contact at 768x432.** `mask_768` is an anisotropic resize of the *fisheye* frame
(`scale_x 0.600`, `scale_y 0.540` -- pixels are not square), and a pinhole `K` applied to fisheye
pixels bends a flat table into a bowl. If you want to *draw* the boundary on a clip, project through
the fisheye model at 1280x800 first and only then apply the two scales; and draw an **ellipse**, not
a circle -- `f*r/z` is a pinhole identity, and through this chain it comes out 4 % too wide and 17 %
too tall.

### 8.4 The Occlusion arm mask is seeded from a shipped mask, not from geometry

`mask_768/<U>_source.png` is the acting arm at frame 0 (`_target` is the object). Seed the tracker
from it -- erode first, so a one-pixel error does not pick the tablecloth -- and track forward from
frame 0 through the window. On the real set the seed came from FK points projected out of the state,
so this also removes the last place the pixel half leaned on the geometry it is meant to corroborate.

The score and the window are unchanged: `max` over the +-16 frames of
`|arm ∩ object_at_frame_0| / |object_at_frame_0|`.

### 8.5 Judge against the generated instruction

`instruction_generated/<U>.txt`, never `prompt_actionnet_real`. See §1 -- and note the instruction
also names the acting arm ("the source **right** robot arm"), so the task hand is given rather than
inferred from hand-channel closure. All 100 say exactly one of `source right` (74) / `source left`
(26); if you match on the string, fail loudly rather than defaulting, or a phrasing change measures
the idle arm on every clip.

---

### 8.6 The frame-0 rule costs nothing here either

Pre-Contact is an **event**: the entry frame is the first frame at distance 0 *having been outside
on the frame before*, so frame 0 can never qualify. **21 of 300 clips start inside the sphere** --
exactly 7 per method, because all three generators share the same 100 conditioning frames, so frame
0 does not depend on the generator. All 21 get an entry event anyway: the hand leaves and comes back.
Nothing is lost to the rule. A clip with no entry is a clip whose fingertip never reached the
boundary, which is the signal.

---

## 9. What came out, and which numbers are shipped

Two Pre-Contact runs are here, and they differ only in the boundary construction:

| | `pre_*/` (shipped as run) | `pre2_*/` (leak fix applied) |
|---|---|---|
| mask | as delivered | largest connected component |
| depth selection | 5-95 percentile | **median +- 6 cm** |
| sphere radius, median | 6.23 cm | **5.75 cm** |
| entry: mot | 30 | **27** |
| entry: diffonly | 26 | **23** |
| entry: block18 | 30 | **25** |

`pre2_*` is the better estimate and the reason is in §7: the fix is surgical, moving the 14 clips
whose object-region depth already spanned under 5 cm by nothing at all (4.02 -> 4.02 cm, worst
individual shift 0.54 cm) while pulling the 21 leaking ones from 11.46 to 5.91 cm. Both are shipped
so the difference can be inspected rather than believed.

The correction is not cosmetic: it **breaks a tie**. On `pre_*` mot and block18 are level at 30;
on `pre2_*` block18 loses 5 against mot's 3, giving **mot 27 > block18 25 > diffonly 23**. block18's
entries leaned on inflated spheres more than the others'. One clip goes the other way and gains an
entry (`mot / 01JMC162SR6WQWELES`) -- dropping the leaked points moved the sphere's *centre* onto the
object, not just shrank it.

**`occ_*/` was scored against `pre_*/`.** 28 clips have a different entry frame under the fix, so
their window moved and their Occlusion score is stale; a rescore is outstanding. Occlusion numbers
in `occ_*/` are valid only for the `pre_*` entries they were computed from.

---

## 10. The second round (2026-08-25): two fixes, and which run to read

Two defects were found by re-auditing the chain, both of which made the filter **too permissive**.
Both are fixed, and both rounds ship so the correction can be inspected rather than believed.

| | first round | second round |
|---|---|---|
| Pre-Contact | `pre_*/` | **`pre2_*/`** |
| Occlusion | `occ_*/` | **`occ2_*/`** |
| tracked arm masks | not kept | **`masks2_*/`** |
| sample videos | — | **`sphere/`, `gallery3/`** |
| summary | — | `gallery_meta2.json`, `summary2.json` |

**Read `pre2_*` + `occ2_*`.** `pre_*` + `occ_*` are kept because they are what the first numbers were
computed from; mixing a `pre2` entry frame with an `occ` score is the one combination that is wrong,
because the window moved.

### Fix 1 -- the boundary swallowed leaked depth (see §7)

Mask-border bleed put points at a neighbouring object's depth into the object cloud, inflating the
sphere. Selecting depth as a band around the object-region median instead of by percentile moved
only the clips that were broken: the 14 whose depth already spanned under 5 cm came out unchanged
(4.02 -> 4.02 cm, worst individual shift 0.54 cm) while the 21 leaking ones fell 11.46 -> 5.91 cm.

### Fix 2 -- the arm mask deleted the hand

The tracker's largest-connected-component step was being applied to the ARM. Its own help says why
that is wrong: *"for an ARM it is dangerous -- when the hand is visually separated from the forearm
the hand blob is the SMALLER one and gets deleted, which is exactly where the mask is needed."*
The moment of contact is exactly that moment. With `--keep-all-blobs`, and the area floor lowered
from 0.002 to 0.0005 of the frame so a hand seen edge-on is reported rather than dropped:

| | before | after |
|---|---|---|
| window frames missing a mask | one clip at 60.6 % coverage | **0** |
| tracking failures | — | **0** |
| masks shrinking below 25 % of their median | not measured | **0** |

`occ2_*` records a `track` block per clip (`want`, `got`, `arm_px_{med,min,max}`, `shrunk`) so a 0 %
score can be told apart from a lost track after the fact. **Every `occ == 0` in `occ_*` is suspect
for this reason; in `occ2_*` it can be checked.**

### What the fixes did to the numbers

| | first round | second round |
|---|---|---|
| entry: mot / block18 / diffonly | 30 / 30 / 26 | **27 / 25 / 23** |
| both levels pass | 28 / 26 / 22 | **25 / 23 / 20** |
| Occlusion median | 46.6 / 26.5 / 53.1 % | **48.1 / 28.4 / 53.8 %** |
| sphere radius, median | 6.23 cm | **5.75 cm** |

The ranking survives (mot > block18 > diffonly) but every count fell: **both fixes removed passes
rather than adding them.** Two clips are worth naming because they show each fix working in
opposite directions. `mot / 01JKF6K1A0MAHZKWXG` passed at 3.64 % and now scores 0.00 % -- that
overlap was a leftover blob, not the hand. `mot / 01JMCA6QKK5TXTFL2E` had a 12.1 cm sphere that
swallowed the hand at frame 0; the corrected 3.38 cm sphere leaves the fingertip 2.31 cm short, so
a clip that was unscoreable became an honest near miss.

---

## 11. The third round (2026-08-25): the run to read is pre4

Two more defects were found and closed; `pre4_*/` is the final Pre-Contact run and carries the full
config stamp per record (`mask_lcc`, `z_band_m`, `freeze_platform`, `right_arm_fit_applied`).

**Fix 3 -- the right arm's zero is session-dependent.** At s0, projected fingertips land ON the
frame-0 arm mask for left-handed clips (0-12 px) and miss by 22-59 px (~4-10 cm) for right-handed
ones, worst on the 01JK sessions. The croissant-era finding that the right arm needs no offset did
not transfer. Per-session 4-joint zeros were fitted on the REAL conditioning frames' arm masks
(`fit_right_arm.py` -> `right_arm_fit_by_session.json`), held-out validated to 0.1-4.2 px, the two
thin sessions pooled (28.0 -> 3.0 px held-out). Coverage: every verdict-relevant arm, 300/300.
This correction is structurally always available: the I2V conditioning image is a REAL photo and
s0 a real state, so every clip carries its own calibration anchor.

**Fix 4 -- the IDM drifts channels whose truth is constant.** Recorded platform commands never move
(waist action range 0.000 deg; idle-hand travel ~0.3 cm), yet the IDM reads out 2.33 deg of
waist_yaw and 15 cm of idle-arm travel -- and the pixels at the IDM-claimed idle-hand destination
do not change, proving hallucination. Legs, head, waist and the idle arm are held at s0 through
the rollout. Only the waist ever touched the verdict (it swivels the task arm ~2 cm).

| | pre2 | pre3 (+freeze) | **pre4 (+right arm)** |
|---|---|---|---|
| mot | 27 | 30 | **31** |
| block18 | 25 | 25 | **21** |
| diffonly | 23 | 24 | **17** |

Side runs, same chain: box boundary 20/14/10 (box-only entries: 0 -- the box nests in the sphere);
per-axis trim 5-95 sensitivity 25/14/10. The primary is 1-99 + sphere.

Sign-off audit on pre4, all passing: invariants 300/300; sphere bit-identical across the three
methods per ULID (it depends only on s0+depth+mask); round-trip reprojection 99/100 in-mask under
both camera models; fingertips converge at entry in 94 % of entries (a signal sharing no code with
the geometry); a rerun is verdict-identical; an unknown session key announces itself instead of
passing uncorrected. Pose-transfer check: at the ENTRY pose the fingertips sit median 1.6 cm
(p90 ~5 cm) from the SAM3-tracked arm -- the tail is what Occlusion exists to arbitrate.

`occ_*/` and `occ2_*/` predate pre4's entry frames and are stale relative to it; the Occlusion
realignment is deliberately deferred.

---

## 12. The fourth round (2026-08-25): pre5 is the final run

Two changes, both in the direction the user's scrutiny pushed: symmetry and fewer hidden priors.

**Left arm, same treatment.** The croissant-era left offset also drifts by session (01JMC: 27.8 px
~ 4.9 cm). Per-session deltas fitted on the same I anchors (`fit_left_arm.py` ->
`left_arm_fit_by_session.json`), same held-out gate. 01JMC's fit lands at 11.4 px with two
parameters at the bound -- adopted, flagged as strained.

**z-selection goes hybrid.** The fixed band's thickness prior is replaced as sole guard by an
intersection of two weak physical statements: a GAP CLUSTER (sort the mask pixels' depths, cut at
jumps > 2 cm that one continuous surface cannot produce, keep the median's cluster -- no thickness
prior) and the +-6 cm band (continuous table bleed, which has no gap). Measured: the known leak
exhibit 10.8 -> 4.2 cm (true cube size recovered), the genuine 24 cm eggplant untouched, >10 cm
tail 3 -> 2, clean-clip spheres move toward the size-predicted truth. Alternatives measured and
rejected: per-axis 1-99 alone (tail 22, max 70 cm), 5-95 (mitigates only), gap alone (g=1 cuts the
real eggplant, g=3 misses the leak), and a support-plane-removal variant with NO thickness prior
(loses 4-0 on exhibits: thin objects live near the plane, 9 clips collapse below the pixel floor).
Every selector carries one object-scale statement; the band's is explicit and gate-checked per
dataset (§13).

| | pre2 | pre3 | pre4 | **pre5 (final)** |
|---|---|---|---|---|
| mot | 27 | 30 | 31 | **28** |
| block18 | 25 | 25 | 21 | **20** |
| diffonly | 23 | 24 | 17 | **17** |
| sphere median | 5.75 | 5.75 | 5.75 | **4.95 cm** |

The tightened boundary removed 4 entries and added none (the hybrid keep-set is a subset of the
band's). Sign-off audit on pre5, 6/6: invariants 300/300, sphere bit-identical across methods,
round-trip 99/98 of 100 in-mask, fingertip convergence 94 %, rerun verdict-identical, unknown
session keys loud.

---

## 13. The fifth round (2026-08-25): pre6 removes the last inherited constant

The left arm had been riding the croissant-era offset as its base -- calibration borrowed from a
DIFFERENT dataset, which is exactly what a batch-portable method must not do. Refitting the left
arm FROM ZERO on this batch's own I anchors (bound widened to 16 deg): three session groups reach
0.4 / 3.8 / 6.8 px held-out; 01JMC fails the gate at any bound (all parameters pinned -- something
beyond a 4-joint zero) and ships UNCORRECTED rather than patched with a borrowed constant. Its
margin audit: all 18 of its left-hand verdicts are no-entry with margins beyond the ~3 cm
uncertainty, one borderline (diffonly / 01JMC162SR6WQWELES, miss 3.04 cm vs ~2.9 cm uncertainty),
flagged here.

The chain now carries NOTHING a new batch cannot re-derive from itself. `pre6_*/` is the final run:

| | mot | block18 | diffonly |
|---|---|---|---|
| entries (n=100 each) | **28** | **20** | **16** |

versus pre5 the only change is one borderline diffonly entry (left offset shifted a few mm).
Sign-off audit re-run on pre6: see the audit block in SS12 -- all six checks hold.

---

## 14. The sixth round: pre7, and the batch-portability guarantee

The band's last dataset-specific number is gone. `+-6 cm` becomes `+- 0.4 * L_max`, where L_max is
the clip's own lateral extent (mask angular size x median depth) -- a dimensionless SHAPE statement
("depth extent <= 0.8x max lateral extent") instead of a centimetre constant. Half-widths now
self-scale 1.1-10.4 cm across this batch (median 2.8) where the fixed band was always 6.0. On this
set it ties the fixed band on every exhibit (leak 4.25 cm, eggplant 13.22, chopsticks 5.52 -- equal
to two decimals) and is tighter at the median (4.61 vs 4.91 cm).

**Final verdicts (`pre7_*/`)**: mot **26** · block18 **18** · diffonly **14**; sphere median
4.71 cm. The ranking held through all six rounds and every fix moved counts DOWN, never up.

**How much the z-selection matters:** removing it entirely (sensor gate + per-axis 1-99 only)
inflates entries to 37 / 26 / 18 and the sphere to median 7.14 cm, max 70.8. It is not a tweak --
it decides ~40 % of the verdicts.

**Running this on a new batch.** Every script takes `SYNTH_BATCH`:

```bash
SYNTH_BATCH=/path/to/new_batch python onboard_batch.py       # 7 gates; fits both arms' zeros
SYNTH_BATCH=/path/to/new_batch python synth_precontact.py --method M -o out/
SYNTH_BATCH=/path/to/new_batch python final_audit.py         # 6/6 = the batch's certificate
```

`onboard_batch.py` re-derives or re-checks every constant from the batch itself and prints a
prescription on failure rather than defaulting: instruction->hand exact partition; platform-static
(measured, not assumed -- a moving camera means DON'T freeze); sensor rails auto-derived from the
depth histogram; both arms' session zeros fitted from THIS batch's I anchors with a held-out gate
(failing sessions ship uncorrected with a margin audit, never patched with a borrowed constant);
the band's bite (does it delete what the cluster kept? deep bites mean it is cutting object);
IDM hand convention via the convention-free convergence test. On this batch: **7/7**, and the
sign-off audit **6/6**.

One gate was itself wrong and got fixed here: #5 first compared the gap-cluster's WIDTH to L_max
and read 1.75, apparently failing -- but the cluster still contains continuous bleed, so its width
overstates thickness (leak-resistant core thickness is 0.49). The operational form -- how much of
the cluster does the band delete -- reads median 0 %, and deep bites on 4/100.

---

## 15. Porting this method to a NEW synthetic dataset

Nothing in the method is tied to this set. What IS tied to a dataset is a short list of fitted
constants -- and every one of them ships with the procedure that fitted it and the gate that
accepted it, so onboarding a new set is running a battery, not redoing research. The structural
guarantee that makes this work: **an I2V clip always carries its own calibration anchor** (the
conditioning image is a real photo, s0 a real state), so the geometry can always be re-zeroed on
the new data itself.

**What a new set must provide (the contract):**
conditioning image I (real) · s0 at that instant · the action stream · a target-object mask at
frame 0 (or a real image SAM can mask) · depth at frame 0 (sensor or predicted) · a rule mapping
instruction -> task hand · the generator's resize transform (ours: anisotropic 0.600/0.540, no crop).

**What gets re-fitted or re-checked on arrival, with what:**

| constant | nature | procedure | acceptance gate |
|---|---|---|---|
| arm zeros, per session | drifts between capture sessions (proven here: right 4-10 cm) | `fit_right_arm.py` / `fit_left_arm.py` on the I anchors | held-out half <= 12 px; unknown session keys announce themselves |
| platform + idle-arm freeze | valid only if the capture platform is static | measure recorded action ranges (here: waist 0.000 deg) and clip background motion | if the platform actually moves, do NOT freeze -- the assumption is checked, not assumed |
| rollout beta/alpha | controller-specific | `validate_fk_gr1t1.py` recipe on held-out real episodes | reproduce recorded states |
| sensor gate (0.05-2.6 m) | this sensor's zero-marker and saturation rail | histogram the raw depth: invalid marker + the p99==max rail | gate sits inside the rails |
| z-band 6 cm | thickness prior | object-region depth-spread distribution on the new set | p95 of genuine spread well under 2x band |
| gap 2 cm | surface-continuity scale | sweep 1/2/3 cm on known-genuine long objects | genuine objects survive, known leaks cut |
| IDM hand units/sign | IDM-specific | convention-free check: fingertips must CONVERGE at entry | >= 80 % of entries |
| instruction -> hand | generation-pipeline phrasing | exact-partition check | ambiguity halts, never defaults |

**What needs no refit:** the boundary construction (LCC x sensor gate x hybrid z-select x 1-99 box
-> circumscribed sphere), the entry-event rule, the two-space split, and the audit battery itself
(`final_audit.py`: invariants, cross-method structure identity, round-trip reprojection, grasp
convergence, determinism, unknown-session alarm). Run the battery; if all six pass on the new set,
the port is done.

---

## 16. Provenance

Generated clips and masks: `multiobj_final` / `multiobj_eval` (minyoung). `block18` there is
byte-identical to `ckpt18` in the eval tree — the same generator under two folder names, confirmed
by hash, so the action files pair as `block18 ↔ ckpt18_unified.data_idm`.

Every ingredient was verified before packaging: 62 checks across two passes over manifest, s₀,
actions, four mask resolutions, videos, conditioning frames, camera and instructions, plus 300
rollout+FK runs across the three generators. No failures.

Method write-up: `filtering/docs/stage5-method.md` in our internal RoboCurate_V2 repo
(not public -- §8 here carries what a reader needs to reimplement).
